#!/bin/sh
# Corrupted inputs. Every command below must end with FAIL (cert_arb.py) or REJECT (verify_rational.py),
# with and without -O. Run from the repository root:  sh results/cc-equal-masses/corrupt_tests.sh
# Uses a temporary directory; the corrupted files are not kept. Needs numpy and python-flint.
P=${PYTHON:-python3}
D=results/cc-equal-masses
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT
echo "== cert_arb.py with class 1 centre moved by 2^-12"
$P -O $D/cert_arb.py $D/candidates/merged_n8.json $T/never_written.json corrupt 2>&1 | tail -1
$P -I - "$T" <<'PYEOF'
import json, sys
T = sys.argv[1]
d = json.load(open('certificates/cc-a1-n8.json'))
def w(name, f):
    a = json.loads(json.dumps(d)); f(a); json.dump(a, open(T + '/' + name + '.json', 'w'))
w('n8_coord_moved', lambda a: a['classes'][4]['centre_num'].__setitem__(3, str(int(a['classes'][4]['centre_num'][3]) + 2 ** 38)))
w('n8_duplicate_class', lambda a: a['classes'].append(a['classes'][0]))
w('n8_wrong_pinned', lambda a: a['classes'][2].__setitem__('pinned_body', (a['classes'][2]['pinned_body'] + 1) % 8))
w('n8_unique_radius_too_big', lambda a: a['classes'][7].__setitem__('uniqueness_radius_exp2', 6))
w('n8_wrong_morse_index', lambda a: a['classes'][9].__setitem__('morse_index', a['classes'][9]['morse_index'] + 1))
w('n8_wrong_sym_order', lambda a: a['classes'][6].__setitem__('sym_order', 2))
w('n8_wrong_labelled_count', lambda a: a.__setitem__('labelled_count', a['labelled_count'] + 2))
PYEOF
for f in $T/n8_*.json; do
  echo "== $(basename $f)"
  $P -I $D/verify_rational.py $f 2>&1 | tail -1
  $P -I -O $D/verify_rational.py $f 2>&1 | tail -1
done
