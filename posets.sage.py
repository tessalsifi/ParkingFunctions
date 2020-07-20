

# This file was *autogenerated* from the file posets.sage
from sage.all_cmdline import *   # import sage library

_sage_const_4 = Integer(4); _sage_const_3 = Integer(3); _sage_const_10 = Integer(10); _sage_const_7 = Integer(7); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_15 = Integer(15); _sage_const_2 = Integer(2)
sage.repl.load.load(sage.repl.load.base64.b64decode("cGVybS5zYWdl"),globals(),False)

print ("Perm")
P0 = Poset ([list (generate_perm (_sage_const_4 )), couvre_perm])
g0 = P0.plot ()
g0.save ('perm_poset_4.pdf')
print (P0.zeta_polynomial ())
print ()

sage.repl.load.load(sage.repl.load.base64.b64decode("cG5jLnNhZ2U="),globals(),False)

print ("PNC")
P1 = Poset ([list (generate_pnc (_sage_const_4 )), couvre_pnc])
g1 = P1.plot (label_elements = False)
g1.save ('pnc_poset_4.pdf')
print (P1.zeta_polynomial ())
print ()

sage.repl.load.load(sage.repl.load.base64.b64decode("ZHBuYy5zYWdl"),globals(),False)

print ("DPNC")
P2 = Poset ([list (generate_dpnc (_sage_const_3 )), couvre_dpnc])
g2 = P2.plot (label_elements = False)
g2.save ('dpnc_poset_3.pdf')
print (P2.zeta_polynomial ())
print ()

sage.repl.load.load(sage.repl.load.base64.b64decode("ZXBuYy5zYWdl"),globals(),False)

print ("EPNC")
P3 = Poset ([list (generate_epnc (_sage_const_3 )), couvre_epnc])
g3 = P3.plot (label_elements = False)
g3.save ('epnc_poset_3.pdf')
print (P3.zeta_polynomial ())
print ()

sage.repl.load.load(sage.repl.load.base64.b64decode("YWJwbmMuc2FnZQ=="),globals(),False)

print ("ABPNC")
a4 = _sage_const_10 
b4 = _sage_const_7 
p4 = [_sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 ]
R4 = RDYCK (a4, b4, p4)
P4, _ = P (R4)
Q4, _ = Q (R4)
A4 = ABPNC (a4, b4, P4, Q4)
L4 = list (P4) + list (Q4)

def cbapnc (B1, B2) :
    return couvre_block_abpnc (A4, B1, B2)

d4 = {}
for e in L4 :
    d4 [e] = list (e)

P4_ = Poset ([L4, cbapnc])
g4 = P4_.plot (element_labels = d4)
g4.save ('abpnc_block_poset.pdf')
print (P4_.zeta_polynomial ())
print ()

print ("ABPNC : Cas Fuß - Catalan")
a4_ = _sage_const_15 
b4_ = _sage_const_7 
p4_ = [_sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 ,
       _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 ]
R4_ = RDYCK (a4_, b4_, p4_)
P4_, _ = P (R4_)
Q4_, _ = Q (R4_)
A4_ = ABPNC (a4_, b4_, P4_, Q4_)
L4_ = list (P4_) + list (Q4_)

d4_ = {}
for e in L4_ :
    d4_ [e] = list (e)

P4__ = Poset ([L4_, cbapnc])
g4_ = P4__.plot (element_labels = d4_)
g4_.save ('abpnc_block_poset_FC.pdf')
print (P4__.zeta_polynomial ())
print ()

sage.repl.load.load(sage.repl.load.base64.b64decode("ZnAuc2FnZQ=="),globals(),False)

print ("FP")
P5 = Poset ([list (generate_fp (_sage_const_3 )), couvre_fp])
g5 = P5.plot (label_elements = False)
g5.save ('fp_poset_3.pdf')
print (P5.zeta_polynomial ())
print ()

sage.repl.load.load(sage.repl.load.base64.b64decode("ZWRlbG1hbi5zYWdl"),globals(),False)

print ("Edelman")
L6 = []
for k in (ellipsis_iter(_sage_const_1 ,Ellipsis,_sage_const_4 )) :
    tmp = generate_pnc_k (_sage_const_4 , k)
    L6 = L6 + list (tmp)
P6 = Poset ([L6, cov])
g6 = P6.plot (label_elements = False)
g6.save ('edelman_poset_4.pdf')
print (P6.zeta_polynomial ())
print ("---")

P7 = Poset ([list (generate_pnc_k_div (_sage_const_3 , _sage_const_2 )), cov])
g7 = P7.plot (label_elements = False)
g7.save ('edelman_2div_poset_3.pdf')
print (P7.zeta_polynomial ())
print ()

sage.repl.load.load(sage.repl.load.base64.b64decode("bXlfcHJpbWl0aXZlX2NvdmVyLnNhZ2U="),globals(),False)

print ("My primitive PF cover")

P8 = Poset ([list (generate_fpp (_sage_const_4 )), my_prim_cov])
g8 = P8.plot ()
g8.save ('MPC_poset_4.pdf')
print (P8.zeta_polynomial ())
print ()

print ("My primitive Dyck cover")
L9 = []
for f in generate_fpp (_sage_const_4 ) :
    L9.append (DyckWord (fpp_to_dyck (f)))
P9 = Poset ([L9, my_prim_cov_dyck])
g9 = P9.plot ()
g9.save ('MPCD_poset_4.pdf')
print (P9.zeta_polynomial ())
print ()

