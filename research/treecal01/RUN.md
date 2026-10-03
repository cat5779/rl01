# Portable checks

Run these commands from this directory with Python 3 and NumPy installed. The exact circuit sums and formal polynomial identity use only the Python standard library. NumPy is required for the three ordered int64 PMF checks. The optional independently authored symbolic network checker requires SymPy. NumPy 2.3.5 was used for the frozen PMF checks.

```text
python -X utf8 verify05.py grid06a1137q1000m16384upper.json --output checks/runa.json
python -X utf8 verify05.py grid06b229q200m16384lower.json --output checks/runblo.json
python -X utf8 verify05.py grid06b229q200m16384upper.json --output checks/runbhi.json
python -X utf8 post05.py grid06a1137q1000m16384upper.json --bins 128 --output checks/runstarlo.json
python -X utf8 post05.py grid06b229q200m16384lower.json --bins 128 --output checks/runstarhi.json
python -X utf8 far04check.py
python -X utf8 farverify04.py far04a1137q1000b229q200m16384k64.json --output checks/runfar.json
python -X utf8 circuit01.py
```

The first three must report PASS_EXACT_ONE_STEP_MESSAGE_ENCLOSURE with all directed CDF differences nonnegative. The two star margins must respectively be

    2354057016113552765273713883740284148 > 0,
    -7432073890617973008830827509244334014942502456169984 < 0.

The distant-pair verifier must report PASS_INDEPENDENT_ORDERED_FAR_CERTIFICATE and

    48N-5E=511814514048962940398470848577989620904633305120 > 0.

For the historical unit-resistance method, run `python -X utf8 history/verifygrid01.py`; it reconstructs the complete ordered finite certificate. No native search, warm-start source, population sample or external data is needed for any required check. Inputs resolve relative to their checking script or the certificate's neighboring PMF. Output paths can be chosen explicitly to retain the supplied receipts.

The computations verify finite integer signs. The infinite wired interpretation, conditional independence and interval/convex directions are analytic parts of THEOREM, BRIDGE and CONVEX; they are not proved by program output alone.
