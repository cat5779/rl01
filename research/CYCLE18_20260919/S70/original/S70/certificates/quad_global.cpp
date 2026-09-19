// S70 NEW: continuum global scalar pair-cap certificate in c,p.
#include "cert_interval_fast.hpp"
#include <omp.h>
using namespace std;
int main(int argc,char**argv){try{
 fesetround(FE_UPWARD);int nc=argc>1?stoi(argv[1]):80,np=argc>2?stoi(argv[2]):240,threads=argc>3?stoi(argv[3]):1,width=argc>4?stoi(argv[4]):7;
 if(nc<=0||np<=0)throw runtime_error("grid arguments");
 uint64_t all=0;int passed=0,failed=0;omp_set_num_threads(threads);
 #pragma omp parallel for schedule(dynamic)
 for(int cell=0;cell<nc*np;cell++){
  fesetround(FE_UPWARD);try{
   int ic=cell/np,ip=cell%np;I cl=rat(1900*nc+width*ic,2000*nc),ch=rat(1900*nc+width*(ic+1),2000*nc),pl=rat(42*np+6*ip,100*np),ph=rat(42*np+6*(ip+1),100*np),rho=rat(1,3);
   I al=(I(1)-ch)*pl,ah=(I(1)-cl)*ph;
   I atplus=(I(1)-ch)*pl,atminus=(I(1)-ch)*ph;
   I dmax=(atplus+ch)/atplus,dmin=(I(1)-atminus-ch)/(I(1)-atminus);
   I LL=al+cl*rho/(rho+dmax*(I(1)-rho)),UU=ah+ch*rho/(rho+dmin*(I(1)-rho));
   I ell0=LL/(I(1)-LL),r0=UU/(I(1)-UU),ell(ell0.l),r(r0.h);
   if(!(ell.h<1&&ell.l>0&&r.l>1&&(ell*r).h<1))throw runtime_error("regime");
   R cap=(rat(1303,1000)+rat(51,200)*pl+I(8)*(cl-rat(19,20))).l;
   vector<pair<R,R>>st={{0,ua(um(r.h,r.h),-1)}};uint64_t nodes=0;
   while(!st.empty()){
    auto xx=st.back();st.pop_back();nodes++;I x(xx.first,xx.second),RR=I(1)+x,di=(I(1)+r*ell)/(I(1)+r+r*ell+ell*RR);
    R ub=ud(lfunup(xx.second),da(1,dm(di.l,xx.first)));if(ub<=cap)continue;
    if(nodes>1000000)throw runtime_error("node limit");R m=(xx.first+xx.second)/2;if(m==xx.first||m==xx.second)throw runtime_error("stalled");st.push_back({xx.first,m});st.push_back({m,xx.second});
   }
   #pragma omp critical
   {all+=nodes;passed++;cout<<setprecision(22)<<"GLOBAL cell "<<cell<<" ic "<<ic<<" ip "<<ip<<" PASS nodes "<<nodes<<" cap "<<cap<<"\n";}
  }catch(exception&e){
   #pragma omp critical
   {failed++;cerr<<"ERROR global "<<cell<<" "<<e.what()<<"\n";}
  }
 }
 cerr<<"SUMMARY global passed "<<passed<<" failed "<<failed<<" cells "<<nc*np<<" nodes "<<all<<"\n";return failed?2:0;
 }catch(exception&e){cerr<<e.what()<<"\n";return 1;}}
