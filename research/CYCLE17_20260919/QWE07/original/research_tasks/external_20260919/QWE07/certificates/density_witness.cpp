#include "density_sine.hpp"
#include <omp.h>
using namespace std;
constexpr int n=22; constexpr uint64_t N=1ULL<<n;
vector<I> V0,V1,basep;I channel_a;
struct Sum {I mass,expect; uint64_t leaves=0; R maxrel=0;};
// Sequential conditioning enumerates every word exactly once; no inverse of
// a nearly singular finite sine projection is formed.
void enumerate(const vector<I>& K,int m,I wt,uint64_t word,int dep,int prefix,bool build,Sum& out){
 if(!m){
  if(wt.l<=0)throw runtime_error("nonpositive atom enclosure");
  if(build)basep[word]=wt;
  else out.expect=out.expect+wt*(V0[word]+(channel_a-rat(1,40))*V1[word]);
  out.mass=out.mass+wt;out.leaves++;out.maxrel=max(out.maxrel,ud(ua(wt.h,-wt.l),wt.l));return;
 }
 I q(max(K[0].l,channel_a.l),min(K[0].h,(channel_a+rat(19,20)).h));
 auto branch=[&](bool bit){I prob=bit?q:I(1)-q;if(prob.l<=0)throw runtime_error("ambiguous conditional pivot");vector<I>L((m-1)*(m-1));
  for(int i=1;i<m;i++)for(int j=i;j<m;j++){
   I v=K[i*m+j]+I(bit?-1:1)*K[i*m]*K[j]/prob;
   L[(i-1)*(m-1)+j-1]=L[(j-1)*(m-1)+i-1]=v;
  }
  enumerate(L,m-1,wt*prob,word|(uint64_t(bit)<<dep),dep+1,prefix,build,out);
 };
 if(dep<2)branch((prefix>>dep)&1);else{branch(false);branch(true);}
}
Sum compute(long long rn,long long rd,long long an,long long ad,bool build){
 channel_a=rat(an,ad);vector<int> co(n);iota(co.begin(),co.end(),0);auto K=sine_Q(co,rn,rd);
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)K[i*n+j]=rat(19,20)*K[i*n+j]+(i==j?channel_a:I(0));
 Sum sums[4];
 #pragma omp parallel for schedule(static)
 for(int k=0;k<4;k++){fesetround(FE_UPWARD);enumerate(K,n,I(1),0,0,k,build,sums[k]);}
 Sum out;for(auto&s:sums){out.mass=out.mass+s.mass;out.expect=out.expect+s.expect;out.leaves+=s.leaves;out.maxrel=max(out.maxrel,s.maxrel);}
 if(out.leaves!=N||out.mass.l>1||out.mass.h<1)throw runtime_error("normalization or complete-word coverage");return out;
}
void build_test(){
 basep.resize(N);auto proof=compute(1,3,1,40,true);V0.resize(N);V1.resize(N);cerr<<"BASE COMPLETE "<<proof.leaves<<endl;
 int lo[256],hi[256];ifstream f("guard_caps_integer.txt");for(int i=0;i<256;i++)if(!(f>>lo[i]>>hi[i]))throw runtime_error("guard data");
 uint64_t bi=1ULL<<10,bj=1ULL<<11;int gp[8]={6,7,8,9,12,13,14,15};R vmax0=0,vmax1=0;
 for(uint64_t base=0;base<N;base++)if(!(base&(bi|bj))){uint64_t ww[4]={base,base|bi,base|bj,base|bi|bj};I ff[4][2];unsigned z=0;for(int k=0;k<8;k++)z|=((base>>gp[k])&1)<<k;
  for(int s=0;s<4;s++){ff[s][0]=I((s&1)?1:-1)*(I(1)+basep[ww[s^1]]/basep[ww[s]]);ff[s][1]=I((s&2)?1:-1)*(I(1)+basep[ww[s^2]]/basep[ww[s]]);}
  for(int order=0;order<2;order++){I CC=order?rat(51,10):rat(573,400),delta=order?rat(51,10)-rat(hi[z]-lo[z],100):rat(573,400)-rat(lo[z]+hi[z],20000);I gg[4][2],tt[4];
   for(int s=0;s<4;s++){gg[s][0]=CC/I(2)*ff[s][0]+delta*ff[s][1];gg[s][1]=CC/I(2)*ff[s][1]+delta*ff[s][0];tt[s]=CC/I(2)*(ff[s][0]*ff[s][0]+ff[s][1]*ff[s][1])+I(2)*delta*ff[s][0]*ff[s][1];}
   for(int s=0;s<4;s++){I val=I(2)*(gg[s|1][0]-gg[s&2][0]+gg[s|2][1]-gg[s&1][1])-tt[s];if(order){V1[ww[s]]=val;vmax1=max(vmax1,absmax(val));}else{V0[ww[s]]=val;vmax0=max(vmax0,absmax(val));}}
  }
 }
 if(vmax0>1500||vmax1>10000)throw runtime_error("witness norm bound");
 ofstream out("witness_cache.bin",ios::binary);uint64_t header=N;out.write((char*)&header,sizeof(header));out.write((char*)V0.data(),N*sizeof(I));out.write((char*)V1.data(),N*sizeof(I));if(!out)throw runtime_error("cache write");
 cout<<setprecision(24)<<"BUILD leaves "<<proof.leaves<<" mass ["<<proof.mass.l<<","<<proof.mass.h<<"] max_relative "<<proof.maxrel<<" V0 "<<vmax0<<" V1 "<<vmax1<<endl;
}
void load_test(){V0.resize(N);V1.resize(N);ifstream in("witness_cache.bin",ios::binary);uint64_t head;in.read((char*)&head,sizeof(head));if(!in||head!=N)throw runtime_error("cache header");in.read((char*)V0.data(),N*sizeof(I));in.read((char*)V1.data(),N*sizeof(I));if(!in)throw runtime_error("cache truncated");for(uint64_t y=0;y<N;y++)if(V0[y].l>V0[y].h||V1[y].l>V1[y].h||absmax(V0[y])>1500||absmax(V1[y])>10000)throw runtime_error("cache enclosure");}
int main(int argc,char**argv){fesetround(FE_UPWARD);omp_set_num_threads(4);if(argc<2)throw runtime_error("usage: build | nodes first last");
 if(string(argv[1])=="build"){build_test();return 0;}load_test();
 if(string(argv[1])=="probe"){
  if(argc!=6)throw runtime_error("probe requires rho numerator denominator and a numerator denominator");
  auto z=compute(stoll(argv[2]),stoll(argv[3]),stoll(argv[4]),stoll(argv[5]),false);
  long long lo=(long long)floorl(dm(z.expect.l,100000000)),hi=(long long)ceill(um(z.expect.h,100000000));
  cout<<setprecision(24)<<"PROBE "<<argv[2]<<" "<<argv[3]<<" "<<argv[4]<<" "<<argv[5]<<" P_interval "<<lo<<" "<<hi<<" 100000000 leaves "<<z.leaves<<" mass ["<<z.mass.l<<","<<z.mass.h<<"] expectation ["<<z.expect.l<<","<<z.expect.h<<"]"<<endl;
  return 0;
 }
 int first=argc>2?stoi(argv[2]):0,last=argc>3?stoi(argv[3]):55;
 for(int id=first;id<last;id++){int j=id/5,k=id%5; // rho=1/3 + 3j/10000; a=.021 + .00075k
  auto start=chrono::steady_clock::now();auto z=compute(10000+9*j,30000,84+3*k,4000,false);
  long long lo=(long long)floorl(dm(z.expect.l,100000000)),hi=(long long)ceill(um(z.expect.h,100000000));
  if(hi-lo>2)throw runtime_error("nodal interval wider than 2e-8");
  cout<<setprecision(24)<<"NODE "<<j<<" "<<k<<" "<<lo<<" "<<hi<<" 100000000 leaves "<<z.leaves<<" mass ["<<z.mass.l<<","<<z.mass.h<<"] expectation ["<<z.expect.l<<","<<z.expect.h<<"] max_relative "<<z.maxrel<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
 }
}
