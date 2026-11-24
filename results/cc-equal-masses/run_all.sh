#!/bin/sh
# Rebuild and check everything that the certificates need. Run from the repository root:
#   sh results/cc-equal-masses/run_all.sh
# Stage 1 (hours, floating point, finds candidates only) is not run here. The stored candidate lists are in candidates/.
# To redo stage 1 with a fresh seed:  python3 results/cc-equal-masses/census.py 8 1200 11 census_n8.json
#   (arguments: n, seconds, seed, output), then merge_census.py and the candidate lists. See README.md.
# Stage 2 builds the certificates with Arb and checks that they equal the stored ones.
# Stage 3 checks them with the exact-rational verifier (also under -O). Stage 4 is a numerical spot check.
set -e
P=${PYTHON:-python3}
D=results/cc-equal-masses
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT
for n in 8 9 10; do
  $P $D/cert_arb.py $D/candidates/merged_n$n.json $T/cert_n$n.json > $T/cert_n$n.out
  cmp $T/cert_n$n.json certificates/cc-a1-n$n.json
  $P -I $D/verify_rational.py certificates/cc-a1-n$n.json
  $P -I -O $D/verify_rational.py certificates/cc-a1-n$n.json
done
$P $D/spot_cc.py certificates/cc-a1-n8.json certificates/cc-a1-n9.json certificates/cc-a1-n10.json
