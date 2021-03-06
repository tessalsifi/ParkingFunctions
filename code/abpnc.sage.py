

# This file was *autogenerated* from the file abpnc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
sage.repl.load.load(sage.repl.load.base64.b64decode("cG5jLnNhZ2U="),globals(),False)
sage.repl.load.load(sage.repl.load.base64.b64decode("cmR5Y2suc2FnZQ=="),globals(),False)

def mut_nc (P, Q) :
    if not P.is_noncrossing () :
        return False
    if not Q.is_noncrossing () :
        return False
    
    for B1 in P :
        for B2 in Q :
            for a in B1 :
                for c in B1 :
                    for b in B2 :
                        for d in B2 :
                            if a < b < c < d :
                                return False
                            if a > b > c > d :
                                return False
    return True

def generate_mut (b) :
    g1 = generate_pnc (b - _sage_const_1 )
    g2 = generate_pnc (b - _sage_const_1 )

    for P in g1 :
        for Q in g2 :
            if mut_nc (P, Q) :
                yield (P, Q)


class ABPNC :
    a = _sage_const_0 
    b = _sage_const_0 
    P = None
    Q = None

    def __init__ (self, a, b, P, Q) :
        self.a = a
        self.b = b
        self.P = P
        self.Q = Q
    
    def is_abpnc (self) :
        a, b, P, Q = self.a, self.b, self.P, self.Q

        if gcd (a, b) != _sage_const_1  :
            return False
        
        np = P.base_set_cardinality ()
        nq = Q.base_set_cardinality ()
        if np != b - _sage_const_1  :
            return False
        if nq != b - _sage_const_1  :
            return False

        return mut_nc (P, Q)

def generate_abpnc (a, b) :
    g = generate_rdyck (a, b)
    for e in g :
        p, lp = P (e)
        q, lq = Q (e)
        yield ABPNC (a, b, p, q), lp, lq

