

# This file was *autogenerated* from the file tests_edelman.sage
from sage.all_cmdline import *   # import sage library

_sage_const_10 = Integer(10); _sage_const_1 = Integer(1); _sage_const_6 = Integer(6); _sage_const_9 = Integer(9); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8); _sage_const_0 = Integer(0)
sage.repl.load.load(sage.repl.load.base64.b64decode("ZWRlbG1hbi5zYWdl"),globals(),False)

m = _sage_const_10 
for b in (ellipsis_iter(_sage_const_1 ,Ellipsis,m)) :
    print (sigb (b, m))
print ()

P1 = [[_sage_const_1 , _sage_const_6 , _sage_const_9 ], [_sage_const_2 ], [_sage_const_3 , _sage_const_4 , _sage_const_5 ], [_sage_const_7 , _sage_const_8 ]]
print (reorder (P1, _sage_const_3 , _sage_const_9 ))
print ()

L2 = [_sage_const_1 , _sage_const_3 , _sage_const_5 , _sage_const_6 , _sage_const_7 ]
R2_1 = [_sage_const_1 , _sage_const_2 , _sage_const_5 ]
R2_2 = [_sage_const_8 ]
s2 = sigb_hat (L2, [R2_1, R2_2], _sage_const_3 , _sage_const_8 )
print (s2)
print ()

s3 = ['(', _sage_const_3 , _sage_const_2 , '(', _sage_const_4 , ')', ')', '(', '(', _sage_const_1 , ')']
print (good_par (s2))
print (good_par (s3))
print ()

cpt = _sage_const_0 
found = _sage_const_0 
for b in (ellipsis_iter(_sage_const_1 ,Ellipsis,_sage_const_8 )) :
    s = sigb_hat (L2, [R2_1, R2_2], b, _sage_const_8 )
    _, r = good_par (s)
    if r :
        cpt = cpt + _sage_const_1 
        found = b
print (cpt, found)
print ()

print (to_part (L2, [R2_1, R2_2], _sage_const_8 ))
print ()

m = _sage_const_6 
k = _sage_const_3 
g = generate_pnc_k (m, k)
kt = _sage_const_0 
for e in g :
    print (e)
    kt = kt + _sage_const_1 

print (kt)
print ((_sage_const_1  / m) * binomial (m, k) * binomial (m, k - _sage_const_1 ))
print ()

print (par_to_pnc_b (L2, R2_1 + R2_2, _sage_const_8 ))
print ()

P3 = [[_sage_const_1 ], [_sage_const_2 , _sage_const_6 ], [_sage_const_3 , _sage_const_4 ], [_sage_const_5 ], [_sage_const_7 , _sage_const_8 ]]
print (pnc_b_to_par (P3, _sage_const_3 , _sage_const_8 ))
print ()

print (rk (P3))
print ()

P4 = [[_sage_const_1 ], [_sage_const_2 , _sage_const_5 , _sage_const_6 ], [_sage_const_3 , _sage_const_4 ], [_sage_const_7 , _sage_const_8 ]]
print (cov (P4, P3))
print (cov (P3, P4))
print ()

g2 = generate_strict_chains ([_sage_const_1 , _sage_const_2 ], _sage_const_4 )
k = _sage_const_0 
for e in g2 :
    print (e)
    k = k + _sage_const_1 
print (k)
print (cpt_strict_chains ([_sage_const_1 , _sage_const_2 ], _sage_const_4 ))
print ()

g3 = generate_max_chains (_sage_const_5 )
k = _sage_const_0 
for e in g3 :
    k = k + _sage_const_1 
print (k)
print (cpt_max_chains (_sage_const_5 ))
print ()

print (zeta_pnc (_sage_const_6 , _sage_const_3 ))
print (cpt_weak_chains (_sage_const_6 , _sage_const_3 ))
