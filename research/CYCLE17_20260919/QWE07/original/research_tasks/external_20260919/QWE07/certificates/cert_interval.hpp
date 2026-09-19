#pragma once
#include <bits/stdc++.h>
#include <cfenv>
#pragma STDC FENV_ACCESS ON
using R=long double;
static_assert(std::numeric_limits<R>::radix==2 && std::numeric_limits<R>::digits==64,"Verifier requires 64-significand-bit binary long double");
inline R ua(R a,R b){if(a==0)return b;if(b==0)return a;if(a==-b)return 0;volatile R z=a+b;return nextafterl(z,INFINITY);}
inline R um(R a,R b){if(a==0||b==0)return 0;if(a==1)return b;if(b==1)return a;volatile R z=a*b;return nextafterl(z,INFINITY);}
inline R ud(R a,R b){if(a==0)return 0;if(b==1)return a;if(a==b)return 1;volatile R z=a/b;return nextafterl(z,INFINITY);}
inline R da(R a,R b){return -ua(-a,-b);}
inline R dm(R a,R b){return -um(-a,b);}
inline R dd(R a,R b){return -ud(-a,b);}
struct I{R l,h; I(R z=0):l(z),h(z){} I(R a,R b):l(a),h(b){if(!(a<=b))throw std::runtime_error("interval");}};
inline I rat(long long x,long long y){return I(dd((R)x,(R)y),ud((R)x,(R)y));}
inline I operator+(I a,I b){return I(da(a.l,b.l),ua(a.h,b.h));}
inline I operator-(I a,I b){return I(da(a.l,-b.h),ua(a.h,-b.l));}
inline I operator-(I a){return I(-a.h,-a.l);}
inline I operator*(I a,I b){return I(std::min({dm(a.l,b.l),dm(a.l,b.h),dm(a.h,b.l),dm(a.h,b.h)}),std::max({um(a.l,b.l),um(a.l,b.h),um(a.h,b.l),um(a.h,b.h)}));}
inline I operator/(I a,I b){if(b.l<=0&&b.h>=0)throw std::runtime_error("zero pivot");return a*I(dd(1,b.h),ud(1,b.l));}
inline R sqlo(R a,R b){if(a<=0&&b>=0)return 0;return std::min(dm(a,a),dm(b,b));}
inline R sqhi(R a,R b){return std::max(um(a,a),um(b,b));}
inline R absmax(I x){return std::max(fabsl(x.l),fabsl(x.h));}
inline R sqrtup(R x){if(x<=0)return 0;R z=nextafterl(sqrtl(x),INFINITY);while(dm(z,z)<x)z=nextafterl(z,INFINITY);return z;}
inline R log2upper(){// log 2 = 2 atanh(1/3), 30 terms and explicit geometric tail
 R t=ud(1,3), t2=um(t,t),p=t,s=0;
 for(int k=0;k<30;k++){s=ua(s,ud(p,2*k+1));p=um(p,t2);}
 R tail=ud(p,dm(61,da(1,-t2)));return um(2,ua(s,tail));
}
inline R logupper(R x){if(x<1)throw std::runtime_error("log below one");if(x==1)return 0;int e;frexpl(x,&e);int k=e-1;R z=ldexpl(x,-k); // exact power-of-two scaling, z in [1,2)
 R t=ud(ua(z,-1),da(z,1));R t2=um(t,t),p=t,s=0;
 for(int j=0;j<24;j++){s=ua(s,ud(p,2*j+1));p=um(p,t2);}
 R tail=ud(p,dm(49,da(1,-t2)));R local=um(2,ua(s,tail));
 return ua(local,um(k,log2upper()));
}
inline R lfunup(R x){if(x<.0001L)return ua(1,um(x,.5L));R z=ua(1,x);return ud(um(z,logupper(z)),x);}
inline std::vector<I> invmat(std::vector<I> a,int n){std::vector<I>b(n*n);for(int i=0;i<n;i++)b[i*n+i]=I(1);
 for(int k=0;k<n;k++){int p=k;R best=0;for(int j=k;j<n;j++){R mid=(a[j*n+k].l+a[j*n+k].h)/2; if(fabsl(mid)>best){best=fabsl(mid);p=j;}}
  if(p!=k)for(int j=0;j<n;j++){std::swap(a[k*n+j],a[p*n+j]);std::swap(b[k*n+j],b[p*n+j]);}
  I pivot=a[k*n+k]; if(pivot.l<=0&&pivot.h>=0)throw std::runtime_error("ambiguous inverse");
  for(int j=0;j<n;j++){a[k*n+j]=a[k*n+j]/pivot;b[k*n+j]=b[k*n+j]/pivot;}
  a[k*n+k]=I(1);
  for(int i=0;i<n;i++)if(i!=k){I f=a[i*n+k];for(int j=0;j<n;j++){a[i*n+j]=a[i*n+j]-f*a[k*n+j];b[i*n+j]=b[i*n+j]-f*b[k*n+j];}a[i*n+k]=I(0);}
 }return b;
}

