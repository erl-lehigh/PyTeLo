\ Model S-WSTL formula: ((G[8.0, 18.0]^<lambda> ((x >= 6.0) &&^<lambda> (y >= 6.0))) &&^<lambda> (G[1.0, 7.0]^<lambda> ((x >= 3.0) ||^<lambda> (x <= -3.0) ||^<lambda> (y >= 3.0) ||^<lambda> (y <= -3.0))))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0 u_18 + 0 v_18 + 0 w_18 + rho_&&_2dx224a090b37463e1e_0
Subject To
 R0: - x_0 - u_0 + x_1 = 0
 R1: - y_0 - v_0 + y_1 = 0
 R2: - z_0 - w_0 + z_1 = 0
 R3: - x_1 - u_1 + x_2 = 0
 R4: - y_1 - v_1 + y_2 = 0
 R5: - z_1 - w_1 + z_2 = 0
 R6: - x_2 - u_2 + x_3 = 0
 R7: - y_2 - v_2 + y_3 = 0
 R8: - z_2 - w_2 + z_3 = 0
 R9: - x_3 - u_3 + x_4 = 0
 R10: - y_3 - v_3 + y_4 = 0
 R11: - z_3 - w_3 + z_4 = 0
 R12: - x_4 - u_4 + x_5 = 0
 R13: - y_4 - v_4 + y_5 = 0
 R14: - z_4 - w_4 + z_5 = 0
 R15: - x_5 - u_5 + x_6 = 0
 R16: - y_5 - v_5 + y_6 = 0
 R17: - z_5 - w_5 + z_6 = 0
 R18: - x_6 - u_6 + x_7 = 0
 R19: - y_6 - v_6 + y_7 = 0
 R20: - z_6 - w_6 + z_7 = 0
 R21: - x_7 - u_7 + x_8 = 0
 R22: - y_7 - v_7 + y_8 = 0
 R23: - z_7 - w_7 + z_8 = 0
 R24: - x_8 - u_8 + x_9 = 0
 R25: - y_8 - v_8 + y_9 = 0
 R26: - z_8 - w_8 + z_9 = 0
 R27: - x_9 - u_9 + x_10 = 0
 R28: - y_9 - v_9 + y_10 = 0
 R29: - z_9 - w_9 + z_10 = 0
 R30: - x_10 - u_10 + x_11 = 0
 R31: - y_10 - v_10 + y_11 = 0
 R32: - z_10 - w_10 + z_11 = 0
 R33: - x_11 - u_11 + x_12 = 0
 R34: - y_11 - v_11 + y_12 = 0
 R35: - z_11 - w_11 + z_12 = 0
 R36: - x_12 - u_12 + x_13 = 0
 R37: - y_12 - v_12 + y_13 = 0
 R38: - z_12 - w_12 + z_13 = 0
 R39: - x_13 - u_13 + x_14 = 0
 R40: - y_13 - v_13 + y_14 = 0
 R41: - z_13 - w_13 + z_14 = 0
 R42: - x_14 - u_14 + x_15 = 0
 R43: - y_14 - v_14 + y_15 = 0
 R44: - z_14 - w_14 + z_15 = 0
 R45: - x_15 - u_15 + x_16 = 0
 R46: - y_15 - v_15 + y_16 = 0
 R47: - z_15 - w_15 + z_16 = 0
 R48: - x_16 - u_16 + x_17 = 0
 R49: - y_16 - v_16 + y_17 = 0
 R50: - z_16 - w_16 + z_17 = 0
 R51: - x_17 - u_17 + x_18 = 0
 R52: - y_17 - v_17 + y_18 = 0
 R53: - z_17 - w_17 + z_18 = 0
 R54: x_0 = -5
 R55: y_0 = -1
 R56: z_0 = 0
 R57: u_0 = 0
 R58: v_0 = 0
 R59: w_0 = 0
 R60: x_8 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_8
   - rho_predicate_2dx4c7fa34b9cfd78d2_8 >= -994
 R61: x_8 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_8
   - rho_predicate_2dx4c7fa34b9cfd78d2_8 <= 6
 R62: y_8 - 1000 z_predicate_2bx32f72cccd281a177_8
   - rho_predicate_2bx32f72cccd281a177_8 >= -994
 R63: y_8 - 1000 z_predicate_2bx32f72cccd281a177_8
   - rho_predicate_2bx32f72cccd281a177_8 <= 6
 R64: rho_&&_2bx47d4d1370e9d7522_8 - rho_predicate_2dx4c7fa34b9cfd78d2_8
   <= 0
 R65: z_&&_2bx47d4d1370e9d7522_8 - z_predicate_2dx4c7fa34b9cfd78d2_8 <= 0
 R66: rho_&&_2bx47d4d1370e9d7522_8 - rho_predicate_2bx32f72cccd281a177_8
   <= 0
 R67: z_&&_2bx47d4d1370e9d7522_8 - z_predicate_2bx32f72cccd281a177_8 <= 0
 R68: z_&&_2bx47d4d1370e9d7522_8 - z_predicate_2dx4c7fa34b9cfd78d2_8
   - z_predicate_2bx32f72cccd281a177_8 >= -1
 R69: x_9 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_9
   - rho_predicate_2dx4c7fa34b9cfd78d2_9 >= -994
 R70: x_9 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_9
   - rho_predicate_2dx4c7fa34b9cfd78d2_9 <= 6
 R71: y_9 - 1000 z_predicate_2bx32f72cccd281a177_9
   - rho_predicate_2bx32f72cccd281a177_9 >= -994
 R72: y_9 - 1000 z_predicate_2bx32f72cccd281a177_9
   - rho_predicate_2bx32f72cccd281a177_9 <= 6
 R73: rho_&&_2bx47d4d1370e9d7522_9 - rho_predicate_2dx4c7fa34b9cfd78d2_9
   <= 0
 R74: z_&&_2bx47d4d1370e9d7522_9 - z_predicate_2dx4c7fa34b9cfd78d2_9 <= 0
 R75: rho_&&_2bx47d4d1370e9d7522_9 - rho_predicate_2bx32f72cccd281a177_9
   <= 0
 R76: z_&&_2bx47d4d1370e9d7522_9 - z_predicate_2bx32f72cccd281a177_9 <= 0
 R77: z_&&_2bx47d4d1370e9d7522_9 - z_predicate_2dx4c7fa34b9cfd78d2_9
   - z_predicate_2bx32f72cccd281a177_9 >= -1
 R78: x_10 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_10
   - rho_predicate_2dx4c7fa34b9cfd78d2_10 >= -994
 R79: x_10 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_10
   - rho_predicate_2dx4c7fa34b9cfd78d2_10 <= 6
 R80: y_10 - 1000 z_predicate_2bx32f72cccd281a177_10
   - rho_predicate_2bx32f72cccd281a177_10 >= -994
 R81: y_10 - 1000 z_predicate_2bx32f72cccd281a177_10
   - rho_predicate_2bx32f72cccd281a177_10 <= 6
 R82: rho_&&_2bx47d4d1370e9d7522_10 - rho_predicate_2dx4c7fa34b9cfd78d2_10
   <= 0
 R83: z_&&_2bx47d4d1370e9d7522_10 - z_predicate_2dx4c7fa34b9cfd78d2_10
   <= 0
 R84: rho_&&_2bx47d4d1370e9d7522_10 - rho_predicate_2bx32f72cccd281a177_10
   <= 0
 R85: z_&&_2bx47d4d1370e9d7522_10 - z_predicate_2bx32f72cccd281a177_10
   <= 0
 R86: z_&&_2bx47d4d1370e9d7522_10 - z_predicate_2dx4c7fa34b9cfd78d2_10
   - z_predicate_2bx32f72cccd281a177_10 >= -1
 R87: x_11 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_11
   - rho_predicate_2dx4c7fa34b9cfd78d2_11 >= -994
 R88: x_11 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_11
   - rho_predicate_2dx4c7fa34b9cfd78d2_11 <= 6
 R89: y_11 - 1000 z_predicate_2bx32f72cccd281a177_11
   - rho_predicate_2bx32f72cccd281a177_11 >= -994
 R90: y_11 - 1000 z_predicate_2bx32f72cccd281a177_11
   - rho_predicate_2bx32f72cccd281a177_11 <= 6
 R91: rho_&&_2bx47d4d1370e9d7522_11 - rho_predicate_2dx4c7fa34b9cfd78d2_11
   <= 0
 R92: z_&&_2bx47d4d1370e9d7522_11 - z_predicate_2dx4c7fa34b9cfd78d2_11
   <= 0
 R93: rho_&&_2bx47d4d1370e9d7522_11 - rho_predicate_2bx32f72cccd281a177_11
   <= 0
 R94: z_&&_2bx47d4d1370e9d7522_11 - z_predicate_2bx32f72cccd281a177_11
   <= 0
 R95: z_&&_2bx47d4d1370e9d7522_11 - z_predicate_2dx4c7fa34b9cfd78d2_11
   - z_predicate_2bx32f72cccd281a177_11 >= -1
 R96: x_12 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_12
   - rho_predicate_2dx4c7fa34b9cfd78d2_12 >= -994
 R97: x_12 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_12
   - rho_predicate_2dx4c7fa34b9cfd78d2_12 <= 6
 R98: y_12 - 1000 z_predicate_2bx32f72cccd281a177_12
   - rho_predicate_2bx32f72cccd281a177_12 >= -994
 R99: y_12 - 1000 z_predicate_2bx32f72cccd281a177_12
   - rho_predicate_2bx32f72cccd281a177_12 <= 6
 R100: rho_&&_2bx47d4d1370e9d7522_12 - rho_predicate_2dx4c7fa34b9cfd78d2_12
   <= 0
 R101: z_&&_2bx47d4d1370e9d7522_12 - z_predicate_2dx4c7fa34b9cfd78d2_12
   <= 0
 R102: rho_&&_2bx47d4d1370e9d7522_12 - rho_predicate_2bx32f72cccd281a177_12
   <= 0
 R103: z_&&_2bx47d4d1370e9d7522_12 - z_predicate_2bx32f72cccd281a177_12
   <= 0
 R104: z_&&_2bx47d4d1370e9d7522_12 - z_predicate_2dx4c7fa34b9cfd78d2_12
   - z_predicate_2bx32f72cccd281a177_12 >= -1
 R105: x_13 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_13
   - rho_predicate_2dx4c7fa34b9cfd78d2_13 >= -994
 R106: x_13 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_13
   - rho_predicate_2dx4c7fa34b9cfd78d2_13 <= 6
 R107: y_13 - 1000 z_predicate_2bx32f72cccd281a177_13
   - rho_predicate_2bx32f72cccd281a177_13 >= -994
 R108: y_13 - 1000 z_predicate_2bx32f72cccd281a177_13
   - rho_predicate_2bx32f72cccd281a177_13 <= 6
 R109: rho_&&_2bx47d4d1370e9d7522_13 - rho_predicate_2dx4c7fa34b9cfd78d2_13
   <= 0
 R110: z_&&_2bx47d4d1370e9d7522_13 - z_predicate_2dx4c7fa34b9cfd78d2_13
   <= 0
 R111: rho_&&_2bx47d4d1370e9d7522_13 - rho_predicate_2bx32f72cccd281a177_13
   <= 0
 R112: z_&&_2bx47d4d1370e9d7522_13 - z_predicate_2bx32f72cccd281a177_13
   <= 0
 R113: z_&&_2bx47d4d1370e9d7522_13 - z_predicate_2dx4c7fa34b9cfd78d2_13
   - z_predicate_2bx32f72cccd281a177_13 >= -1
 R114: x_14 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_14
   - rho_predicate_2dx4c7fa34b9cfd78d2_14 >= -994
 R115: x_14 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_14
   - rho_predicate_2dx4c7fa34b9cfd78d2_14 <= 6
 R116: y_14 - 1000 z_predicate_2bx32f72cccd281a177_14
   - rho_predicate_2bx32f72cccd281a177_14 >= -994
 R117: y_14 - 1000 z_predicate_2bx32f72cccd281a177_14
   - rho_predicate_2bx32f72cccd281a177_14 <= 6
 R118: rho_&&_2bx47d4d1370e9d7522_14 - rho_predicate_2dx4c7fa34b9cfd78d2_14
   <= 0
 R119: z_&&_2bx47d4d1370e9d7522_14 - z_predicate_2dx4c7fa34b9cfd78d2_14
   <= 0
 R120: rho_&&_2bx47d4d1370e9d7522_14 - rho_predicate_2bx32f72cccd281a177_14
   <= 0
 R121: z_&&_2bx47d4d1370e9d7522_14 - z_predicate_2bx32f72cccd281a177_14
   <= 0
 R122: z_&&_2bx47d4d1370e9d7522_14 - z_predicate_2dx4c7fa34b9cfd78d2_14
   - z_predicate_2bx32f72cccd281a177_14 >= -1
 R123: x_15 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_15
   - rho_predicate_2dx4c7fa34b9cfd78d2_15 >= -994
 R124: x_15 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_15
   - rho_predicate_2dx4c7fa34b9cfd78d2_15 <= 6
 R125: y_15 - 1000 z_predicate_2bx32f72cccd281a177_15
   - rho_predicate_2bx32f72cccd281a177_15 >= -994
 R126: y_15 - 1000 z_predicate_2bx32f72cccd281a177_15
   - rho_predicate_2bx32f72cccd281a177_15 <= 6
 R127: rho_&&_2bx47d4d1370e9d7522_15 - rho_predicate_2dx4c7fa34b9cfd78d2_15
   <= 0
 R128: z_&&_2bx47d4d1370e9d7522_15 - z_predicate_2dx4c7fa34b9cfd78d2_15
   <= 0
 R129: rho_&&_2bx47d4d1370e9d7522_15 - rho_predicate_2bx32f72cccd281a177_15
   <= 0
 R130: z_&&_2bx47d4d1370e9d7522_15 - z_predicate_2bx32f72cccd281a177_15
   <= 0
 R131: z_&&_2bx47d4d1370e9d7522_15 - z_predicate_2dx4c7fa34b9cfd78d2_15
   - z_predicate_2bx32f72cccd281a177_15 >= -1
 R132: x_16 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_16
   - rho_predicate_2dx4c7fa34b9cfd78d2_16 >= -994
 R133: x_16 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_16
   - rho_predicate_2dx4c7fa34b9cfd78d2_16 <= 6
 R134: y_16 - 1000 z_predicate_2bx32f72cccd281a177_16
   - rho_predicate_2bx32f72cccd281a177_16 >= -994
 R135: y_16 - 1000 z_predicate_2bx32f72cccd281a177_16
   - rho_predicate_2bx32f72cccd281a177_16 <= 6
 R136: rho_&&_2bx47d4d1370e9d7522_16 - rho_predicate_2dx4c7fa34b9cfd78d2_16
   <= 0
 R137: z_&&_2bx47d4d1370e9d7522_16 - z_predicate_2dx4c7fa34b9cfd78d2_16
   <= 0
 R138: rho_&&_2bx47d4d1370e9d7522_16 - rho_predicate_2bx32f72cccd281a177_16
   <= 0
 R139: z_&&_2bx47d4d1370e9d7522_16 - z_predicate_2bx32f72cccd281a177_16
   <= 0
 R140: z_&&_2bx47d4d1370e9d7522_16 - z_predicate_2dx4c7fa34b9cfd78d2_16
   - z_predicate_2bx32f72cccd281a177_16 >= -1
 R141: x_17 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_17
   - rho_predicate_2dx4c7fa34b9cfd78d2_17 >= -994
 R142: x_17 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_17
   - rho_predicate_2dx4c7fa34b9cfd78d2_17 <= 6
 R143: y_17 - 1000 z_predicate_2bx32f72cccd281a177_17
   - rho_predicate_2bx32f72cccd281a177_17 >= -994
 R144: y_17 - 1000 z_predicate_2bx32f72cccd281a177_17
   - rho_predicate_2bx32f72cccd281a177_17 <= 6
 R145: rho_&&_2bx47d4d1370e9d7522_17 - rho_predicate_2dx4c7fa34b9cfd78d2_17
   <= 0
 R146: z_&&_2bx47d4d1370e9d7522_17 - z_predicate_2dx4c7fa34b9cfd78d2_17
   <= 0
 R147: rho_&&_2bx47d4d1370e9d7522_17 - rho_predicate_2bx32f72cccd281a177_17
   <= 0
 R148: z_&&_2bx47d4d1370e9d7522_17 - z_predicate_2bx32f72cccd281a177_17
   <= 0
 R149: z_&&_2bx47d4d1370e9d7522_17 - z_predicate_2dx4c7fa34b9cfd78d2_17
   - z_predicate_2bx32f72cccd281a177_17 >= -1
 R150: x_18 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_18
   - rho_predicate_2dx4c7fa34b9cfd78d2_18 >= -994
 R151: x_18 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_18
   - rho_predicate_2dx4c7fa34b9cfd78d2_18 <= 6
 R152: y_18 - 1000 z_predicate_2bx32f72cccd281a177_18
   - rho_predicate_2bx32f72cccd281a177_18 >= -994
 R153: y_18 - 1000 z_predicate_2bx32f72cccd281a177_18
   - rho_predicate_2bx32f72cccd281a177_18 <= 6
 R154: rho_&&_2bx47d4d1370e9d7522_18 - rho_predicate_2dx4c7fa34b9cfd78d2_18
   <= 0
 R155: z_&&_2bx47d4d1370e9d7522_18 - z_predicate_2dx4c7fa34b9cfd78d2_18
   <= 0
 R156: rho_&&_2bx47d4d1370e9d7522_18 - rho_predicate_2bx32f72cccd281a177_18
   <= 0
 R157: z_&&_2bx47d4d1370e9d7522_18 - z_predicate_2bx32f72cccd281a177_18
   <= 0
 R158: z_&&_2bx47d4d1370e9d7522_18 - z_predicate_2dx4c7fa34b9cfd78d2_18
   - z_predicate_2bx32f72cccd281a177_18 >= -1
 R159: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_8 <= 0
 R160: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_8 <= 0
 R161: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_9 <= 0
 R162: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_9 <= 0
 R163: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_10 <= 0
 R164: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_10 <= 0
 R165: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_11 <= 0
 R166: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_11 <= 0
 R167: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_12 <= 0
 R168: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_12 <= 0
 R169: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_13 <= 0
 R170: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_13 <= 0
 R171: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_14 <= 0
 R172: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_14 <= 0
 R173: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_15 <= 0
 R174: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_15 <= 0
 R175: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_16 <= 0
 R176: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_16 <= 0
 R177: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_17 <= 0
 R178: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_17 <= 0
 R179: rho_G_2dx202841f650fddfca_0 - rho_&&_2bx47d4d1370e9d7522_18 <= 0
 R180: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_18 <= 0
 R181: z_G_2dx202841f650fddfca_0 - z_&&_2bx47d4d1370e9d7522_8
   - z_&&_2bx47d4d1370e9d7522_9 - z_&&_2bx47d4d1370e9d7522_10
   - z_&&_2bx47d4d1370e9d7522_11 - z_&&_2bx47d4d1370e9d7522_12
   - z_&&_2bx47d4d1370e9d7522_13 - z_&&_2bx47d4d1370e9d7522_14
   - z_&&_2bx47d4d1370e9d7522_15 - z_&&_2bx47d4d1370e9d7522_16
   - z_&&_2bx47d4d1370e9d7522_17 - z_&&_2bx47d4d1370e9d7522_18 >= -10
 R182: x_1 - 1000 z_predicate_2dx22dd95ed78b4d217_1
   - rho_predicate_2dx22dd95ed78b4d217_1 >= -997
 R183: x_1 - 1000 z_predicate_2dx22dd95ed78b4d217_1
   - rho_predicate_2dx22dd95ed78b4d217_1 <= 3
 R184: x_1 + 1000 z_predicate_2dx5f1149c769efb91f_1
   + rho_predicate_2dx5f1149c769efb91f_1 <= 997
 R185: x_1 + 1000 z_predicate_2dx5f1149c769efb91f_1
   + rho_predicate_2dx5f1149c769efb91f_1 >= -3
 R186: y_1 - 1000 z_predicate_2bx955025411f5da14_1
   - rho_predicate_2bx955025411f5da14_1 >= -997
 R187: y_1 - 1000 z_predicate_2bx955025411f5da14_1
   - rho_predicate_2bx955025411f5da14_1 <= 3
 R188: y_1 + 1000 z_predicate_2bx7f11325f1c65baf6_1
   + rho_predicate_2bx7f11325f1c65baf6_1 <= 997
 R189: y_1 + 1000 z_predicate_2bx7f11325f1c65baf6_1
   + rho_predicate_2bx7f11325f1c65baf6_1 >= -3
 R190: rho_||_2bx22f6bca85b580f1b_1
   + 1000 z_predicate_2dx22dd95ed78b4d217_1
   - rho_predicate_2dx22dd95ed78b4d217_1 <= 1000
 R191: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2dx22dd95ed78b4d217_1 >= 0
 R192: rho_||_2bx22f6bca85b580f1b_1
   + 1000 z_predicate_2dx5f1149c769efb91f_1
   - rho_predicate_2dx5f1149c769efb91f_1 <= 1000
 R193: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2dx5f1149c769efb91f_1 >= 0
 R194: rho_||_2bx22f6bca85b580f1b_1 + 1000 z_predicate_2bx955025411f5da14_1
   - rho_predicate_2bx955025411f5da14_1 <= 1000
 R195: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2bx955025411f5da14_1 >= 0
 R196: rho_||_2bx22f6bca85b580f1b_1
   + 1000 z_predicate_2bx7f11325f1c65baf6_1
   - rho_predicate_2bx7f11325f1c65baf6_1 <= 1000
 R197: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2bx7f11325f1c65baf6_1 >= 0
 R198: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2dx22dd95ed78b4d217_1
   - z_predicate_2dx5f1149c769efb91f_1 - z_predicate_2bx955025411f5da14_1
   - z_predicate_2bx7f11325f1c65baf6_1 <= 0
 R199: x_2 - 1000 z_predicate_2dx22dd95ed78b4d217_2
   - rho_predicate_2dx22dd95ed78b4d217_2 >= -997
 R200: x_2 - 1000 z_predicate_2dx22dd95ed78b4d217_2
   - rho_predicate_2dx22dd95ed78b4d217_2 <= 3
 R201: x_2 + 1000 z_predicate_2dx5f1149c769efb91f_2
   + rho_predicate_2dx5f1149c769efb91f_2 <= 997
 R202: x_2 + 1000 z_predicate_2dx5f1149c769efb91f_2
   + rho_predicate_2dx5f1149c769efb91f_2 >= -3
 R203: y_2 - 1000 z_predicate_2bx955025411f5da14_2
   - rho_predicate_2bx955025411f5da14_2 >= -997
 R204: y_2 - 1000 z_predicate_2bx955025411f5da14_2
   - rho_predicate_2bx955025411f5da14_2 <= 3
 R205: y_2 + 1000 z_predicate_2bx7f11325f1c65baf6_2
   + rho_predicate_2bx7f11325f1c65baf6_2 <= 997
 R206: y_2 + 1000 z_predicate_2bx7f11325f1c65baf6_2
   + rho_predicate_2bx7f11325f1c65baf6_2 >= -3
 R207: rho_||_2bx22f6bca85b580f1b_2
   + 1000 z_predicate_2dx22dd95ed78b4d217_2
   - rho_predicate_2dx22dd95ed78b4d217_2 <= 1000
 R208: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2dx22dd95ed78b4d217_2 >= 0
 R209: rho_||_2bx22f6bca85b580f1b_2
   + 1000 z_predicate_2dx5f1149c769efb91f_2
   - rho_predicate_2dx5f1149c769efb91f_2 <= 1000
 R210: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2dx5f1149c769efb91f_2 >= 0
 R211: rho_||_2bx22f6bca85b580f1b_2 + 1000 z_predicate_2bx955025411f5da14_2
   - rho_predicate_2bx955025411f5da14_2 <= 1000
 R212: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2bx955025411f5da14_2 >= 0
 R213: rho_||_2bx22f6bca85b580f1b_2
   + 1000 z_predicate_2bx7f11325f1c65baf6_2
   - rho_predicate_2bx7f11325f1c65baf6_2 <= 1000
 R214: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2bx7f11325f1c65baf6_2 >= 0
 R215: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2dx22dd95ed78b4d217_2
   - z_predicate_2dx5f1149c769efb91f_2 - z_predicate_2bx955025411f5da14_2
   - z_predicate_2bx7f11325f1c65baf6_2 <= 0
 R216: x_3 - 1000 z_predicate_2dx22dd95ed78b4d217_3
   - rho_predicate_2dx22dd95ed78b4d217_3 >= -997
 R217: x_3 - 1000 z_predicate_2dx22dd95ed78b4d217_3
   - rho_predicate_2dx22dd95ed78b4d217_3 <= 3
 R218: x_3 + 1000 z_predicate_2dx5f1149c769efb91f_3
   + rho_predicate_2dx5f1149c769efb91f_3 <= 997
 R219: x_3 + 1000 z_predicate_2dx5f1149c769efb91f_3
   + rho_predicate_2dx5f1149c769efb91f_3 >= -3
 R220: y_3 - 1000 z_predicate_2bx955025411f5da14_3
   - rho_predicate_2bx955025411f5da14_3 >= -997
 R221: y_3 - 1000 z_predicate_2bx955025411f5da14_3
   - rho_predicate_2bx955025411f5da14_3 <= 3
 R222: y_3 + 1000 z_predicate_2bx7f11325f1c65baf6_3
   + rho_predicate_2bx7f11325f1c65baf6_3 <= 997
 R223: y_3 + 1000 z_predicate_2bx7f11325f1c65baf6_3
   + rho_predicate_2bx7f11325f1c65baf6_3 >= -3
 R224: rho_||_2bx22f6bca85b580f1b_3
   + 1000 z_predicate_2dx22dd95ed78b4d217_3
   - rho_predicate_2dx22dd95ed78b4d217_3 <= 1000
 R225: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2dx22dd95ed78b4d217_3 >= 0
 R226: rho_||_2bx22f6bca85b580f1b_3
   + 1000 z_predicate_2dx5f1149c769efb91f_3
   - rho_predicate_2dx5f1149c769efb91f_3 <= 1000
 R227: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2dx5f1149c769efb91f_3 >= 0
 R228: rho_||_2bx22f6bca85b580f1b_3 + 1000 z_predicate_2bx955025411f5da14_3
   - rho_predicate_2bx955025411f5da14_3 <= 1000
 R229: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2bx955025411f5da14_3 >= 0
 R230: rho_||_2bx22f6bca85b580f1b_3
   + 1000 z_predicate_2bx7f11325f1c65baf6_3
   - rho_predicate_2bx7f11325f1c65baf6_3 <= 1000
 R231: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2bx7f11325f1c65baf6_3 >= 0
 R232: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2dx22dd95ed78b4d217_3
   - z_predicate_2dx5f1149c769efb91f_3 - z_predicate_2bx955025411f5da14_3
   - z_predicate_2bx7f11325f1c65baf6_3 <= 0
 R233: x_4 - 1000 z_predicate_2dx22dd95ed78b4d217_4
   - rho_predicate_2dx22dd95ed78b4d217_4 >= -997
 R234: x_4 - 1000 z_predicate_2dx22dd95ed78b4d217_4
   - rho_predicate_2dx22dd95ed78b4d217_4 <= 3
 R235: x_4 + 1000 z_predicate_2dx5f1149c769efb91f_4
   + rho_predicate_2dx5f1149c769efb91f_4 <= 997
 R236: x_4 + 1000 z_predicate_2dx5f1149c769efb91f_4
   + rho_predicate_2dx5f1149c769efb91f_4 >= -3
 R237: y_4 - 1000 z_predicate_2bx955025411f5da14_4
   - rho_predicate_2bx955025411f5da14_4 >= -997
 R238: y_4 - 1000 z_predicate_2bx955025411f5da14_4
   - rho_predicate_2bx955025411f5da14_4 <= 3
 R239: y_4 + 1000 z_predicate_2bx7f11325f1c65baf6_4
   + rho_predicate_2bx7f11325f1c65baf6_4 <= 997
 R240: y_4 + 1000 z_predicate_2bx7f11325f1c65baf6_4
   + rho_predicate_2bx7f11325f1c65baf6_4 >= -3
 R241: rho_||_2bx22f6bca85b580f1b_4
   + 1000 z_predicate_2dx22dd95ed78b4d217_4
   - rho_predicate_2dx22dd95ed78b4d217_4 <= 1000
 R242: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2dx22dd95ed78b4d217_4 >= 0
 R243: rho_||_2bx22f6bca85b580f1b_4
   + 1000 z_predicate_2dx5f1149c769efb91f_4
   - rho_predicate_2dx5f1149c769efb91f_4 <= 1000
 R244: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2dx5f1149c769efb91f_4 >= 0
 R245: rho_||_2bx22f6bca85b580f1b_4 + 1000 z_predicate_2bx955025411f5da14_4
   - rho_predicate_2bx955025411f5da14_4 <= 1000
 R246: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2bx955025411f5da14_4 >= 0
 R247: rho_||_2bx22f6bca85b580f1b_4
   + 1000 z_predicate_2bx7f11325f1c65baf6_4
   - rho_predicate_2bx7f11325f1c65baf6_4 <= 1000
 R248: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2bx7f11325f1c65baf6_4 >= 0
 R249: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2dx22dd95ed78b4d217_4
   - z_predicate_2dx5f1149c769efb91f_4 - z_predicate_2bx955025411f5da14_4
   - z_predicate_2bx7f11325f1c65baf6_4 <= 0
 R250: x_5 - 1000 z_predicate_2dx22dd95ed78b4d217_5
   - rho_predicate_2dx22dd95ed78b4d217_5 >= -997
 R251: x_5 - 1000 z_predicate_2dx22dd95ed78b4d217_5
   - rho_predicate_2dx22dd95ed78b4d217_5 <= 3
 R252: x_5 + 1000 z_predicate_2dx5f1149c769efb91f_5
   + rho_predicate_2dx5f1149c769efb91f_5 <= 997
 R253: x_5 + 1000 z_predicate_2dx5f1149c769efb91f_5
   + rho_predicate_2dx5f1149c769efb91f_5 >= -3
 R254: y_5 - 1000 z_predicate_2bx955025411f5da14_5
   - rho_predicate_2bx955025411f5da14_5 >= -997
 R255: y_5 - 1000 z_predicate_2bx955025411f5da14_5
   - rho_predicate_2bx955025411f5da14_5 <= 3
 R256: y_5 + 1000 z_predicate_2bx7f11325f1c65baf6_5
   + rho_predicate_2bx7f11325f1c65baf6_5 <= 997
 R257: y_5 + 1000 z_predicate_2bx7f11325f1c65baf6_5
   + rho_predicate_2bx7f11325f1c65baf6_5 >= -3
 R258: rho_||_2bx22f6bca85b580f1b_5
   + 1000 z_predicate_2dx22dd95ed78b4d217_5
   - rho_predicate_2dx22dd95ed78b4d217_5 <= 1000
 R259: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2dx22dd95ed78b4d217_5 >= 0
 R260: rho_||_2bx22f6bca85b580f1b_5
   + 1000 z_predicate_2dx5f1149c769efb91f_5
   - rho_predicate_2dx5f1149c769efb91f_5 <= 1000
 R261: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2dx5f1149c769efb91f_5 >= 0
 R262: rho_||_2bx22f6bca85b580f1b_5 + 1000 z_predicate_2bx955025411f5da14_5
   - rho_predicate_2bx955025411f5da14_5 <= 1000
 R263: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2bx955025411f5da14_5 >= 0
 R264: rho_||_2bx22f6bca85b580f1b_5
   + 1000 z_predicate_2bx7f11325f1c65baf6_5
   - rho_predicate_2bx7f11325f1c65baf6_5 <= 1000
 R265: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2bx7f11325f1c65baf6_5 >= 0
 R266: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2dx22dd95ed78b4d217_5
   - z_predicate_2dx5f1149c769efb91f_5 - z_predicate_2bx955025411f5da14_5
   - z_predicate_2bx7f11325f1c65baf6_5 <= 0
 R267: x_6 - 1000 z_predicate_2dx22dd95ed78b4d217_6
   - rho_predicate_2dx22dd95ed78b4d217_6 >= -997
 R268: x_6 - 1000 z_predicate_2dx22dd95ed78b4d217_6
   - rho_predicate_2dx22dd95ed78b4d217_6 <= 3
 R269: x_6 + 1000 z_predicate_2dx5f1149c769efb91f_6
   + rho_predicate_2dx5f1149c769efb91f_6 <= 997
 R270: x_6 + 1000 z_predicate_2dx5f1149c769efb91f_6
   + rho_predicate_2dx5f1149c769efb91f_6 >= -3
 R271: y_6 - 1000 z_predicate_2bx955025411f5da14_6
   - rho_predicate_2bx955025411f5da14_6 >= -997
 R272: y_6 - 1000 z_predicate_2bx955025411f5da14_6
   - rho_predicate_2bx955025411f5da14_6 <= 3
 R273: y_6 + 1000 z_predicate_2bx7f11325f1c65baf6_6
   + rho_predicate_2bx7f11325f1c65baf6_6 <= 997
 R274: y_6 + 1000 z_predicate_2bx7f11325f1c65baf6_6
   + rho_predicate_2bx7f11325f1c65baf6_6 >= -3
 R275: rho_||_2bx22f6bca85b580f1b_6
   + 1000 z_predicate_2dx22dd95ed78b4d217_6
   - rho_predicate_2dx22dd95ed78b4d217_6 <= 1000
 R276: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2dx22dd95ed78b4d217_6 >= 0
 R277: rho_||_2bx22f6bca85b580f1b_6
   + 1000 z_predicate_2dx5f1149c769efb91f_6
   - rho_predicate_2dx5f1149c769efb91f_6 <= 1000
 R278: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2dx5f1149c769efb91f_6 >= 0
 R279: rho_||_2bx22f6bca85b580f1b_6 + 1000 z_predicate_2bx955025411f5da14_6
   - rho_predicate_2bx955025411f5da14_6 <= 1000
 R280: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2bx955025411f5da14_6 >= 0
 R281: rho_||_2bx22f6bca85b580f1b_6
   + 1000 z_predicate_2bx7f11325f1c65baf6_6
   - rho_predicate_2bx7f11325f1c65baf6_6 <= 1000
 R282: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2bx7f11325f1c65baf6_6 >= 0
 R283: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2dx22dd95ed78b4d217_6
   - z_predicate_2dx5f1149c769efb91f_6 - z_predicate_2bx955025411f5da14_6
   - z_predicate_2bx7f11325f1c65baf6_6 <= 0
 R284: x_7 - 1000 z_predicate_2dx22dd95ed78b4d217_7
   - rho_predicate_2dx22dd95ed78b4d217_7 >= -997
 R285: x_7 - 1000 z_predicate_2dx22dd95ed78b4d217_7
   - rho_predicate_2dx22dd95ed78b4d217_7 <= 3
 R286: x_7 + 1000 z_predicate_2dx5f1149c769efb91f_7
   + rho_predicate_2dx5f1149c769efb91f_7 <= 997
 R287: x_7 + 1000 z_predicate_2dx5f1149c769efb91f_7
   + rho_predicate_2dx5f1149c769efb91f_7 >= -3
 R288: y_7 - 1000 z_predicate_2bx955025411f5da14_7
   - rho_predicate_2bx955025411f5da14_7 >= -997
 R289: y_7 - 1000 z_predicate_2bx955025411f5da14_7
   - rho_predicate_2bx955025411f5da14_7 <= 3
 R290: y_7 + 1000 z_predicate_2bx7f11325f1c65baf6_7
   + rho_predicate_2bx7f11325f1c65baf6_7 <= 997
 R291: y_7 + 1000 z_predicate_2bx7f11325f1c65baf6_7
   + rho_predicate_2bx7f11325f1c65baf6_7 >= -3
 R292: rho_||_2bx22f6bca85b580f1b_7
   + 1000 z_predicate_2dx22dd95ed78b4d217_7
   - rho_predicate_2dx22dd95ed78b4d217_7 <= 1000
 R293: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2dx22dd95ed78b4d217_7 >= 0
 R294: rho_||_2bx22f6bca85b580f1b_7
   + 1000 z_predicate_2dx5f1149c769efb91f_7
   - rho_predicate_2dx5f1149c769efb91f_7 <= 1000
 R295: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2dx5f1149c769efb91f_7 >= 0
 R296: rho_||_2bx22f6bca85b580f1b_7 + 1000 z_predicate_2bx955025411f5da14_7
   - rho_predicate_2bx955025411f5da14_7 <= 1000
 R297: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2bx955025411f5da14_7 >= 0
 R298: rho_||_2bx22f6bca85b580f1b_7
   + 1000 z_predicate_2bx7f11325f1c65baf6_7
   - rho_predicate_2bx7f11325f1c65baf6_7 <= 1000
 R299: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2bx7f11325f1c65baf6_7 >= 0
 R300: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2dx22dd95ed78b4d217_7
   - z_predicate_2dx5f1149c769efb91f_7 - z_predicate_2bx955025411f5da14_7
   - z_predicate_2bx7f11325f1c65baf6_7 <= 0
 R301: rho_G_2dx215e7514fa3a514b_0 - rho_||_2bx22f6bca85b580f1b_1 <= 0
 R302: z_G_2dx215e7514fa3a514b_0 - z_||_2bx22f6bca85b580f1b_1 <= 0
 R303: rho_G_2dx215e7514fa3a514b_0 - rho_||_2bx22f6bca85b580f1b_2 <= 0
 R304: z_G_2dx215e7514fa3a514b_0 - z_||_2bx22f6bca85b580f1b_2 <= 0
 R305: rho_G_2dx215e7514fa3a514b_0 - rho_||_2bx22f6bca85b580f1b_3 <= 0
 R306: z_G_2dx215e7514fa3a514b_0 - z_||_2bx22f6bca85b580f1b_3 <= 0
 R307: rho_G_2dx215e7514fa3a514b_0 - rho_||_2bx22f6bca85b580f1b_4 <= 0
 R308: z_G_2dx215e7514fa3a514b_0 - z_||_2bx22f6bca85b580f1b_4 <= 0
 R309: rho_G_2dx215e7514fa3a514b_0 - rho_||_2bx22f6bca85b580f1b_5 <= 0
 R310: z_G_2dx215e7514fa3a514b_0 - z_||_2bx22f6bca85b580f1b_5 <= 0
 R311: rho_G_2dx215e7514fa3a514b_0 - rho_||_2bx22f6bca85b580f1b_6 <= 0
 R312: z_G_2dx215e7514fa3a514b_0 - z_||_2bx22f6bca85b580f1b_6 <= 0
 R313: rho_G_2dx215e7514fa3a514b_0 - rho_||_2bx22f6bca85b580f1b_7 <= 0
 R314: z_G_2dx215e7514fa3a514b_0 - z_||_2bx22f6bca85b580f1b_7 <= 0
 R315: z_G_2dx215e7514fa3a514b_0 - z_||_2bx22f6bca85b580f1b_1
   - z_||_2bx22f6bca85b580f1b_2 - z_||_2bx22f6bca85b580f1b_3
   - z_||_2bx22f6bca85b580f1b_4 - z_||_2bx22f6bca85b580f1b_5
   - z_||_2bx22f6bca85b580f1b_6 - z_||_2bx22f6bca85b580f1b_7 >= -6
 R316: rho_&&_2dx224a090b37463e1e_0 - 0.1 rho_G_2dx202841f650fddfca_0 <= 0
 R317: z_&&_2dx224a090b37463e1e_0 - z_G_2dx202841f650fddfca_0 <= 0
 R318: rho_&&_2dx224a090b37463e1e_0 - 2 rho_G_2dx215e7514fa3a514b_0 <= 0
 R319: z_&&_2dx224a090b37463e1e_0 - z_G_2dx215e7514fa3a514b_0 <= 0
 R320: z_&&_2dx224a090b37463e1e_0 - z_G_2dx202841f650fddfca_0
   - z_G_2dx215e7514fa3a514b_0 >= -1
 formula_satisfaction: z_&&_2dx224a090b37463e1e_0 = 1
Bounds
 -9 <= x_0 <= 9
 -9 <= y_0 <= 9
 -9 <= z_0 <= 9
 -3 <= u_0 <= 3
 -3 <= v_0 <= 3
 -3 <= w_0 <= 3
 -9 <= x_1 <= 9
 -9 <= y_1 <= 9
 -9 <= z_1 <= 9
 -3 <= u_1 <= 3
 -3 <= v_1 <= 3
 -3 <= w_1 <= 3
 -9 <= x_2 <= 9
 -9 <= y_2 <= 9
 -9 <= z_2 <= 9
 -3 <= u_2 <= 3
 -3 <= v_2 <= 3
 -3 <= w_2 <= 3
 -9 <= x_3 <= 9
 -9 <= y_3 <= 9
 -9 <= z_3 <= 9
 -3 <= u_3 <= 3
 -3 <= v_3 <= 3
 -3 <= w_3 <= 3
 -9 <= x_4 <= 9
 -9 <= y_4 <= 9
 -9 <= z_4 <= 9
 -3 <= u_4 <= 3
 -3 <= v_4 <= 3
 -3 <= w_4 <= 3
 -9 <= x_5 <= 9
 -9 <= y_5 <= 9
 -9 <= z_5 <= 9
 -3 <= u_5 <= 3
 -3 <= v_5 <= 3
 -3 <= w_5 <= 3
 -9 <= x_6 <= 9
 -9 <= y_6 <= 9
 -9 <= z_6 <= 9
 -3 <= u_6 <= 3
 -3 <= v_6 <= 3
 -3 <= w_6 <= 3
 -9 <= x_7 <= 9
 -9 <= y_7 <= 9
 -9 <= z_7 <= 9
 -3 <= u_7 <= 3
 -3 <= v_7 <= 3
 -3 <= w_7 <= 3
 -9 <= x_8 <= 9
 -9 <= y_8 <= 9
 -9 <= z_8 <= 9
 -3 <= u_8 <= 3
 -3 <= v_8 <= 3
 -3 <= w_8 <= 3
 -9 <= x_9 <= 9
 -9 <= y_9 <= 9
 -9 <= z_9 <= 9
 -3 <= u_9 <= 3
 -3 <= v_9 <= 3
 -3 <= w_9 <= 3
 -9 <= x_10 <= 9
 -9 <= y_10 <= 9
 -9 <= z_10 <= 9
 -3 <= u_10 <= 3
 -3 <= v_10 <= 3
 -3 <= w_10 <= 3
 -9 <= x_11 <= 9
 -9 <= y_11 <= 9
 -9 <= z_11 <= 9
 -3 <= u_11 <= 3
 -3 <= v_11 <= 3
 -3 <= w_11 <= 3
 -9 <= x_12 <= 9
 -9 <= y_12 <= 9
 -9 <= z_12 <= 9
 -3 <= u_12 <= 3
 -3 <= v_12 <= 3
 -3 <= w_12 <= 3
 -9 <= x_13 <= 9
 -9 <= y_13 <= 9
 -9 <= z_13 <= 9
 -3 <= u_13 <= 3
 -3 <= v_13 <= 3
 -3 <= w_13 <= 3
 -9 <= x_14 <= 9
 -9 <= y_14 <= 9
 -9 <= z_14 <= 9
 -3 <= u_14 <= 3
 -3 <= v_14 <= 3
 -3 <= w_14 <= 3
 -9 <= x_15 <= 9
 -9 <= y_15 <= 9
 -9 <= z_15 <= 9
 -3 <= u_15 <= 3
 -3 <= v_15 <= 3
 -3 <= w_15 <= 3
 -9 <= x_16 <= 9
 -9 <= y_16 <= 9
 -9 <= z_16 <= 9
 -3 <= u_16 <= 3
 -3 <= v_16 <= 3
 -3 <= w_16 <= 3
 -9 <= x_17 <= 9
 -9 <= y_17 <= 9
 -9 <= z_17 <= 9
 -3 <= u_17 <= 3
 -3 <= v_17 <= 3
 -3 <= w_17 <= 3
 -9 <= x_18 <= 9
 -9 <= y_18 <= 9
 -9 <= z_18 <= 9
 -3 <= u_18 <= 3
 -3 <= v_18 <= 3
 -3 <= w_18 <= 3
 z_&&_2dx224a090b37463e1e_0 <= 1
 rho_&&_2dx224a090b37463e1e_0 free
 z_G_2dx202841f650fddfca_0 <= 1
 rho_G_2dx202841f650fddfca_0 free
 z_&&_2bx47d4d1370e9d7522_8 <= 1
 rho_&&_2bx47d4d1370e9d7522_8 free
 rho_predicate_2dx4c7fa34b9cfd78d2_8 free
 rho_predicate_2bx32f72cccd281a177_8 free
 z_&&_2bx47d4d1370e9d7522_9 <= 1
 rho_&&_2bx47d4d1370e9d7522_9 free
 rho_predicate_2dx4c7fa34b9cfd78d2_9 free
 rho_predicate_2bx32f72cccd281a177_9 free
 z_&&_2bx47d4d1370e9d7522_10 <= 1
 rho_&&_2bx47d4d1370e9d7522_10 free
 rho_predicate_2dx4c7fa34b9cfd78d2_10 free
 rho_predicate_2bx32f72cccd281a177_10 free
 z_&&_2bx47d4d1370e9d7522_11 <= 1
 rho_&&_2bx47d4d1370e9d7522_11 free
 rho_predicate_2dx4c7fa34b9cfd78d2_11 free
 rho_predicate_2bx32f72cccd281a177_11 free
 z_&&_2bx47d4d1370e9d7522_12 <= 1
 rho_&&_2bx47d4d1370e9d7522_12 free
 rho_predicate_2dx4c7fa34b9cfd78d2_12 free
 rho_predicate_2bx32f72cccd281a177_12 free
 z_&&_2bx47d4d1370e9d7522_13 <= 1
 rho_&&_2bx47d4d1370e9d7522_13 free
 rho_predicate_2dx4c7fa34b9cfd78d2_13 free
 rho_predicate_2bx32f72cccd281a177_13 free
 z_&&_2bx47d4d1370e9d7522_14 <= 1
 rho_&&_2bx47d4d1370e9d7522_14 free
 rho_predicate_2dx4c7fa34b9cfd78d2_14 free
 rho_predicate_2bx32f72cccd281a177_14 free
 z_&&_2bx47d4d1370e9d7522_15 <= 1
 rho_&&_2bx47d4d1370e9d7522_15 free
 rho_predicate_2dx4c7fa34b9cfd78d2_15 free
 rho_predicate_2bx32f72cccd281a177_15 free
 z_&&_2bx47d4d1370e9d7522_16 <= 1
 rho_&&_2bx47d4d1370e9d7522_16 free
 rho_predicate_2dx4c7fa34b9cfd78d2_16 free
 rho_predicate_2bx32f72cccd281a177_16 free
 z_&&_2bx47d4d1370e9d7522_17 <= 1
 rho_&&_2bx47d4d1370e9d7522_17 free
 rho_predicate_2dx4c7fa34b9cfd78d2_17 free
 rho_predicate_2bx32f72cccd281a177_17 free
 z_&&_2bx47d4d1370e9d7522_18 <= 1
 rho_&&_2bx47d4d1370e9d7522_18 free
 rho_predicate_2dx4c7fa34b9cfd78d2_18 free
 rho_predicate_2bx32f72cccd281a177_18 free
 z_G_2dx215e7514fa3a514b_0 <= 1
 rho_G_2dx215e7514fa3a514b_0 free
 z_||_2bx22f6bca85b580f1b_1 <= 1
 rho_||_2bx22f6bca85b580f1b_1 free
 rho_predicate_2dx22dd95ed78b4d217_1 free
 rho_predicate_2dx5f1149c769efb91f_1 free
 rho_predicate_2bx955025411f5da14_1 free
 rho_predicate_2bx7f11325f1c65baf6_1 free
 z_||_2bx22f6bca85b580f1b_2 <= 1
 rho_||_2bx22f6bca85b580f1b_2 free
 rho_predicate_2dx22dd95ed78b4d217_2 free
 rho_predicate_2dx5f1149c769efb91f_2 free
 rho_predicate_2bx955025411f5da14_2 free
 rho_predicate_2bx7f11325f1c65baf6_2 free
 z_||_2bx22f6bca85b580f1b_3 <= 1
 rho_||_2bx22f6bca85b580f1b_3 free
 rho_predicate_2dx22dd95ed78b4d217_3 free
 rho_predicate_2dx5f1149c769efb91f_3 free
 rho_predicate_2bx955025411f5da14_3 free
 rho_predicate_2bx7f11325f1c65baf6_3 free
 z_||_2bx22f6bca85b580f1b_4 <= 1
 rho_||_2bx22f6bca85b580f1b_4 free
 rho_predicate_2dx22dd95ed78b4d217_4 free
 rho_predicate_2dx5f1149c769efb91f_4 free
 rho_predicate_2bx955025411f5da14_4 free
 rho_predicate_2bx7f11325f1c65baf6_4 free
 z_||_2bx22f6bca85b580f1b_5 <= 1
 rho_||_2bx22f6bca85b580f1b_5 free
 rho_predicate_2dx22dd95ed78b4d217_5 free
 rho_predicate_2dx5f1149c769efb91f_5 free
 rho_predicate_2bx955025411f5da14_5 free
 rho_predicate_2bx7f11325f1c65baf6_5 free
 z_||_2bx22f6bca85b580f1b_6 <= 1
 rho_||_2bx22f6bca85b580f1b_6 free
 rho_predicate_2dx22dd95ed78b4d217_6 free
 rho_predicate_2dx5f1149c769efb91f_6 free
 rho_predicate_2bx955025411f5da14_6 free
 rho_predicate_2bx7f11325f1c65baf6_6 free
 z_||_2bx22f6bca85b580f1b_7 <= 1
 rho_||_2bx22f6bca85b580f1b_7 free
 rho_predicate_2dx22dd95ed78b4d217_7 free
 rho_predicate_2dx5f1149c769efb91f_7 free
 rho_predicate_2bx955025411f5da14_7 free
 rho_predicate_2bx7f11325f1c65baf6_7 free
Binaries
 z_predicate_2dx4c7fa34b9cfd78d2_8 z_predicate_2bx32f72cccd281a177_8
 z_predicate_2dx4c7fa34b9cfd78d2_9 z_predicate_2bx32f72cccd281a177_9
 z_predicate_2dx4c7fa34b9cfd78d2_10 z_predicate_2bx32f72cccd281a177_10
 z_predicate_2dx4c7fa34b9cfd78d2_11 z_predicate_2bx32f72cccd281a177_11
 z_predicate_2dx4c7fa34b9cfd78d2_12 z_predicate_2bx32f72cccd281a177_12
 z_predicate_2dx4c7fa34b9cfd78d2_13 z_predicate_2bx32f72cccd281a177_13
 z_predicate_2dx4c7fa34b9cfd78d2_14 z_predicate_2bx32f72cccd281a177_14
 z_predicate_2dx4c7fa34b9cfd78d2_15 z_predicate_2bx32f72cccd281a177_15
 z_predicate_2dx4c7fa34b9cfd78d2_16 z_predicate_2bx32f72cccd281a177_16
 z_predicate_2dx4c7fa34b9cfd78d2_17 z_predicate_2bx32f72cccd281a177_17
 z_predicate_2dx4c7fa34b9cfd78d2_18 z_predicate_2bx32f72cccd281a177_18
 z_predicate_2dx22dd95ed78b4d217_1 z_predicate_2dx5f1149c769efb91f_1
 z_predicate_2bx955025411f5da14_1 z_predicate_2bx7f11325f1c65baf6_1
 z_predicate_2dx22dd95ed78b4d217_2 z_predicate_2dx5f1149c769efb91f_2
 z_predicate_2bx955025411f5da14_2 z_predicate_2bx7f11325f1c65baf6_2
 z_predicate_2dx22dd95ed78b4d217_3 z_predicate_2dx5f1149c769efb91f_3
 z_predicate_2bx955025411f5da14_3 z_predicate_2bx7f11325f1c65baf6_3
 z_predicate_2dx22dd95ed78b4d217_4 z_predicate_2dx5f1149c769efb91f_4
 z_predicate_2bx955025411f5da14_4 z_predicate_2bx7f11325f1c65baf6_4
 z_predicate_2dx22dd95ed78b4d217_5 z_predicate_2dx5f1149c769efb91f_5
 z_predicate_2bx955025411f5da14_5 z_predicate_2bx7f11325f1c65baf6_5
 z_predicate_2dx22dd95ed78b4d217_6 z_predicate_2dx5f1149c769efb91f_6
 z_predicate_2bx955025411f5da14_6 z_predicate_2bx7f11325f1c65baf6_6
 z_predicate_2dx22dd95ed78b4d217_7 z_predicate_2dx5f1149c769efb91f_7
 z_predicate_2bx955025411f5da14_7 z_predicate_2bx7f11325f1c65baf6_7
End
