# S60 cycle09 bundle

Files:

- `S60_CYCLE09_RESULT.md` — complete mathematical report.
- `s60_checks.py` — exact arithmetic checks and optional floating falsification search.

Suggested exact check:

```bash
python s60_checks.py --exact
```

Optional floating search:

```bash
python s60_checks.py --random --n 5 --trials 5000
```

The report's main universal verdict is **INCOMPLETE**. Floating output is not a counterexample certificate.
