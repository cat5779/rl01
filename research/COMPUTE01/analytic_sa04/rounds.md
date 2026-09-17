# Rounds

## Round 1

- Froze the positive-central-difference target.
- Audited PR #4: it contains the assignment only, not a competing result.
- Promoted a binary-testing witness for the deletion term.
- Proved `A_k>=c^4/72` for every `k>=2`.
- Main target remains incomplete at the explicit asymptotic obstruction
  `limsup E_k<2c^4/9`.

## Round 2

- Strengthened the deletion result to `liminf A_k>=2c^4/9`.
- Proved `s_k-s_(k-1)=1/(2k^2)+O(k^-3)`.
- Since the raw layer rate is `k^2-1`, the bridge contains asymptotically one
  half exchange on average.  This rules out the shortcut "the time gap tends
  to zero, hence E_k tends to zero".
- The remaining object is the limiting entropy cost of that finite exchange
  window.
