

# This file was *autogenerated* from the file pnc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2)
sage.repl.load.load(sage.repl.load.base64.b64decode("cGVybS5zYWdl"),globals(),False)

def is_pnc (P) :
    L = []
    for b in P :
        for e in b :
            L.append (e)
    n = len (L)
    L2 = [i for i in (ellipsis_iter(_sage_const_1 ,Ellipsis,n))]
    if not (sorted (L) == L2) :
        return False
    return P.is_noncrossing ()

def generate_pnc (n) :
    k = _sage_const_0 
    L = SetPartitions (n).list ()
    for P in L :
        if P.is_noncrossing () :
            k = k + _sage_const_1 
            yield P
    return (k)

def couvre_pnc (P1, P2) :
    if not is_pnc (P1) :
        print (P1, "n'est pas une pnc")
        return False
    if not is_pnc (P2) :
        print (P2, "n'est pas une pnc")
        return False

    b1 = P1.base_set ()
    b2 = P2.base_set ()
    if b1 != b2 :
        return False

    S = SetPartitions (b1.cardinality ())

    for P3 in S :
        b3 = P3.base_set ()
        if b1 != b3 :
            print (b1, "pas", b3)
            return False
        if b2 != b3 :
            print (b2, "pas", b3)
            return False

        if S.is_less_than (P1, P3) and S.is_less_than (P3, P2) :
            return False
    return S.is_less_than (P1, P2)

def pnc_to_perm (P) :
    if not is_pnc (P) :
        return []
    return P.to_permutation ()

def Kreweras (P) :
    if not is_pnc (P) :
        return []

    n = P.base_set_cardinality ()
    om = Permutation ([i for i in (ellipsis_iter(_sage_const_2 ,Ellipsis,n))] + [_sage_const_1 ])
    pi = P.to_permutation ()
    pib = pi.inverse ()
    k = om.left_action_product (pib)
    B = blocs_perm (k)
    return SetPartition (B)

