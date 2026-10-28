import importlib.util,pathlib,math,unittest
p=pathlib.Path(__file__).resolve().parents[1]/'tools/reduced_equations.py';s=importlib.util.spec_from_file_location('eq',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Controls(unittest.TestCase):
 def test_classical_three_body(self):
  for a in (0,1):
   side=3**(1/(a+2));h=math.sqrt(3)*side/2;u=[side/2,0,2*h/3]
   self.assertLess(max(map(abs,m.reduced(u,a))),1e-12)
   radius=(1+2**(-(a+1)))**(1/(a+2))
   self.assertLess(max(map(abs,m.reduced([radius,0,0],a))),1e-12)
 def test_translation_and_torque_identities(self):
  q=m.unpack([2,.1,.4]);F=m.residual(q,1)
  self.assertLess(abs(sum(f[0]for f in F))+abs(sum(f[1]for f in F)),1e-12)
  self.assertLess(abs(sum(p[0]*f[1]-p[1]*f[0]for p,f in zip(q,F))),1e-12)
 def test_chart_rejected(self):
  with self.assertRaises(ValueError):m.unpack([-1,0,0])
if __name__=='__main__':unittest.main()
