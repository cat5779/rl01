// S70 NEW: uniform c,p guard certificate. Adapted from the supplied S63
// guard branch-and-bound, with multivariate mixed-corner posterior fields.
#include "cert_interval_fast.hpp"
#include <omp.h>
using namespace std;
struct Mat2 {R x,y,w;};
I alpha(){return I(dd(2756644477108960247.L,10000000000000000000.L),ud(2756644477108960248.L,10000000000000000000.L));}
vector<I> Qmat(const vector<int>&co){int n=co.size();vector<I>q(n*n);I al=alpha();for(int i=0;i<n;i++)for(int j=0;j<n;j++){int d=co[i]-co[j];if(!d)q[i*n+j]=rat(1,3);else if(d%3==0)q[i*n+j]=I(0);else{int z=((d%6)+6)%6;q[i*n+j]=I(z==1||z==2?1:-1)*al/I(d);}}return q;}
I dplus(I c,I p){I a=(I(1)-c)*p;return (a+c)/a;}
I dminus(I c,I p){I a=(I(1)-c)*p;return (I(1)-a-c)/(I(1)-a);}
// Every entry in this finite inverse is an enclosure of a SINGLE mixed-corner
// comparison matrix. It is not interval inversion of a varying Gram matrix.
Mat2 guardmat(int sep,unsigned word,I cl,I ch,I pl,I ph,bool upper){
 vector<int>co={0,sep};for(int i=-4;i<=5;i++)if(i!=0&&i!=sep)co.push_back(i);
 int n=co.size();auto q=Qmat(co);
 I plus=upper?dplus(cl,ph):dplus(ch,pl);
 I minus=upper?dminus(ch,ph):dminus(cl,pl);
 I d=upper?dminus(ch,ph):dplus(ch,pl);
 vector<I>A(n*n),fields(n,I(1));for(int i=2;i<n;i++)fields[i]=((word>>(i-2))&1)?plus:minus;
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)A[i*n+j]=(i==j?d:I(0))+(fields[i]-d)*q[i*n+j];
 auto inv=invmat(A,n);I b[4];for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<n;k++)b[2*i+j]=b[2*i+j]+q[i*n+k]*inv[k*n+j];
 I sym=(b[1]+b[2])/I(2);R xx=(b[0].l+b[0].h)/2,yy=(b[3].l+b[3].h)/2,ww=(sym.l+sym.h)/2;
 R eps=ua(max(absmax(b[0]-I(xx)),absmax(b[3]-I(yy))),absmax(sym-I(ww)));
 if(eps>1e-6L)throw runtime_error("loose inverse"); // Actual eps, not this abort threshold, enters the Loewner bounds.
 return upper?Mat2{ua(xx,eps),ua(yy,eps),ww}:Mat2{da(xx,-eps),da(yy,-eps),ww};
}
struct Box{R x0,x1,y0,y1,z0,z1;};
struct Report{bool pass;uint64_t nodes;size_t peak;R worst;};
// Multi-affine q=(1-c)p+c m: extrema of the independent box are at vertices.
I output_mean(I c,I p,I m){R lo=INFINITY,hi=-INFINITY;for(R cc:{c.l,c.h})for(R pp:{p.l,p.h})for(R mm:{m.l,m.h}){I v=(I(1)-I(cc))*I(pp)+I(cc)*I(mm);lo=min(lo,v.l);hi=max(hi,v.h);}return I(lo,hi);}
Report certify(Mat2 L,Mat2 U,I c,I p,R cap,uint64_t maxnodes){
 if(U.x<L.x||U.y<L.y)throw runtime_error("inverted Loewner diagonals");
 R halfw=sqrtup(um(ua(U.x,-L.x),ua(U.y,-L.y)))/2;
 R midlo=da(L.w,U.w)/2,midhi=ua(L.w,U.w)/2;
 vector<Box>st={{L.x,U.x,L.y,U.y,da(midlo,-halfw),ua(midhi,halfw)}};uint64_t nodes=0;size_t peak=1;
 R atom=dm(da(1,-c.h),min(p.l,da(1,-p.h))),atomlower=dm(atom,atom);
 if(!(atomlower>0))throw runtime_error("nonlegal box");
 I c2=c*c;
 R aLL=dm(da(1,-c.l),p.l),aHL=dm(da(1,-c.h),p.l),aLU=um(ua(1,-c.l),p.h),aHU=um(ua(1,-c.h),p.h);
 auto qbound=[&](R ml,R mh){return I(min(da(aLL,dm(c.l,ml)),da(aHL,dm(c.h,ml))),max(ua(aLU,um(c.l,mh)),ua(aHU,um(c.h,mh))));};
 while(!st.empty()){
  Box b=st.back();st.pop_back();nodes++;bool dead=false;
  for(int it=0;it<3;it++){
   R dl=sqlo(da(b.z0,-L.w),ua(b.z1,-L.w)),du=sqlo(da(b.z0,-U.w),ua(b.z1,-U.w));
   R xl=ua(b.x1,-L.x),yl=ua(b.y1,-L.y),xu=ua(U.x,-b.x0),yu=ua(U.y,-b.y0);
   if(um(xl,yl)<dl||um(xu,yu)<du){dead=true;break;}
   if(dl>0){b.x0=max(b.x0,da(L.x,dd(dl,yl)));b.y0=max(b.y0,da(L.y,dd(dl,xl)));}
   if(du>0){b.x1=min(b.x1,ua(U.x,-dd(du,yu)));b.y1=min(b.y1,ua(U.y,-dd(du,xu)));}
   if(b.x0>b.x1||b.y0>b.y1){dead=true;break;}
   R wl=sqrtup(um(ua(b.x1,-L.x),ua(b.y1,-L.y))),wu=sqrtup(um(ua(U.x,-b.x0),ua(U.y,-b.y0)));
   b.z0=max({b.z0,da(L.w,-wl),da(U.w,-wu)});b.z1=min({b.z1,ua(L.w,wl),ua(U.w,wu)});
   if(b.z0>b.z1){dead=true;break;}
  }
  if(dead)continue;
  I q=qbound(b.x0,b.x1),r=qbound(b.y0,b.y1);
  I ss=c2*I(sqlo(b.z0,b.z1),sqhi(b.z0,b.z1));
  I AA=(I(1)-q)*(I(1)-r)-ss,DD=q*r-ss;
  R A0=max(atomlower,AA.l),D0=max(atomlower,DD.l),A1=AA.h,D1=DD.h;
  if(A1<=0||D1<=0)continue;
  R xlo=dd(ss.l,um(A1,D1)),xhi=ud(ss.h,dm(A0,D0)),dlo=max((R)0,da(A0,D0));
  R ub=ud(lfunup(xhi),da(1,dm(dlo,xlo)));if(ub<=cap)continue;
  if(nodes>=maxnodes)return{false,nodes,st.size(),ub};
  R dx=b.x1-b.x0,dy=b.y1-b.y0,dz=b.z1-b.z0;Box other=b;
  if(dx>=dy&&dx>=dz){R m=(b.x0+b.x1)/2;if(m==b.x0||m==b.x1)return{false,nodes,st.size(),ub};b.x1=m;other.x0=m;}
  else if(dy>=dz){R m=(b.y0+b.y1)/2;if(m==b.y0||m==b.y1)return{false,nodes,st.size(),ub};b.y1=m;other.y0=m;}
  else{R m=(b.z0+b.z1)/2;if(m==b.z0||m==b.z1)return{false,nodes,st.size(),ub};b.z1=m;other.z0=m;}
  st.push_back(b);st.push_back(other);peak=max(peak,st.size());
 }
 return{true,nodes,peak,0};
}
I Cglobal(I c,I p){return rat(1303,1000)+rat(51,200)*p+I(8)*(c-rat(19,20));}
int main(int argc,char**argv){try{
 fesetround(FE_UPWARD);
 // sep nc np start_job end_job threads maxnodes width; ch=.95+width/2000
 int sep=argc>1?stoi(argv[1]):1,nc=argc>2?stoi(argv[2]):7,np=argc>3?stoi(argv[3]):6;
 int first=argc>4?stoi(argv[4]):0,last=argc>5?stoi(argv[5]):nc*np*256,threads=argc>6?stoi(argv[6]):4;
 uint64_t limit=argc>7?stoull(argv[7]):2000000; int width=argc>8?stoi(argv[8]):7;
 if((sep<1||sep>3)||nc<=0||np<=0||first<0||last>nc*np*256||last<first)throw runtime_error("arguments");
 vector<int>lo(256),hi(256),tau(256);ifstream f("guard_caps_integer.txt"),tf(sep==3?"quad_tau3_integer.txt":"far_tau_integer.txt");
 for(int z=0;z<256;z++)if(!(f>>lo[z]>>hi[z])||!(tf>>tau[z]))throw runtime_error("input");
 set<int> selected; if(argc>9){istringstream ss(argv[9]);string token;while(getline(ss,token,',')){int z=stoi(token);if(z<0||z>255)throw runtime_error("selected word");selected.insert(z);}}
 int passed=0,failed=0;uint64_t totalnodes=0;auto start=chrono::steady_clock::now();omp_set_num_threads(threads);
 #pragma omp parallel for schedule(dynamic)
 for(int job=first;job<last;job++){
  fesetround(FE_UPWARD);int z=job%256,cp=job/256,ic=cp/np,ip=cp%np;
  if(!selected.empty()&&!selected.count(z))continue;
  try{
   I cl=rat(1900*nc+width*ic,2000*nc),ch=rat(1900*nc+width*(ic+1),2000*nc);
   I pl=rat(42*np+6*ip,100*np),ph=rat(42*np+6*(ip+1),100*np);
   auto L=guardmat(sep,z,cl,ch,pl,ph,false),U=guardmat(sep,z,cl,ch,pl,ph,true);
   R cap;if(sep==1){auto fun=[&](I p){I a=p/I(20);return ((rat(3,100)-a)*I(lo[z])+(a-rat(1,50))*I(hi[z]))/I(100)+rat(1,50);};cap=min(fun(pl).l,fun(ph).l);}
   else cap=(Cglobal(cl,pl)-rat(tau[z],1000)).l;
   auto rep=certify(L,U,I(cl.l,ch.h),I(pl.l,ph.h),cap,limit);
   #pragma omp critical
   {totalnodes+=rep.nodes;passed+=rep.pass;failed+=!rep.pass;cout<<setprecision(22)<<"GUARD sep "<<sep<<" job "<<job<<" word "<<z<<" ic "<<ic<<" ip "<<ip<<" "<<(rep.pass?"PASS":"FAIL")<<" nodes "<<rep.nodes<<" cap "<<cap<<" worst "<<rep.worst<<"\n";cout.flush();}
  }catch(exception&e){
   #pragma omp critical
   {failed++;cerr<<"ERROR job "<<job<<" "<<e.what()<<"\n";}
  }
 }
 cerr<<setprecision(16)<<"SUMMARY sep "<<sep<<" range "<<first<<" "<<last<<" passed "<<passed<<" failed "<<failed<<" nodes "<<totalnodes<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
 return failed?2:0;
 }catch(exception&e){cerr<<e.what()<<"\n";return 1;}}
