s0: load a2
s1: boxdot s0 26 26
s2: not s1
s3: boxdot s0 4 4
s4: not s3
s5: boxdot s0 6 6
s6: not s5
s7: and s4 s6
s8: not s7
s9: not s8
s10: boxdot s0 8 8
s11: not s10
s12: and s9 s11
s13: not s12
s14: not s13
s15: boxdot s0 10 10
s16: not s15
s17: and s14 s16
s18: not s17
s19: not s18
s20: boxdot s0 12 12
s21: not s20
s22: and s19 s21
s23: not s22
s24: not s23
s25: boxdot s0 14 14
s26: not s25
s27: and s24 s26
s28: not s27
s29: not s28
s30: boxdot s0 16 16
s31: not s30
s32: and s29 s31
s33: not s32
s34: not s33
s35: boxdot s0 18 18
s36: not s35
s37: and s34 s36
s38: not s37
s39: not s38
s40: boxdot s0 20 20
s41: not s40
s42: and s39 s41
s43: not s42
s44: not s43
s45: boxdot s0 22 22
s46: not s45
s47: and s44 s46
s48: not s47
s49: not s48
s50: boxdot s0 24 24
s51: not s50
s52: and s49 s51
s53: not s52
s54: not s53
s55: and s54 s2
s56: not s55
s57: not s56
s58: boxdot s0 28 28
s59: not s58
s60: and s57 s59
s61: not s60
s62: boxdot s61 12 12
s63: load a1
s64: boxdot s63 6 6
s65: boxdot s63 12 12
s66: and s64 s65
s67: and s66 s3
s68: and s67 s5
s69: and s68 s10
s70: boxdot s63 2 2
s71: boxdot s63 4 4
s72: and s70 s71
s73: and s72 s3
s74: and s73 s5
s75: and s74 s10
s76: boxdot s75 6 6
s77: boxdot s75 12 12
s78: and s76 s77
s79: end s78 8
s80: and s64 s20
s81: not s80
s82: and s6 s81
s83: not s82
s84: end s83 9
s85: boxdot s61 18 18
s86: end s69 7
s87: and s62 s85
s88: boxdot s61 30 30
s89: end s63 1
s90: and s63 s0
s91: end s90 2
s92: boxdot s63 1 2
s93: end s92 3
s94: boxdot s63 8 8
s95: and s64 s94
s96: end s95 4
s97: boxdot s92 6 6
s98: boxdot s92 8 8
s99: and s97 s98
s100: boxdot s99 6 6
s101: boxdot s99 12 12
s102: and s100 s101
s103: end s102 5
s104: and s66 s20
s105: and s104 s35
s106: and s105 s50
s107: end s106 6
s108: not s64
s109: and s5 s65
s110: not s109
s111: and s108 s110
s112: not s111
s113: and s112 s20
s114: not s113
s115: load a3
s116: boxdot s115 12 12
s117: and s116 s35
s118: not s117
s119: and s114 s118
s120: not s119
s121: not s120
s122: boxdot s115 18 18
s123: and s116 s122
s124: and s123 s50
s125: not s124
s126: and s121 s125
s127: not s126
s128: end s127 10
s129: end s61 11
s130: boxdot s61 24 24
s131: and s87 s130
s132: and s131 s88
s133: end s132 12
s134: end sequence