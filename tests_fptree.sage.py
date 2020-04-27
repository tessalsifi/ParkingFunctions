

# This file was *autogenerated* from the file tests_fptree.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_6 = Integer(6); _sage_const_0 = Integer(0)
sage.repl.load.load(sage.repl.load.base64.b64decode("ZnB0cmVlLnNhZ2U="),globals(),False)

# TESTS FPT
print ("Tests FPT")

T1 = FPT (
    [_sage_const_1 , _sage_const_2 , _sage_const_3 , _sage_const_4 , _sage_const_5 , _sage_const_6 ],
    [_sage_const_2 , _sage_const_5 ],
    [
        FPT (
            [_sage_const_1 , _sage_const_3 , _sage_const_4 ],
            [_sage_const_1 , _sage_const_3 , _sage_const_4 ],
            [
                FPT ([], [], []),
                FPT ([], [], []),
                FPT ([], [], [])
            ]
            ),
        FPT (
            [_sage_const_6 ],
            [_sage_const_6 ],
            [FPT ([], [], [])]
        )
    ]
)

T2 = FPT (
    [_sage_const_1 , _sage_const_2 , _sage_const_3 , _sage_const_4 , _sage_const_5 , _sage_const_6 ],
    [_sage_const_2 , _sage_const_5 ],
    [
        FPT (
            [_sage_const_1 , _sage_const_3 , _sage_const_4 , _sage_const_5 ],
            [_sage_const_1 , _sage_const_3 , _sage_const_4 , _sage_const_5 ],
            [
                FPT ([], [], []),
                FPT ([], [], []),
                FPT ([], [], []),
                FPT ([], [], [])
            ]
            ),
        FPT (
            [_sage_const_6 ],
            [_sage_const_6 ],
            [FPT ([], [], [])]
        )
    ]
)

T3 = FPT (
    [_sage_const_1 , _sage_const_2 , _sage_const_3 , _sage_const_4 , _sage_const_5 , _sage_const_6 ],
    [_sage_const_2 , _sage_const_5 ],
    [
        FPT (
            [_sage_const_1 , _sage_const_3 , _sage_const_5 ],
            [_sage_const_1 , _sage_const_3 , _sage_const_4 ],
            [
                FPT ([], [], []),
                FPT ([], [], []),
                FPT ([], [], [])
            ]
            ),
        FPT (
            [_sage_const_6 ],
            [_sage_const_6 ],
            [FPT ([], [], [])]
        )
    ]
)

T4 = FPT (
    [_sage_const_1 , _sage_const_2 , _sage_const_3 , _sage_const_4 , _sage_const_5 , _sage_const_6 ],
    [_sage_const_2 , _sage_const_5 ],
    [
        FPT (
            [_sage_const_1 , _sage_const_3 , _sage_const_4 ],
            [_sage_const_1 , _sage_const_3 , _sage_const_4 ],
            [
                FPT ([], [], []),
                FPT ([], [], [])
            ]
            ),
        FPT (
            [_sage_const_6 ],
            [_sage_const_6 ],
            [FPT ([], [], [])]
        )
    ]
)

print (T1.is_FPT ())
print (T2.is_FPT ())
print (T3.is_FPT ())
print (T4.is_FPT ())

T1.pretty_print ()

print (pref (T1))
print (fpt_to_fp (T1))
print ()

L = ParkingFunction ([_sage_const_1 , _sage_const_6 , _sage_const_2 , _sage_const_2 , _sage_const_3 , _sage_const_5 , _sage_const_3 ])
T5 = fp_to_fpt (L)
T5.pretty_print ()
print ()

T6 = fp_to_fpt (fpt_to_fp (T1))
T6.pretty_print ()
print ()

n = _sage_const_3 
g = generate_fpt (n)
k = _sage_const_0 
for e in g :
    e.pretty_print ()
    print ()
    k = k + _sage_const_1 
print (k)
print ((n + _sage_const_1 )**(n - _sage_const_1 ))
print ()

