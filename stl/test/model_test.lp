\ Model STL formula: ((G[0.0, 10.0] (x >= 3.0)) && (G[12.0, 15.0] (x <= 1.0)) && (G[17.0, 24.0] (x >= 4.0)))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - rho + 0 u_0 + 0 v_0 + 0 w_0 + 0 u_1 + 0 v_1 + 0 w_1 + 0 u_2 + 0 v_2
   + 0 w_2 + 0 u_3 + 0 v_3 + 0 w_3 + 0 u_4 + 0 v_4 + 0 w_4 + 0 u_5 + 0 v_5
   + 0 w_5 + 0 u_6 + 0 v_6 + 0 w_6 + 0 u_7 + 0 v_7 + 0 w_7 + 0 u_8 + 0 v_8
   + 0 w_8 + 0 u_9 + 0 v_9 + 0 w_9 + 0 u_10 + 0 v_10 + 0 w_10 + 0 u_11
   + 0 v_11 + 0 w_11 + 0 u_12 + 0 v_12 + 0 w_12 + 0 u_13 + 0 v_13 + 0 w_13
   + 0 u_14 + 0 v_14 + 0 w_14 + 0 u_15 + 0 v_15 + 0 w_15 + 0 u_16 + 0 v_16
   + 0 w_16 + 0 u_17 + 0 v_17 + 0 w_17 + 0 u_18 + 0 v_18 + 0 w_18 + 0 u_19
   + 0 v_19 + 0 w_19 + 0 u_20 + 0 v_20 + 0 w_20 + 0 u_21 + 0 v_21 + 0 w_21
   + 0 u_22 + 0 v_22 + 0 w_22 + 0 u_23 + 0 v_23 + 0 w_23 + 0 u_48 + 0 v_48
   + 0 w_48
Subject To
 R0: x_0 = 3
 R1: y_0 = 5
 R2: z_0 = 5
 R3: x_1 = 3
 R4: y_1 = 3
 R5: z_1 = 2
 R6: x_2 = 3
 R7: y_2 = 5
 R8: z_2 = 2
 R9: x_3 = 3
 R10: y_3 = 3
 R11: z_3 = 5
 R12: x_4 = 3
 R13: y_4 = 2
 R14: z_4 = 2
 R15: x_5 = 3
 R16: y_5 = 2
 R17: z_5 = -1
 R18: x_6 = 0
 R19: y_6 = 0
 R20: z_6 = 2
 R21: x_7 = -3
 R22: y_7 = -2
 R23: z_7 = 5
 R24: x_8 = -1
 R25: y_8 = 1
 R26: z_8 = 2
 R27: x_9 = 1
 R28: y_9 = 4
 R29: z_9 = 5
 R30: x_10 = 0
 R31: y_10 = 2
 R32: z_10 = 2
 R33: x_11 = 2
 R34: y_11 = 5
 R35: z_11 = 5
 R36: x_12 = 4
 R37: y_12 = 3
 R38: z_12 = 2
 R39: x_13 = 4
 R40: y_13 = 1
 R41: z_13 = 2
 R42: x_14 = 4
 R43: y_14 = -1
 R44: z_14 = -1
 R45: x_15 = 4
 R46: y_15 = 2
 R47: z_15 = 2
 R48: x_16 = 4
 R49: y_16 = 5
 R50: z_16 = -1
 R51: x_17 = 4
 R52: y_17 = 3
 R53: z_17 = 2
 R54: x_18 = 4
 R55: y_18 = 4
 R56: z_18 = 5
 R57: x_19 = 5
 R58: y_19 = 2
 R59: z_19 = 2
 R60: x_20 = 2
 R61: y_20 = 0
 R62: z_20 = 2
 R63: x_21 = 2
 R64: y_21 = 3
 R65: z_21 = 2
 R66: x_22 = 2
 R67: y_22 = 1
 R68: z_22 = 2
 R69: x_23 = 2
 R70: y_23 = -1
 R71: z_23 = 2
 R72: x_24 = 2
 R73: y_24 = 2
 R74: z_24 = 2
 R75: - x_24 - u_24 + x_25 = 0
 R76: - y_24 - v_24 + y_25 = 0
 R77: - z_24 - w_24 + z_25 = 0
 R78: - x_25 - u_25 + x_26 = 0
 R79: - y_25 - v_25 + y_26 = 0
 R80: - z_25 - w_25 + z_26 = 0
 R81: - x_26 - u_26 + x_27 = 0
 R82: - y_26 - v_26 + y_27 = 0
 R83: - z_26 - w_26 + z_27 = 0
 R84: - x_27 - u_27 + x_28 = 0
 R85: - y_27 - v_27 + y_28 = 0
 R86: - z_27 - w_27 + z_28 = 0
 R87: - x_28 - u_28 + x_29 = 0
 R88: - y_28 - v_28 + y_29 = 0
 R89: - z_28 - w_28 + z_29 = 0
 R90: - x_29 - u_29 + x_30 = 0
 R91: - y_29 - v_29 + y_30 = 0
 R92: - z_29 - w_29 + z_30 = 0
 R93: - x_30 - u_30 + x_31 = 0
 R94: - y_30 - v_30 + y_31 = 0
 R95: - z_30 - w_30 + z_31 = 0
 R96: - x_31 - u_31 + x_32 = 0
 R97: - y_31 - v_31 + y_32 = 0
 R98: - z_31 - w_31 + z_32 = 0
 R99: - x_32 - u_32 + x_33 = 0
 R100: - y_32 - v_32 + y_33 = 0
 R101: - z_32 - w_32 + z_33 = 0
 R102: - x_33 - u_33 + x_34 = 0
 R103: - y_33 - v_33 + y_34 = 0
 R104: - z_33 - w_33 + z_34 = 0
 R105: - x_34 - u_34 + x_35 = 0
 R106: - y_34 - v_34 + y_35 = 0
 R107: - z_34 - w_34 + z_35 = 0
 R108: - x_35 - u_35 + x_36 = 0
 R109: - y_35 - v_35 + y_36 = 0
 R110: - z_35 - w_35 + z_36 = 0
 R111: - x_36 - u_36 + x_37 = 0
 R112: - y_36 - v_36 + y_37 = 0
 R113: - z_36 - w_36 + z_37 = 0
 R114: - x_37 - u_37 + x_38 = 0
 R115: - y_37 - v_37 + y_38 = 0
 R116: - z_37 - w_37 + z_38 = 0
 R117: - x_38 - u_38 + x_39 = 0
 R118: - y_38 - v_38 + y_39 = 0
 R119: - z_38 - w_38 + z_39 = 0
 R120: - x_39 - u_39 + x_40 = 0
 R121: - y_39 - v_39 + y_40 = 0
 R122: - z_39 - w_39 + z_40 = 0
 R123: - x_40 - u_40 + x_41 = 0
 R124: - y_40 - v_40 + y_41 = 0
 R125: - z_40 - w_40 + z_41 = 0
 R126: - x_41 - u_41 + x_42 = 0
 R127: - y_41 - v_41 + y_42 = 0
 R128: - z_41 - w_41 + z_42 = 0
 R129: - x_42 - u_42 + x_43 = 0
 R130: - y_42 - v_42 + y_43 = 0
 R131: - z_42 - w_42 + z_43 = 0
 R132: - x_43 - u_43 + x_44 = 0
 R133: - y_43 - v_43 + y_44 = 0
 R134: - z_43 - w_43 + z_44 = 0
 R135: - x_44 - u_44 + x_45 = 0
 R136: - y_44 - v_44 + y_45 = 0
 R137: - z_44 - w_44 + z_45 = 0
 R138: - x_45 - u_45 + x_46 = 0
 R139: - y_45 - v_45 + y_46 = 0
 R140: - z_45 - w_45 + z_46 = 0
 R141: - x_46 - u_46 + x_47 = 0
 R142: - y_46 - v_46 + y_47 = 0
 R143: - z_46 - w_46 + z_47 = 0
 R144: - x_47 - u_47 + x_48 = 0
 R145: - y_47 - v_47 + y_48 = 0
 R146: - z_47 - w_47 + z_48 = 0
 R147: - rho + x_0 - 20 predicate_2dx22dd95ed78b4d217_0 <= 3
 R148: - rho + x_0 - 20 predicate_2dx22dd95ed78b4d217_0 >= -17
 R149: - rho + x_1 - 20 predicate_2dx22dd95ed78b4d217_1 <= 3
 R150: - rho + x_1 - 20 predicate_2dx22dd95ed78b4d217_1 >= -17
 R151: - rho + x_2 - 20 predicate_2dx22dd95ed78b4d217_2 <= 3
 R152: - rho + x_2 - 20 predicate_2dx22dd95ed78b4d217_2 >= -17
 R153: - rho + x_3 - 20 predicate_2dx22dd95ed78b4d217_3 <= 3
 R154: - rho + x_3 - 20 predicate_2dx22dd95ed78b4d217_3 >= -17
 R155: - rho + x_4 - 20 predicate_2dx22dd95ed78b4d217_4 <= 3
 R156: - rho + x_4 - 20 predicate_2dx22dd95ed78b4d217_4 >= -17
 R157: - rho + x_5 - 20 predicate_2dx22dd95ed78b4d217_5 <= 3
 R158: - rho + x_5 - 20 predicate_2dx22dd95ed78b4d217_5 >= -17
 R159: - rho + x_6 - 20 predicate_2dx22dd95ed78b4d217_6 <= 3
 R160: - rho + x_6 - 20 predicate_2dx22dd95ed78b4d217_6 >= -17
 R161: - rho + x_7 - 20 predicate_2dx22dd95ed78b4d217_7 <= 3
 R162: - rho + x_7 - 20 predicate_2dx22dd95ed78b4d217_7 >= -17
 R163: - rho + x_8 - 20 predicate_2dx22dd95ed78b4d217_8 <= 3
 R164: - rho + x_8 - 20 predicate_2dx22dd95ed78b4d217_8 >= -17
 R165: - rho + x_9 - 20 predicate_2dx22dd95ed78b4d217_9 <= 3
 R166: - rho + x_9 - 20 predicate_2dx22dd95ed78b4d217_9 >= -17
 R167: - rho + x_10 - 20 predicate_2dx22dd95ed78b4d217_10 <= 3
 R168: - rho + x_10 - 20 predicate_2dx22dd95ed78b4d217_10 >= -17
 R169: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_0 <= 0
 R170: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_1 <= 0
 R171: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_2 <= 0
 R172: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_3 <= 0
 R173: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_4 <= 0
 R174: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_5 <= 0
 R175: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_6 <= 0
 R176: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_7 <= 0
 R177: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_8 <= 0
 R178: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_9 <= 0
 R179: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_10
   <= 0
 R180: always_2dx778710aa24bf45ad_0 - predicate_2dx22dd95ed78b4d217_0
   - predicate_2dx22dd95ed78b4d217_1 - predicate_2dx22dd95ed78b4d217_2
   - predicate_2dx22dd95ed78b4d217_3 - predicate_2dx22dd95ed78b4d217_4
   - predicate_2dx22dd95ed78b4d217_5 - predicate_2dx22dd95ed78b4d217_6
   - predicate_2dx22dd95ed78b4d217_7 - predicate_2dx22dd95ed78b4d217_8
   - predicate_2dx22dd95ed78b4d217_9 - predicate_2dx22dd95ed78b4d217_10
   >= -10
 R181: rho + x_12 + 20 predicate_2dx797b9146c700e2d3_12 >= 1
 R182: rho + x_12 + 20 predicate_2dx797b9146c700e2d3_12 <= 21
 R183: rho + x_13 + 20 predicate_2dx797b9146c700e2d3_13 >= 1
 R184: rho + x_13 + 20 predicate_2dx797b9146c700e2d3_13 <= 21
 R185: rho + x_14 + 20 predicate_2dx797b9146c700e2d3_14 >= 1
 R186: rho + x_14 + 20 predicate_2dx797b9146c700e2d3_14 <= 21
 R187: rho + x_15 + 20 predicate_2dx797b9146c700e2d3_15 >= 1
 R188: rho + x_15 + 20 predicate_2dx797b9146c700e2d3_15 <= 21
 R189: always_2dx96788d971626418_0 - predicate_2dx797b9146c700e2d3_12 <= 0
 R190: always_2dx96788d971626418_0 - predicate_2dx797b9146c700e2d3_13 <= 0
 R191: always_2dx96788d971626418_0 - predicate_2dx797b9146c700e2d3_14 <= 0
 R192: always_2dx96788d971626418_0 - predicate_2dx797b9146c700e2d3_15 <= 0
 R193: always_2dx96788d971626418_0 - predicate_2dx797b9146c700e2d3_12
   - predicate_2dx797b9146c700e2d3_13 - predicate_2dx797b9146c700e2d3_14
   - predicate_2dx797b9146c700e2d3_15 >= -3
 R194: - rho + x_17 - 20 predicate_2dx30be4d89f565bb0c_17 <= 4
 R195: - rho + x_17 - 20 predicate_2dx30be4d89f565bb0c_17 >= -16
 R196: - rho + x_18 - 20 predicate_2dx30be4d89f565bb0c_18 <= 4
 R197: - rho + x_18 - 20 predicate_2dx30be4d89f565bb0c_18 >= -16
 R198: - rho + x_19 - 20 predicate_2dx30be4d89f565bb0c_19 <= 4
 R199: - rho + x_19 - 20 predicate_2dx30be4d89f565bb0c_19 >= -16
 R200: - rho + x_20 - 20 predicate_2dx30be4d89f565bb0c_20 <= 4
 R201: - rho + x_20 - 20 predicate_2dx30be4d89f565bb0c_20 >= -16
 R202: - rho + x_21 - 20 predicate_2dx30be4d89f565bb0c_21 <= 4
 R203: - rho + x_21 - 20 predicate_2dx30be4d89f565bb0c_21 >= -16
 R204: - rho + x_22 - 20 predicate_2dx30be4d89f565bb0c_22 <= 4
 R205: - rho + x_22 - 20 predicate_2dx30be4d89f565bb0c_22 >= -16
 R206: - rho + x_23 - 20 predicate_2dx30be4d89f565bb0c_23 <= 4
 R207: - rho + x_23 - 20 predicate_2dx30be4d89f565bb0c_23 >= -16
 R208: - rho + x_24 - 20 predicate_2dx30be4d89f565bb0c_24 <= 4
 R209: - rho + x_24 - 20 predicate_2dx30be4d89f565bb0c_24 >= -16
 R210: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_17
   <= 0
 R211: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_18
   <= 0
 R212: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_19
   <= 0
 R213: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_20
   <= 0
 R214: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_21
   <= 0
 R215: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_22
   <= 0
 R216: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_23
   <= 0
 R217: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_24
   <= 0
 R218: always_2dx33306d9e7f58b6b0_0 - predicate_2dx30be4d89f565bb0c_17
   - predicate_2dx30be4d89f565bb0c_18 - predicate_2dx30be4d89f565bb0c_19
   - predicate_2dx30be4d89f565bb0c_20 - predicate_2dx30be4d89f565bb0c_21
   - predicate_2dx30be4d89f565bb0c_22 - predicate_2dx30be4d89f565bb0c_23
   - predicate_2dx30be4d89f565bb0c_24 >= -7
 R219: and_2bx774dabba49604f84_0 - always_2dx778710aa24bf45ad_0 <= 0
 R220: and_2bx774dabba49604f84_0 - always_2dx96788d971626418_0 <= 0
 R221: and_2bx774dabba49604f84_0 - always_2dx33306d9e7f58b6b0_0 <= 0
 R222: and_2bx774dabba49604f84_0 - always_2dx778710aa24bf45ad_0
   - always_2dx96788d971626418_0 - always_2dx33306d9e7f58b6b0_0 >= -2
 formula_satisfaction: and_2bx774dabba49604f84_0 = 1
Bounds
 -infinity <= rho <= 999
 -4 <= x_0 <= 5
 -4 <= y_0 <= 5
 -4 <= z_0 <= 5
 -3 <= u_0 <= 2
 -2 <= v_0 <= 3
 -3 <= w_0 <= 3
 -4 <= x_1 <= 5
 -4 <= y_1 <= 5
 -4 <= z_1 <= 5
 -3 <= u_1 <= 2
 -2 <= v_1 <= 3
 -3 <= w_1 <= 3
 -4 <= x_2 <= 5
 -4 <= y_2 <= 5
 -4 <= z_2 <= 5
 -3 <= u_2 <= 2
 -2 <= v_2 <= 3
 -3 <= w_2 <= 3
 -4 <= x_3 <= 5
 -4 <= y_3 <= 5
 -4 <= z_3 <= 5
 -3 <= u_3 <= 2
 -2 <= v_3 <= 3
 -3 <= w_3 <= 3
 -4 <= x_4 <= 5
 -4 <= y_4 <= 5
 -4 <= z_4 <= 5
 -3 <= u_4 <= 2
 -2 <= v_4 <= 3
 -3 <= w_4 <= 3
 -4 <= x_5 <= 5
 -4 <= y_5 <= 5
 -4 <= z_5 <= 5
 -3 <= u_5 <= 2
 -2 <= v_5 <= 3
 -3 <= w_5 <= 3
 -4 <= x_6 <= 5
 -4 <= y_6 <= 5
 -4 <= z_6 <= 5
 -3 <= u_6 <= 2
 -2 <= v_6 <= 3
 -3 <= w_6 <= 3
 -4 <= x_7 <= 5
 -4 <= y_7 <= 5
 -4 <= z_7 <= 5
 -3 <= u_7 <= 2
 -2 <= v_7 <= 3
 -3 <= w_7 <= 3
 -4 <= x_8 <= 5
 -4 <= y_8 <= 5
 -4 <= z_8 <= 5
 -3 <= u_8 <= 2
 -2 <= v_8 <= 3
 -3 <= w_8 <= 3
 -4 <= x_9 <= 5
 -4 <= y_9 <= 5
 -4 <= z_9 <= 5
 -3 <= u_9 <= 2
 -2 <= v_9 <= 3
 -3 <= w_9 <= 3
 -4 <= x_10 <= 5
 -4 <= y_10 <= 5
 -4 <= z_10 <= 5
 -3 <= u_10 <= 2
 -2 <= v_10 <= 3
 -3 <= w_10 <= 3
 -4 <= x_11 <= 5
 -4 <= y_11 <= 5
 -4 <= z_11 <= 5
 -3 <= u_11 <= 2
 -2 <= v_11 <= 3
 -3 <= w_11 <= 3
 -4 <= x_12 <= 5
 -4 <= y_12 <= 5
 -4 <= z_12 <= 5
 -3 <= u_12 <= 2
 -2 <= v_12 <= 3
 -3 <= w_12 <= 3
 -4 <= x_13 <= 5
 -4 <= y_13 <= 5
 -4 <= z_13 <= 5
 -3 <= u_13 <= 2
 -2 <= v_13 <= 3
 -3 <= w_13 <= 3
 -4 <= x_14 <= 5
 -4 <= y_14 <= 5
 -4 <= z_14 <= 5
 -3 <= u_14 <= 2
 -2 <= v_14 <= 3
 -3 <= w_14 <= 3
 -4 <= x_15 <= 5
 -4 <= y_15 <= 5
 -4 <= z_15 <= 5
 -3 <= u_15 <= 2
 -2 <= v_15 <= 3
 -3 <= w_15 <= 3
 -4 <= x_16 <= 5
 -4 <= y_16 <= 5
 -4 <= z_16 <= 5
 -3 <= u_16 <= 2
 -2 <= v_16 <= 3
 -3 <= w_16 <= 3
 -4 <= x_17 <= 5
 -4 <= y_17 <= 5
 -4 <= z_17 <= 5
 -3 <= u_17 <= 2
 -2 <= v_17 <= 3
 -3 <= w_17 <= 3
 -4 <= x_18 <= 5
 -4 <= y_18 <= 5
 -4 <= z_18 <= 5
 -3 <= u_18 <= 2
 -2 <= v_18 <= 3
 -3 <= w_18 <= 3
 -4 <= x_19 <= 5
 -4 <= y_19 <= 5
 -4 <= z_19 <= 5
 -3 <= u_19 <= 2
 -2 <= v_19 <= 3
 -3 <= w_19 <= 3
 -4 <= x_20 <= 5
 -4 <= y_20 <= 5
 -4 <= z_20 <= 5
 -3 <= u_20 <= 2
 -2 <= v_20 <= 3
 -3 <= w_20 <= 3
 -4 <= x_21 <= 5
 -4 <= y_21 <= 5
 -4 <= z_21 <= 5
 -3 <= u_21 <= 2
 -2 <= v_21 <= 3
 -3 <= w_21 <= 3
 -4 <= x_22 <= 5
 -4 <= y_22 <= 5
 -4 <= z_22 <= 5
 -3 <= u_22 <= 2
 -2 <= v_22 <= 3
 -3 <= w_22 <= 3
 -4 <= x_23 <= 5
 -4 <= y_23 <= 5
 -4 <= z_23 <= 5
 -3 <= u_23 <= 2
 -2 <= v_23 <= 3
 -3 <= w_23 <= 3
 -4 <= x_24 <= 5
 -4 <= y_24 <= 5
 -4 <= z_24 <= 5
 -3 <= u_24 <= 2
 -2 <= v_24 <= 3
 -3 <= w_24 <= 3
 -4 <= x_25 <= 5
 -4 <= y_25 <= 5
 -4 <= z_25 <= 5
 -3 <= u_25 <= 2
 -2 <= v_25 <= 3
 -3 <= w_25 <= 3
 -4 <= x_26 <= 5
 -4 <= y_26 <= 5
 -4 <= z_26 <= 5
 -3 <= u_26 <= 2
 -2 <= v_26 <= 3
 -3 <= w_26 <= 3
 -4 <= x_27 <= 5
 -4 <= y_27 <= 5
 -4 <= z_27 <= 5
 -3 <= u_27 <= 2
 -2 <= v_27 <= 3
 -3 <= w_27 <= 3
 -4 <= x_28 <= 5
 -4 <= y_28 <= 5
 -4 <= z_28 <= 5
 -3 <= u_28 <= 2
 -2 <= v_28 <= 3
 -3 <= w_28 <= 3
 -4 <= x_29 <= 5
 -4 <= y_29 <= 5
 -4 <= z_29 <= 5
 -3 <= u_29 <= 2
 -2 <= v_29 <= 3
 -3 <= w_29 <= 3
 -4 <= x_30 <= 5
 -4 <= y_30 <= 5
 -4 <= z_30 <= 5
 -3 <= u_30 <= 2
 -2 <= v_30 <= 3
 -3 <= w_30 <= 3
 -4 <= x_31 <= 5
 -4 <= y_31 <= 5
 -4 <= z_31 <= 5
 -3 <= u_31 <= 2
 -2 <= v_31 <= 3
 -3 <= w_31 <= 3
 -4 <= x_32 <= 5
 -4 <= y_32 <= 5
 -4 <= z_32 <= 5
 -3 <= u_32 <= 2
 -2 <= v_32 <= 3
 -3 <= w_32 <= 3
 -4 <= x_33 <= 5
 -4 <= y_33 <= 5
 -4 <= z_33 <= 5
 -3 <= u_33 <= 2
 -2 <= v_33 <= 3
 -3 <= w_33 <= 3
 -4 <= x_34 <= 5
 -4 <= y_34 <= 5
 -4 <= z_34 <= 5
 -3 <= u_34 <= 2
 -2 <= v_34 <= 3
 -3 <= w_34 <= 3
 -4 <= x_35 <= 5
 -4 <= y_35 <= 5
 -4 <= z_35 <= 5
 -3 <= u_35 <= 2
 -2 <= v_35 <= 3
 -3 <= w_35 <= 3
 -4 <= x_36 <= 5
 -4 <= y_36 <= 5
 -4 <= z_36 <= 5
 -3 <= u_36 <= 2
 -2 <= v_36 <= 3
 -3 <= w_36 <= 3
 -4 <= x_37 <= 5
 -4 <= y_37 <= 5
 -4 <= z_37 <= 5
 -3 <= u_37 <= 2
 -2 <= v_37 <= 3
 -3 <= w_37 <= 3
 -4 <= x_38 <= 5
 -4 <= y_38 <= 5
 -4 <= z_38 <= 5
 -3 <= u_38 <= 2
 -2 <= v_38 <= 3
 -3 <= w_38 <= 3
 -4 <= x_39 <= 5
 -4 <= y_39 <= 5
 -4 <= z_39 <= 5
 -3 <= u_39 <= 2
 -2 <= v_39 <= 3
 -3 <= w_39 <= 3
 -4 <= x_40 <= 5
 -4 <= y_40 <= 5
 -4 <= z_40 <= 5
 -3 <= u_40 <= 2
 -2 <= v_40 <= 3
 -3 <= w_40 <= 3
 -4 <= x_41 <= 5
 -4 <= y_41 <= 5
 -4 <= z_41 <= 5
 -3 <= u_41 <= 2
 -2 <= v_41 <= 3
 -3 <= w_41 <= 3
 -4 <= x_42 <= 5
 -4 <= y_42 <= 5
 -4 <= z_42 <= 5
 -3 <= u_42 <= 2
 -2 <= v_42 <= 3
 -3 <= w_42 <= 3
 -4 <= x_43 <= 5
 -4 <= y_43 <= 5
 -4 <= z_43 <= 5
 -3 <= u_43 <= 2
 -2 <= v_43 <= 3
 -3 <= w_43 <= 3
 -4 <= x_44 <= 5
 -4 <= y_44 <= 5
 -4 <= z_44 <= 5
 -3 <= u_44 <= 2
 -2 <= v_44 <= 3
 -3 <= w_44 <= 3
 -4 <= x_45 <= 5
 -4 <= y_45 <= 5
 -4 <= z_45 <= 5
 -3 <= u_45 <= 2
 -2 <= v_45 <= 3
 -3 <= w_45 <= 3
 -4 <= x_46 <= 5
 -4 <= y_46 <= 5
 -4 <= z_46 <= 5
 -3 <= u_46 <= 2
 -2 <= v_46 <= 3
 -3 <= w_46 <= 3
 -4 <= x_47 <= 5
 -4 <= y_47 <= 5
 -4 <= z_47 <= 5
 -3 <= u_47 <= 2
 -2 <= v_47 <= 3
 -3 <= w_47 <= 3
 -4 <= x_48 <= 5
 -4 <= y_48 <= 5
 -4 <= z_48 <= 5
 -3 <= u_48 <= 2
 -2 <= v_48 <= 3
 -3 <= w_48 <= 3
Binaries
 and_2bx774dabba49604f84_0 always_2dx778710aa24bf45ad_0
 predicate_2dx22dd95ed78b4d217_0 predicate_2dx22dd95ed78b4d217_1
 predicate_2dx22dd95ed78b4d217_2 predicate_2dx22dd95ed78b4d217_3
 predicate_2dx22dd95ed78b4d217_4 predicate_2dx22dd95ed78b4d217_5
 predicate_2dx22dd95ed78b4d217_6 predicate_2dx22dd95ed78b4d217_7
 predicate_2dx22dd95ed78b4d217_8 predicate_2dx22dd95ed78b4d217_9
 predicate_2dx22dd95ed78b4d217_10 always_2dx96788d971626418_0
 predicate_2dx797b9146c700e2d3_12 predicate_2dx797b9146c700e2d3_13
 predicate_2dx797b9146c700e2d3_14 predicate_2dx797b9146c700e2d3_15
 always_2dx33306d9e7f58b6b0_0 predicate_2dx30be4d89f565bb0c_17
 predicate_2dx30be4d89f565bb0c_18 predicate_2dx30be4d89f565bb0c_19
 predicate_2dx30be4d89f565bb0c_20 predicate_2dx30be4d89f565bb0c_21
 predicate_2dx30be4d89f565bb0c_22 predicate_2dx30be4d89f565bb0c_23
 predicate_2dx30be4d89f565bb0c_24
End
