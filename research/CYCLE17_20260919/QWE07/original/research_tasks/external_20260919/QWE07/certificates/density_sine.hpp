#pragma once
#include "cert_interval.hpp"
// pi enclosure is proved by exact Machin-series arithmetic in verify_density.py.
inline I pi_box(){return I(dd(3141592653589793238.L,1000000000000000000.L),ud(3141592653589793239.L,1000000000000000000.L));}
inline I sin_pi_rat(long long p,long long q){
 if(q<=0)throw std::runtime_error("sine denominator");
 p%=2*q;if(p>q)p-=2*q;if(p<-q)p+=2*q;
 if(2*p>q)p=q-p;if(2*p<-q)p=-q-p;
 if(!p)return I(0);if(2*p==q)return I(1);if(2*p==-q)return I(-1);
 I x=pi_box()*rat(p,q),xx=x*x,term=x,sum=x;
 for(int k=1;k<12;k++){term=-term*xx/I((2*k)*(2*k+1));sum=sum+term;}
 // |x| <= pi/2 < 8/5; (8/5)^25/25! < 1e-20.
 I rem=rat(1,10000000000LL)*rat(1,10000000000LL);
 return sum+I(-rem.h,rem.h);
}
inline std::vector<I> sine_Q(const std::vector<int>& co,long long num,long long den){
 int n=co.size();std::vector<I> q(n*n);for(int i=0;i<n;i++)for(int j=0;j<n;j++){long long d=co[i]-co[j];q[i*n+j]=d?sin_pi_rat(num*d,den)/(pi_box()*I(d)):rat(num,den);}return q;
}
