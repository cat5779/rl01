#include <bits/stdc++.h>
using namespace std; using R=long double;
constexpr int n=22;constexpr uint64_t N=1ULL<<n;
void rec(const vector<R>&K,int m,R wt,uint64_t word,int dep,vector<R>&p){
 if(!m){p[word]=wt;return;} R q=K[0];if(q<=0||q>=1)throw runtime_error("bad probability");
 for(int bit=0;bit<2;bit++){R pr=bit?q:1-q;vector<R>L((m-1)*(m-1));
 for(int i=1;i<m;i++)for(int j=1;j<m;j++)L[(i-1)*(m-1)+j-1]=K[i*m+j]+(bit?-1:1)*K[i*m]*K[j]/pr;
 rec(L,m-1,wt*pr,word|(uint64_t(bit)<<dep),dep+1,p);}
}
vector<R> probs(R rho,R a){vector<R>K(n*n),p(N);R pi=acosl(-1.L);for(int i=0;i<n;i++)for(int j=0;j<n;j++){int d=i-j;K[i*n+j]=.95L*(d?sinl(pi*rho*d)/(pi*d):rho)+(i==j?a:0);}rec(K,n,1,0,0,p);return p;}
int main(int argc,char**argv){auto p=probs(1.L/3,.025L);vector<R> V0(N),V1(N);int lo[256],hi[256];ifstream f("guard_caps_integer.txt");for(int i=0;i<256;i++)f>>lo[i]>>hi[i];if(!f)throw runtime_error("caps");uint64_t bi=1<<10,bj=1<<11;int gp[8]={6,7,8,9,12,13,14,15};
 for(uint64_t base=0;base<N;base++)if(!(base&(bi|bj))){uint64_t ww[4]={base,base|bi,base|bj,base|bi|bj};R ff[4][2];unsigned z=0;for(int k=0;k<8;k++)z|=((base>>gp[k])&1)<<k;
 for(int s=0;s<4;s++){ff[s][0]=((s&1)?1:-1)*(1+p[ww[s^1]]/p[ww[s]]);ff[s][1]=((s&2)?1:-1)*(1+p[ww[s^2]]/p[ww[s]]);}
 for(int order=0;order<2;order++){R C=order?5.1L:1.4325L,delta=order?5.1L-(hi[z]-lo[z])/100.L:1.4325L-(lo[z]+hi[z])/20000.L;R gg[4][2],tt[4];
 for(int s=0;s<4;s++){gg[s][0]=C/2*ff[s][0]+delta*ff[s][1];gg[s][1]=C/2*ff[s][1]+delta*ff[s][0];tt[s]=C/2*(ff[s][0]*ff[s][0]+ff[s][1]*ff[s][1])+2*delta*ff[s][0]*ff[s][1];}
 for(int s=0;s<4;s++){R val=2*(gg[s|1][0]-gg[s&2][0]+gg[s|2][1]-gg[s&1][1])-tt[s];(order?V1:V0)[ww[s]]=val;}}
 }
 cout<<setprecision(17);
 vector<R> rr={1.L/3,1.L/3+1e-4L,1.L/3+1e-3L,.34L,.35L,.4L,.5L};if(argc>1){rr.clear();for(int i=1;i<argc;i++)rr.push_back(stold(argv[i]));}
 for(R rho:rr)for(R a:{.021L,.0225L,.024L}){auto q=probs(rho,a);R P=0,second=0,mass=0;for(uint64_t y=0;y<N;y++){R V=V0[y]+(a-.025L)*V1[y];P+=q[y]*V;second+=q[y]*V*V;mass+=q[y];}R d=(1-rho)/(a*(1-a))+rho/((a+.95L)*(.05L-a));cout<<"rho "<<rho<<" a "<<a<<" P "<<P<<" gap "<<P-(.305L+5.1L*a)*d<<" second "<<second<<" mass "<<mass<<endl;}
}
