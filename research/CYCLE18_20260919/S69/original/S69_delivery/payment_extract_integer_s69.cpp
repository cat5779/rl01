#include "cert_interval.hpp"
#include <omp.h>
using namespace std;
static void read_vec(const string&name,vector<I>&v,uint64_t N){ifstream f(name,ios::binary);uint64_t n;f.read((char*)&n,sizeof(n));if(n!=N)throw runtime_error("bad vector size "+name);for(uint64_t i=0;i<N;i++){R l,h;if(!f.read((char*)&l,sizeof(l))||!f.read((char*)&h,sizeof(h)))throw runtime_error("truncated "+name);v[i]=I(l,h);}}
static void read_p(vector<I>&p,uint64_t N){vector<unsigned char>seen(N);uint64_t cnt=0;for(int file=0;file<4;file++){ifstream f("./prob22_"+to_string(file)+".bin",ios::binary);uint64_t w;R l,h;while(f.read((char*)&w,sizeof(w))){if(!f.read((char*)&l,sizeof(l))||!f.read((char*)&h,sizeof(h)))throw runtime_error("truncated p");if(w>=N||seen[w])throw runtime_error("bad p");seen[w]=1;p[w]=I(l,h);cnt++;}}if(cnt!=N)throw runtime_error("p cover");}
int main(int argc,char**argv){if(argc!=2){cerr<<"usage: payment_extract_integer_s69 K\n";return 2;}fesetround(FE_UPWARD);omp_set_num_threads(5);int k=stoi(argv[1]);if(k<0||k>7)throw runtime_error("k");constexpr int n=22;const uint64_t N=1ULL<<n;vector<I>q(N),V0(N),V1(N);read_vec("./V0_s69.bin",V0,N);read_vec("./V1_s69.bin",V1,N);if(k==0)read_p(q,N);else read_vec("./q_s69_"+to_string(k)+".bin",q,N);
 int nt=omp_get_max_threads();vector<I>sa(nt),sb(nt);
 #pragma omp parallel
 {fesetround(FE_UPWARD);int tid=omp_get_thread_num();I a(0),b(0);
  #pragma omp for schedule(static)
  for(uint64_t w=0;w<N;w++){a=a+q[w]*V0[w];b=b+q[w]*V1[w];}
  sa[tid]=a;sb[tid]=b;
 }
 I aa(0),bb(0);for(int i=0;i<nt;i++){aa=aa+sa[i];bb=bb+sb[i];}
 const R den=1000000000000000.L;
 long long al=(long long)floorl(dm(aa.l,den));
 long long ah=(long long)ceill(um(aa.h,den));
 long long bl=(long long)floorl(dm(bb.l,den));
 long long bh=(long long)ceill(um(bb.h,den));
 ofstream out("./raw_integer_s69_"+to_string(k)+".txt");out<<al<<" "<<ah<<" "<<bl<<" "<<bh<<" 1000000000000000\n";
 cout<<setprecision(30)<<"RAWINT "<<k<<" ca ["<<aa.l<<","<<aa.h<<"] cb ["<<bb.l<<","<<bb.h<<"] ints "<<al<<" "<<ah<<" "<<bl<<" "<<bh<<" den 1000000000000000\n";
}
