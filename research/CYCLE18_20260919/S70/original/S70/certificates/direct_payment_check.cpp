// S70 independent full-word point check: direct tensor transport, NO Walsh
// transform, coefficient truncation, or tail. This checks but does not replace
// the continuum proof. The local potential uses the same explicit fixed witness.
#include "cert_interval.hpp"
#include <omp.h>
using namespace std;
constexpr int n=22,KMAX=8;constexpr uint64_t N=1ULL<<n;
void walsh(vector<I>&v){
 for(int bit=0;bit<n;bit++){uint64_t stride=1ULL<<bit;
  #pragma omp parallel for schedule(static)
  for(uint64_t block=0;block<N;block+=2*stride){fesetround(FE_UPWARD);for(uint64_t off=0;off<stride;off++){uint64_t x=block+off,y=x+stride;I a=v[x],b=v[y];v[x]=a+b;v[y]=a-b;}}
 }
}
long long choose(int n0,int k){if(k<0||n0<k)return 0;long long v=1;for(int j=1;j<=k;j++)v=v*(n0-j+1)/j;return v;}
int main(int argc,char**argv){try{
 fesetround(FE_UPWARD);int threads=argc>1?stoi(argv[1]):4;omp_set_num_threads(threads);
 vector<I>p(N),V0(N),VP(N),VC(N);vector<unsigned char>seen(N);uint64_t cnt=0;I mass(0);
 for(int file=0;file<4;file++){ifstream f("prob22_"+to_string(file)+".bin",ios::binary);if(!f)throw runtime_error("missing probability cache");uint64_t w;R l,h;while(f.read((char*)&w,sizeof(w))){if(!f.read((char*)&l,sizeof(l))||!f.read((char*)&h,sizeof(h)))throw runtime_error("truncated probability record");if(w>=N||seen[w]||!(l>0)||h<l)throw runtime_error("bad probability record");seen[w]=1;cnt++;p[w]=I(l,h);mass=mass+p[w];}}
 if(cnt!=N||mass.l>1||mass.h<1)throw runtime_error("incomplete probability cover");

 vector<int>lo(256),hi(256),tau2(256),tau3(256);ifstream caps("guard_caps_integer.txt"),far2("far_tau_integer.txt"),far3("quad_tau3_integer.txt");for(int z=0;z<256;z++)if(!(caps>>lo[z]>>hi[z])||!(far2>>tau2[z])||!(far3>>tau3[z]))throw runtime_error("caps");
 for(int z=0;z<256;z++)if(tau2[z]<0||tau3[z]<0)throw runtime_error("negative pair allocation");
 I C0=rat(2861,2000),Cp=rat(51,200),Cc(8),weights[4]={rat(19,60),rat(11,60),rat(11,60),rat(19,60)};
 I b0[3][256],bp[256];for(int z=0;z<256;z++){
  b0[0][z]=(C0-rat(lo[z]+hi[z],20000)-rat(1,50))/I(3);
  bp[z]=(Cp-rat(hi[z]-lo[z],2000))/I(3);
  b0[1][z]=rat(tau2[z],2000);b0[2][z]=rat(tau3[z],1000);
 }
 int ei[6]={0,0,0,1,1,2},ej[6]={1,2,3,2,3,3},guard[6][8];
 for(int e=0;e<6;e++){int k=0;for(int off=-4;off<=5;off++)if(off!=0&&off!=ej[e]-ei[e])guard[e][k++]=9+ei[e]+off;if(k!=8)throw runtime_error("guard definition");}
 R vmax[3]={0,0,0},fmax=0;uint64_t masks[4]={1ULL<<9,1ULL<<10,1ULL<<11,1ULL<<12},tmask=masks[0]|masks[1]|masks[2]|masks[3];
 #pragma omp parallel
 {
  fesetround(FE_UPWARD);R vm[3]={0,0,0},fm=0;
  #pragma omp for schedule(static)
  for(uint64_t base=0;base<N;base++)if(!(base&tmask)){
   uint64_t ww[16];I f[16][4];for(int s=0;s<16;s++){ww[s]=base;for(int j=0;j<4;j++)if((s>>j)&1)ww[s]|=masks[j];}
   for(int s=0;s<16;s++)for(int j=0;j<4;j++){f[s][j]=I((s>>j)&1?1:-1)*(I(1)+p[ww[s^(1<<j)]]/p[ww[s]]);fm=max(fm,absmax(f[s][j]));}
   for(int s=0;s<16;s++){
    I ds(0);for(int j=0;j<4;j++)ds=ds+weights[j]*(I(2)*(f[s|(1<<j)][j]-f[s&~(1<<j)][j])-f[s][j]*f[s][j]);
    I v0=C0*ds,vp=Cp*ds,vc=Cc*ds;
    for(int e=0;e<6;e++){
     int i=ei[e],j=ej[e],sep=j-i;unsigned z=0;for(int k=0;k<8;k++)z|=((ww[s]>>guard[e][k])&1)<<k;
     I xx=I(2)*(f[s|(1<<i)][j]-f[s&~(1<<i)][j]+f[s|(1<<j)][i]-f[s&~(1<<j)][i]-f[s][i]*f[s][j]);
     v0=v0+b0[sep-1][z]*xx;if(sep==1){vp=vp+bp[z]*xx;vc=vc+Cc/I(3)*xx;}
    }
    V0[ww[s]]=v0;VP[ww[s]]=vp;VC[ww[s]]=vc;vm[0]=max(vm[0],absmax(v0));vm[1]=max(vm[1],absmax(vp));vm[2]=max(vm[2],absmax(vc));
   }
  }
  #pragma omp critical
  {fmax=max(fmax,fm);for(int j=0;j<3;j++)vmax[j]=max(vmax[j],vm[j]);}
 }
 cout<<setprecision(25)<<"FULL_WORDS "<<cnt<<" MASS ["<<mass.l<<","<<mass.h<<"] FMAX "<<fmax<<" VMAX "<<vmax[0]<<" "<<vmax[1]<<" "<<vmax[2]<<"\n";cout.flush();
 if(fmax>40.00000001L||vmax[0]>20000||vmax[1]>20000||vmax[2]>200000)throw runtime_error("declared norm bound failed");
 ofstream norms("quad_payment_norms_integer.txt");for(int j=0;j<3;j++)norms<<(long long)ceill(vmax[j])<<"\n";norms.close();

 for(int which=0;which<2;which++){
  I c=which?rat(24,25):rat(1907,2000),bias=which?rat(9,20):rat(21,50);
  I ep=bias-rat(1,2),ec=c-rat(19,20),s=(I(1)-c)*ep,v=ec/rat(19,20);
  vector<I>moving=p;
  for(int bit=0;bit<n;bit++){uint64_t stride=1ULL<<bit;
   #pragma omp parallel for schedule(static)
   for(uint64_t block=0;block<N;block+=2*stride){fesetround(FE_UPWARD);for(uint64_t off=0;off<stride;off++){
    uint64_t i=block+off,j=i+stride;I x=moving[i],y=moving[j];I delta=-s*(x+y)+v*(x-y)/I(2);
    moving[i]=x+delta;moving[j]=y-delta;
   }}
  }
  I payment(0),movingmass(0);
  #pragma omp parallel
  {
   fesetround(FE_UPWARD);I local(0),lm(0);
   #pragma omp for schedule(static)
   for(uint64_t w=0;w<N;w++){local=local+moving[w]*(V0[w]+ep*VP[w]+ec*VC[w]);lm=lm+moving[w];}
   #pragma omp critical
   {payment=payment+local;movingmass=movingmass+lm;}
  }
  if(movingmass.l>1||movingmass.h<1)throw runtime_error("direct moving normalization");
  I a=(I(1)-c)*bias,d=rat(2,3)/(a*(I(1)-a))+rat(1,3)/((a+c)*(I(1)-a-c));
  I C=rat(1303,1000)+rat(51,200)*bias+I(8)*ec,gap=payment-(C-I(1))*d;
  cout<<setprecision(25)<<"DIRECT_POINT "<<which<<" c ["<<c.l<<","<<c.h<<"] p ["<<bias.l<<","<<bias.h<<"] MASS ["<<movingmass.l<<","<<movingmass.h<<"] PAYMENT ["<<payment.l<<","<<payment.h<<"] GAP ["<<gap.l<<","<<gap.h<<"]\n";cout.flush();
  if(!which && gap.l<rat(1,25).h)throw runtime_error("direct broad-corner payment failed");
  if(which && gap.h>=-3)throw runtime_error("direct witness obstruction failed");
 }
 cout<<"DIRECT_FULL_WORD_POINT_CHECKS_COMPLETE two exact rational parameter pairs, all 4194304 words\n";
 return 0;
 }catch(exception&e){cerr<<"DIRECT CHECK ERROR "<<e.what()<<"\n";return 1;}}
