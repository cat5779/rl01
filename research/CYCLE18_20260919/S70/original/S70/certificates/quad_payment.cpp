// S70 NEW FINAL QUAD: all-word interval payment via exact two-parameter channel transport
// and Walsh degree aggregation. No word truncation or moving-law freezing.
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
 // Walsh transform H= [[1,1],[1,-1]] tensor n. Parseval includes exactly 1/N.
 walsh(p);walsh(V0);walsh(VP);walsh(VC);
 cout<<"WALSH_DONE\n";cout.flush();
 vector<I>q=p,work(N);p.clear();p.shrink_to_fit();seen.clear();seen.shrink_to_fit();
 ofstream out("quad_payment_coefficients_bivariate.txt");out<<"# k l V0lo V0hi VPlo VPhi VClo VChi; denominator 1000000000\n";
 for(int k=0;k<=KMAX;k++){
  vector<array<I,3>>mom(n+1);
  #pragma omp parallel
  {
   fesetround(FE_UPWARD);array<array<I,3>,n+1>local{};
   #pragma omp for schedule(static)
   for(uint64_t w=0;w<N;w++){int r=__builtin_popcountll(w);if(r<k)continue;local[r][0]=local[r][0]+q[w]*V0[w];local[r][1]=local[r][1]+q[w]*VP[w];local[r][2]=local[r][2]+q[w]*VC[w];}
   #pragma omp critical
   for(int r=k;r<=n;r++)for(int j=0;j<3;j++)mom[r][j]=mom[r][j]+local[r][j];
  }
  for(int r=k;r<=n;r++)for(int j=0;j<3;j++)mom[r][j]=mom[r][j]/I(N);
  I vscale(1);
  for(int l=0;l<=KMAX-k;l++){
   I value[3];for(int r=k+l;r<=n;r++)for(int j=0;j<3;j++)value[j]=value[j]+I(choose(r-k,l))*vscale*mom[r][j];
   out<<k<<" "<<l;cout<<"COEFF "<<k<<" "<<l;
   for(int j=0;j<3;j++){long long lower=(long long)floorl(dm(value[j].l,1000000000.L)),upper=(long long)ceill(um(value[j].h,1000000000.L));out<<" "<<lower<<" "<<upper;cout<<" ["<<value[j].l<<","<<value[j].h<<"]";}
   out<<"\n";out.flush();cout<<"\n";cout.flush();vscale=vscale/rat(950,1);
  }
  if(k==KMAX)break;
  fill(work.begin(),work.end(),I(0));
  // H D_i H^-1 sends the zero bit to the one bit with coefficient -2.
  for(int bit=0;bit<n;bit++){uint64_t stride=1ULL<<bit;
   #pragma omp parallel for schedule(static)
   for(uint64_t block=0;block<N;block+=2*stride){fesetround(FE_UPWARD);for(uint64_t off=0;off<stride;off++){uint64_t x=block+off;work[x+stride]=work[x+stride]+q[x];}}
  }
  I scale=-rat(1,100*(k+1));
  #pragma omp parallel for schedule(static)
  for(uint64_t w=0;w<N;w++){fesetround(FE_UPWARD);q[w]=scale*work[w];}
 }
 out.close();cout<<"COEFFICIENT_ENCLOSURES_COMPLETE degree 8 normalization 1/4194304\n";
 return 0;
 }catch(exception&e){cerr<<"PAYMENT ERROR "<<e.what()<<"\n";return 1;}}
