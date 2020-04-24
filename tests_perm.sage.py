

# This file was *autogenerated* from the file tests_perm.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_5 = Integer(5); _sage_const_2 = Integer(2); _sage_const_4 = Integer(4); _sage_const_3 = Integer(3)
sage.repl.load.load(sage.repl.load.base64.b64decode("cGVybS5zYWdl"),globals(),False)

# Tests Perm
print ("Tests Perm")

L1 = [_sage_const_1 , _sage_const_5 , _sage_const_2 , _sage_const_4 , _sage_const_3 ]
L2 = [_sage_const_1 , _sage_const_3 , _sage_const_2 , _sage_const_4 , _sage_const_2 ]
print (is_perm (L1))
print (is_perm (L2))
print ()

print (inv_perm (L1))
print ()

L3 = [_sage_const_5 , _sage_const_1 , _sage_const_3 , _sage_const_2 , _sage_const_4 ]
print (comp_perm (L1, L3))
print (comp_perm (L1, inv_perm (L1)))
print ()

R  = blocs_perm (L3)
for e in R :
    print (list (e))

