#!/usr/bin/env python3
"""Numerical symmetric five-vortex controls. No classification or certification."""
import argparse,math,json

def candidates(n=5):
 if n<3:raise ValueError('at least three vortices')
 out=[]
 for centre in (False,True):
  ring=n-1 if centre else n;r=math.sqrt((ring-1)/2+int(centre));q=[[r*math.cos(2*math.pi*j/ring),r*math.sin(2*math.pi*j/ring)]for j in range(ring)]
  if centre:q.append([0.,0.])
  F=[]
  for i,p in enumerate(q):
   v=[-p[0],-p[1]]
   for j,x in enumerate(q):
    if i==j:continue
    d=[p[k]-x[k]for k in (0,1)];r2=sum(z*z for z in d)
    for k in (0,1):v[k]+=d[k]/r2
   F+=v
  out.append({'family':'regular_ring_plus_centre'if centre else'regular_ring','n':n,'exponent':0,'lambda':1,'positions':q,'max_float_residual':max(map(abs,F)),'status':'known symmetric numerical control; not certified'})
 return out
if __name__=='__main__':print(json.dumps(candidates(),indent=2))
