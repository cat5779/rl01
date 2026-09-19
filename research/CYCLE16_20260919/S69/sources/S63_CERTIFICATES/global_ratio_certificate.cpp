#include "cert_interval.hpp"
using namespace std;
int main(){fesetround(FE_UPWARD);I c=rat(19,20),rho=rat(1,3);uint64_t all=0;for(int cell=0;cell<60;cell++){
 I al=rat(420+cell,20000),ah=rat(421+cell,20000);
 I dmax=(al+c)/al,dmin=(I(1)-ah-c)/(I(1)-ah);
 I LL=al+c*rho/(rho+dmax*(I(1)-rho)),UU=ah+c*rho/(rho+dmin*(I(1)-rho));
 I ell0=LL/(I(1)-LL),r0=UU/(I(1)-UU);I ell(ell0.l),r(r0.h);
 if(!(ell.h<1&&r.l>1&&(ell*r).h<1))throw runtime_error("regime");
 I C=rat(261,200)+rat(51,10)*al;R cap=C.l;
 vector<pair<R,R>>st={{0,ua(um(r.h,r.h),-1)}};uint64_t nodes=0;
 while(!st.empty()){auto xx=st.back();st.pop_back();nodes++;
  I x(xx.first,xx.second),RR=I(1)+x,di=(I(1)+r*ell)/(I(1)+r+r*ell+ell*RR);
  R ub=ud(lfunup(xx.second),da(1,dm(di.l,xx.first)));
  if(ub<=cap)continue;
  if(nodes>1000000)throw runtime_error("node limit");
  R m=(xx.first+xx.second)/2;if(m==xx.first||m==xx.second)throw runtime_error("stalled");st.push_back({xx.first,m});st.push_back({m,xx.second});
 }
 all+=nodes;cout<<setprecision(21)<<"global cell "<<cell<<" PASS nodes "<<nodes<<" C_lower "<<cap<<"\n";
 }
 cerr<<"GLOBAL PASS cells 60 nodes "<<all<<"\n";
}
