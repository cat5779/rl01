# S7 certificate packaging repair

This directory stages only the PR111 delta after the previously reviewed head
`5950f93b927bad324f48dff7f17896e6554d645e`.

**Status: ACCEPTED_CERTIFICATE_REPAIR.**  The three restored scripts and six
committed certificate payloads reproduce.  This closes the earlier packaging
gap for the six-site witness and finite algebra checks.  The already accepted
analytic localization proof was not reviewed again.

`PRIOR_ANALYTIC_AUDIT.md` is the frozen earlier audit that identifies the
packaging gap closed here.

Run the commands in `REPRODUCE.md` from this directory.  They write fresh
outputs under `rerun/` and leave the committed payloads unchanged.
