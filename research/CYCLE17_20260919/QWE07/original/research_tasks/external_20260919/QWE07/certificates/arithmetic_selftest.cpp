#include "cert_interval.hpp"
#include "exact_fixed.hpp"
using namespace std;
using Qrat=boost::multiprecision::cpp_rational;
using Big=boost::multiprecision::cpp_int;
Qrat exact(R x){
 if(!isfinite(x))throw runtime_error("nonfinite test input");
 if(x==0)return 0;
 int e;R f=frexpl(fabsl(x),&e);uint64_t m=(uint64_t)ldexpl(f,64);
 Qrat z=Big(m);int s=e-64;if(s>=0)z*=Big(1)<<s;else z/=Big(1)<<(-s);
 return x<0?-z:z;
}
void check(bool b,const char* message){if(!b)throw runtime_error(message);}
int main(){
 mt19937_64 rng(0x536333ULL);uint64_t checks=0;
 for(int mode:{FE_TONEAREST,FE_UPWARD,FE_DOWNWARD,FE_TOWARDZERO}){
  if(fesetround(mode))throw runtime_error("rounding mode unsupported");
  for(int k=0;k<4096;k++){
   uint64_t ma=rng(),mb=rng();int ea=int(rng()%241)-120,eb=int(rng()%241)-120;
   R a=ldexpl((R)ma,ea-64),b=ldexpl((R)mb,eb-64);
   if(rng()&1)a=-a;if(rng()&1)b=-b;
   if(k<20){a=k%5-2;b=(k/5)-2;}
   Qrat A=exact(a),Bq=exact(b);
   check(exact(da(a,b))<=A+Bq,"addition lower");
   check(exact(ua(a,b))>=A+Bq,"addition upper");
   check(exact(dm(a,b))<=A*Bq,"multiply lower");
   check(exact(um(a,b))>=A*Bq,"multiply upper");checks+=4;
   if(b!=0){check(exact(dd(a,b))<=A/Bq,"divide lower");check(exact(ud(a,b))>=A/Bq,"divide upper");checks+=2;}
  }
 }
 for(int a=-97;a<=97;a++)for(int b=-31;b<=31;b++)if(b){
  W q=floordiv(W(a),W(b));Qrat v=Qrat(a)/b;
  check(Qrat(q.convert_to<string>())<=v&&v<Qrat((q+1).convert_to<string>()),"fixed floor");
  W r=ceildiv(W(a),W(b));check(Qrat((r-1).convert_to<string>())<v&&v<=Qrat(r.convert_to<string>()),"fixed ceil");checks+=2;
 }
 fesetround(FE_UPWARD);
 for(int k=0;k<4096;k++){
  long long a=(long long)(rng()%2000001)-1000000,b=(long long)(rng()%1000000)+1;
  BI v=br(a,b);Qrat target=Qrat(a)/b;
  check(Qrat(v.l.convert_to<string>())/Qrat(UNIT.convert_to<string>())<=target,"fixed rational lower");
  check(Qrat(v.h.convert_to<string>())/Qrat(UNIT.convert_to<string>())>=target,"fixed rational upper");
  check(exact(tolo(v.l))<=Qrat(v.l.convert_to<string>())/Qrat(UNIT.convert_to<string>()),"binary conversion lower");
  check(exact(tohi(v.h))>=Qrat(v.h.convert_to<string>())/Qrat(UNIT.convert_to<string>()),"binary conversion upper");checks+=4;
 }
 cout<<"ARITHMETIC SELFTEST PASS exact comparisons "<<checks<<"; four rounding modes; checked signed division and endpoint conversion.\n";
}

