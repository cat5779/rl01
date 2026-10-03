# C04 exact interval: star calibration does not identify the WUSF law

Status: scoped different-author review passed; see [REVIEW.md](REVIEW.md).

Let B be iid Bernoulli(1/2) bond percolation on the three-regular tree.
For lambda>1, contract every B-cluster and give a closed original edge uv
resistance lambda^(deg_B(u)+deg_B(v)). Take the weighted wired uniform
spanning forest of this quotient and lift its edges to the original tree,
adjoining B. Denote this upper law by T_lambda. This is the same family
as [CONSTRUCTION.md](CONSTRUCTION.md), with no change to its conditional law.

Set a=1137/1000 and b=229/200. For adjacent edges e,f and for edges e1,e3
in a three-edge path e1,e2,e3, prove

1. P(e,f absent from T_a)>1/12.
2. P(e,f absent from T_b)<1/12.
3. P(e1,e3 absent from T_lambda)>5/48 for every lambda in [a,b].

Hence at least one lambda in (a,b) gives exactly the unit WUSF law on
every one-vertex star, but its distance-two pair law is different.
Every parameter in this interval has the stated wrong distant-pair
cylinder. This does not locate a unique star root or cover star roots
outside this interval. It is not a counterexample to the original
Bernoulli/WUSF endpoint joining problem and gives no iid-factor joining.

All probabilities and integer certificates refer to the actual infinite
wired quotient law. A finite-depth or population approximation alone is
insufficient. The only new specialization of statement04 is the explicit
rational interval; its original goal and assumptions are unchanged.
