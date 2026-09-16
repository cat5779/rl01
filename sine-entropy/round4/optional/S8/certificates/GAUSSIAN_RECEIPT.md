# Restoring the exact 34-site Gaussian receipt

The canonical checker produces one JSON file named `gaussian_n34.json`. Its
source receipt is large enough that this connector upload stores it losslessly
as five text parts instead of one GitHub contents write.

Canonical source receipt:

```text
SHA-256  ea2d502f3592e1af4402aa3f9b8eda9f3d7fb82f4cb39ca5b1047b326d17e322
size     209627 bytes
```

It was compressed with Python `gzip.compress(source, mtime=0)` and then base64
encoded. The compressed byte stream has

```text
SHA-256  47562250ab85e1d160419100f1fd95a665be2628ecc8e487bcc5193abd2c3cc5
```

The base64 text is stored, in order, as

```text
gaussian_n34.json.gz.b64.part00
gaussian_n34.json.gz.b64.part01
gaussian_n34.json.gz.b64.part02
gaussian_n34.json.gz.b64.part03
gaussian_n34.json.gz.b64.part04
```

On a POSIX shell, restore the exact checker receipt with

```sh
cat research/s8-round2-higher-rank-20260916/certificates/gaussian_n34.json.gz.b64.part0[0-4] \
  | base64 -d | gzip -d > /tmp/gaussian_n34.json
sha256sum /tmp/gaussian_n34.json
```

The hash must be
`ea2d502f3592e1af4402aa3f9b8eda9f3d7fb82f4cb39ca5b1047b326d17e322`.
This is a transport representation only: no atoms, multiplicities, jets, or
interval endpoints are omitted. The standard-library checker independently
regenerates the same JSON when run as documented in `../RESULT.md`.
