# An explicit positive convolution kernel with a spectral zero arc

Work on Gamma=Z and put

    f(theta)=(1-2|theta|/pi)_+^3, -pi<=theta<=pi.

Extend periodically. Let v_n=(1/(2pi)) integral_(-pi)^pi f(theta)e^(-in theta)dtheta.
The function is real and even. Direct integration, with a=pi/2, gives

    v_0=1/8,
    v_n=6/(pi^2 n^2)-48(1-cos(n pi/2))/(pi^4 n^4), n!=0.       (1)

For verification, before normalization the integral on [0,a] is
3a^2/n^2-6(1-cos(na))/n^4 for the cubic (a-theta)^3.
Dividing by pi a^3 gives (1). The zero-frequency integral is a/(4pi)=1/8.

We claim the explicit two-sided bounds

    1/[16(1+n^2)] <= v_n <= 1/(1+n^2).                         (2)

Use only 9<pi^2<10. For |n|=1, write x=pi^2; then
v_1=6(x-8)/x^2. It lies between 6/100 and 12/81, hence between
1/32 and 1/2. For |n|>=2, writing y=n^2>=4 and z=1-cos(n pi/2) in [0,2],
the numerator of (1) in the denominator x^2 y^2 is 6xy-48z.
It is at least 54y-96>=30y, while x^2<=100; hence v_n>=3/(10y).
Also v_n<=6/(xy)<=2/(3y)<=1/(1+y) for y>=2.
The lower 3/(10y)>=1/[16(1+y)] is immediate. n=0 is direct.
This proves (2), including strict positivity of every v_n.

Absolute summability follows. Its absolutely convergent Fourier series
has the coefficients of f and therefore equals f everywhere by Fourier
uniqueness and continuity. At theta=0 this gives sum_n v_n=f(0)=1.
Thus v is a symmetric strictly positive probability on Z. In particular
V is a self-adjoint contraction with multiplier f and H=V^2 has multiplier
f^2. (The operator positivity of V follows here from f>=0, but the general relative theorem only
requires the positivity of H=VV*.)

## Triple-convolution bound

Let rho_n=1/(1+n^2). If a+b+c=n, at least one of |a|,|b|,|c| is >=|n|/3.
For that index, say a, (2) gives

    v_a <= rho_a <= 9 rho_n.

Split the nonnegative convolution sum by the union of those three events.
For the first event, bound v_a by 9rho_n and sum v_b v_c over all b,c;
the probability normalization makes this at most 9rho_n. The other two
events have the same bound. Therefore

    (v*v*v)_n <= 27 rho_n <= 432 v_n.                         (3)

No limiting convolution exchange has signs; Tonelli suffices. The bound
is deliberately not optimized. It gives the triple-convolution hypothesis with M=432.

## Spectral separation

The multiplier f vanishes on the open arc pi/2<|theta|<pi. A finite Laurent polynomial whose squared modulus is dominated by f^2 must vanish on that arc, and hence identically. The central-coset version, including nonequivariant finite-propagation square minorants, is proved in [CENTER.md](CENTER.md). This is a classical Fourier-zero obstruction to a particular square-decomposition method, not a coupling counterexample.
