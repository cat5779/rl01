#include "cert_interval.hpp"
#include "exact_fixed.hpp"
using namespace std;
int n;uint64_t leaves=0;ofstream out;R masslo=0,masshi=0,maxrel=0;int targetprefix=-1,prefixbits=0;
void recurse(const vector<BI>&mat,int m,BI weight,uint64_t word,int dep){
 if(!m){if(weight.l<=0)throw runtime_error("zero mass lower");R l=tolo(weight.l),h=tohi(weight.h);masslo=da(masslo,l);masshi=ua(masshi,h);maxrel=max(maxrel,ud(ua(h,-l),l));out.write((char*)&word,sizeof(word));out.write((char*)&l,sizeof(l));out.write((char*)&h,sizeof(h));leaves++;return;}
 auto branch=[&](bool included){vector<BI>next((m-1)*(m-1));BI p=mat[0];if(included&&p.l<=0)throw runtime_error("Schur pivot nonpositive");
  for(int i=1;i<m;i++)for(int j=1;j<m;j++){BI z=mat[i*m+j];if(included)z=z-mat[i*m]*mat[j]/p;next[(i-1)*(m-1)+j-1]=z;}
  for(int i=0;i<m-1;i++)for(int j=i+1;j<m-1;j++){BI z=bintersect(next[i*(m-1)+j],next[j*(m-1)+i]);next[i*(m-1)+j]=z;next[j*(m-1)+i]=z;}
  recurse(next,m-1,included?weight*p:weight,included?(word|(1ULL<<dep)):word,dep+1);
 };
 if(dep<prefixbits){branch((targetprefix>>dep)&1);}else{branch(false);branch(true);}
}
int main(int argc,char**argv){fesetround(FE_UPWARD);n=argc>1?stoi(argv[1]):22;prefixbits=argc>2?stoi(argv[2]):0;targetprefix=argc>3?stoi(argv[3]):0;string dest=argc>4?argv[4]:"./probabilities.bin";
 ifstream ai("./alpha60.txt");string al,ah,den;ai>>al>>ah>>den;BI alpha(bdec(al,den).l,bdec(ah,den).h),c=br(19,20),a=br(13,500);vector<BI>A(n*n);
 for(int i=0;i<n;i++)for(int j=0;j<n;j++){int d=i-j;BI q;if(!d)q=br(1,3);else if(d%3==0)q=BI(0);else{int dm6=((d%6)+6)%6;q=((dm6==1||dm6==2)?alpha:-alpha)/BI(d);}BI k=c*q+(i==j?a:BI(0));A[i*n+j]=(i==j?BI(1):BI(0))-k;}
 auto rr=binverse(A,n);auto L=rr.first;for(int i=0;i<n;i++)L[i*n+i]=L[i*n+i]-BI(1);for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){BI z=bintersect(L[i*n+j],L[j*n+i]);L[i*n+j]=z;L[j*n+i]=z;}
 out.open(dest,ios::binary);auto t0=chrono::steady_clock::now();recurse(L,n,rr.second,0,0);out.close();cout<<setprecision(24)<<"PROBABILITY PASS n "<<n<<" prefixbits "<<prefixbits<<" prefix "<<targetprefix<<" leaves "<<leaves<<" mass ["<<masslo<<","<<masshi<<"] max_relative_width "<<maxrel<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n";
}
