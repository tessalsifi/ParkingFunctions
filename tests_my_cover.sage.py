

# This file was *autogenerated* from the file tests_my_cover.sage
from sage.all_cmdline import *   # import sage library

_sage_const_5 = Integer(5); _sage_const_1 = Integer(1); _sage_const_3 = Integer(3); _sage_const_7 = Integer(7); _sage_const_4 = Integer(4); _sage_const_6 = Integer(6); _sage_const_2 = Integer(2)
sage.repl.load.load(sage.repl.load.base64.b64decode("bXlfY292ZXIuc2FnZQ=="),globals(),False)

# TESTS MC
print ("Tests MC")

L1 = [_sage_const_5 , _sage_const_1 , _sage_const_3 , _sage_const_7 , _sage_const_4 , _sage_const_1 , _sage_const_4 ]
L2 = [_sage_const_6 , _sage_const_1 , _sage_const_3 , _sage_const_7 , _sage_const_4 , _sage_const_1 , _sage_const_4 ]
L3 = [_sage_const_6 , _sage_const_2 , _sage_const_3 , _sage_const_7 , _sage_const_4 , _sage_const_1 , _sage_const_4 ]
L4 = [_sage_const_4 , _sage_const_2 , _sage_const_3 , _sage_const_7 , _sage_const_4 , _sage_const_1 , _sage_const_4 ]

print (my_cov (L1, L2))
print (my_cov (L2, L1))
print (my_cov (L3, L1))
print (my_cov (L3, L2))
print (my_cov (L4, L1))
print ()

D1 = fp_to_ddyck (L1)
D2 = fp_to_ddyck (L2)
D3 = fp_to_ddyck (L3)
D4 = fp_to_ddyck (L4)

#print (my_cov_ddyck (D1, D2))
#print (my_cov_ddyck (D2, D1))
#print (my_cov_ddyck (D3, D1))
#print (my_cov_ddyck (D3, D2))
#print (my_cov_ddyck (D4, D1))
#print ()


L = list (generate_fp (_sage_const_5 ))
P1 = Poset ([L, my_cov])
print (len (P1.cover_relations ()))
print (P1.relations_number ())
print ()

L2 = []
for f in L :
    L2.append (fp_to_ddyck (f))
#P2 = Poset ([L2, my_cov_ddyck])
#print (len (P2.cover_relations ()))
#print (P2.relations_number ())
#print ()

#print (num_cov (7))
#print (num_rel (7))
