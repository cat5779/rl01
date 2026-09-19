#include "cert_interval.hpp"
#include <omp.h>
using namespace std;
static vector<I> read_vec(const string&fn){ifstream f(fn,ios::binary);uint64_t n;f.read((char*)&n,sizeof(n));vector<I>v(n);for(auto &z:v){f.read((char*)&z.l,sizeof(R));f.read((char*)&z.h,sizeof(R));}if(!f)throw runtime_error("read vec "+fn);return v;}
static void write_vec(const string&fn,const vector<I>&v){ofstream f(fn,ios::binary);uint64_t n=v.size();f.write((char*)&n,sizeof(n));for(auto z:v){f.write((char*)&z.l,sizeof(R));f.write((char*)&z.h,sizeof(R));}if(!f)throw runtime_error("write vec");}
static vector<I> read_p(){constexpr int n=22;const uint64_t N=1ULL<<n;vector<I>p(N);vector<unsigned char>seen(N);uint64_t cnt=0;for(int file=0;file<4;file++){ifstream f("./prob22_"+to_string(file)+".bin",ios::binary);uint64_t w;R l,h;while(f.read((char*)&w,sizeof(w))){if(!f.read((char*)&l,sizeof(l))||!f.read((char*)&h,sizeof(h))||w>=N||seen[w])throw runtime_error("p cache");seen[w]=1;p[w]=I(l,h);cnt++;}}if(cnt!=N)throw runtime_error("p count");return p;}
int main(int argc,char**argv){fesetround(FE_UPWARD);omp_set_num_threads(5);if(argc!=2)throw runtime_error("usage step k");int k=stoi(argv[1]);constexpr int n=22;const uint64_t N=1ULL<<n;auto V0=read_vec("V0_s69.bin"),V1=read_vec("V1_s69.bin");vector<I>q=k?read_vec("q_s69_"+to_string(k)+".bin"):read_p();if(q.size()!=N||V0.size()!=N||V1.size()!=N)throw runtime_error("size");int nt=omp_get_max_threads();vector<I>sa(nt),sb(nt);
 #pragma omp parallel
 {fesetround(FE_UPWARD);int tid=omp_get_thread_num();I a(0),b(0);
  #pragma omp for schedule(static)
  for(uint64_t w=0;w<N;w++){a=a+q[w]*V0[w];b=b+q[w]*V1[w];}
  sa[tid]=a;sb[tid]=b;
 }
 I aa(0),bb(0);for(int t=0;t<nt;t++){aa=aa+sa[t];bb=bb+sb[t];}ofstream raw("raw_s69_"+to_string(k)+".txt");raw<<setprecision(30)<<aa.l<<" "<<aa.h<<" "<<bb.l<<" "<<bb.h<<"\n";
 if(k<7){vector<I>work(N,I(0));for(int bit=0;bit<n;bit++){uint64_t stride=1ULL<<bit;
   #pragma omp parallel for schedule(static)
   for(uint64_t block=0;block<N;block+=2*stride)for(uint64_t off=0;off<stride;off++){uint64_t w0=block+off,w1=w0+stride;I ss=q[w0]+q[w1];work[w0]=work[w0]-ss;work[w1]=work[w1]+ss;}}
  I scale=rat(1,200)/I(k+1);vector<I>qn(N);
  #pragma omp parallel for schedule(static)
  for(uint64_t w=0;w<N;w++)qn[w]=scale*work[w];write_vec("q_s69_"+to_string(k+1)+".bin",qn);
 }
 cout<<setprecision(24)<<"STEP "<<k<<" PASS RAW ["<<aa.l<<","<<aa.h<<"] ["<<bb.l<<","<<bb.h<<"]\n";
}
