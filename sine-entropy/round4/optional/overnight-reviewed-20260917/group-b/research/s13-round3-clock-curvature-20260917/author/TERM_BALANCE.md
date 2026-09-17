# Exact term balance and sign ledger

All quantities below are for even `n`, half density, and the corrected law

`qhat_l(a)=u_l exp(tauhat_l(a)L_l) r_l^max`,
`tauhat_l=-log(theta_nl(z(a,c)))/gamma_2l`.

## 1. Conditional time response

Let

`K_l(t)=D(u_l e^(tL_l)r_l^max || u_l)`,
`I_l(t)=-K_l'(t)>=0`,
`P_l(t)=E_(q_l,t)U-E_(u_l)U=A_l e^(-gamma_2l t)`.

For the Fourier Gibbs reference,

`D_l(t)=K_l(t)-P_l(t)+B_nl`,

hence

`D_(l,t)=-I_l+gamma_2l P_l`,
`D_(l,tt)=-I_l'-gamma_2l^2 P_l`.

The complete layer chain rule is

`Dhat_l'=tau_l'(-I_l+gamma_2l P_l)`,

`Dhat_l''=tau_l''(-I_l+gamma_2l P_l)
 +(tau_l')^2(-I_l'-gamma_2l^2 P_l)`.

## 2. Actual moving count weights

Before any estimate,

`Dhat_F''=sum_l [
  pi_l'' D_l
 +2 pi_l' tau_l'(-I_l+gamma_2l P_l)
 +pi_l tau_l''(-I_l+gamma_2l P_l)
 +pi_l (tau_l')^2(-I_l'-gamma_2l^2 P_l)]`.

Relative to the uniform slice law,

`Khat_n''=sum_l [
 pi_l'' K_l
 -2 pi_l' tau_l' I_l
 -pi_l tau_l'' I_l
 -pi_l (tau_l')^2 I_l']`.

No count derivative, score-layer term, Fisher term, or time acceleration is
silently removed.

## 3. Reference cancellation

Potential matching gives

`Dhat_F''=Khat_n''-2n log n-(sum_l pi_l log binom(n,l))''`.

The correction is preserved explicitly:

- `(E M log n)''=0`;
- `(E U_n(Y))''=2n log n`;
- therefore the `-2n log n` term comes from the negative potential expectation.

Also

`Hhat''=Phi''-Khat_n''`,
`Phi=H(M)+sum_l pi_l log binom(n,l)`.

## 4. Midpoint decomposition

At `a_*=(1-c)/2`, `z'(a_*)=0`, so every first-clock and cross term vanishes
for an exact reason. Then

`Khat_n''(a_*)=W_n(c)+C_n(c)`,

`W_n(c)=sum_l pi_l'' K_l`  (**unpaid**),

`C_n(c)=sum_l pi_l[-tau_l''] I_l`  (**paid this round**).

Theorem 3.1 proves

`liminf C_n(c)/n >= 2 D_pair(c)/(1-c^2)>0`.

Thus `C_n` contributes positively to `Dhat_F''` and negatively, favorably, to
`Hhat''`. This is not a full sign because `W_n` is live.

## 5. Explicit constant

Let `d=c^2/pi^2`, `p_-=1/4-d`, `p_+=1/4+d`. Then

`D_pair(c)=2[p_- log(4p_-)+p_+ log(4p_+)]`.

At `c=19/20`,

`D_pair=0.06847130817780112...`,
`2D_pair/(1-c^2)=1.4045396549292533...`.
