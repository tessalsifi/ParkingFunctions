

# This file was *autogenerated* from the file tests_pnc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_5 = Integer(5); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4)
sage.repl.load.load(sage.repl.load.base64.b64decode("cG5jLnNhZ2U="),globals(),False)

# TESTS PNC
print ("Tests PNC")

P1 = SetPartition ([{_sage_const_1 , _sage_const_5 }, {_sage_const_2 }, {_sage_const_3 , _sage_const_4 }])
P2 = SetPartition ([{_sage_const_1 , _sage_const_3 , _sage_const_4 }, {_sage_const_2 }, {_sage_const_5 }])
P3 = SetPartition ([{_sage_const_1 , _sage_const_3 , _sage_const_4 }, {_sage_const_2 , _sage_const_5 }])
print (is_pnc (P1))
print (is_pnc (P2))
print (is_pnc (P3))
print ()

n = _sage_const_5 
g = generate_pnc (n)
while True :
    try :
        print (g.send (None))
    except :
        break
print (catalan_number (n))
print ()

P4 = SetPartition ([{_sage_const_1 , _sage_const_4 }, {_sage_const_2 }, {_sage_const_3 }, {_sage_const_5 }])
print (couvre_pnc (P4, P2))
print (couvre_pnc (P4, P3))
print ()

print (pnc_to_perm (P1))
print ()

print (Kreweras (P1))

