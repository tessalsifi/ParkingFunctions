load perm.sage

def is_pnc (P) :
    L = []
    for b in P :
        for e in b :
            L.append (e)
    n = len (L)
    L2 = [i for i in (1..n)]
    if not (sorted (L) == L2) :
        return False
    return P.is_noncrossing ()

def generate_pnc (n) :
    L = SetPartitions (n).list ()
    for P in L :
        if P.is_noncrossing () :
            yield P

def is_subset (S1, S2) :
    for e in S1 :
        if not e in S2 :
            return False
    return True

def couvre_part (P1, P2) :
    d = {}
    for i, b2 in enumerate (P2) :
        d [i] = 0
        for b1 in P1 :
            if is_subset (b1, b2) :
                d [i] = d [i] + 1
    found = False
    for k in d :
        v = d [k]
        if v < 1 or v > 2 :
            return False
        if v == 2 :
            if found :
                return False
            found = True
    return found

def couvre_pnc (P1, P2) :
    if not is_pnc (P1) :
        return False
    if not is_pnc (P2) :
        return False
        
    return couvre_part (P1, P2)

def pnc_to_perm (P) :
    if not is_pnc (P) :
        return None
    return P.to_permutation ()

def Kreweras (P) :
    if not is_pnc (P) :
        return None

    n = P.base_set_cardinality ()
    lom = [n] + [i for i in range (1, n)]
    om = Permutation (lom)
    pi = P.to_permutation ()

    k = om.left_action_product (pi)
    B = blocs_perm (k)
    return SetPartition (B)

def label (P1, P2) :
    if not couvre_pnc (P1, P2) :
        return None

    p1 = pnc_to_perm (P1)
    p2 = pnc_to_perm (P2)
    p1i = p1.inverse ()
    t = p2.left_action_product (p1i)
    return t

def rot (P) :
    if not is_pnc (P) :
        return None

    n = P.base_set_cardinality ()
    Parts = []

    for p in P :
        part = []
        for e in p :
            if e == n :
                part.append (1)
            else :
                part.append (e + 1)
        Parts.append (part)
    
    return SetPartition (Parts)

def rotb (P) :
    if not is_pnc (P) :
        return None
    
    n = P.base_set_cardinality ()
    Parts = []

    for p in P :
        part = []
        for e in p :
            if e == 1 :
                part.append (n)
            else :
                part.append (e - 1)
        Parts.append (part)
    
    return SetPartition (Parts)