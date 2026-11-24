#!/usr/bin/env python3
"""Check exact Krawczyk algebra on supplied enclosures, not their derivation."""
import argparse,json
from fractions import Fraction as Q

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(c,a):return (c*a[0],c*a[1])if c>=0 else(c*a[1],c*a[0])
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def total(values):
 v=(Q(0),Q(0))
 for w in values:v=add(v,w)
 return v
def check(d):
 X=[tuple(map(Q,x))for x in d['box']];c=list(map(Q,d['centre']));C=[list(map(Q,r))for r in d['preconditioner']];F=[tuple(map(Q,x))for x in d['residual_at_centre']];J=[[tuple(map(Q,x))for x in r]for r in d['jacobian_enclosure']];n=len(X)
 if not n or len(c)!=n or len(C)!=n or len(F)!=n or len(J)!=n or any(len(r)!=n for r in C+J):raise ValueError('shape mismatch')
 if any(a>=b for a,b in X)or any(a>b for a,b in F+sum(J,[])):raise ValueError('invalid interval')
 if any(not a<=v<=b for (a,b),v in zip(X,c)):raise ValueError('centre outside box')
 B=[]
 for i in range(n):
  row=[]
  for j in range(n):
   v=total(scale(C[i][k],J[k][j])for k in range(n));row.append((Q(i==j)-v[1],Q(i==j)-v[0]))
  B.append(row)
 norm=max(sum(max(abs(a),abs(b))for a,b in row)for row in B)
 if norm>=1:raise ValueError('contraction fails')
 K=[]
 for i in range(n):
  v=total(scale(C[i][k],F[k])for k in range(n));base=(c[i]-v[1],c[i]-v[0]);K.append(add(base,total(mul(B[i][j],(X[j][0]-c[j],X[j][1]-c[j]))for j in range(n))))
 if any(not(a<lo and hi<b)for (a,b),(lo,hi)in zip(X,K)):raise ValueError('strict inclusion fails')
 return {'algebraic_conditions':True,'norm_bound':str(norm),'status':'function enclosure derivation and global coverage not verified'}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('matrix_evidence');a=p.parse_args();print(json.dumps(check(json.load(open(a.matrix_evidence))),indent=2))
