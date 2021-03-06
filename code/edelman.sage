load pnc.sage

def sigb (b, m) :
    if b < 1 or b > m :
        return None
    L = [i for i in (b..m)] + [i for i in range(1,b)]
    return L

def reorder_part (part, order) :
    res = []
    new_order = []
    for e in order :
        if e in part :
            res.append (e)
        else :
            new_order.append (e)
    return res, new_order

def reorder (P, b, m) :
    P1 = SetPartition (P)
    if not is_pnc (P1) :
        return None

    n = P1.base_set_cardinality ()
    if n != m :
        return None

    P2 = []

    s = sigb (b, m)
    while (s != []) :
        e = s [0]
        for p in P :
            if e in p :
                r, s = reorder_part (p, s)
                P2.append (r)

    return P2

def sigb_hat (L, R, b, m) :
    s = sigb (b, m)

    allR = []
    for Ri in R :
        allR = allR + Ri

    if len (L) != len (allR) + 1 :
        return None

    res = []

    for e in s :
        if e in L :
            res.append ("(")

        res.append (e)

        c = allR.count (e)
        res = res + [")"] * c

    return res

def good_par (L) :
    if L [0] != '(' :
        return None, False

    s = ""
    for e in L :
        s = s + str (e)
        if e != '(' and e != ')' :
            s = s + ','
    s = s [1:]

    open = 0
    for e in s :
        if e == '(' :
            open = open + 1
        if e == ')' :
            open = open - 1
            if open < 0 :
                return None, False

    return s, (open == 0)

def to_part (L, R, m) :
    good = []
    b_good = 0

    for b in (1..m) :
        s = sigb_hat (L, R, b, m)
        s2, r = good_par (s)
        if r :
            good = list (s2)
            b_good = b
            break

    Parts = []

    while (good != []) :
        c = good.count('(')

        if c == 0 :
            part = []
            tmp = ''
            for e in good :
                if e != ',' :
                    tmp = tmp + e
                else :
                    part.append (int (tmp))
                    tmp = ''
            good = []
            Parts.append (part)

        else :
            idx = (good [: : -1]).index ('(')
            i = len (good) - idx - 1
            j = i
            part = []
            tmp = ''
            while (good [j] != ')') :
                e = good [j]
                if e != ',' and e != '(' :
                    tmp = tmp + e
                if e == ',' :
                    part.append (int (tmp))
                    tmp = ''
                j = j + 1
            Parts.append (part)
            good = good [:i] + good [j + 1:]

    return reorder (Parts, b_good, m)

def generate_pnc_k (m, k) :
    g = generate_pnc (m)
    for P in g :
        if len(P) == k :
            yield P

def par_to_pnc_b (L, R, m) :
    k = len (L)
    if k != len (R) + 1 :
        return None
    
    P = to_part (L, [R], m)
    b = P [0] [0]
    return P, b

def pnc_b_to_par (P, b, m) :
    P2 = reorder (P, b, m)
    L = []
    R = []
    first = True

    for p in P2 :
        if first :
            first = False
            L.append (p [0])
        else :
            L.append (p [0])
            R.append (p [-1])
    
    return (sorted (L), sorted (R))

def rk (P) :
    P1 = SetPartition (P)
    if not is_pnc (P1) :
        return None

    m = P1.base_set_cardinality ()
    l = len (P)
    return m - l

def cov (P1, P2) :
    P1_ = SetPartition (P1)
    P2_ = SetPartition (P2)
    return couvre_pnc (P2_, P1_)

def generate_strict_chains (T, m) :
    P = Poset ([list (generate_pnc (m)), couvre_pnc])

    for c in P.chains () :
        c2 = c [ : : -1]
        T2 = []
        for e in c2 :
            T2.append (rk (e))
        if T [: : - 1] == T2 :
            yield c2


def cpt_strict_chains (T, m) :
    T = [0] + T + [m - 1]
    S = []
    l = len (T)
    for i in range (1, l) :
        s = T[i] - T [i - 1]
        S.append (s)

    res = 1
    for e in S :
        res = res * binomial (m, e)
    
    res = res / m
    return res

def generate_max_chains (m) :
    T = [i for i in range (m)]
    return generate_strict_chains (T, m)

def cpt_max_chains (m) :
    return m^(m-2)

def zeta_pnc (n, m) :
    P = Poset ([list (generate_pnc (m)), couvre_pnc])
    res = P.zeta_polynomial ()
    return res (q = n)

def cpt_weak_chains (n, m) :
    res = binomial (n * m, m - 1)
    res = res / m
    return res

def is_k_divisible (P, k, m) :
    P1 = SetPartition (P)
    if not is_pnc (P1) :
        return False

    n = P1.base_set_cardinality ()
    if n != k * m :
        return False

    for p in P :
        l = len (p)
        if l % k != 0 :
            return False

    return True

def rk_k (P, k, m) :
    if not is_k_divisible (P, k, m) :
        return None

    return m - len (P)

def generate_pnc_k_h (m, k, h) :
    g = generate_pnc_k (m * k, h)
    for P in g :
        if is_k_divisible (P, k, m) :
            yield P

def cpt_pnc_k_h (m, k, h) :
    res = binomial (m, h) 
    res = res * binomial (k * m, h - 1)
    res = res / m
    return res

def generate_pnc_k_div (m, k) :
    g = generate_pnc (m * k)
    for P in g :
        if is_k_divisible (P, k, m) :
            yield P

def cpt_pnc_k_div (m, k) :
    res = 0
    for h in (1..m) :
        res = res + cpt_pnc_k_h (m, k, h)
    return res

def par_to_pnc_b_k (L, R, m, k) :
    h = len (L)
    if h != len (R) + 1 :
        return None

    R2 = []
    for e in R :
        for i in (1..m) :
            if k * (i - 1) + 1 <= e <= k * i :
                R2.append (i)
                break

    P, b = par_to_pnc_b (L, R2, m)
    s = sigb_hat (L, [R2], b, m)
    good, _ = good_par (s)
    w = k * (b - 1) + 1

    s3 = sigb (w, m * k)

    sizes = []
    good = list (good)
    good = good [ : : -1]

    while (good.count (')') != 0) :
        idx = (good [: : -1]).index (')')
        i = len (good) - idx - 1
        j = i
        size = 0

        while (good [j] != '(') :
            e = good [j]
            if e != ',' and e != ')' :
                size = size + 1
            j = j + 1

        sizes.append (size * k)
        good [i] = '*'

    L = [w]
    for i, e in enumerate (R) :
        l = sizes [i]
        idx = s3.index (e)
        idy = s3 [idx - l + 1]
        L.append (idy)

    return  (to_part (L, [R], m * k), w)

def generate_strict_chains_k (T, m, k) :
    P = Poset ([list (generate_pnc_k_div (m, k)), couvre_pnc])
    for c in P.chains () :
        c2 = c [ : : -1]
        T2 = []
        for e in c2 :
            T2.append (rk_k (e, k, m))
        if T [: : - 1] == T2 :
            yield c2

def cpt_strict_chains_k (T, m, k) :
    T = [0] + T + [m - 1]
    S = []
    l = len (T)
    for i in range (1, l) :
        s = T[i] - T [i - 1]
        S.append (s)

    res = binomial (m, S[0])
    for e in S [1 : ] :
        res = res * binomial (m * k, e)
    
    res = res / m
    return res

def generate_max_chains_k (m, k) :
    T = [i for i in range (m)]
    return generate_strict_chains_k (T, m, k)

def cpt_max_chains_k (m, k) :
    res = (k * m) ^ (m - 2)
    res = k * res
    return res

def zeta_pnc_k (n, m, k) :
    P = Poset ([list (generate_pnc_k_div (m, k)), couvre_pnc])
    res = P.zeta_polynomial ()
    return res (q = n)

def cpt_weak_chains_k (n, m, k) :
    res = binomial (m * (k * (n - 1) + 1), m - 1)
    res = res / m
    return res