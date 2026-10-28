#!/usr/bin/env python3
"""Numerical equal-weight reduced equations. No interval or completeness claim."""
import math

def unpack(u):
 if len(u)<3 or len(u)%2!=1:raise ValueError('expected 2n-3 variables')
 n=(len(u)+3)//2;x=list(u[:n-1]);ys=list(u[n-1:]);y0=-sum(ys)/2
 q=[[x[0],y0]]+[[x[i],ys[i-1]]for i in range(1,n-1)]
 q.append([-sum(x),y0])
 if q[0][0]-q[-1][0]<=0:raise ValueError('rotation chart requires x0>x_last')
 return q

def residual(q,a):
 if a<0 or not math.isfinite(a):raise ValueError('invalid exponent')
 n=len(q);c=[sum(p[k]for p in q)/n for k in (0,1)];F=[]
 for i,p in enumerate(q):
  v=[-(p[k]-c[k])for k in (0,1)]
  for j,r in enumerate(q):
   if i==j:continue
   d=[p[k]-r[k]for k in (0,1)];r2=sum(z*z for z in d)
   if r2<=0:raise ValueError('collision')
   scale=r2**(-(a+2)/2)
   for k in (0,1):v[k]+=d[k]*scale
  F.append(v)
 return F

def reduced(u,a):
 q=unpack(u);F=residual(q,a)
 return [F[0][0]]+[z for f in F[1:-1]for z in f]
