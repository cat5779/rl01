#pragma once
#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
using namespace boost::multiprecision;
using B=number<cpp_int_backend<256,256,signed_magnitude,checked,void>>;
using W=number<cpp_int_backend<512,512,signed_magnitude,checked,void>>;
constexpr int PREC=192;
const B UNIT=B(1)<<PREC;
inline W floordiv(W a,W b){W q=a/b,r=a%b;if(r!=0&&((a<0)!=(b<0)))--q;return q;}
inline W ceildiv(W a,W b){return -floordiv(-a,b);}
inline B mlo(B a,B b){W z=W(a)*W(b);return B(floordiv(z,W(UNIT)));}
inline B mhi(B a,B b){W z=W(a)*W(b);return B(ceildiv(z,W(UNIT)));}
inline B dlo(B a,B b){return B(floordiv(W(a)*W(UNIT),W(b)));}
inline B dhi(B a,B b){return B(ceildiv(W(a)*W(UNIT),W(b)));}
struct BI{B l,h;BI():l(0),h(0){} BI(int z):l(B(z)*UNIT),h(l){} BI(B x,B y):l(x),h(y){if(l>h)throw std::runtime_error("fixed interval bad");}};
inline BI br(long long n,long long d){return BI(B(floordiv(W(n)*W(UNIT),W(d))),B(ceildiv(W(n)*W(UNIT),W(d))));}
inline BI bdec(const std::string& n,const std::string& d){W nn(n),dd(d);return BI(B(floordiv(nn*W(UNIT),dd)),B(ceildiv(nn*W(UNIT),dd)));}
inline BI operator+(const BI&a,const BI&b){return BI(a.l+b.l,a.h+b.h);}
inline BI operator-(const BI&a,const BI&b){return BI(a.l-b.h,a.h-b.l);}
inline BI operator-(const BI&a){return BI(-a.h,-a.l);}
inline BI operator*(const BI&a,const BI&b){B l=std::min({mlo(a.l,b.l),mlo(a.l,b.h),mlo(a.h,b.l),mlo(a.h,b.h)}),h=std::max({mhi(a.l,b.l),mhi(a.l,b.h),mhi(a.h,b.l),mhi(a.h,b.h)});return BI(l,h);}
inline BI operator/(const BI&a,const BI&b){if(b.l<=0&&b.h>=0)throw std::runtime_error("fixed zero divide");return a*BI(dlo(UNIT,b.h),dhi(UNIT,b.l));}
inline BI bintersect(BI a,BI b){return BI(std::max(a.l,b.l),std::min(a.h,b.h));}
inline int compare_scaled_ld(const B& x,long double v){if(v==0)return x>0?1:(x<0?-1:0);int e;long double f=frexpl(fabsl(v),&e);uint64_t mant=(uint64_t)ldexpl(f,64);W m=mant;if(v<0)m=-m;int sh=e-64+PREC;W xx=x;if(sh>=0)m*=W(1)<<sh;else xx*=W(1)<<(-sh);return xx>m?1:(xx<m?-1:0);}
inline long double tolo(const B&x){long double z=ldexpl(x.convert_to<long double>(),-PREC);while(compare_scaled_ld(x,z)<0)z=nextafterl(z,-INFINITY);return z;}
inline long double tohi(const B&x){long double z=ldexpl(x.convert_to<long double>(),-PREC);while(compare_scaled_ld(x,z)>0)z=nextafterl(z,INFINITY);return z;}
inline std::pair<std::vector<BI>,BI> binverse(std::vector<BI>a,int n){std::vector<BI>b(n*n);for(int i=0;i<n;i++)b[i*n+i]=BI(1);BI det(1);for(int k=0;k<n;k++){BI piv=a[k*n+k];if(piv.l<=0)throw std::runtime_error("nonpositive exact pivot");det=det*piv;for(int j=0;j<n;j++){a[k*n+j]=a[k*n+j]/piv;b[k*n+j]=b[k*n+j]/piv;}a[k*n+k]=BI(1);for(int i=0;i<n;i++)if(i!=k){BI f=a[i*n+k];for(int j=0;j<n;j++){a[i*n+j]=a[i*n+j]-f*a[k*n+j];b[i*n+j]=b[i*n+j]-f*b[k*n+j];}a[i*n+k]=BI(0);}}return {b,det};}
