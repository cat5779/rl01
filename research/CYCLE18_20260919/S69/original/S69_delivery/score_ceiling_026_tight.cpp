#include "cert_interval.hpp"
#include <omp.h>
using namespace std;
int main(){
 fesetround(FE_UPWARD); omp_set_num_threads(8);
 constexpr int n=22,i0=10,j0=11; const uint64_t N=1ULL<<n;
 vector<I>p(N); vector<unsigned char>seen(N); uint64_t cnt=0; I mass(0);
 for(int file=0;file<4;file++){
  ifstream f("./prob26_"+to_string(file)+".bin",ios::binary); uint64_t w;R l,h;
  while(f.read((char*)&w,sizeof(w))){
   if(!f.read((char*)&l,sizeof(l))||!f.read((char*)&h,sizeof(h)))throw runtime_error("truncated");
   if(w>=N||seen[w]||l<=0||h<l)throw runtime_error("bad p record");
   seen[w]=1;p[w]=I(l,h);mass=mass+p[w];cnt++;
  }
 }
 if(cnt!=N||mass.l>1||mass.h<1)throw runtime_error("mass/cover");
 vector<int>lo(256),hi(256);ifstream capin("./guard_caps_integer.txt");for(int z=0;z<256;z++)if(!(capin>>lo[z]>>hi[z]))throw runtime_error("caps");
 I a=rat(13,500),c=rat(19,20),C=rat(6501,5000)+rat(2067,400)*a+rat(1,1000),half=rat(1,2);
 uint64_t bi=1ULL<<i0,bj=1ULL<<j0;int gp[8]={6,7,8,9,12,13,14,15};
 int nt=omp_get_max_threads();vector<I>part(nt);
 #pragma omp parallel
 {
  fesetround(FE_UPWARD);int tid=omp_get_thread_num();I sum(0);
  #pragma omp for schedule(static)
  for(uint64_t base=0;base<N;base++)if(!(base&(bi|bj))){
   uint64_t w[4]={base,base|bi,base|bj,base|bi|bj};unsigned z=0;for(int k=0;k<8;k++)z|=((base>>gp[k])&1)<<k;
   I cap=(I(2*lo[z]+3*hi[z]))/I(50000);I delta=C-cap;
   for(int s=0;s<4;s++){
    I f0=I((s&1)?1:-1)*(I(1)+p[w[s^1]]/p[w[s]]);
    I f1=I((s&2)?1:-1)*(I(1)+p[w[s^2]]/p[w[s]]);
    I q=half*C*(f0*f0+f1*f1)+I(2)*delta*f0*f1;
    sum=sum+p[w[s]]*q;
   }
  }
  part[tid]=sum;
 }
 I P(0);for(auto s:part)P=P+s;
 I d=rat(2,3)/(a*(I(1)-a))+rat(1,3)/((a+c)*(I(1)-a-c));I burden=(C-I(1))*d;I gap=P-burden;
 cout<<setprecision(30)
     <<"SCORE CEILING 026 PASS words "<<cnt<<" mass ["<<mass.l<<","<<mass.h<<"]\n"
     <<"Popt ["<<P.l<<","<<P.h<<"] burden ["<<burden.l<<","<<burden.h<<"] gap ["<<gap.l<<","<<gap.h<<"]\n";
 if(!(gap.h<0))throw runtime_error("ceiling not negative");
}
