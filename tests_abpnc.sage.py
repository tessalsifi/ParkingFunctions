

# This file was *autogenerated* from the file tests_abpnc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_6 = Integer(6); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_5 = Integer(5); _sage_const_0 = Integer(0); _sage_const_10 = Integer(10); _sage_const_7 = Integer(7)
sage.repl.load.load(sage.repl.load.base64.b64decode("YWJwbmMuc2FnZQ=="),globals(),False)
sage.repl.load.load(sage.repl.load.base64.b64decode("cmR5Y2suc2FnZQ=="),globals(),False)

# TESTS ABPNC
print ("Tests ABPNC")

P1 = SetPartition ([[_sage_const_1 , _sage_const_4 , _sage_const_6 ], [_sage_const_2 ], [_sage_const_3 ], [_sage_const_5 ]])
P2 = SetPartition ([[_sage_const_1 , _sage_const_3 ], [_sage_const_2 ], [_sage_const_4 , _sage_const_5 ], [_sage_const_6 ]])
Q1 = SetPartition ([[_sage_const_1 ], [_sage_const_2 , _sage_const_3 , _sage_const_4 ], [_sage_const_5 , _sage_const_6 ]])
print (mut_nc (P1, Q1))
print (mut_nc (P2, Q1))
print ()

b = _sage_const_4 
g = generate_mut (b)
k = _sage_const_0 
for e in g :
    print (e)
    k = k + _sage_const_1 
print (k)
print ()

A1 = ABPNC (_sage_const_10 , _sage_const_7 , P1, Q1)
A2 = ABPNC (_sage_const_10 , _sage_const_7 , P2, Q1)
print (A1.is_abpnc ())
print (A2.is_abpnc ())
print ()

a3 = _sage_const_10 
b3 = _sage_const_7 
p3 = [_sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 ]
R3 = RDYCK (a3, b3, p3)
P3, _ = P (R3)
Q3, _ = Q (R3)
A3 = ABPNC (a3, b3, P3, Q3)
print (A3.is_abpnc ())
print ()

a = _sage_const_3 
b = _sage_const_4 
g = generate_abpnc (a, b)
k = _sage_const_0 
for e, lp, lq in g :
    print (e.P, e.Q, lp, lq)
    s = _sage_const_0 
    for e in lp :
        s = s + lp [e]
    for e in lq :
        s = s + lq [e]
    print (s, s == a)
    k = k + _sage_const_1 
print (k)
print ((_sage_const_1  / (a + b)) * binomial (a + b, a))
print ()

A4 = abrot (A1)
print (A4.P, A4.Q)
print (A4.is_abpnc ())
print ()

A5 = abrotb (A1)
print (A5.P, A5.Q)
print (A5.is_abpnc ())
print ()

print (A1.P, A1.Q)
A6 = abrotb (A4)
print (A6.P, A6.Q)
A7 = abrot (A5)
print (A7.P, A7.Q)
print ()

a8 = _sage_const_10 
b8 = _sage_const_7 
p8 = [_sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 ]
R8 = RDYCK (a8, b8, p8)
R8.pretty_print ()
P8, rp8 = P (R8)
Q8, rq8 = Q (R8)
A8 = ABPNC (a8, b8, P8, Q8)
print (P8, Q8)

R9 = rotr (R8)
R9.pretty_print ()
P9, _ = P (R9)
Q9, _ = Q (R9)
print (P9, Q9)

A9 = abrotb (A8)
print (A9.P, A9.Q)
print ()

print (P9, Q9)
P10 = rotb (P8)
Q10 = rotb (Q8)
print (P10, Q10)
print ()

print (ranks (A8, rp8, rq8))
R11 = abpnc_to_rdyck (A8, rp8, rq8)
R11.pretty_print ()
print ()

for B1 in P8 :
    for B2 in P8 :
        if couvre_block_abpnc (A8, B1, B2) :
            print (list (B1), list (B2))

for B1 in P8 : 
    for B2 in Q8 :
        if couvre_block_abpnc (A8, B1, B2) :
            print (list (B1), list (B2))

