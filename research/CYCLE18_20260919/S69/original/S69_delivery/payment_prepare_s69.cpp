#include "cert_interval.hpp"
#include <omp.h>
using namespace std;
static void write_vec(const string&fn,const vector<I>&v){ofstream f(fn,ios::binary);uint64_t n=v.size();f.write((char*)&n,sizeof(n));for(auto z:v){f.write((char*)&z.l,sizeof(R));f.write((char*)&z.h,sizeof(R));}if(!f)throw runtime_error("write vec");}
int main(){fesetround(FE_UPWARD);omp_set_num_threads(5);constexpr int n=22,gi0=10,gj0=11;const uint64_t N=1ULL<<n;vector<I>p(N),V0(N),V1(N);vector<unsigned char>seen(N);uint64_t cnt=0;I mass(0);
 for(int file=0;file<4;file++){ifstream f("./prob22_"+to_string(file)+".bin",ios::binary);uint64_t w;R l,h;while(f.read((char*)&w,sizeof(w))){if(!f.read((char*)&l,sizeof(l))||!f.read((char*)&h,sizeof(h)))throw runtime_error("truncated file");if(w>=N||seen[w]||l<=0||h<l)throw runtime_error("bad probability record");seen[w]=1;cnt++;p[w]=I(l,h);mass=mass+p[w];}}
 if(cnt!=N||mass.l>1||mass.h<1)throw runtime_error("incomplete probability cover");
 vector<int>lo(256),hi(256);ifstream caps("./guard_caps_integer.txt");for(int k=0;k<256;k++)if(!(caps>>lo[k]>>hi[k]))throw runtime_error("caps");
 I C0=rat(114351,80000),CS=rat(2067,400),half=rat(1,2);vector<I>d0(256),d1(256);for(int k=0;k<256;k++){d0[k]=C0-rat(lo[k]+hi[k],20000);d1[k]=CS-rat(hi[k]-lo[k],100);for(I aa:{rat(1,50),rat(51,2000)}){I CC=rat(6501,5000)+CS*aa,delta=d0[k]+(aa-rat(1,40))*d1[k];if(delta.l<0||(CC*half-delta).l<0)throw runtime_error("PSD cap test");}}
 R vmax0=0,vmax1=0;uint64_t bi=1ULL<<gi0,bj=1ULL<<gj0;int gp[8]={6,7,8,9,12,13,14,15};
 #pragma omp parallel for schedule(static) reduction(max:vmax0,vmax1)
 for(uint64_t base=0;base<N;base++)if(!(base&(bi|bj))){uint64_t ww[4]={base,base|bi,base|bj,base|bi|bj};I ff[4][2];unsigned z=0;for(int k=0;k<8;k++)z|=((base>>gp[k])&1)<<k;for(int s=0;s<4;s++){ff[s][0]=I((s&1)?1:-1)*(I(1)+p[ww[s^1]]/p[ww[s]]);ff[s][1]=I((s&2)?1:-1)*(I(1)+p[ww[s^2]]/p[ww[s]]);}for(int order=0;order<2;order++){I CC=order?CS:C0,delta=order?d1[z]:d0[z],gg[4][2],tt[4];for(int s=0;s<4;s++){gg[s][0]=half*CC*ff[s][0]+delta*ff[s][1];gg[s][1]=half*CC*ff[s][1]+delta*ff[s][0];tt[s]=half*CC*(ff[s][0]*ff[s][0]+ff[s][1]*ff[s][1])+I(2)*delta*ff[s][0]*ff[s][1];}for(int s=0;s<4;s++){I val=I(2)*(gg[s|1][0]-gg[s&2][0]+gg[s|2][1]-gg[s&1][1])-tt[s];if(!order){V0[ww[s]]=val;vmax0=max(vmax0,absmax(val));}else{V1[ww[s]]=val;vmax1=max(vmax1,absmax(val));}}}}
 if(vmax0>1500||vmax1>10000)throw runtime_error("declared V norm bound failed");write_vec("V0_s69.bin",V0);write_vec("V1_s69.bin",V1);cout<<setprecision(24)<<"PREPARE PASS mass ["<<mass.l<<","<<mass.h<<"] VMAX "<<vmax0<<" "<<vmax1<<" words "<<N<<"\n";
}
