

# This file was *autogenerated* from the file ../tests/tests_dpnc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_0 = Integer(0)
sage.repl.load.load(sage.repl.load.base64.b64decode("Li4vY29kZS9kcG5jLnNhZ2U="),globals(),False)

# TESTS DPNC
print ("Tests DPNC")

pi = SetPartition ([{_sage_const_1 , _sage_const_4 , _sage_const_5 }, {_sage_const_2 , _sage_const_3 }])
rho = SetPartition ([{_sage_const_1 , _sage_const_3 , _sage_const_5 }, {_sage_const_2 , _sage_const_4 }])
lam = {_sage_const_0  : _sage_const_0 , _sage_const_1  : _sage_const_1 }
d = DPNC (pi, rho, lam)
print (d.is_dpnc ())

lam2 = {_sage_const_0  : _sage_const_1 , _sage_const_1  : _sage_const_0 }
d2 = DPNC (pi, rho, lam2)
print (d2.is_dpnc ())

d3 = DPNC (rho, rho, lam)
print (d3.is_dpnc ())
print ()

n = _sage_const_4 
g = generate_dpnc (n)
k = _sage_const_0 
for e in g :
    print (e.pi, e.rho, e.lam)
    k = k + _sage_const_1 
print (k)
print ((n + _sage_const_1 )**(n - _sage_const_1 ))
print ()

pi4 = SetPartition ([{_sage_const_1 , _sage_const_5 }, {_sage_const_2 , _sage_const_3 }, {_sage_const_4 }])
rho4 = SetPartition ([{_sage_const_1 }, {_sage_const_2 , _sage_const_4 }, {_sage_const_3 , _sage_const_5 }])
lam4 = {_sage_const_0  : _sage_const_2 , _sage_const_1  : _sage_const_1 , _sage_const_2  : _sage_const_0 }
d4 = DPNC (pi4, rho4, lam4)
print (couvre_dpnc (d4, d))

lam5 = {_sage_const_0  : _sage_const_1 , _sage_const_1  : _sage_const_2 , _sage_const_2  : _sage_const_0 }
d5 = DPNC (pi4, rho4, lam5)
print (couvre_dpnc (d5, d))
print ()

print (d.rang ())
print (d4.rang ())
print ()

P = Permutation ([_sage_const_4 , _sage_const_5 , _sage_const_2 , _sage_const_1 , _sage_const_3 ])
d6 = perm_dpnc (P, d)
print (d6.pi)
print (d6.rho)
print (d6.lam)

