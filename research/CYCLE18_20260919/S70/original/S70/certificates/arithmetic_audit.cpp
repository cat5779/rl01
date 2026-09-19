// S70 independent audit of outward arithmetic, including the faster log.
// Exact interpretation/checking of every emitted binary number is in
// arithmetic_audit.py. The mathematical enclosure argument remains in RESULT.
#include "cert_interval_fast.hpp"
using namespace std;
string hexnum(R x){if(!isfinite(x))throw runtime_error("nonfinite audit number");char buf[128];snprintf(buf,sizeof(buf),"%.20La",x);return buf;}
void emit(const string&tag,int mode,R a,R b,I result){cout<<tag<<' '<<mode<<' '<<hexnum(a)<<' '<<hexnum(b)<<' '<<hexnum(result.l)<<' '<<hexnum(result.h)<<'\n';}
int main(){uint64_t seed=0x4f7037301234abcdULL;int modes[4]={FE_TONEAREST,FE_UPWARD,FE_DOWNWARD,FE_TOWARDZERO};
 for(int mode:modes){fesetround(mode);for(int k=0;k<1000;k++){
  seed=seed*6364136223846793005ULL+1442695040888963407ULL;R a=ldexpl((R)(seed>>1),-63+(k%17)-8);if(k&1)a=-a;
  seed=seed*6364136223846793005ULL+1442695040888963407ULL;R b=ldexpl((R)((seed>>1)|1),-63+(k%13)-6);if(k&2)b=-b;
  if(k%11==0)b=-a;if(k%17==0)b=a;
  emit("add",mode,a,b,I(a)+I(b));emit("sub",mode,a,b,I(a)-I(b));emit("mul",mode,a,b,I(a)*I(b));if(b)emit("div",mode,a,b,I(a)/I(b));
  R x=fabsl(a);emit("sqrt",mode,x,0,I(sqrtup(x)));
  if(k%64==0){R y=1+x;emit("log",mode,y,0,I(logupper(y)));emit("L",mode,x,0,I(lfunup(x)));}
 }}
 return 0;
}
