#include "cert_interval.hpp"
#include <omp.h>
using namespace std;
struct Mat2 {R x,y,w;};
I alpha(){ // enclosing rational endpoints, justified independently by Machin and square bounds
 return I(dd(2756644477108960247.L,10000000000000000000.L),ud(2756644477108960248.L,10000000000000000000.L));
}
vector<I> Qmat(const vector<int>& co){int n=co.size();vector<I>q(n*n);I al=alpha();for(int i=0;i<n;i++)for(int j=0;j<n;j++){int d=co[i]-co[j];if(!d)q[i*n+j]=rat(1,3);else if(d%3==0)q[i*n+j]=I(0);else {int dm6=((d%6)+6)%6;I sg=(dm6==1||dm6==2)?I(1):I(-1);q[i*n+j]=sg*al/I(d);}}return q;}
Mat2 guardmat(int rad,unsigned word,I a,bool upper){vector<int>co={0,1};for(int i=-rad;i<0;i++)co.push_back(i);for(int i=2;i<=rad+1;i++)co.push_back(i);int n=co.size();auto q=Qmat(co);I c=rat(19,20),dmax=(a+c)/a,dmin=(I(1)-a-c)/(I(1)-a),d=upper?dmin:dmax;
 vector<I>mat(n*n),fields(n,I(1));for(int i=2;i<n;i++)fields[i]=((word>>(i-2))&1)?dmax:dmin;
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)mat[i*n+j]=(i==j?d:I(0))+(fields[i]-d)*q[i*n+j];
 auto inv=invmat(mat,n);I b[4];for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<n;k++)b[i*2+j]=b[i*2+j]+q[i*n+k]*inv[k*n+j];
 I sym=(b[1]+b[2])/I(2);R xx=(b[0].l+b[0].h)/2,yy=(b[3].l+b[3].h)/2,ww=(sym.l+sym.h)/2;
 R e0=absmax(b[0]-I(xx)),e1=absmax(b[3]-I(yy)),ew=absmax(sym-I(ww));R eps=ua(max(e0,e1),ew);
 if(eps>1e-8L)throw runtime_error("loose guard inverse");
 if(upper)return {ua(xx,eps),ua(yy,eps),ww};else return {da(xx,-eps),da(yy,-eps),ww};
}
struct Box {R x0,x1,y0,y1,z0,z1;};
struct Report {bool pass;uint64_t nodes;size_t peak;R worst;};
Report certify(Mat2 L,Mat2 U,I a,R cap,uint64_t maxnodes){R mid=ua(L.w,U.w)/2; // midpoint enclosure offset handled below
 R halfw=sqrtup(um(ua(U.x,-L.x),ua(U.y,-L.y)))/2;
 R midlo=da(L.w,U.w)/2,midhi=ua(L.w,U.w)/2;
 vector<Box>st={{L.x,U.x,L.y,U.y,da(midlo,-halfw),ua(midhi,halfw)}};uint64_t nodes=0;size_t peak=1;I c=rat(19,20);R atomlower=dm(min(a.l,da(da(1,-a.h),-c.h)),min(a.l,da(da(1,-a.h),-c.h)));
 while(!st.empty()){auto b=st.back();st.pop_back();nodes++;bool dead=false;
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
  I q=a+c*I(b.x0,b.x1),r=a+c*I(b.y0,b.y1);I ss=c*c*I(sqlo(b.z0,b.z1),sqhi(b.z0,b.z1));
  I AA=(I(1)-q)*(I(1)-r)-ss,DD=q*r-ss;
  R A0=max(atomlower,AA.l),D0=max(atomlower,DD.l),A1=AA.h,D1=DD.h;
  if(A1<=0||D1<=0)continue;
  R xlo=dd(ss.l,um(A1,D1)),xhi=ud(ss.h,dm(A0,D0)),dlo=max((R)0,da(A0,D0));
  R ub=ud(lfunup(xhi),da(1,dm(dlo,xlo)));
  if(ub<=cap)continue;
  if(nodes>=maxnodes)return {false,nodes,st.size(),ub};
  R dx=b.x1-b.x0,dy=b.y1-b.y0,dz=b.z1-b.z0;Box other=b;
  if(dx>=dy&&dx>=dz){R m=(b.x0+b.x1)/2;if(m==b.x0||m==b.x1)return {false,nodes,st.size(),ub};b.x1=m;other.x0=m;}
  else if(dy>=dz){R m=(b.y0+b.y1)/2;if(m==b.y0||m==b.y1)return {false,nodes,st.size(),ub};b.y1=m;other.y0=m;}
  else{R m=(b.z0+b.z1)/2;if(m==b.z0||m==b.z1)return {false,nodes,st.size(),ub};b.z1=m;other.z0=m;}
  st.push_back(b);st.push_back(other);peak=max(peak,st.size());
 }return {true,nodes,peak,0};
}
int main(int argc,char**argv){fesetround(FE_UPWARD);int rad=4,nc=argc>1?stoi(argv[1]):6;int select=argc>2?stoi(argv[2]):-1;int threads=argc>3?stoi(argv[3]):4;uint64_t maxnodes=argc>4?stoull(argv[4]):2000000;vector<int>lo(256),hi(256);ifstream f("./guard_caps_integer.txt");for(int i=0;i<256;i++)f>>lo[i]>>hi[i];if(!f){cerr<<"caps input error";return 1;}
 uint64_t totalnodes=0;int passed=0,failed=0;omp_set_num_threads(threads);auto t0=chrono::steady_clock::now();
 #pragma omp parallel for schedule(dynamic)
 for(int job=(argc>5?stoi(argv[5]):0);job<(argc>6?stoi(argv[6]):nc*256);job++){fesetround(FE_UPWARD);int cell=job/256,word=job%256;if(select>=0&&word!=select)continue;
  try{I al=rat(21*nc+3*cell,1000*nc),ah=rat(21*nc+3*(cell+1),1000*nc);I aa(al.l,ah.h);auto L=guardmat(rad,word,al,false),U=guardmat(rad,word,ah,true);
   I capl=(rat(3,100)-al)*I(lo[word])*I(100)+(al-rat(1,50))*I(hi[word])*I(100);capl=capl/I(10000);
   I caph=(rat(3,100)-ah)*I(lo[word])*I(100)+(ah-rat(1,50))*I(hi[word])*I(100);caph=caph/I(10000);R cap=min(capl.l,caph.l);
   auto rep=certify(L,U,aa,cap,maxnodes);
   #pragma omp critical
   {totalnodes+=rep.nodes;if(rep.pass)passed++;else failed++;cout<<setprecision(21)<<"guard "<<word<<" cell "<<cell<<" "<<(rep.pass?"PASS":"FAIL")<<" nodes "<<rep.nodes<<" cap "<<cap<<" worst "<<rep.worst<<"\n";cout.flush();}
  }catch(exception&e){
   #pragma omp critical
   {failed++;cerr<<"ERROR word "<<word<<" cell "<<cell<<" "<<e.what()<<"\n";}
  }
 }
 cerr<<setprecision(17)<<"SUMMARY passed "<<passed<<" failed "<<failed<<" nodes "<<totalnodes<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n";return failed?2:0;
}
