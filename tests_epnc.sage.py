

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

n = _sage_const_4 
g = generate_epnc (n)
k = _sage_const_0 
for e in g :
    print (e.pi, e.sig)
    k = k + _sage_const_1 
print (k)
print ((n + _sage_const_1 )**(n - _sage_const_1 ))

pi3 = SetPartition ([{_sage_const_1 , _sage_const_5 }, {_sage_const_4 }, {_sage_const_2 , _sage_const_3 }])
sig3 = Permutation ([_sage_const_2 , _sage_const_1 , _sage_const_4 , _sage_const_3 , _sage_const_5 ])
e3 = EPNC (pi3, sig1)
e4 = EPNC (pi3, sig3)
print (couvre_epnc (e3, e1))
print (couvre_epnc (e4, e1))
print (couvre_epnc (e1, e3))
