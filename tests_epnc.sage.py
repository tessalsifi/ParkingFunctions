

# This file was *autogenerated* from the file tests_epnc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_0 = Integer(0)
sage.repl.load.load(sage.repl.load.base64.b64decode("ZXBuYy5zYWdl"),globals(),False)

# TESTS EPNC
print ("Tests EPNC")

pi = SetPartition ([{_sage_const_1 , _sage_const_4 , _sage_const_5 }, {_sage_const_2 , _sage_const_3 }])
sig1 = Permutation ([_sage_const_2 , _sage_const_1 , _sage_const_5 , _sage_const_3 , _sage_const_4 ])
sig2 = Permutation ([_sage_const_2 , _sage_const_1 , _sage_const_5 , _sage_const_4 , _sage_const_3 ])
e1 = EPNC (pi, sig1)
e2 = EPNC (pi, sig2)
print (e1.is_epnc ())
print (e2.is_epnc ())
print ()

n = _sage_const_4 
g = generate_epnc (n)
k = _sage_const_0 
for e in g :
    print (e.pi, e.sig)
    k = k + _sage_const_1 
print (k)
print ((n + _sage_const_1 )**(n - _sage_const_1 ))
print ()

pi3 = SetPartition ([{_sage_const_1 , _sage_const_5 }, {_sage_const_4 }, {_sage_const_2 , _sage_const_3 }])
sig3 = Permutation ([_sage_const_2 , _sage_const_1 , _sage_const_4 , _sage_const_3 , _sage_const_5 ])
e3 = EPNC (pi3, sig1)
e4 = EPNC (pi3, sig3)
print (couvre_epnc (e3, e1))
print (couvre_epnc (e4, e1))
print (couvre_epnc (e1, e3))
print ()

pi5 = SetPartition ([{_sage_const_1 , _sage_const_4 , _sage_const_5 }, {_sage_const_2 , _sage_const_3 }])
rho5 = SetPartition ([{_sage_const_1 , _sage_const_3 , _sage_const_5 }, {_sage_const_2 , _sage_const_4 }])
lam5 = {_sage_const_0  : _sage_const_0 , _sage_const_1  : _sage_const_1 }
d5 = DPNC (pi5, rho5, lam5)
e5 = dpnc_to_epnc (d5)
ed5 = epnc_to_dpnc (e5)
print (e5.pi, e5.sig)
print (ed5.pi, ed5.rho, ed5.lam)
print ()

d6 = epnc_to_dpnc (e1)
de6 = dpnc_to_epnc (d6)
print (d6.pi, d6.rho, d6.lam)
print (de6.pi, de6.sig)
print ()

pi7 = SetPartition ([{_sage_const_1 , _sage_const_4 , _sage_const_5 }, {_sage_const_2 }, {_sage_const_3 }])
sig7 = Permutation ([_sage_const_2 , _sage_const_5 , _sage_const_1 , _sage_const_3 , _sage_const_4 ])
e7 = EPNC (pi7, sig7)
print (epnc_label (e3, e1))
print (epnc_label (e7, e1))
print ()

print (precede_label (e1, e3, e7))
print (precede_label (e1, e7, e3))

