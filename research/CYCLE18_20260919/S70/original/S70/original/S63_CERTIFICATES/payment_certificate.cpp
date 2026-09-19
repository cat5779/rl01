#include "cert_interval.hpp"
using namespace std;
int main(){fesetround(FE_UPWARD);constexpr int n=22,gi0=10,gj0=11,KMAX=8;const uint64_t N=1ULL<<n;vector<I>p(N),V0(N),V1(N),q(N),work(N);vector<unsigned char>seen(N);uint64_t cnt=0;I mass(0);
 for(int file=0;file<4;file++){ifstream f("./prob22_"+to_string(file)+".bin",ios::binary);uint64_t w;R l,h;while(f.read((char*)&w,sizeof(w))){if(!f.read((char*)&l,sizeof(l))||!f.read((char*)&h,sizeof(h)))throw runtime_error("truncated file");if(w>=N||seen[w]||l<=0||h<l)throw runtime_error("bad probability record");seen[w]=1;cnt++;p[w]=I(l,h);mass=mass+p[w];}}
 if(cnt!=N||mass.l>1||mass.h<1)throw runtime_error("incomplete probability cover");
 vector<int>lo(256),hi(256);ifstream caps("./guard_caps_integer.txt");for(int k=0;k<256;k++)if(!(caps>>lo[k]>>hi[k]))throw runtime_error("caps");
 I C0=rat(573,400),CS=rat(51,10),half=rat(1,2);vector<I>d0(256),d1(256);for(int k=0;k<256;k++){d0[k]=C0-rat(lo[k]+hi[k],20000);d1[k]=CS-rat(hi[k]-lo[k],100);
  for(I aa:{rat(21,1000),rat(3,125)}){I CC=rat(261,200)+CS*aa,delta=d0[k]+(aa-rat(1,40))*d1[k];if(delta.l<0||(CC*half-delta).l<0)throw runtime_error("PSD cap test");}}
 R vmax0=0,vmax1=0;uint64_t bi=1ULL<<gi0,bj=1ULL<<gj0;int gp[8]={6,7,8,9,12,13,14,15};
 for(uint64_t base=0;base<N;base++)if(!(base&(bi|bj))){uint64_t ww[4]={base,base|bi,base|bj,base|bi|bj};I ff[4][2];unsigned z=0;for(int k=0;k<8;k++)z|=((base>>gp[k])&1)<<k;
  for(int s=0;s<4;s++){ff[s][0]=I((s&1)?1:-1)*(I(1)+p[ww[s^1]]/p[ww[s]]);ff[s][1]=I((s&2)?1:-1)*(I(1)+p[ww[s^2]]/p[ww[s]]);}
  for(int order=0;order<2;order++){I CC=order?CS:C0,delta=order?d1[z]:d0[z],gg[4][2],tt[4];
   for(int s=0;s<4;s++){gg[s][0]=half*CC*ff[s][0]+delta*ff[s][1];gg[s][1]=half*CC*ff[s][1]+delta*ff[s][0];tt[s]=half*CC*(ff[s][0]*ff[s][0]+ff[s][1]*ff[s][1])+I(2)*delta*ff[s][0]*ff[s][1];}
   for(int s=0;s<4;s++){I val=I(2)*(gg[s|1][0]-gg[s&2][0]+gg[s|2][1]-gg[s&1][1])-tt[s];if(!order){V0[ww[s]]=val;vmax0=max(vmax0,absmax(val));}else{V1[ww[s]]=val;vmax1=max(vmax1,absmax(val));}}
  }
 }
 cout<<setprecision(24)<<"MASS ["<<mass.l<<","<<mass.h<<"] VMAX "<<vmax0<<" "<<vmax1<<"\n";cout.flush();
 if(vmax0>1500||vmax1>10000)throw runtime_error("declared V norm bound failed");
 q=p;vector<I>ca(KMAX+1),cb(KMAX+1),A(KMAX+2);I hs=rat(1,200);
 for(int k=0;k<=KMAX;k++){I aa(0),bb(0);for(uint64_t w=0;w<N;w++){aa=aa+q[w]*V0[w];bb=bb+q[w]*V1[w];}ca[k]=aa;cb[k]=bb;cout<<setprecision(24)<<"RAW "<<k<<" ["<<aa.l<<","<<aa.h<<"] ["<<bb.l<<","<<bb.h<<"]\n";cout.flush();if(k==KMAX)break;
  fill(work.begin(),work.end(),I(0));for(int bit=0;bit<n;bit++){uint64_t stride=1ULL<<bit;for(uint64_t block=0;block<N;block+=2*stride)for(uint64_t off=0;off<stride;off++){uint64_t w0=block+off,w1=w0+stride;I ss=q[w0]+q[w1];work[w0]=work[w0]-ss;work[w1]=work[w1]+ss;}}
  I scale=hs/I(k+1);for(uint64_t w=0;w<N;w++)q[w]=scale*work[w];
 }
 A[0]=ca[0];for(int k=1;k<=KMAX;k++)A[k]=ca[k]+hs*cb[k-1];A[KMAX+1]=hs*cb[KMAX];ofstream ac("./payment_coefficients_integer.txt");for(int k=0;k<=KMAX+1;k++){long long ll=(long long)floorl(dm(A[k].l,100000000)),hh=(long long)ceill(um(A[k].h,100000000));ac<<ll<<" "<<hh<<"\n";cout<<"COEFFICIENT "<<k<<" "<<ll<<" "<<hh<<" denominator 100000000\n";A[k]=I(dd(ll,100000000),ud(hh,100000000));}
 I x=rat(11,50),power(1);for(int k=1;k<=KMAX+1;k++)power=power*x/I(k);I tail=(I(vmax0)+hs*I(vmax1))*power/(I(1)-x/I(KMAX+2));if(tail.h>1e-6L)throw runtime_error("tail exceeds declared remainder");cout<<setprecision(24)<<"TAIL_UPPER "<<tail.h<<" DECLARED_REMAINDER 1/1000000\n";
 R ming=INFINITY,maxp=-INFINITY;for(int cell=0;cell<600;cell++){I a0=rat(4200+cell,200000),a1=rat(4201+cell,200000),aa(a0.l,a1.h),t=(aa-rat(1,40))*I(200),pp(0);for(int k=KMAX+1;k>=0;k--)pp=pp*t+A[k];pp=pp+I(-1e-6L,1e-6L);I cc=rat(261,200)+CS*aa,c=rat(19,20),dd0=rat(2,3)/(aa*(I(1)-aa))+rat(1,3)/((aa+c)*(I(1)-aa-c)),gap=pp-(cc-I(1))*dd0;ming=min(ming,gap.l);maxp=max(maxp,pp.h);if(gap.l<.04L||pp.h>19)throw runtime_error("interval payment not closed");}
 cout<<setprecision(24)<<"PAYMENT PASS cells 600 gap_lower "<<ming<<" P_upper "<<maxp<<" epsilon 1/25\n";
}
