# Assumptions and fixed objects

- `c=19/20`, odd positive `R`, `N=R+1`, and `u in [1/N,1]`.
- The finite kernel is the actual Fejer Toeplitz compression on `[-R,R]`.
- The exterior word has its determinantal atom probability.  Spectral
  Bernoulli selections are used only inside an exact DPP sampler, never as the
  observed word.
- The normalized local kernel is exactly (V14).  Its four residual pieces are
  `phi''-8`, `B_(phi')`, the parameter derivative of `B_phi`, and the signed
  transport of `B_phi`.
- Binary64 enumeration and Monte Carlo are route-selection evidence, not
  interval proofs of the infinite-volume sign.
