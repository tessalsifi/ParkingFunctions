

# This file was *autogenerated* from the file tests_abfp.sage
from sage.all_cmdline import *   # import sage library

_sage_const_10 = Integer(10); _sage_const_7 = Integer(7); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_0 = Integer(0); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8)
sage.repl.load.load(sage.repl.load.base64.b64decode("YWJmcC5zYWdl"),globals(),False)

# TESTS ABFP
print ("TESTS ABFP")

a1 = _sage_const_10 
b1 = _sage_const_7 
P1 = SetPartition ([[_sage_const_1 , _sage_const_2 ], [_sage_const_3 , _sage_const_6 ], [_sage_const_4 ], [_sage_const_5 ]])
Q1 = SetPartition ([[_sage_const_1 ], [_sage_const_2 , _sage_const_6 ], [_sage_const_3 , _sage_const_4 , _sage_const_5 ]])
fP1 = {_sage_const_0  : {_sage_const_1 , _sage_const_7 }, _sage_const_1  : {_sage_const_2 , _sage_const_3 }, _sage_const_2  : {_sage_const_5 , _sage_const_9 }, _sage_const_3  : {_sage_const_4 , _sage_const_6 }}
fQ1 = {_sage_const_0  : {_sage_const_10 }, _sage_const_1  : {_sage_const_8 }, _sage_const_2  : {}}
fP2 = {_sage_const_0  : {_sage_const_1 , _sage_const_7 }, _sage_const_1  : {_sage_const_2 , _sage_const_3 , _sage_const_5 }, _sage_const_2  : {_sage_const_9 }, _sage_const_3  : {_sage_const_4 , _sage_const_6 }}
A1 = ABFP (a1, b1, P1, Q1, fP1, fQ1)
A2 = ABFP (a1, b1, P1, Q1, fP2, fQ1)
print (A1.is_abfp ())
print (A2.is_abfp ())
print ()

a = _sage_const_3 
b = _sage_const_4 
g = generate_abfp (a, b)
k = _sage_const_0 
for e in g :
    print (e.P, e.Q)
    print (e.fP, e.fQ)
    print ()
    k = k + _sage_const_1 
print (k)
print (b ** (a - _sage_const_1 ))
