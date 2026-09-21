# Reviewer-supplied completion from independent RL01 PR66

Verbatim review section, completing the source phrase direct binary calculation without additional assumptions.

## 5. 补全 posterior-variance payment

这是可见稿最需要补写的步骤。

固定一条 oriented edge \((i,y)\)，记

\[
P=P_y,\quad Q=P_{y^i},\quad M=(P+Q)/2,
\]

并始终用未翻转的 \(y\) 定义 \(\zeta=\sigma_i\tau_i\)。因为 \(P,Q\) 只在第 \(i\) 个 binary factor 上相反，\(M\) 下 \(\zeta\) 是公平符号，而且

\[
\frac{dP}{dM}=1-k\zeta,
\qquad
\frac{dQ}{dM}=1+k\zeta.
\]

令

\[
m(t)=\mathbb E_M[\zeta\mid T=t].
\]

通过任意固定 Markov channel \(W\) 后，真实输出参考权重是 \(M^W\)，并有

\[
\frac{dP^W}{dM^W}=1-km(t),
\qquad
\frac{dQ^W}{dM^W}=1+km(t).
\]

因此

\[
J(P^W,Q^W)
=4k\,\mathbb E_{M^W}[m(T)\operatorname{atanh}(km(T))].
\]

输入 Jeffreys 是 \(4k\operatorname{atanh}(k)=2kL\)。逐 edge 的归一化损失为

\[
1-\frac{\mathbb E_{M^W}[m\operatorname{atanh}(km)]}
{\operatorname{atanh}(k)}.
\]

函数 \(\operatorname{atanh}\) 在 \([0,1)\) 上凸且过原点，所以对 \(0\le u\le1\)，

\[
\operatorname{atanh}(ku)\le u\operatorname{atanh}(k).
\]

利用 \(m\operatorname{atanh}(km)\) 的偶性，得到

\[
m\operatorname{atanh}(km)
\le m^2\operatorname{atanh}(k).
\]

故逐 edge 损失至少为

\[
\mathbb E_{M^W}[1-m(T)^2]
=\mathbb E_{M^W}\operatorname{Var}_M(\zeta\mid T).
\]

最后对 \(i\) 和均匀 \(y\) 平均。因为每条输入 edge 的 \(J_{in}=2kL\) 相同，平均后的左边恰是 \(\eta_J\)，右边恰是正文的 \(\overline V_W\)。这证明

\[
\eta_J\ge\overline V_W.
\]

没有把 \(M^W\) 换成 \(P^W\) 或均匀输出权重，也没有把不同 \(y\) 的 reference 混为一个全局 measure。

