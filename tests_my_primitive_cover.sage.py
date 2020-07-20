

# This file was *autogenerated* from the file tests_my_primitive_cover.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_2 = Integer(2)
sage.repl.load.load(sage.repl.load.base64.b64decode("bXlfcHJpbWl0aXZlX2NvdmVyLnNhZ2U="),globals(),False)

# TESTS MPC
print ("Tests MPC")

L1 = [_sage_const_1 , _sage_const_1 , _sage_const_3 , _sage_const_4 , _sage_const_4 , _sage_const_5 , _sage_const_7 ]
L2 = [_sage_const_1 , _sage_const_1 , _sage_const_3 , _sage_const_4 , _sage_const_4 , _sage_const_6 , _sage_const_7 ]
L3 = [_sage_const_1 , _sage_const_2 , _sage_const_3 , _sage_const_4 , _sage_const_4 , _sage_const_6 , _sage_const_7 ]
L4 = [_sage_const_1 , _sage_const_2 , _sage_const_3 , _sage_const_4 , _sage_const_4 , _sage_const_4 , _sage_const_7 ]

print (my_prim_cov (L1, L2))
print (my_prim_cov (L2, L1))
print (my_prim_cov (L3, L1))
print (my_prim_cov (L3, L2))
print (my_prim_cov (L4, L1))
print ()

D1 = fpp_to_dyck (L1)
print (D1)
D2 = fpp_to_dyck (L2)
D3 = fpp_to_dyck (L3)
D4 = fpp_to_dyck (L4)

print (my_prim_cov_dyck (D1, D2))
print (my_prim_cov_dyck (D2, D1))
print (my_prim_cov_dyck (D3, D1))
print (my_prim_cov_dyck (D3, D2))
print (my_prim_cov_dyck (D4, D1))

