s0: load a1
s1: boxdot s0 0 0
s2: not s1
s3: load a2
s4: boxdot s3 0 0
s5: not s4
s6: and s2 s5
s7: not s6
s8: boxdot s7 96 96
s9: not s8
s10: load a0
s11: boxdot s10 96 96
s12: boxdot s7 120 120
s13: and s11 s12
s14: not s13
s15: and s9 s14
s16: not s15
s17: not s16
s18: boxdot s10 120 120
s19: and s11 s18
s20: boxdot s7 144 144
s21: and s19 s20
s22: not s21
s23: and s17 s22
s24: not s23
s25: boxdot s24 0 0
s26: end s25 0
s27: end sequence