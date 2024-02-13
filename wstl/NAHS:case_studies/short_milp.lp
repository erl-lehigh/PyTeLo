\ Model wSTL formula: ((G[13.0, 20.0]^<lambda> ((x >= 6.0) &&^<lambda> (y >= 6.0))) &&^<lambda> (G[0.0, 20.0]^<lambda> ((x >= -3.0) ||^<lambda> (x <= -8.0) ||^<lambda> (y >= 8.0) ||^<lambda> (y <= 3.0))) &&^<lambda> (G[0.0, 20.0]^<lambda> ((x >= 3.0) ||^<lambda> (x <= -3.0) ||^<lambda> (y >= 3.0) ||^<lambda> (y <= -3.0))) &&^<lambda> (G[0.0, 20.0]^<lambda> ((x >= 8.0) ||^<lambda> (x <= 3.0) ||^<lambda> (y >= -3.0) ||^<lambda> (y <= -8.0))))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0 u_20 + 0 v_20 + 0 w_20 + rho_&&_2bx41f61981721fa2dd_0
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
 R54: - x_18 - u_18 + x_19 = 0
 R55: - y_18 - v_18 + y_19 = 0
 R56: - z_18 - w_18 + z_19 = 0
 R57: - x_19 - u_19 + x_20 = 0
 R58: - y_19 - v_19 + y_20 = 0
 R59: - z_19 - w_19 + z_20 = 0
 R60: x_0 = -8
 R61: y_0 = -8
 R62: z_0 = -8
 R63: u_0 = 0
 R64: v_0 = 0
 R65: w_0 = 0
 R66: x_13 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_13
   - rho_predicate_2dx4c7fa34b9cfd78d2_13 >= -994
 R67: x_13 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_13
   - rho_predicate_2dx4c7fa34b9cfd78d2_13 <= 6
 R68: y_13 - 1000 z_predicate_2bx32f72cccd281a177_13
   - rho_predicate_2bx32f72cccd281a177_13 >= -994
 R69: y_13 - 1000 z_predicate_2bx32f72cccd281a177_13
   - rho_predicate_2bx32f72cccd281a177_13 <= 6
 R70: rho_&&_2bx47d4d1370e9d7522_13 - rho_predicate_2dx4c7fa34b9cfd78d2_13
   <= 0
 R71: z_&&_2bx47d4d1370e9d7522_13 - z_predicate_2dx4c7fa34b9cfd78d2_13
   <= 0
 R72: rho_&&_2bx47d4d1370e9d7522_13 - rho_predicate_2bx32f72cccd281a177_13
   <= 0
 R73: z_&&_2bx47d4d1370e9d7522_13 - z_predicate_2bx32f72cccd281a177_13
   <= 0
 R74: z_&&_2bx47d4d1370e9d7522_13 - z_predicate_2dx4c7fa34b9cfd78d2_13
   - z_predicate_2bx32f72cccd281a177_13 >= -1
 R75: x_14 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_14
   - rho_predicate_2dx4c7fa34b9cfd78d2_14 >= -994
 R76: x_14 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_14
   - rho_predicate_2dx4c7fa34b9cfd78d2_14 <= 6
 R77: y_14 - 1000 z_predicate_2bx32f72cccd281a177_14
   - rho_predicate_2bx32f72cccd281a177_14 >= -994
 R78: y_14 - 1000 z_predicate_2bx32f72cccd281a177_14
   - rho_predicate_2bx32f72cccd281a177_14 <= 6
 R79: rho_&&_2bx47d4d1370e9d7522_14 - rho_predicate_2dx4c7fa34b9cfd78d2_14
   <= 0
 R80: z_&&_2bx47d4d1370e9d7522_14 - z_predicate_2dx4c7fa34b9cfd78d2_14
   <= 0
 R81: rho_&&_2bx47d4d1370e9d7522_14 - rho_predicate_2bx32f72cccd281a177_14
   <= 0
 R82: z_&&_2bx47d4d1370e9d7522_14 - z_predicate_2bx32f72cccd281a177_14
   <= 0
 R83: z_&&_2bx47d4d1370e9d7522_14 - z_predicate_2dx4c7fa34b9cfd78d2_14
   - z_predicate_2bx32f72cccd281a177_14 >= -1
 R84: x_15 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_15
   - rho_predicate_2dx4c7fa34b9cfd78d2_15 >= -994
 R85: x_15 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_15
   - rho_predicate_2dx4c7fa34b9cfd78d2_15 <= 6
 R86: y_15 - 1000 z_predicate_2bx32f72cccd281a177_15
   - rho_predicate_2bx32f72cccd281a177_15 >= -994
 R87: y_15 - 1000 z_predicate_2bx32f72cccd281a177_15
   - rho_predicate_2bx32f72cccd281a177_15 <= 6
 R88: rho_&&_2bx47d4d1370e9d7522_15 - rho_predicate_2dx4c7fa34b9cfd78d2_15
   <= 0
 R89: z_&&_2bx47d4d1370e9d7522_15 - z_predicate_2dx4c7fa34b9cfd78d2_15
   <= 0
 R90: rho_&&_2bx47d4d1370e9d7522_15 - rho_predicate_2bx32f72cccd281a177_15
   <= 0
 R91: z_&&_2bx47d4d1370e9d7522_15 - z_predicate_2bx32f72cccd281a177_15
   <= 0
 R92: z_&&_2bx47d4d1370e9d7522_15 - z_predicate_2dx4c7fa34b9cfd78d2_15
   - z_predicate_2bx32f72cccd281a177_15 >= -1
 R93: x_16 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_16
   - rho_predicate_2dx4c7fa34b9cfd78d2_16 >= -994
 R94: x_16 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_16
   - rho_predicate_2dx4c7fa34b9cfd78d2_16 <= 6
 R95: y_16 - 1000 z_predicate_2bx32f72cccd281a177_16
   - rho_predicate_2bx32f72cccd281a177_16 >= -994
 R96: y_16 - 1000 z_predicate_2bx32f72cccd281a177_16
   - rho_predicate_2bx32f72cccd281a177_16 <= 6
 R97: rho_&&_2bx47d4d1370e9d7522_16 - rho_predicate_2dx4c7fa34b9cfd78d2_16
   <= 0
 R98: z_&&_2bx47d4d1370e9d7522_16 - z_predicate_2dx4c7fa34b9cfd78d2_16
   <= 0
 R99: rho_&&_2bx47d4d1370e9d7522_16 - rho_predicate_2bx32f72cccd281a177_16
   <= 0
 R100: z_&&_2bx47d4d1370e9d7522_16 - z_predicate_2bx32f72cccd281a177_16
   <= 0
 R101: z_&&_2bx47d4d1370e9d7522_16 - z_predicate_2dx4c7fa34b9cfd78d2_16
   - z_predicate_2bx32f72cccd281a177_16 >= -1
 R102: x_17 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_17
   - rho_predicate_2dx4c7fa34b9cfd78d2_17 >= -994
 R103: x_17 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_17
   - rho_predicate_2dx4c7fa34b9cfd78d2_17 <= 6
 R104: y_17 - 1000 z_predicate_2bx32f72cccd281a177_17
   - rho_predicate_2bx32f72cccd281a177_17 >= -994
 R105: y_17 - 1000 z_predicate_2bx32f72cccd281a177_17
   - rho_predicate_2bx32f72cccd281a177_17 <= 6
 R106: rho_&&_2bx47d4d1370e9d7522_17 - rho_predicate_2dx4c7fa34b9cfd78d2_17
   <= 0
 R107: z_&&_2bx47d4d1370e9d7522_17 - z_predicate_2dx4c7fa34b9cfd78d2_17
   <= 0
 R108: rho_&&_2bx47d4d1370e9d7522_17 - rho_predicate_2bx32f72cccd281a177_17
   <= 0
 R109: z_&&_2bx47d4d1370e9d7522_17 - z_predicate_2bx32f72cccd281a177_17
   <= 0
 R110: z_&&_2bx47d4d1370e9d7522_17 - z_predicate_2dx4c7fa34b9cfd78d2_17
   - z_predicate_2bx32f72cccd281a177_17 >= -1
 R111: x_18 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_18
   - rho_predicate_2dx4c7fa34b9cfd78d2_18 >= -994
 R112: x_18 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_18
   - rho_predicate_2dx4c7fa34b9cfd78d2_18 <= 6
 R113: y_18 - 1000 z_predicate_2bx32f72cccd281a177_18
   - rho_predicate_2bx32f72cccd281a177_18 >= -994
 R114: y_18 - 1000 z_predicate_2bx32f72cccd281a177_18
   - rho_predicate_2bx32f72cccd281a177_18 <= 6
 R115: rho_&&_2bx47d4d1370e9d7522_18 - rho_predicate_2dx4c7fa34b9cfd78d2_18
   <= 0
 R116: z_&&_2bx47d4d1370e9d7522_18 - z_predicate_2dx4c7fa34b9cfd78d2_18
   <= 0
 R117: rho_&&_2bx47d4d1370e9d7522_18 - rho_predicate_2bx32f72cccd281a177_18
   <= 0
 R118: z_&&_2bx47d4d1370e9d7522_18 - z_predicate_2bx32f72cccd281a177_18
   <= 0
 R119: z_&&_2bx47d4d1370e9d7522_18 - z_predicate_2dx4c7fa34b9cfd78d2_18
   - z_predicate_2bx32f72cccd281a177_18 >= -1
 R120: x_19 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_19
   - rho_predicate_2dx4c7fa34b9cfd78d2_19 >= -994
 R121: x_19 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_19
   - rho_predicate_2dx4c7fa34b9cfd78d2_19 <= 6
 R122: y_19 - 1000 z_predicate_2bx32f72cccd281a177_19
   - rho_predicate_2bx32f72cccd281a177_19 >= -994
 R123: y_19 - 1000 z_predicate_2bx32f72cccd281a177_19
   - rho_predicate_2bx32f72cccd281a177_19 <= 6
 R124: rho_&&_2bx47d4d1370e9d7522_19 - rho_predicate_2dx4c7fa34b9cfd78d2_19
   <= 0
 R125: z_&&_2bx47d4d1370e9d7522_19 - z_predicate_2dx4c7fa34b9cfd78d2_19
   <= 0
 R126: rho_&&_2bx47d4d1370e9d7522_19 - rho_predicate_2bx32f72cccd281a177_19
   <= 0
 R127: z_&&_2bx47d4d1370e9d7522_19 - z_predicate_2bx32f72cccd281a177_19
   <= 0
 R128: z_&&_2bx47d4d1370e9d7522_19 - z_predicate_2dx4c7fa34b9cfd78d2_19
   - z_predicate_2bx32f72cccd281a177_19 >= -1
 R129: x_20 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_20
   - rho_predicate_2dx4c7fa34b9cfd78d2_20 >= -994
 R130: x_20 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_20
   - rho_predicate_2dx4c7fa34b9cfd78d2_20 <= 6
 R131: y_20 - 1000 z_predicate_2bx32f72cccd281a177_20
   - rho_predicate_2bx32f72cccd281a177_20 >= -994
 R132: y_20 - 1000 z_predicate_2bx32f72cccd281a177_20
   - rho_predicate_2bx32f72cccd281a177_20 <= 6
 R133: rho_&&_2bx47d4d1370e9d7522_20 - rho_predicate_2dx4c7fa34b9cfd78d2_20
   <= 0
 R134: z_&&_2bx47d4d1370e9d7522_20 - z_predicate_2dx4c7fa34b9cfd78d2_20
   <= 0
 R135: rho_&&_2bx47d4d1370e9d7522_20 - rho_predicate_2bx32f72cccd281a177_20
   <= 0
 R136: z_&&_2bx47d4d1370e9d7522_20 - z_predicate_2bx32f72cccd281a177_20
   <= 0
 R137: z_&&_2bx47d4d1370e9d7522_20 - z_predicate_2dx4c7fa34b9cfd78d2_20
   - z_predicate_2bx32f72cccd281a177_20 >= -1
 R138: rho_G_2bx1635c42e821daeea_0 - rho_&&_2bx47d4d1370e9d7522_13 <= 0
 R139: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_13 <= 0
 R140: rho_G_2bx1635c42e821daeea_0 - rho_&&_2bx47d4d1370e9d7522_14 <= 0
 R141: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_14 <= 0
 R142: rho_G_2bx1635c42e821daeea_0 - rho_&&_2bx47d4d1370e9d7522_15 <= 0
 R143: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_15 <= 0
 R144: rho_G_2bx1635c42e821daeea_0 - rho_&&_2bx47d4d1370e9d7522_16 <= 0
 R145: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_16 <= 0
 R146: rho_G_2bx1635c42e821daeea_0 - rho_&&_2bx47d4d1370e9d7522_17 <= 0
 R147: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_17 <= 0
 R148: rho_G_2bx1635c42e821daeea_0 - rho_&&_2bx47d4d1370e9d7522_18 <= 0
 R149: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_18 <= 0
 R150: rho_G_2bx1635c42e821daeea_0 - rho_&&_2bx47d4d1370e9d7522_19 <= 0
 R151: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_19 <= 0
 R152: rho_G_2bx1635c42e821daeea_0 - rho_&&_2bx47d4d1370e9d7522_20 <= 0
 R153: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_20 <= 0
 R154: z_G_2bx1635c42e821daeea_0 - z_&&_2bx47d4d1370e9d7522_13
   - z_&&_2bx47d4d1370e9d7522_14 - z_&&_2bx47d4d1370e9d7522_15
   - z_&&_2bx47d4d1370e9d7522_16 - z_&&_2bx47d4d1370e9d7522_17
   - z_&&_2bx47d4d1370e9d7522_18 - z_&&_2bx47d4d1370e9d7522_19
   - z_&&_2bx47d4d1370e9d7522_20 >= -7
 R155: x_0 - 1000 z_predicate_2bx454ca952238e72db_0
   - rho_predicate_2bx454ca952238e72db_0 >= -1003
 R156: x_0 - 1000 z_predicate_2bx454ca952238e72db_0
   - rho_predicate_2bx454ca952238e72db_0 <= -3
 R157: x_0 + 1000 z_predicate_2dx19adc98cf842ca58_0
   + rho_predicate_2dx19adc98cf842ca58_0 <= 992
 R158: x_0 + 1000 z_predicate_2dx19adc98cf842ca58_0
   + rho_predicate_2dx19adc98cf842ca58_0 >= -8
 R159: y_0 - 1000 z_predicate_2bx70ac945c4f28d9ed_0
   - rho_predicate_2bx70ac945c4f28d9ed_0 >= -992
 R160: y_0 - 1000 z_predicate_2bx70ac945c4f28d9ed_0
   - rho_predicate_2bx70ac945c4f28d9ed_0 <= 8
 R161: y_0 + 1000 z_predicate_2dx7894b0affacefa_0
   + rho_predicate_2dx7894b0affacefa_0 <= 1003
 R162: y_0 + 1000 z_predicate_2dx7894b0affacefa_0
   + rho_predicate_2dx7894b0affacefa_0 >= 3
 R163: rho_||_2dx6fafc74611e76e89_0 - rho_predicate_2bx454ca952238e72db_0
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_0 <= 1000
 R164: z_||_2dx6fafc74611e76e89_0 - z_predicate_2bx454ca952238e72db_0 >= 0
 R165: - z_predicate_2bx454ca952238e72db_0
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_0 <= 0
 R166: rho_||_2dx6fafc74611e76e89_0 - rho_predicate_2dx19adc98cf842ca58_0
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_0 <= 1000
 R167: z_||_2dx6fafc74611e76e89_0 - z_predicate_2dx19adc98cf842ca58_0 >= 0
 R168: - z_predicate_2dx19adc98cf842ca58_0
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_0 <= 0
 R169: rho_||_2dx6fafc74611e76e89_0 - rho_predicate_2bx70ac945c4f28d9ed_0
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_0 <= 1000
 R170: z_||_2dx6fafc74611e76e89_0 - z_predicate_2bx70ac945c4f28d9ed_0 >= 0
 R171: - z_predicate_2bx70ac945c4f28d9ed_0
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_0 <= 0
 R172: rho_||_2dx6fafc74611e76e89_0 - rho_predicate_2dx7894b0affacefa_0
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_0 <= 1000
 R173: z_||_2dx6fafc74611e76e89_0 - z_predicate_2dx7894b0affacefa_0 >= 0
 R174: - z_predicate_2dx7894b0affacefa_0
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_0 <= 0
 R175: z_||_2dx6fafc74611e76e89_0 - z_predicate_2bx454ca952238e72db_0
   - z_predicate_2dx19adc98cf842ca58_0 - z_predicate_2bx70ac945c4f28d9ed_0
   - z_predicate_2dx7894b0affacefa_0 <= 0
 R176: - z_||_2dx6fafc74611e76e89_0
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_0
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_0
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_0
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_0 >= 0
 R177: x_1 - 1000 z_predicate_2bx454ca952238e72db_1
   - rho_predicate_2bx454ca952238e72db_1 >= -1003
 R178: x_1 - 1000 z_predicate_2bx454ca952238e72db_1
   - rho_predicate_2bx454ca952238e72db_1 <= -3
 R179: x_1 + 1000 z_predicate_2dx19adc98cf842ca58_1
   + rho_predicate_2dx19adc98cf842ca58_1 <= 992
 R180: x_1 + 1000 z_predicate_2dx19adc98cf842ca58_1
   + rho_predicate_2dx19adc98cf842ca58_1 >= -8
 R181: y_1 - 1000 z_predicate_2bx70ac945c4f28d9ed_1
   - rho_predicate_2bx70ac945c4f28d9ed_1 >= -992
 R182: y_1 - 1000 z_predicate_2bx70ac945c4f28d9ed_1
   - rho_predicate_2bx70ac945c4f28d9ed_1 <= 8
 R183: y_1 + 1000 z_predicate_2dx7894b0affacefa_1
   + rho_predicate_2dx7894b0affacefa_1 <= 1003
 R184: y_1 + 1000 z_predicate_2dx7894b0affacefa_1
   + rho_predicate_2dx7894b0affacefa_1 >= 3
 R185: rho_||_2dx6fafc74611e76e89_1 - rho_predicate_2bx454ca952238e72db_1
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_1 <= 1000
 R186: z_||_2dx6fafc74611e76e89_1 - z_predicate_2bx454ca952238e72db_1 >= 0
 R187: - z_predicate_2bx454ca952238e72db_1
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_1 <= 0
 R188: rho_||_2dx6fafc74611e76e89_1 - rho_predicate_2dx19adc98cf842ca58_1
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_1 <= 1000
 R189: z_||_2dx6fafc74611e76e89_1 - z_predicate_2dx19adc98cf842ca58_1 >= 0
 R190: - z_predicate_2dx19adc98cf842ca58_1
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_1 <= 0
 R191: rho_||_2dx6fafc74611e76e89_1 - rho_predicate_2bx70ac945c4f28d9ed_1
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_1 <= 1000
 R192: z_||_2dx6fafc74611e76e89_1 - z_predicate_2bx70ac945c4f28d9ed_1 >= 0
 R193: - z_predicate_2bx70ac945c4f28d9ed_1
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_1 <= 0
 R194: rho_||_2dx6fafc74611e76e89_1 - rho_predicate_2dx7894b0affacefa_1
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_1 <= 1000
 R195: z_||_2dx6fafc74611e76e89_1 - z_predicate_2dx7894b0affacefa_1 >= 0
 R196: - z_predicate_2dx7894b0affacefa_1
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_1 <= 0
 R197: z_||_2dx6fafc74611e76e89_1 - z_predicate_2bx454ca952238e72db_1
   - z_predicate_2dx19adc98cf842ca58_1 - z_predicate_2bx70ac945c4f28d9ed_1
   - z_predicate_2dx7894b0affacefa_1 <= 0
 R198: - z_||_2dx6fafc74611e76e89_1
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_1
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_1
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_1
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_1 >= 0
 R199: x_2 - 1000 z_predicate_2bx454ca952238e72db_2
   - rho_predicate_2bx454ca952238e72db_2 >= -1003
 R200: x_2 - 1000 z_predicate_2bx454ca952238e72db_2
   - rho_predicate_2bx454ca952238e72db_2 <= -3
 R201: x_2 + 1000 z_predicate_2dx19adc98cf842ca58_2
   + rho_predicate_2dx19adc98cf842ca58_2 <= 992
 R202: x_2 + 1000 z_predicate_2dx19adc98cf842ca58_2
   + rho_predicate_2dx19adc98cf842ca58_2 >= -8
 R203: y_2 - 1000 z_predicate_2bx70ac945c4f28d9ed_2
   - rho_predicate_2bx70ac945c4f28d9ed_2 >= -992
 R204: y_2 - 1000 z_predicate_2bx70ac945c4f28d9ed_2
   - rho_predicate_2bx70ac945c4f28d9ed_2 <= 8
 R205: y_2 + 1000 z_predicate_2dx7894b0affacefa_2
   + rho_predicate_2dx7894b0affacefa_2 <= 1003
 R206: y_2 + 1000 z_predicate_2dx7894b0affacefa_2
   + rho_predicate_2dx7894b0affacefa_2 >= 3
 R207: rho_||_2dx6fafc74611e76e89_2 - rho_predicate_2bx454ca952238e72db_2
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_2 <= 1000
 R208: z_||_2dx6fafc74611e76e89_2 - z_predicate_2bx454ca952238e72db_2 >= 0
 R209: - z_predicate_2bx454ca952238e72db_2
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_2 <= 0
 R210: rho_||_2dx6fafc74611e76e89_2 - rho_predicate_2dx19adc98cf842ca58_2
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_2 <= 1000
 R211: z_||_2dx6fafc74611e76e89_2 - z_predicate_2dx19adc98cf842ca58_2 >= 0
 R212: - z_predicate_2dx19adc98cf842ca58_2
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_2 <= 0
 R213: rho_||_2dx6fafc74611e76e89_2 - rho_predicate_2bx70ac945c4f28d9ed_2
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_2 <= 1000
 R214: z_||_2dx6fafc74611e76e89_2 - z_predicate_2bx70ac945c4f28d9ed_2 >= 0
 R215: - z_predicate_2bx70ac945c4f28d9ed_2
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_2 <= 0
 R216: rho_||_2dx6fafc74611e76e89_2 - rho_predicate_2dx7894b0affacefa_2
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_2 <= 1000
 R217: z_||_2dx6fafc74611e76e89_2 - z_predicate_2dx7894b0affacefa_2 >= 0
 R218: - z_predicate_2dx7894b0affacefa_2
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_2 <= 0
 R219: z_||_2dx6fafc74611e76e89_2 - z_predicate_2bx454ca952238e72db_2
   - z_predicate_2dx19adc98cf842ca58_2 - z_predicate_2bx70ac945c4f28d9ed_2
   - z_predicate_2dx7894b0affacefa_2 <= 0
 R220: - z_||_2dx6fafc74611e76e89_2
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_2
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_2
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_2
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_2 >= 0
 R221: x_3 - 1000 z_predicate_2bx454ca952238e72db_3
   - rho_predicate_2bx454ca952238e72db_3 >= -1003
 R222: x_3 - 1000 z_predicate_2bx454ca952238e72db_3
   - rho_predicate_2bx454ca952238e72db_3 <= -3
 R223: x_3 + 1000 z_predicate_2dx19adc98cf842ca58_3
   + rho_predicate_2dx19adc98cf842ca58_3 <= 992
 R224: x_3 + 1000 z_predicate_2dx19adc98cf842ca58_3
   + rho_predicate_2dx19adc98cf842ca58_3 >= -8
 R225: y_3 - 1000 z_predicate_2bx70ac945c4f28d9ed_3
   - rho_predicate_2bx70ac945c4f28d9ed_3 >= -992
 R226: y_3 - 1000 z_predicate_2bx70ac945c4f28d9ed_3
   - rho_predicate_2bx70ac945c4f28d9ed_3 <= 8
 R227: y_3 + 1000 z_predicate_2dx7894b0affacefa_3
   + rho_predicate_2dx7894b0affacefa_3 <= 1003
 R228: y_3 + 1000 z_predicate_2dx7894b0affacefa_3
   + rho_predicate_2dx7894b0affacefa_3 >= 3
 R229: rho_||_2dx6fafc74611e76e89_3 - rho_predicate_2bx454ca952238e72db_3
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_3 <= 1000
 R230: z_||_2dx6fafc74611e76e89_3 - z_predicate_2bx454ca952238e72db_3 >= 0
 R231: - z_predicate_2bx454ca952238e72db_3
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_3 <= 0
 R232: rho_||_2dx6fafc74611e76e89_3 - rho_predicate_2dx19adc98cf842ca58_3
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_3 <= 1000
 R233: z_||_2dx6fafc74611e76e89_3 - z_predicate_2dx19adc98cf842ca58_3 >= 0
 R234: - z_predicate_2dx19adc98cf842ca58_3
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_3 <= 0
 R235: rho_||_2dx6fafc74611e76e89_3 - rho_predicate_2bx70ac945c4f28d9ed_3
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_3 <= 1000
 R236: z_||_2dx6fafc74611e76e89_3 - z_predicate_2bx70ac945c4f28d9ed_3 >= 0
 R237: - z_predicate_2bx70ac945c4f28d9ed_3
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_3 <= 0
 R238: rho_||_2dx6fafc74611e76e89_3 - rho_predicate_2dx7894b0affacefa_3
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_3 <= 1000
 R239: z_||_2dx6fafc74611e76e89_3 - z_predicate_2dx7894b0affacefa_3 >= 0
 R240: - z_predicate_2dx7894b0affacefa_3
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_3 <= 0
 R241: z_||_2dx6fafc74611e76e89_3 - z_predicate_2bx454ca952238e72db_3
   - z_predicate_2dx19adc98cf842ca58_3 - z_predicate_2bx70ac945c4f28d9ed_3
   - z_predicate_2dx7894b0affacefa_3 <= 0
 R242: - z_||_2dx6fafc74611e76e89_3
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_3
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_3
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_3
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_3 >= 0
 R243: x_4 - 1000 z_predicate_2bx454ca952238e72db_4
   - rho_predicate_2bx454ca952238e72db_4 >= -1003
 R244: x_4 - 1000 z_predicate_2bx454ca952238e72db_4
   - rho_predicate_2bx454ca952238e72db_4 <= -3
 R245: x_4 + 1000 z_predicate_2dx19adc98cf842ca58_4
   + rho_predicate_2dx19adc98cf842ca58_4 <= 992
 R246: x_4 + 1000 z_predicate_2dx19adc98cf842ca58_4
   + rho_predicate_2dx19adc98cf842ca58_4 >= -8
 R247: y_4 - 1000 z_predicate_2bx70ac945c4f28d9ed_4
   - rho_predicate_2bx70ac945c4f28d9ed_4 >= -992
 R248: y_4 - 1000 z_predicate_2bx70ac945c4f28d9ed_4
   - rho_predicate_2bx70ac945c4f28d9ed_4 <= 8
 R249: y_4 + 1000 z_predicate_2dx7894b0affacefa_4
   + rho_predicate_2dx7894b0affacefa_4 <= 1003
 R250: y_4 + 1000 z_predicate_2dx7894b0affacefa_4
   + rho_predicate_2dx7894b0affacefa_4 >= 3
 R251: rho_||_2dx6fafc74611e76e89_4 - rho_predicate_2bx454ca952238e72db_4
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_4 <= 1000
 R252: z_||_2dx6fafc74611e76e89_4 - z_predicate_2bx454ca952238e72db_4 >= 0
 R253: - z_predicate_2bx454ca952238e72db_4
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_4 <= 0
 R254: rho_||_2dx6fafc74611e76e89_4 - rho_predicate_2dx19adc98cf842ca58_4
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_4 <= 1000
 R255: z_||_2dx6fafc74611e76e89_4 - z_predicate_2dx19adc98cf842ca58_4 >= 0
 R256: - z_predicate_2dx19adc98cf842ca58_4
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_4 <= 0
 R257: rho_||_2dx6fafc74611e76e89_4 - rho_predicate_2bx70ac945c4f28d9ed_4
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_4 <= 1000
 R258: z_||_2dx6fafc74611e76e89_4 - z_predicate_2bx70ac945c4f28d9ed_4 >= 0
 R259: - z_predicate_2bx70ac945c4f28d9ed_4
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_4 <= 0
 R260: rho_||_2dx6fafc74611e76e89_4 - rho_predicate_2dx7894b0affacefa_4
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_4 <= 1000
 R261: z_||_2dx6fafc74611e76e89_4 - z_predicate_2dx7894b0affacefa_4 >= 0
 R262: - z_predicate_2dx7894b0affacefa_4
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_4 <= 0
 R263: z_||_2dx6fafc74611e76e89_4 - z_predicate_2bx454ca952238e72db_4
   - z_predicate_2dx19adc98cf842ca58_4 - z_predicate_2bx70ac945c4f28d9ed_4
   - z_predicate_2dx7894b0affacefa_4 <= 0
 R264: - z_||_2dx6fafc74611e76e89_4
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_4
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_4
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_4
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_4 >= 0
 R265: x_5 - 1000 z_predicate_2bx454ca952238e72db_5
   - rho_predicate_2bx454ca952238e72db_5 >= -1003
 R266: x_5 - 1000 z_predicate_2bx454ca952238e72db_5
   - rho_predicate_2bx454ca952238e72db_5 <= -3
 R267: x_5 + 1000 z_predicate_2dx19adc98cf842ca58_5
   + rho_predicate_2dx19adc98cf842ca58_5 <= 992
 R268: x_5 + 1000 z_predicate_2dx19adc98cf842ca58_5
   + rho_predicate_2dx19adc98cf842ca58_5 >= -8
 R269: y_5 - 1000 z_predicate_2bx70ac945c4f28d9ed_5
   - rho_predicate_2bx70ac945c4f28d9ed_5 >= -992
 R270: y_5 - 1000 z_predicate_2bx70ac945c4f28d9ed_5
   - rho_predicate_2bx70ac945c4f28d9ed_5 <= 8
 R271: y_5 + 1000 z_predicate_2dx7894b0affacefa_5
   + rho_predicate_2dx7894b0affacefa_5 <= 1003
 R272: y_5 + 1000 z_predicate_2dx7894b0affacefa_5
   + rho_predicate_2dx7894b0affacefa_5 >= 3
 R273: rho_||_2dx6fafc74611e76e89_5 - rho_predicate_2bx454ca952238e72db_5
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_5 <= 1000
 R274: z_||_2dx6fafc74611e76e89_5 - z_predicate_2bx454ca952238e72db_5 >= 0
 R275: - z_predicate_2bx454ca952238e72db_5
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_5 <= 0
 R276: rho_||_2dx6fafc74611e76e89_5 - rho_predicate_2dx19adc98cf842ca58_5
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_5 <= 1000
 R277: z_||_2dx6fafc74611e76e89_5 - z_predicate_2dx19adc98cf842ca58_5 >= 0
 R278: - z_predicate_2dx19adc98cf842ca58_5
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_5 <= 0
 R279: rho_||_2dx6fafc74611e76e89_5 - rho_predicate_2bx70ac945c4f28d9ed_5
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_5 <= 1000
 R280: z_||_2dx6fafc74611e76e89_5 - z_predicate_2bx70ac945c4f28d9ed_5 >= 0
 R281: - z_predicate_2bx70ac945c4f28d9ed_5
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_5 <= 0
 R282: rho_||_2dx6fafc74611e76e89_5 - rho_predicate_2dx7894b0affacefa_5
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_5 <= 1000
 R283: z_||_2dx6fafc74611e76e89_5 - z_predicate_2dx7894b0affacefa_5 >= 0
 R284: - z_predicate_2dx7894b0affacefa_5
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_5 <= 0
 R285: z_||_2dx6fafc74611e76e89_5 - z_predicate_2bx454ca952238e72db_5
   - z_predicate_2dx19adc98cf842ca58_5 - z_predicate_2bx70ac945c4f28d9ed_5
   - z_predicate_2dx7894b0affacefa_5 <= 0
 R286: - z_||_2dx6fafc74611e76e89_5
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_5
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_5
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_5
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_5 >= 0
 R287: x_6 - 1000 z_predicate_2bx454ca952238e72db_6
   - rho_predicate_2bx454ca952238e72db_6 >= -1003
 R288: x_6 - 1000 z_predicate_2bx454ca952238e72db_6
   - rho_predicate_2bx454ca952238e72db_6 <= -3
 R289: x_6 + 1000 z_predicate_2dx19adc98cf842ca58_6
   + rho_predicate_2dx19adc98cf842ca58_6 <= 992
 R290: x_6 + 1000 z_predicate_2dx19adc98cf842ca58_6
   + rho_predicate_2dx19adc98cf842ca58_6 >= -8
 R291: y_6 - 1000 z_predicate_2bx70ac945c4f28d9ed_6
   - rho_predicate_2bx70ac945c4f28d9ed_6 >= -992
 R292: y_6 - 1000 z_predicate_2bx70ac945c4f28d9ed_6
   - rho_predicate_2bx70ac945c4f28d9ed_6 <= 8
 R293: y_6 + 1000 z_predicate_2dx7894b0affacefa_6
   + rho_predicate_2dx7894b0affacefa_6 <= 1003
 R294: y_6 + 1000 z_predicate_2dx7894b0affacefa_6
   + rho_predicate_2dx7894b0affacefa_6 >= 3
 R295: rho_||_2dx6fafc74611e76e89_6 - rho_predicate_2bx454ca952238e72db_6
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_6 <= 1000
 R296: z_||_2dx6fafc74611e76e89_6 - z_predicate_2bx454ca952238e72db_6 >= 0
 R297: - z_predicate_2bx454ca952238e72db_6
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_6 <= 0
 R298: rho_||_2dx6fafc74611e76e89_6 - rho_predicate_2dx19adc98cf842ca58_6
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_6 <= 1000
 R299: z_||_2dx6fafc74611e76e89_6 - z_predicate_2dx19adc98cf842ca58_6 >= 0
 R300: - z_predicate_2dx19adc98cf842ca58_6
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_6 <= 0
 R301: rho_||_2dx6fafc74611e76e89_6 - rho_predicate_2bx70ac945c4f28d9ed_6
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_6 <= 1000
 R302: z_||_2dx6fafc74611e76e89_6 - z_predicate_2bx70ac945c4f28d9ed_6 >= 0
 R303: - z_predicate_2bx70ac945c4f28d9ed_6
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_6 <= 0
 R304: rho_||_2dx6fafc74611e76e89_6 - rho_predicate_2dx7894b0affacefa_6
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_6 <= 1000
 R305: z_||_2dx6fafc74611e76e89_6 - z_predicate_2dx7894b0affacefa_6 >= 0
 R306: - z_predicate_2dx7894b0affacefa_6
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_6 <= 0
 R307: z_||_2dx6fafc74611e76e89_6 - z_predicate_2bx454ca952238e72db_6
   - z_predicate_2dx19adc98cf842ca58_6 - z_predicate_2bx70ac945c4f28d9ed_6
   - z_predicate_2dx7894b0affacefa_6 <= 0
 R308: - z_||_2dx6fafc74611e76e89_6
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_6
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_6
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_6
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_6 >= 0
 R309: x_7 - 1000 z_predicate_2bx454ca952238e72db_7
   - rho_predicate_2bx454ca952238e72db_7 >= -1003
 R310: x_7 - 1000 z_predicate_2bx454ca952238e72db_7
   - rho_predicate_2bx454ca952238e72db_7 <= -3
 R311: x_7 + 1000 z_predicate_2dx19adc98cf842ca58_7
   + rho_predicate_2dx19adc98cf842ca58_7 <= 992
 R312: x_7 + 1000 z_predicate_2dx19adc98cf842ca58_7
   + rho_predicate_2dx19adc98cf842ca58_7 >= -8
 R313: y_7 - 1000 z_predicate_2bx70ac945c4f28d9ed_7
   - rho_predicate_2bx70ac945c4f28d9ed_7 >= -992
 R314: y_7 - 1000 z_predicate_2bx70ac945c4f28d9ed_7
   - rho_predicate_2bx70ac945c4f28d9ed_7 <= 8
 R315: y_7 + 1000 z_predicate_2dx7894b0affacefa_7
   + rho_predicate_2dx7894b0affacefa_7 <= 1003
 R316: y_7 + 1000 z_predicate_2dx7894b0affacefa_7
   + rho_predicate_2dx7894b0affacefa_7 >= 3
 R317: rho_||_2dx6fafc74611e76e89_7 - rho_predicate_2bx454ca952238e72db_7
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_7 <= 1000
 R318: z_||_2dx6fafc74611e76e89_7 - z_predicate_2bx454ca952238e72db_7 >= 0
 R319: - z_predicate_2bx454ca952238e72db_7
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_7 <= 0
 R320: rho_||_2dx6fafc74611e76e89_7 - rho_predicate_2dx19adc98cf842ca58_7
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_7 <= 1000
 R321: z_||_2dx6fafc74611e76e89_7 - z_predicate_2dx19adc98cf842ca58_7 >= 0
 R322: - z_predicate_2dx19adc98cf842ca58_7
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_7 <= 0
 R323: rho_||_2dx6fafc74611e76e89_7 - rho_predicate_2bx70ac945c4f28d9ed_7
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_7 <= 1000
 R324: z_||_2dx6fafc74611e76e89_7 - z_predicate_2bx70ac945c4f28d9ed_7 >= 0
 R325: - z_predicate_2bx70ac945c4f28d9ed_7
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_7 <= 0
 R326: rho_||_2dx6fafc74611e76e89_7 - rho_predicate_2dx7894b0affacefa_7
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_7 <= 1000
 R327: z_||_2dx6fafc74611e76e89_7 - z_predicate_2dx7894b0affacefa_7 >= 0
 R328: - z_predicate_2dx7894b0affacefa_7
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_7 <= 0
 R329: z_||_2dx6fafc74611e76e89_7 - z_predicate_2bx454ca952238e72db_7
   - z_predicate_2dx19adc98cf842ca58_7 - z_predicate_2bx70ac945c4f28d9ed_7
   - z_predicate_2dx7894b0affacefa_7 <= 0
 R330: - z_||_2dx6fafc74611e76e89_7
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_7
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_7
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_7
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_7 >= 0
 R331: x_8 - 1000 z_predicate_2bx454ca952238e72db_8
   - rho_predicate_2bx454ca952238e72db_8 >= -1003
 R332: x_8 - 1000 z_predicate_2bx454ca952238e72db_8
   - rho_predicate_2bx454ca952238e72db_8 <= -3
 R333: x_8 + 1000 z_predicate_2dx19adc98cf842ca58_8
   + rho_predicate_2dx19adc98cf842ca58_8 <= 992
 R334: x_8 + 1000 z_predicate_2dx19adc98cf842ca58_8
   + rho_predicate_2dx19adc98cf842ca58_8 >= -8
 R335: y_8 - 1000 z_predicate_2bx70ac945c4f28d9ed_8
   - rho_predicate_2bx70ac945c4f28d9ed_8 >= -992
 R336: y_8 - 1000 z_predicate_2bx70ac945c4f28d9ed_8
   - rho_predicate_2bx70ac945c4f28d9ed_8 <= 8
 R337: y_8 + 1000 z_predicate_2dx7894b0affacefa_8
   + rho_predicate_2dx7894b0affacefa_8 <= 1003
 R338: y_8 + 1000 z_predicate_2dx7894b0affacefa_8
   + rho_predicate_2dx7894b0affacefa_8 >= 3
 R339: rho_||_2dx6fafc74611e76e89_8 - rho_predicate_2bx454ca952238e72db_8
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_8 <= 1000
 R340: z_||_2dx6fafc74611e76e89_8 - z_predicate_2bx454ca952238e72db_8 >= 0
 R341: - z_predicate_2bx454ca952238e72db_8
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_8 <= 0
 R342: rho_||_2dx6fafc74611e76e89_8 - rho_predicate_2dx19adc98cf842ca58_8
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_8 <= 1000
 R343: z_||_2dx6fafc74611e76e89_8 - z_predicate_2dx19adc98cf842ca58_8 >= 0
 R344: - z_predicate_2dx19adc98cf842ca58_8
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_8 <= 0
 R345: rho_||_2dx6fafc74611e76e89_8 - rho_predicate_2bx70ac945c4f28d9ed_8
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_8 <= 1000
 R346: z_||_2dx6fafc74611e76e89_8 - z_predicate_2bx70ac945c4f28d9ed_8 >= 0
 R347: - z_predicate_2bx70ac945c4f28d9ed_8
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_8 <= 0
 R348: rho_||_2dx6fafc74611e76e89_8 - rho_predicate_2dx7894b0affacefa_8
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_8 <= 1000
 R349: z_||_2dx6fafc74611e76e89_8 - z_predicate_2dx7894b0affacefa_8 >= 0
 R350: - z_predicate_2dx7894b0affacefa_8
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_8 <= 0
 R351: z_||_2dx6fafc74611e76e89_8 - z_predicate_2bx454ca952238e72db_8
   - z_predicate_2dx19adc98cf842ca58_8 - z_predicate_2bx70ac945c4f28d9ed_8
   - z_predicate_2dx7894b0affacefa_8 <= 0
 R352: - z_||_2dx6fafc74611e76e89_8
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_8
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_8
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_8
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_8 >= 0
 R353: x_9 - 1000 z_predicate_2bx454ca952238e72db_9
   - rho_predicate_2bx454ca952238e72db_9 >= -1003
 R354: x_9 - 1000 z_predicate_2bx454ca952238e72db_9
   - rho_predicate_2bx454ca952238e72db_9 <= -3
 R355: x_9 + 1000 z_predicate_2dx19adc98cf842ca58_9
   + rho_predicate_2dx19adc98cf842ca58_9 <= 992
 R356: x_9 + 1000 z_predicate_2dx19adc98cf842ca58_9
   + rho_predicate_2dx19adc98cf842ca58_9 >= -8
 R357: y_9 - 1000 z_predicate_2bx70ac945c4f28d9ed_9
   - rho_predicate_2bx70ac945c4f28d9ed_9 >= -992
 R358: y_9 - 1000 z_predicate_2bx70ac945c4f28d9ed_9
   - rho_predicate_2bx70ac945c4f28d9ed_9 <= 8
 R359: y_9 + 1000 z_predicate_2dx7894b0affacefa_9
   + rho_predicate_2dx7894b0affacefa_9 <= 1003
 R360: y_9 + 1000 z_predicate_2dx7894b0affacefa_9
   + rho_predicate_2dx7894b0affacefa_9 >= 3
 R361: rho_||_2dx6fafc74611e76e89_9 - rho_predicate_2bx454ca952238e72db_9
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_9 <= 1000
 R362: z_||_2dx6fafc74611e76e89_9 - z_predicate_2bx454ca952238e72db_9 >= 0
 R363: - z_predicate_2bx454ca952238e72db_9
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_9 <= 0
 R364: rho_||_2dx6fafc74611e76e89_9 - rho_predicate_2dx19adc98cf842ca58_9
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_9 <= 1000
 R365: z_||_2dx6fafc74611e76e89_9 - z_predicate_2dx19adc98cf842ca58_9 >= 0
 R366: - z_predicate_2dx19adc98cf842ca58_9
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_9 <= 0
 R367: rho_||_2dx6fafc74611e76e89_9 - rho_predicate_2bx70ac945c4f28d9ed_9
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_9 <= 1000
 R368: z_||_2dx6fafc74611e76e89_9 - z_predicate_2bx70ac945c4f28d9ed_9 >= 0
 R369: - z_predicate_2bx70ac945c4f28d9ed_9
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_9 <= 0
 R370: rho_||_2dx6fafc74611e76e89_9 - rho_predicate_2dx7894b0affacefa_9
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_9 <= 1000
 R371: z_||_2dx6fafc74611e76e89_9 - z_predicate_2dx7894b0affacefa_9 >= 0
 R372: - z_predicate_2dx7894b0affacefa_9
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_9 <= 0
 R373: z_||_2dx6fafc74611e76e89_9 - z_predicate_2bx454ca952238e72db_9
   - z_predicate_2dx19adc98cf842ca58_9 - z_predicate_2bx70ac945c4f28d9ed_9
   - z_predicate_2dx7894b0affacefa_9 <= 0
 R374: - z_||_2dx6fafc74611e76e89_9
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_9
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_9
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_9
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_9 >= 0
 R375: x_10 - 1000 z_predicate_2bx454ca952238e72db_10
   - rho_predicate_2bx454ca952238e72db_10 >= -1003
 R376: x_10 - 1000 z_predicate_2bx454ca952238e72db_10
   - rho_predicate_2bx454ca952238e72db_10 <= -3
 R377: x_10 + 1000 z_predicate_2dx19adc98cf842ca58_10
   + rho_predicate_2dx19adc98cf842ca58_10 <= 992
 R378: x_10 + 1000 z_predicate_2dx19adc98cf842ca58_10
   + rho_predicate_2dx19adc98cf842ca58_10 >= -8
 R379: y_10 - 1000 z_predicate_2bx70ac945c4f28d9ed_10
   - rho_predicate_2bx70ac945c4f28d9ed_10 >= -992
 R380: y_10 - 1000 z_predicate_2bx70ac945c4f28d9ed_10
   - rho_predicate_2bx70ac945c4f28d9ed_10 <= 8
 R381: y_10 + 1000 z_predicate_2dx7894b0affacefa_10
   + rho_predicate_2dx7894b0affacefa_10 <= 1003
 R382: y_10 + 1000 z_predicate_2dx7894b0affacefa_10
   + rho_predicate_2dx7894b0affacefa_10 >= 3
 R383: rho_||_2dx6fafc74611e76e89_10 - rho_predicate_2bx454ca952238e72db_10
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_10
   <= 1000
 R384: z_||_2dx6fafc74611e76e89_10 - z_predicate_2bx454ca952238e72db_10
   >= 0
 R385: - z_predicate_2bx454ca952238e72db_10
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_10 <= 0
 R386: rho_||_2dx6fafc74611e76e89_10 - rho_predicate_2dx19adc98cf842ca58_10
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_10
   <= 1000
 R387: z_||_2dx6fafc74611e76e89_10 - z_predicate_2dx19adc98cf842ca58_10
   >= 0
 R388: - z_predicate_2dx19adc98cf842ca58_10
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_10 <= 0
 R389: rho_||_2dx6fafc74611e76e89_10 - rho_predicate_2bx70ac945c4f28d9ed_10
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_10
   <= 1000
 R390: z_||_2dx6fafc74611e76e89_10 - z_predicate_2bx70ac945c4f28d9ed_10
   >= 0
 R391: - z_predicate_2bx70ac945c4f28d9ed_10
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_10 <= 0
 R392: rho_||_2dx6fafc74611e76e89_10 - rho_predicate_2dx7894b0affacefa_10
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_10 <= 1000
 R393: z_||_2dx6fafc74611e76e89_10 - z_predicate_2dx7894b0affacefa_10 >= 0
 R394: - z_predicate_2dx7894b0affacefa_10
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_10 <= 0
 R395: z_||_2dx6fafc74611e76e89_10 - z_predicate_2bx454ca952238e72db_10
   - z_predicate_2dx19adc98cf842ca58_10
   - z_predicate_2bx70ac945c4f28d9ed_10 - z_predicate_2dx7894b0affacefa_10
   <= 0
 R396: - z_||_2dx6fafc74611e76e89_10
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_10
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_10
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_10
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_10 >= 0
 R397: x_11 - 1000 z_predicate_2bx454ca952238e72db_11
   - rho_predicate_2bx454ca952238e72db_11 >= -1003
 R398: x_11 - 1000 z_predicate_2bx454ca952238e72db_11
   - rho_predicate_2bx454ca952238e72db_11 <= -3
 R399: x_11 + 1000 z_predicate_2dx19adc98cf842ca58_11
   + rho_predicate_2dx19adc98cf842ca58_11 <= 992
 R400: x_11 + 1000 z_predicate_2dx19adc98cf842ca58_11
   + rho_predicate_2dx19adc98cf842ca58_11 >= -8
 R401: y_11 - 1000 z_predicate_2bx70ac945c4f28d9ed_11
   - rho_predicate_2bx70ac945c4f28d9ed_11 >= -992
 R402: y_11 - 1000 z_predicate_2bx70ac945c4f28d9ed_11
   - rho_predicate_2bx70ac945c4f28d9ed_11 <= 8
 R403: y_11 + 1000 z_predicate_2dx7894b0affacefa_11
   + rho_predicate_2dx7894b0affacefa_11 <= 1003
 R404: y_11 + 1000 z_predicate_2dx7894b0affacefa_11
   + rho_predicate_2dx7894b0affacefa_11 >= 3
 R405: rho_||_2dx6fafc74611e76e89_11 - rho_predicate_2bx454ca952238e72db_11
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_11
   <= 1000
 R406: z_||_2dx6fafc74611e76e89_11 - z_predicate_2bx454ca952238e72db_11
   >= 0
 R407: - z_predicate_2bx454ca952238e72db_11
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_11 <= 0
 R408: rho_||_2dx6fafc74611e76e89_11 - rho_predicate_2dx19adc98cf842ca58_11
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_11
   <= 1000
 R409: z_||_2dx6fafc74611e76e89_11 - z_predicate_2dx19adc98cf842ca58_11
   >= 0
 R410: - z_predicate_2dx19adc98cf842ca58_11
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_11 <= 0
 R411: rho_||_2dx6fafc74611e76e89_11 - rho_predicate_2bx70ac945c4f28d9ed_11
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_11
   <= 1000
 R412: z_||_2dx6fafc74611e76e89_11 - z_predicate_2bx70ac945c4f28d9ed_11
   >= 0
 R413: - z_predicate_2bx70ac945c4f28d9ed_11
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_11 <= 0
 R414: rho_||_2dx6fafc74611e76e89_11 - rho_predicate_2dx7894b0affacefa_11
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_11 <= 1000
 R415: z_||_2dx6fafc74611e76e89_11 - z_predicate_2dx7894b0affacefa_11 >= 0
 R416: - z_predicate_2dx7894b0affacefa_11
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_11 <= 0
 R417: z_||_2dx6fafc74611e76e89_11 - z_predicate_2bx454ca952238e72db_11
   - z_predicate_2dx19adc98cf842ca58_11
   - z_predicate_2bx70ac945c4f28d9ed_11 - z_predicate_2dx7894b0affacefa_11
   <= 0
 R418: - z_||_2dx6fafc74611e76e89_11
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_11
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_11
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_11
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_11 >= 0
 R419: x_12 - 1000 z_predicate_2bx454ca952238e72db_12
   - rho_predicate_2bx454ca952238e72db_12 >= -1003
 R420: x_12 - 1000 z_predicate_2bx454ca952238e72db_12
   - rho_predicate_2bx454ca952238e72db_12 <= -3
 R421: x_12 + 1000 z_predicate_2dx19adc98cf842ca58_12
   + rho_predicate_2dx19adc98cf842ca58_12 <= 992
 R422: x_12 + 1000 z_predicate_2dx19adc98cf842ca58_12
   + rho_predicate_2dx19adc98cf842ca58_12 >= -8
 R423: y_12 - 1000 z_predicate_2bx70ac945c4f28d9ed_12
   - rho_predicate_2bx70ac945c4f28d9ed_12 >= -992
 R424: y_12 - 1000 z_predicate_2bx70ac945c4f28d9ed_12
   - rho_predicate_2bx70ac945c4f28d9ed_12 <= 8
 R425: y_12 + 1000 z_predicate_2dx7894b0affacefa_12
   + rho_predicate_2dx7894b0affacefa_12 <= 1003
 R426: y_12 + 1000 z_predicate_2dx7894b0affacefa_12
   + rho_predicate_2dx7894b0affacefa_12 >= 3
 R427: rho_||_2dx6fafc74611e76e89_12 - rho_predicate_2bx454ca952238e72db_12
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_12
   <= 1000
 R428: z_||_2dx6fafc74611e76e89_12 - z_predicate_2bx454ca952238e72db_12
   >= 0
 R429: - z_predicate_2bx454ca952238e72db_12
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_12 <= 0
 R430: rho_||_2dx6fafc74611e76e89_12 - rho_predicate_2dx19adc98cf842ca58_12
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_12
   <= 1000
 R431: z_||_2dx6fafc74611e76e89_12 - z_predicate_2dx19adc98cf842ca58_12
   >= 0
 R432: - z_predicate_2dx19adc98cf842ca58_12
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_12 <= 0
 R433: rho_||_2dx6fafc74611e76e89_12 - rho_predicate_2bx70ac945c4f28d9ed_12
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_12
   <= 1000
 R434: z_||_2dx6fafc74611e76e89_12 - z_predicate_2bx70ac945c4f28d9ed_12
   >= 0
 R435: - z_predicate_2bx70ac945c4f28d9ed_12
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_12 <= 0
 R436: rho_||_2dx6fafc74611e76e89_12 - rho_predicate_2dx7894b0affacefa_12
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_12 <= 1000
 R437: z_||_2dx6fafc74611e76e89_12 - z_predicate_2dx7894b0affacefa_12 >= 0
 R438: - z_predicate_2dx7894b0affacefa_12
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_12 <= 0
 R439: z_||_2dx6fafc74611e76e89_12 - z_predicate_2bx454ca952238e72db_12
   - z_predicate_2dx19adc98cf842ca58_12
   - z_predicate_2bx70ac945c4f28d9ed_12 - z_predicate_2dx7894b0affacefa_12
   <= 0
 R440: - z_||_2dx6fafc74611e76e89_12
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_12
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_12
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_12
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_12 >= 0
 R441: x_13 - 1000 z_predicate_2bx454ca952238e72db_13
   - rho_predicate_2bx454ca952238e72db_13 >= -1003
 R442: x_13 - 1000 z_predicate_2bx454ca952238e72db_13
   - rho_predicate_2bx454ca952238e72db_13 <= -3
 R443: x_13 + 1000 z_predicate_2dx19adc98cf842ca58_13
   + rho_predicate_2dx19adc98cf842ca58_13 <= 992
 R444: x_13 + 1000 z_predicate_2dx19adc98cf842ca58_13
   + rho_predicate_2dx19adc98cf842ca58_13 >= -8
 R445: y_13 - 1000 z_predicate_2bx70ac945c4f28d9ed_13
   - rho_predicate_2bx70ac945c4f28d9ed_13 >= -992
 R446: y_13 - 1000 z_predicate_2bx70ac945c4f28d9ed_13
   - rho_predicate_2bx70ac945c4f28d9ed_13 <= 8
 R447: y_13 + 1000 z_predicate_2dx7894b0affacefa_13
   + rho_predicate_2dx7894b0affacefa_13 <= 1003
 R448: y_13 + 1000 z_predicate_2dx7894b0affacefa_13
   + rho_predicate_2dx7894b0affacefa_13 >= 3
 R449: rho_||_2dx6fafc74611e76e89_13 - rho_predicate_2bx454ca952238e72db_13
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_13
   <= 1000
 R450: z_||_2dx6fafc74611e76e89_13 - z_predicate_2bx454ca952238e72db_13
   >= 0
 R451: - z_predicate_2bx454ca952238e72db_13
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_13 <= 0
 R452: rho_||_2dx6fafc74611e76e89_13 - rho_predicate_2dx19adc98cf842ca58_13
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_13
   <= 1000
 R453: z_||_2dx6fafc74611e76e89_13 - z_predicate_2dx19adc98cf842ca58_13
   >= 0
 R454: - z_predicate_2dx19adc98cf842ca58_13
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_13 <= 0
 R455: rho_||_2dx6fafc74611e76e89_13 - rho_predicate_2bx70ac945c4f28d9ed_13
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_13
   <= 1000
 R456: z_||_2dx6fafc74611e76e89_13 - z_predicate_2bx70ac945c4f28d9ed_13
   >= 0
 R457: - z_predicate_2bx70ac945c4f28d9ed_13
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_13 <= 0
 R458: rho_||_2dx6fafc74611e76e89_13 - rho_predicate_2dx7894b0affacefa_13
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_13 <= 1000
 R459: z_||_2dx6fafc74611e76e89_13 - z_predicate_2dx7894b0affacefa_13 >= 0
 R460: - z_predicate_2dx7894b0affacefa_13
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_13 <= 0
 R461: z_||_2dx6fafc74611e76e89_13 - z_predicate_2bx454ca952238e72db_13
   - z_predicate_2dx19adc98cf842ca58_13
   - z_predicate_2bx70ac945c4f28d9ed_13 - z_predicate_2dx7894b0affacefa_13
   <= 0
 R462: - z_||_2dx6fafc74611e76e89_13
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_13
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_13
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_13
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_13 >= 0
 R463: x_14 - 1000 z_predicate_2bx454ca952238e72db_14
   - rho_predicate_2bx454ca952238e72db_14 >= -1003
 R464: x_14 - 1000 z_predicate_2bx454ca952238e72db_14
   - rho_predicate_2bx454ca952238e72db_14 <= -3
 R465: x_14 + 1000 z_predicate_2dx19adc98cf842ca58_14
   + rho_predicate_2dx19adc98cf842ca58_14 <= 992
 R466: x_14 + 1000 z_predicate_2dx19adc98cf842ca58_14
   + rho_predicate_2dx19adc98cf842ca58_14 >= -8
 R467: y_14 - 1000 z_predicate_2bx70ac945c4f28d9ed_14
   - rho_predicate_2bx70ac945c4f28d9ed_14 >= -992
 R468: y_14 - 1000 z_predicate_2bx70ac945c4f28d9ed_14
   - rho_predicate_2bx70ac945c4f28d9ed_14 <= 8
 R469: y_14 + 1000 z_predicate_2dx7894b0affacefa_14
   + rho_predicate_2dx7894b0affacefa_14 <= 1003
 R470: y_14 + 1000 z_predicate_2dx7894b0affacefa_14
   + rho_predicate_2dx7894b0affacefa_14 >= 3
 R471: rho_||_2dx6fafc74611e76e89_14 - rho_predicate_2bx454ca952238e72db_14
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_14
   <= 1000
 R472: z_||_2dx6fafc74611e76e89_14 - z_predicate_2bx454ca952238e72db_14
   >= 0
 R473: - z_predicate_2bx454ca952238e72db_14
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_14 <= 0
 R474: rho_||_2dx6fafc74611e76e89_14 - rho_predicate_2dx19adc98cf842ca58_14
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_14
   <= 1000
 R475: z_||_2dx6fafc74611e76e89_14 - z_predicate_2dx19adc98cf842ca58_14
   >= 0
 R476: - z_predicate_2dx19adc98cf842ca58_14
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_14 <= 0
 R477: rho_||_2dx6fafc74611e76e89_14 - rho_predicate_2bx70ac945c4f28d9ed_14
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_14
   <= 1000
 R478: z_||_2dx6fafc74611e76e89_14 - z_predicate_2bx70ac945c4f28d9ed_14
   >= 0
 R479: - z_predicate_2bx70ac945c4f28d9ed_14
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_14 <= 0
 R480: rho_||_2dx6fafc74611e76e89_14 - rho_predicate_2dx7894b0affacefa_14
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_14 <= 1000
 R481: z_||_2dx6fafc74611e76e89_14 - z_predicate_2dx7894b0affacefa_14 >= 0
 R482: - z_predicate_2dx7894b0affacefa_14
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_14 <= 0
 R483: z_||_2dx6fafc74611e76e89_14 - z_predicate_2bx454ca952238e72db_14
   - z_predicate_2dx19adc98cf842ca58_14
   - z_predicate_2bx70ac945c4f28d9ed_14 - z_predicate_2dx7894b0affacefa_14
   <= 0
 R484: - z_||_2dx6fafc74611e76e89_14
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_14
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_14
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_14
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_14 >= 0
 R485: x_15 - 1000 z_predicate_2bx454ca952238e72db_15
   - rho_predicate_2bx454ca952238e72db_15 >= -1003
 R486: x_15 - 1000 z_predicate_2bx454ca952238e72db_15
   - rho_predicate_2bx454ca952238e72db_15 <= -3
 R487: x_15 + 1000 z_predicate_2dx19adc98cf842ca58_15
   + rho_predicate_2dx19adc98cf842ca58_15 <= 992
 R488: x_15 + 1000 z_predicate_2dx19adc98cf842ca58_15
   + rho_predicate_2dx19adc98cf842ca58_15 >= -8
 R489: y_15 - 1000 z_predicate_2bx70ac945c4f28d9ed_15
   - rho_predicate_2bx70ac945c4f28d9ed_15 >= -992
 R490: y_15 - 1000 z_predicate_2bx70ac945c4f28d9ed_15
   - rho_predicate_2bx70ac945c4f28d9ed_15 <= 8
 R491: y_15 + 1000 z_predicate_2dx7894b0affacefa_15
   + rho_predicate_2dx7894b0affacefa_15 <= 1003
 R492: y_15 + 1000 z_predicate_2dx7894b0affacefa_15
   + rho_predicate_2dx7894b0affacefa_15 >= 3
 R493: rho_||_2dx6fafc74611e76e89_15 - rho_predicate_2bx454ca952238e72db_15
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_15
   <= 1000
 R494: z_||_2dx6fafc74611e76e89_15 - z_predicate_2bx454ca952238e72db_15
   >= 0
 R495: - z_predicate_2bx454ca952238e72db_15
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_15 <= 0
 R496: rho_||_2dx6fafc74611e76e89_15 - rho_predicate_2dx19adc98cf842ca58_15
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_15
   <= 1000
 R497: z_||_2dx6fafc74611e76e89_15 - z_predicate_2dx19adc98cf842ca58_15
   >= 0
 R498: - z_predicate_2dx19adc98cf842ca58_15
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_15 <= 0
 R499: rho_||_2dx6fafc74611e76e89_15 - rho_predicate_2bx70ac945c4f28d9ed_15
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_15
   <= 1000
 R500: z_||_2dx6fafc74611e76e89_15 - z_predicate_2bx70ac945c4f28d9ed_15
   >= 0
 R501: - z_predicate_2bx70ac945c4f28d9ed_15
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_15 <= 0
 R502: rho_||_2dx6fafc74611e76e89_15 - rho_predicate_2dx7894b0affacefa_15
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_15 <= 1000
 R503: z_||_2dx6fafc74611e76e89_15 - z_predicate_2dx7894b0affacefa_15 >= 0
 R504: - z_predicate_2dx7894b0affacefa_15
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_15 <= 0
 R505: z_||_2dx6fafc74611e76e89_15 - z_predicate_2bx454ca952238e72db_15
   - z_predicate_2dx19adc98cf842ca58_15
   - z_predicate_2bx70ac945c4f28d9ed_15 - z_predicate_2dx7894b0affacefa_15
   <= 0
 R506: - z_||_2dx6fafc74611e76e89_15
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_15
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_15
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_15
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_15 >= 0
 R507: x_16 - 1000 z_predicate_2bx454ca952238e72db_16
   - rho_predicate_2bx454ca952238e72db_16 >= -1003
 R508: x_16 - 1000 z_predicate_2bx454ca952238e72db_16
   - rho_predicate_2bx454ca952238e72db_16 <= -3
 R509: x_16 + 1000 z_predicate_2dx19adc98cf842ca58_16
   + rho_predicate_2dx19adc98cf842ca58_16 <= 992
 R510: x_16 + 1000 z_predicate_2dx19adc98cf842ca58_16
   + rho_predicate_2dx19adc98cf842ca58_16 >= -8
 R511: y_16 - 1000 z_predicate_2bx70ac945c4f28d9ed_16
   - rho_predicate_2bx70ac945c4f28d9ed_16 >= -992
 R512: y_16 - 1000 z_predicate_2bx70ac945c4f28d9ed_16
   - rho_predicate_2bx70ac945c4f28d9ed_16 <= 8
 R513: y_16 + 1000 z_predicate_2dx7894b0affacefa_16
   + rho_predicate_2dx7894b0affacefa_16 <= 1003
 R514: y_16 + 1000 z_predicate_2dx7894b0affacefa_16
   + rho_predicate_2dx7894b0affacefa_16 >= 3
 R515: rho_||_2dx6fafc74611e76e89_16 - rho_predicate_2bx454ca952238e72db_16
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_16
   <= 1000
 R516: z_||_2dx6fafc74611e76e89_16 - z_predicate_2bx454ca952238e72db_16
   >= 0
 R517: - z_predicate_2bx454ca952238e72db_16
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_16 <= 0
 R518: rho_||_2dx6fafc74611e76e89_16 - rho_predicate_2dx19adc98cf842ca58_16
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_16
   <= 1000
 R519: z_||_2dx6fafc74611e76e89_16 - z_predicate_2dx19adc98cf842ca58_16
   >= 0
 R520: - z_predicate_2dx19adc98cf842ca58_16
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_16 <= 0
 R521: rho_||_2dx6fafc74611e76e89_16 - rho_predicate_2bx70ac945c4f28d9ed_16
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_16
   <= 1000
 R522: z_||_2dx6fafc74611e76e89_16 - z_predicate_2bx70ac945c4f28d9ed_16
   >= 0
 R523: - z_predicate_2bx70ac945c4f28d9ed_16
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_16 <= 0
 R524: rho_||_2dx6fafc74611e76e89_16 - rho_predicate_2dx7894b0affacefa_16
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_16 <= 1000
 R525: z_||_2dx6fafc74611e76e89_16 - z_predicate_2dx7894b0affacefa_16 >= 0
 R526: - z_predicate_2dx7894b0affacefa_16
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_16 <= 0
 R527: z_||_2dx6fafc74611e76e89_16 - z_predicate_2bx454ca952238e72db_16
   - z_predicate_2dx19adc98cf842ca58_16
   - z_predicate_2bx70ac945c4f28d9ed_16 - z_predicate_2dx7894b0affacefa_16
   <= 0
 R528: - z_||_2dx6fafc74611e76e89_16
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_16
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_16
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_16
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_16 >= 0
 R529: x_17 - 1000 z_predicate_2bx454ca952238e72db_17
   - rho_predicate_2bx454ca952238e72db_17 >= -1003
 R530: x_17 - 1000 z_predicate_2bx454ca952238e72db_17
   - rho_predicate_2bx454ca952238e72db_17 <= -3
 R531: x_17 + 1000 z_predicate_2dx19adc98cf842ca58_17
   + rho_predicate_2dx19adc98cf842ca58_17 <= 992
 R532: x_17 + 1000 z_predicate_2dx19adc98cf842ca58_17
   + rho_predicate_2dx19adc98cf842ca58_17 >= -8
 R533: y_17 - 1000 z_predicate_2bx70ac945c4f28d9ed_17
   - rho_predicate_2bx70ac945c4f28d9ed_17 >= -992
 R534: y_17 - 1000 z_predicate_2bx70ac945c4f28d9ed_17
   - rho_predicate_2bx70ac945c4f28d9ed_17 <= 8
 R535: y_17 + 1000 z_predicate_2dx7894b0affacefa_17
   + rho_predicate_2dx7894b0affacefa_17 <= 1003
 R536: y_17 + 1000 z_predicate_2dx7894b0affacefa_17
   + rho_predicate_2dx7894b0affacefa_17 >= 3
 R537: rho_||_2dx6fafc74611e76e89_17 - rho_predicate_2bx454ca952238e72db_17
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_17
   <= 1000
 R538: z_||_2dx6fafc74611e76e89_17 - z_predicate_2bx454ca952238e72db_17
   >= 0
 R539: - z_predicate_2bx454ca952238e72db_17
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_17 <= 0
 R540: rho_||_2dx6fafc74611e76e89_17 - rho_predicate_2dx19adc98cf842ca58_17
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_17
   <= 1000
 R541: z_||_2dx6fafc74611e76e89_17 - z_predicate_2dx19adc98cf842ca58_17
   >= 0
 R542: - z_predicate_2dx19adc98cf842ca58_17
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_17 <= 0
 R543: rho_||_2dx6fafc74611e76e89_17 - rho_predicate_2bx70ac945c4f28d9ed_17
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_17
   <= 1000
 R544: z_||_2dx6fafc74611e76e89_17 - z_predicate_2bx70ac945c4f28d9ed_17
   >= 0
 R545: - z_predicate_2bx70ac945c4f28d9ed_17
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_17 <= 0
 R546: rho_||_2dx6fafc74611e76e89_17 - rho_predicate_2dx7894b0affacefa_17
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_17 <= 1000
 R547: z_||_2dx6fafc74611e76e89_17 - z_predicate_2dx7894b0affacefa_17 >= 0
 R548: - z_predicate_2dx7894b0affacefa_17
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_17 <= 0
 R549: z_||_2dx6fafc74611e76e89_17 - z_predicate_2bx454ca952238e72db_17
   - z_predicate_2dx19adc98cf842ca58_17
   - z_predicate_2bx70ac945c4f28d9ed_17 - z_predicate_2dx7894b0affacefa_17
   <= 0
 R550: - z_||_2dx6fafc74611e76e89_17
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_17
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_17
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_17
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_17 >= 0
 R551: x_18 - 1000 z_predicate_2bx454ca952238e72db_18
   - rho_predicate_2bx454ca952238e72db_18 >= -1003
 R552: x_18 - 1000 z_predicate_2bx454ca952238e72db_18
   - rho_predicate_2bx454ca952238e72db_18 <= -3
 R553: x_18 + 1000 z_predicate_2dx19adc98cf842ca58_18
   + rho_predicate_2dx19adc98cf842ca58_18 <= 992
 R554: x_18 + 1000 z_predicate_2dx19adc98cf842ca58_18
   + rho_predicate_2dx19adc98cf842ca58_18 >= -8
 R555: y_18 - 1000 z_predicate_2bx70ac945c4f28d9ed_18
   - rho_predicate_2bx70ac945c4f28d9ed_18 >= -992
 R556: y_18 - 1000 z_predicate_2bx70ac945c4f28d9ed_18
   - rho_predicate_2bx70ac945c4f28d9ed_18 <= 8
 R557: y_18 + 1000 z_predicate_2dx7894b0affacefa_18
   + rho_predicate_2dx7894b0affacefa_18 <= 1003
 R558: y_18 + 1000 z_predicate_2dx7894b0affacefa_18
   + rho_predicate_2dx7894b0affacefa_18 >= 3
 R559: rho_||_2dx6fafc74611e76e89_18 - rho_predicate_2bx454ca952238e72db_18
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_18
   <= 1000
 R560: z_||_2dx6fafc74611e76e89_18 - z_predicate_2bx454ca952238e72db_18
   >= 0
 R561: - z_predicate_2bx454ca952238e72db_18
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_18 <= 0
 R562: rho_||_2dx6fafc74611e76e89_18 - rho_predicate_2dx19adc98cf842ca58_18
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_18
   <= 1000
 R563: z_||_2dx6fafc74611e76e89_18 - z_predicate_2dx19adc98cf842ca58_18
   >= 0
 R564: - z_predicate_2dx19adc98cf842ca58_18
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_18 <= 0
 R565: rho_||_2dx6fafc74611e76e89_18 - rho_predicate_2bx70ac945c4f28d9ed_18
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_18
   <= 1000
 R566: z_||_2dx6fafc74611e76e89_18 - z_predicate_2bx70ac945c4f28d9ed_18
   >= 0
 R567: - z_predicate_2bx70ac945c4f28d9ed_18
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_18 <= 0
 R568: rho_||_2dx6fafc74611e76e89_18 - rho_predicate_2dx7894b0affacefa_18
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_18 <= 1000
 R569: z_||_2dx6fafc74611e76e89_18 - z_predicate_2dx7894b0affacefa_18 >= 0
 R570: - z_predicate_2dx7894b0affacefa_18
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_18 <= 0
 R571: z_||_2dx6fafc74611e76e89_18 - z_predicate_2bx454ca952238e72db_18
   - z_predicate_2dx19adc98cf842ca58_18
   - z_predicate_2bx70ac945c4f28d9ed_18 - z_predicate_2dx7894b0affacefa_18
   <= 0
 R572: - z_||_2dx6fafc74611e76e89_18
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_18
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_18
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_18
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_18 >= 0
 R573: x_19 - 1000 z_predicate_2bx454ca952238e72db_19
   - rho_predicate_2bx454ca952238e72db_19 >= -1003
 R574: x_19 - 1000 z_predicate_2bx454ca952238e72db_19
   - rho_predicate_2bx454ca952238e72db_19 <= -3
 R575: x_19 + 1000 z_predicate_2dx19adc98cf842ca58_19
   + rho_predicate_2dx19adc98cf842ca58_19 <= 992
 R576: x_19 + 1000 z_predicate_2dx19adc98cf842ca58_19
   + rho_predicate_2dx19adc98cf842ca58_19 >= -8
 R577: y_19 - 1000 z_predicate_2bx70ac945c4f28d9ed_19
   - rho_predicate_2bx70ac945c4f28d9ed_19 >= -992
 R578: y_19 - 1000 z_predicate_2bx70ac945c4f28d9ed_19
   - rho_predicate_2bx70ac945c4f28d9ed_19 <= 8
 R579: y_19 + 1000 z_predicate_2dx7894b0affacefa_19
   + rho_predicate_2dx7894b0affacefa_19 <= 1003
 R580: y_19 + 1000 z_predicate_2dx7894b0affacefa_19
   + rho_predicate_2dx7894b0affacefa_19 >= 3
 R581: rho_||_2dx6fafc74611e76e89_19 - rho_predicate_2bx454ca952238e72db_19
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_19
   <= 1000
 R582: z_||_2dx6fafc74611e76e89_19 - z_predicate_2bx454ca952238e72db_19
   >= 0
 R583: - z_predicate_2bx454ca952238e72db_19
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_19 <= 0
 R584: rho_||_2dx6fafc74611e76e89_19 - rho_predicate_2dx19adc98cf842ca58_19
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_19
   <= 1000
 R585: z_||_2dx6fafc74611e76e89_19 - z_predicate_2dx19adc98cf842ca58_19
   >= 0
 R586: - z_predicate_2dx19adc98cf842ca58_19
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_19 <= 0
 R587: rho_||_2dx6fafc74611e76e89_19 - rho_predicate_2bx70ac945c4f28d9ed_19
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_19
   <= 1000
 R588: z_||_2dx6fafc74611e76e89_19 - z_predicate_2bx70ac945c4f28d9ed_19
   >= 0
 R589: - z_predicate_2bx70ac945c4f28d9ed_19
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_19 <= 0
 R590: rho_||_2dx6fafc74611e76e89_19 - rho_predicate_2dx7894b0affacefa_19
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_19 <= 1000
 R591: z_||_2dx6fafc74611e76e89_19 - z_predicate_2dx7894b0affacefa_19 >= 0
 R592: - z_predicate_2dx7894b0affacefa_19
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_19 <= 0
 R593: z_||_2dx6fafc74611e76e89_19 - z_predicate_2bx454ca952238e72db_19
   - z_predicate_2dx19adc98cf842ca58_19
   - z_predicate_2bx70ac945c4f28d9ed_19 - z_predicate_2dx7894b0affacefa_19
   <= 0
 R594: - z_||_2dx6fafc74611e76e89_19
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_19
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_19
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_19
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_19 >= 0
 R595: x_20 - 1000 z_predicate_2bx454ca952238e72db_20
   - rho_predicate_2bx454ca952238e72db_20 >= -1003
 R596: x_20 - 1000 z_predicate_2bx454ca952238e72db_20
   - rho_predicate_2bx454ca952238e72db_20 <= -3
 R597: x_20 + 1000 z_predicate_2dx19adc98cf842ca58_20
   + rho_predicate_2dx19adc98cf842ca58_20 <= 992
 R598: x_20 + 1000 z_predicate_2dx19adc98cf842ca58_20
   + rho_predicate_2dx19adc98cf842ca58_20 >= -8
 R599: y_20 - 1000 z_predicate_2bx70ac945c4f28d9ed_20
   - rho_predicate_2bx70ac945c4f28d9ed_20 >= -992
 R600: y_20 - 1000 z_predicate_2bx70ac945c4f28d9ed_20
   - rho_predicate_2bx70ac945c4f28d9ed_20 <= 8
 R601: y_20 + 1000 z_predicate_2dx7894b0affacefa_20
   + rho_predicate_2dx7894b0affacefa_20 <= 1003
 R602: y_20 + 1000 z_predicate_2dx7894b0affacefa_20
   + rho_predicate_2dx7894b0affacefa_20 >= 3
 R603: rho_||_2dx6fafc74611e76e89_20 - rho_predicate_2bx454ca952238e72db_20
   + 1000 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_20
   <= 1000
 R604: z_||_2dx6fafc74611e76e89_20 - z_predicate_2bx454ca952238e72db_20
   >= 0
 R605: - z_predicate_2bx454ca952238e72db_20
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_20 <= 0
 R606: rho_||_2dx6fafc74611e76e89_20 - rho_predicate_2dx19adc98cf842ca58_20
   + 1000 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_20
   <= 1000
 R607: z_||_2dx6fafc74611e76e89_20 - z_predicate_2dx19adc98cf842ca58_20
   >= 0
 R608: - z_predicate_2dx19adc98cf842ca58_20
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_20 <= 0
 R609: rho_||_2dx6fafc74611e76e89_20 - rho_predicate_2bx70ac945c4f28d9ed_20
   + 1000 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_20
   <= 1000
 R610: z_||_2dx6fafc74611e76e89_20 - z_predicate_2bx70ac945c4f28d9ed_20
   >= 0
 R611: - z_predicate_2bx70ac945c4f28d9ed_20
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_20 <= 0
 R612: rho_||_2dx6fafc74611e76e89_20 - rho_predicate_2dx7894b0affacefa_20
   + 1000 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_20 <= 1000
 R613: z_||_2dx6fafc74611e76e89_20 - z_predicate_2dx7894b0affacefa_20 >= 0
 R614: - z_predicate_2dx7894b0affacefa_20
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_20 <= 0
 R615: z_||_2dx6fafc74611e76e89_20 - z_predicate_2bx454ca952238e72db_20
   - z_predicate_2dx19adc98cf842ca58_20
   - z_predicate_2bx70ac945c4f28d9ed_20 - z_predicate_2dx7894b0affacefa_20
   <= 0
 R616: - z_||_2dx6fafc74611e76e89_20
   + zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_20
   + zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_20
   + zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_20
   + zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_20 >= 0
 R617: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_0 <= 0
 R618: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_0 <= 0
 R619: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_1 <= 0
 R620: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_1 <= 0
 R621: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_2 <= 0
 R622: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_2 <= 0
 R623: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_3 <= 0
 R624: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_3 <= 0
 R625: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_4 <= 0
 R626: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_4 <= 0
 R627: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_5 <= 0
 R628: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_5 <= 0
 R629: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_6 <= 0
 R630: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_6 <= 0
 R631: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_7 <= 0
 R632: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_7 <= 0
 R633: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_8 <= 0
 R634: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_8 <= 0
 R635: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_9 <= 0
 R636: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_9 <= 0
 R637: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_10 <= 0
 R638: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_10 <= 0
 R639: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_11 <= 0
 R640: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_11 <= 0
 R641: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_12 <= 0
 R642: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_12 <= 0
 R643: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_13 <= 0
 R644: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_13 <= 0
 R645: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_14 <= 0
 R646: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_14 <= 0
 R647: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_15 <= 0
 R648: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_15 <= 0
 R649: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_16 <= 0
 R650: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_16 <= 0
 R651: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_17 <= 0
 R652: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_17 <= 0
 R653: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_18 <= 0
 R654: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_18 <= 0
 R655: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_19 <= 0
 R656: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_19 <= 0
 R657: rho_G_2bx1fbb236baa38c772_0 - rho_||_2dx6fafc74611e76e89_20 <= 0
 R658: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_20 <= 0
 R659: z_G_2bx1fbb236baa38c772_0 - z_||_2dx6fafc74611e76e89_0
   - z_||_2dx6fafc74611e76e89_1 - z_||_2dx6fafc74611e76e89_2
   - z_||_2dx6fafc74611e76e89_3 - z_||_2dx6fafc74611e76e89_4
   - z_||_2dx6fafc74611e76e89_5 - z_||_2dx6fafc74611e76e89_6
   - z_||_2dx6fafc74611e76e89_7 - z_||_2dx6fafc74611e76e89_8
   - z_||_2dx6fafc74611e76e89_9 - z_||_2dx6fafc74611e76e89_10
   - z_||_2dx6fafc74611e76e89_11 - z_||_2dx6fafc74611e76e89_12
   - z_||_2dx6fafc74611e76e89_13 - z_||_2dx6fafc74611e76e89_14
   - z_||_2dx6fafc74611e76e89_15 - z_||_2dx6fafc74611e76e89_16
   - z_||_2dx6fafc74611e76e89_17 - z_||_2dx6fafc74611e76e89_18
   - z_||_2dx6fafc74611e76e89_19 - z_||_2dx6fafc74611e76e89_20 >= -20
 R660: x_0 - 1000 z_predicate_2dx22dd95ed78b4d217_0
   - rho_predicate_2dx22dd95ed78b4d217_0 >= -997
 R661: x_0 - 1000 z_predicate_2dx22dd95ed78b4d217_0
   - rho_predicate_2dx22dd95ed78b4d217_0 <= 3
 R662: x_0 + 1000 z_predicate_2dx5f1149c769efb91f_0
   + rho_predicate_2dx5f1149c769efb91f_0 <= 997
 R663: x_0 + 1000 z_predicate_2dx5f1149c769efb91f_0
   + rho_predicate_2dx5f1149c769efb91f_0 >= -3
 R664: y_0 - 1000 z_predicate_2bx955025411f5da14_0
   - rho_predicate_2bx955025411f5da14_0 >= -997
 R665: y_0 - 1000 z_predicate_2bx955025411f5da14_0
   - rho_predicate_2bx955025411f5da14_0 <= 3
 R666: y_0 + 1000 z_predicate_2bx7f11325f1c65baf6_0
   + rho_predicate_2bx7f11325f1c65baf6_0 <= 997
 R667: y_0 + 1000 z_predicate_2bx7f11325f1c65baf6_0
   + rho_predicate_2bx7f11325f1c65baf6_0 >= -3
 R668: rho_||_2bx22f6bca85b580f1b_0 - rho_predicate_2dx22dd95ed78b4d217_0
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_0 <= 1000
 R669: z_||_2bx22f6bca85b580f1b_0 - z_predicate_2dx22dd95ed78b4d217_0 >= 0
 R670: - z_predicate_2dx22dd95ed78b4d217_0
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_0 <= 0
 R671: rho_||_2bx22f6bca85b580f1b_0 - rho_predicate_2dx5f1149c769efb91f_0
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_0 <= 1000
 R672: z_||_2bx22f6bca85b580f1b_0 - z_predicate_2dx5f1149c769efb91f_0 >= 0
 R673: - z_predicate_2dx5f1149c769efb91f_0
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_0 <= 0
 R674: rho_||_2bx22f6bca85b580f1b_0 - rho_predicate_2bx955025411f5da14_0
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_0 <= 1000
 R675: z_||_2bx22f6bca85b580f1b_0 - z_predicate_2bx955025411f5da14_0 >= 0
 R676: - z_predicate_2bx955025411f5da14_0
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_0 <= 0
 R677: rho_||_2bx22f6bca85b580f1b_0 - rho_predicate_2bx7f11325f1c65baf6_0
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_0 <= 1000
 R678: z_||_2bx22f6bca85b580f1b_0 - z_predicate_2bx7f11325f1c65baf6_0 >= 0
 R679: - z_predicate_2bx7f11325f1c65baf6_0
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_0 <= 0
 R680: z_||_2bx22f6bca85b580f1b_0 - z_predicate_2dx22dd95ed78b4d217_0
   - z_predicate_2dx5f1149c769efb91f_0 - z_predicate_2bx955025411f5da14_0
   - z_predicate_2bx7f11325f1c65baf6_0 <= 0
 R681: - z_||_2bx22f6bca85b580f1b_0
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_0
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_0
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_0
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_0 >= 0
 R682: x_1 - 1000 z_predicate_2dx22dd95ed78b4d217_1
   - rho_predicate_2dx22dd95ed78b4d217_1 >= -997
 R683: x_1 - 1000 z_predicate_2dx22dd95ed78b4d217_1
   - rho_predicate_2dx22dd95ed78b4d217_1 <= 3
 R684: x_1 + 1000 z_predicate_2dx5f1149c769efb91f_1
   + rho_predicate_2dx5f1149c769efb91f_1 <= 997
 R685: x_1 + 1000 z_predicate_2dx5f1149c769efb91f_1
   + rho_predicate_2dx5f1149c769efb91f_1 >= -3
 R686: y_1 - 1000 z_predicate_2bx955025411f5da14_1
   - rho_predicate_2bx955025411f5da14_1 >= -997
 R687: y_1 - 1000 z_predicate_2bx955025411f5da14_1
   - rho_predicate_2bx955025411f5da14_1 <= 3
 R688: y_1 + 1000 z_predicate_2bx7f11325f1c65baf6_1
   + rho_predicate_2bx7f11325f1c65baf6_1 <= 997
 R689: y_1 + 1000 z_predicate_2bx7f11325f1c65baf6_1
   + rho_predicate_2bx7f11325f1c65baf6_1 >= -3
 R690: rho_||_2bx22f6bca85b580f1b_1 - rho_predicate_2dx22dd95ed78b4d217_1
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_1 <= 1000
 R691: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2dx22dd95ed78b4d217_1 >= 0
 R692: - z_predicate_2dx22dd95ed78b4d217_1
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_1 <= 0
 R693: rho_||_2bx22f6bca85b580f1b_1 - rho_predicate_2dx5f1149c769efb91f_1
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_1 <= 1000
 R694: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2dx5f1149c769efb91f_1 >= 0
 R695: - z_predicate_2dx5f1149c769efb91f_1
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_1 <= 0
 R696: rho_||_2bx22f6bca85b580f1b_1 - rho_predicate_2bx955025411f5da14_1
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_1 <= 1000
 R697: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2bx955025411f5da14_1 >= 0
 R698: - z_predicate_2bx955025411f5da14_1
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_1 <= 0
 R699: rho_||_2bx22f6bca85b580f1b_1 - rho_predicate_2bx7f11325f1c65baf6_1
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_1 <= 1000
 R700: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2bx7f11325f1c65baf6_1 >= 0
 R701: - z_predicate_2bx7f11325f1c65baf6_1
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_1 <= 0
 R702: z_||_2bx22f6bca85b580f1b_1 - z_predicate_2dx22dd95ed78b4d217_1
   - z_predicate_2dx5f1149c769efb91f_1 - z_predicate_2bx955025411f5da14_1
   - z_predicate_2bx7f11325f1c65baf6_1 <= 0
 R703: - z_||_2bx22f6bca85b580f1b_1
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_1
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_1
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_1
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_1 >= 0
 R704: x_2 - 1000 z_predicate_2dx22dd95ed78b4d217_2
   - rho_predicate_2dx22dd95ed78b4d217_2 >= -997
 R705: x_2 - 1000 z_predicate_2dx22dd95ed78b4d217_2
   - rho_predicate_2dx22dd95ed78b4d217_2 <= 3
 R706: x_2 + 1000 z_predicate_2dx5f1149c769efb91f_2
   + rho_predicate_2dx5f1149c769efb91f_2 <= 997
 R707: x_2 + 1000 z_predicate_2dx5f1149c769efb91f_2
   + rho_predicate_2dx5f1149c769efb91f_2 >= -3
 R708: y_2 - 1000 z_predicate_2bx955025411f5da14_2
   - rho_predicate_2bx955025411f5da14_2 >= -997
 R709: y_2 - 1000 z_predicate_2bx955025411f5da14_2
   - rho_predicate_2bx955025411f5da14_2 <= 3
 R710: y_2 + 1000 z_predicate_2bx7f11325f1c65baf6_2
   + rho_predicate_2bx7f11325f1c65baf6_2 <= 997
 R711: y_2 + 1000 z_predicate_2bx7f11325f1c65baf6_2
   + rho_predicate_2bx7f11325f1c65baf6_2 >= -3
 R712: rho_||_2bx22f6bca85b580f1b_2 - rho_predicate_2dx22dd95ed78b4d217_2
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_2 <= 1000
 R713: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2dx22dd95ed78b4d217_2 >= 0
 R714: - z_predicate_2dx22dd95ed78b4d217_2
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_2 <= 0
 R715: rho_||_2bx22f6bca85b580f1b_2 - rho_predicate_2dx5f1149c769efb91f_2
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_2 <= 1000
 R716: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2dx5f1149c769efb91f_2 >= 0
 R717: - z_predicate_2dx5f1149c769efb91f_2
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_2 <= 0
 R718: rho_||_2bx22f6bca85b580f1b_2 - rho_predicate_2bx955025411f5da14_2
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_2 <= 1000
 R719: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2bx955025411f5da14_2 >= 0
 R720: - z_predicate_2bx955025411f5da14_2
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_2 <= 0
 R721: rho_||_2bx22f6bca85b580f1b_2 - rho_predicate_2bx7f11325f1c65baf6_2
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_2 <= 1000
 R722: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2bx7f11325f1c65baf6_2 >= 0
 R723: - z_predicate_2bx7f11325f1c65baf6_2
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_2 <= 0
 R724: z_||_2bx22f6bca85b580f1b_2 - z_predicate_2dx22dd95ed78b4d217_2
   - z_predicate_2dx5f1149c769efb91f_2 - z_predicate_2bx955025411f5da14_2
   - z_predicate_2bx7f11325f1c65baf6_2 <= 0
 R725: - z_||_2bx22f6bca85b580f1b_2
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_2
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_2
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_2
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_2 >= 0
 R726: x_3 - 1000 z_predicate_2dx22dd95ed78b4d217_3
   - rho_predicate_2dx22dd95ed78b4d217_3 >= -997
 R727: x_3 - 1000 z_predicate_2dx22dd95ed78b4d217_3
   - rho_predicate_2dx22dd95ed78b4d217_3 <= 3
 R728: x_3 + 1000 z_predicate_2dx5f1149c769efb91f_3
   + rho_predicate_2dx5f1149c769efb91f_3 <= 997
 R729: x_3 + 1000 z_predicate_2dx5f1149c769efb91f_3
   + rho_predicate_2dx5f1149c769efb91f_3 >= -3
 R730: y_3 - 1000 z_predicate_2bx955025411f5da14_3
   - rho_predicate_2bx955025411f5da14_3 >= -997
 R731: y_3 - 1000 z_predicate_2bx955025411f5da14_3
   - rho_predicate_2bx955025411f5da14_3 <= 3
 R732: y_3 + 1000 z_predicate_2bx7f11325f1c65baf6_3
   + rho_predicate_2bx7f11325f1c65baf6_3 <= 997
 R733: y_3 + 1000 z_predicate_2bx7f11325f1c65baf6_3
   + rho_predicate_2bx7f11325f1c65baf6_3 >= -3
 R734: rho_||_2bx22f6bca85b580f1b_3 - rho_predicate_2dx22dd95ed78b4d217_3
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_3 <= 1000
 R735: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2dx22dd95ed78b4d217_3 >= 0
 R736: - z_predicate_2dx22dd95ed78b4d217_3
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_3 <= 0
 R737: rho_||_2bx22f6bca85b580f1b_3 - rho_predicate_2dx5f1149c769efb91f_3
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_3 <= 1000
 R738: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2dx5f1149c769efb91f_3 >= 0
 R739: - z_predicate_2dx5f1149c769efb91f_3
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_3 <= 0
 R740: rho_||_2bx22f6bca85b580f1b_3 - rho_predicate_2bx955025411f5da14_3
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_3 <= 1000
 R741: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2bx955025411f5da14_3 >= 0
 R742: - z_predicate_2bx955025411f5da14_3
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_3 <= 0
 R743: rho_||_2bx22f6bca85b580f1b_3 - rho_predicate_2bx7f11325f1c65baf6_3
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_3 <= 1000
 R744: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2bx7f11325f1c65baf6_3 >= 0
 R745: - z_predicate_2bx7f11325f1c65baf6_3
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_3 <= 0
 R746: z_||_2bx22f6bca85b580f1b_3 - z_predicate_2dx22dd95ed78b4d217_3
   - z_predicate_2dx5f1149c769efb91f_3 - z_predicate_2bx955025411f5da14_3
   - z_predicate_2bx7f11325f1c65baf6_3 <= 0
 R747: - z_||_2bx22f6bca85b580f1b_3
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_3
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_3
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_3
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_3 >= 0
 R748: x_4 - 1000 z_predicate_2dx22dd95ed78b4d217_4
   - rho_predicate_2dx22dd95ed78b4d217_4 >= -997
 R749: x_4 - 1000 z_predicate_2dx22dd95ed78b4d217_4
   - rho_predicate_2dx22dd95ed78b4d217_4 <= 3
 R750: x_4 + 1000 z_predicate_2dx5f1149c769efb91f_4
   + rho_predicate_2dx5f1149c769efb91f_4 <= 997
 R751: x_4 + 1000 z_predicate_2dx5f1149c769efb91f_4
   + rho_predicate_2dx5f1149c769efb91f_4 >= -3
 R752: y_4 - 1000 z_predicate_2bx955025411f5da14_4
   - rho_predicate_2bx955025411f5da14_4 >= -997
 R753: y_4 - 1000 z_predicate_2bx955025411f5da14_4
   - rho_predicate_2bx955025411f5da14_4 <= 3
 R754: y_4 + 1000 z_predicate_2bx7f11325f1c65baf6_4
   + rho_predicate_2bx7f11325f1c65baf6_4 <= 997
 R755: y_4 + 1000 z_predicate_2bx7f11325f1c65baf6_4
   + rho_predicate_2bx7f11325f1c65baf6_4 >= -3
 R756: rho_||_2bx22f6bca85b580f1b_4 - rho_predicate_2dx22dd95ed78b4d217_4
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_4 <= 1000
 R757: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2dx22dd95ed78b4d217_4 >= 0
 R758: - z_predicate_2dx22dd95ed78b4d217_4
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_4 <= 0
 R759: rho_||_2bx22f6bca85b580f1b_4 - rho_predicate_2dx5f1149c769efb91f_4
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_4 <= 1000
 R760: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2dx5f1149c769efb91f_4 >= 0
 R761: - z_predicate_2dx5f1149c769efb91f_4
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_4 <= 0
 R762: rho_||_2bx22f6bca85b580f1b_4 - rho_predicate_2bx955025411f5da14_4
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_4 <= 1000
 R763: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2bx955025411f5da14_4 >= 0
 R764: - z_predicate_2bx955025411f5da14_4
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_4 <= 0
 R765: rho_||_2bx22f6bca85b580f1b_4 - rho_predicate_2bx7f11325f1c65baf6_4
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_4 <= 1000
 R766: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2bx7f11325f1c65baf6_4 >= 0
 R767: - z_predicate_2bx7f11325f1c65baf6_4
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_4 <= 0
 R768: z_||_2bx22f6bca85b580f1b_4 - z_predicate_2dx22dd95ed78b4d217_4
   - z_predicate_2dx5f1149c769efb91f_4 - z_predicate_2bx955025411f5da14_4
   - z_predicate_2bx7f11325f1c65baf6_4 <= 0
 R769: - z_||_2bx22f6bca85b580f1b_4
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_4
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_4
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_4
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_4 >= 0
 R770: x_5 - 1000 z_predicate_2dx22dd95ed78b4d217_5
   - rho_predicate_2dx22dd95ed78b4d217_5 >= -997
 R771: x_5 - 1000 z_predicate_2dx22dd95ed78b4d217_5
   - rho_predicate_2dx22dd95ed78b4d217_5 <= 3
 R772: x_5 + 1000 z_predicate_2dx5f1149c769efb91f_5
   + rho_predicate_2dx5f1149c769efb91f_5 <= 997
 R773: x_5 + 1000 z_predicate_2dx5f1149c769efb91f_5
   + rho_predicate_2dx5f1149c769efb91f_5 >= -3
 R774: y_5 - 1000 z_predicate_2bx955025411f5da14_5
   - rho_predicate_2bx955025411f5da14_5 >= -997
 R775: y_5 - 1000 z_predicate_2bx955025411f5da14_5
   - rho_predicate_2bx955025411f5da14_5 <= 3
 R776: y_5 + 1000 z_predicate_2bx7f11325f1c65baf6_5
   + rho_predicate_2bx7f11325f1c65baf6_5 <= 997
 R777: y_5 + 1000 z_predicate_2bx7f11325f1c65baf6_5
   + rho_predicate_2bx7f11325f1c65baf6_5 >= -3
 R778: rho_||_2bx22f6bca85b580f1b_5 - rho_predicate_2dx22dd95ed78b4d217_5
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_5 <= 1000
 R779: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2dx22dd95ed78b4d217_5 >= 0
 R780: - z_predicate_2dx22dd95ed78b4d217_5
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_5 <= 0
 R781: rho_||_2bx22f6bca85b580f1b_5 - rho_predicate_2dx5f1149c769efb91f_5
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_5 <= 1000
 R782: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2dx5f1149c769efb91f_5 >= 0
 R783: - z_predicate_2dx5f1149c769efb91f_5
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_5 <= 0
 R784: rho_||_2bx22f6bca85b580f1b_5 - rho_predicate_2bx955025411f5da14_5
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_5 <= 1000
 R785: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2bx955025411f5da14_5 >= 0
 R786: - z_predicate_2bx955025411f5da14_5
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_5 <= 0
 R787: rho_||_2bx22f6bca85b580f1b_5 - rho_predicate_2bx7f11325f1c65baf6_5
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_5 <= 1000
 R788: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2bx7f11325f1c65baf6_5 >= 0
 R789: - z_predicate_2bx7f11325f1c65baf6_5
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_5 <= 0
 R790: z_||_2bx22f6bca85b580f1b_5 - z_predicate_2dx22dd95ed78b4d217_5
   - z_predicate_2dx5f1149c769efb91f_5 - z_predicate_2bx955025411f5da14_5
   - z_predicate_2bx7f11325f1c65baf6_5 <= 0
 R791: - z_||_2bx22f6bca85b580f1b_5
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_5
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_5
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_5
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_5 >= 0
 R792: x_6 - 1000 z_predicate_2dx22dd95ed78b4d217_6
   - rho_predicate_2dx22dd95ed78b4d217_6 >= -997
 R793: x_6 - 1000 z_predicate_2dx22dd95ed78b4d217_6
   - rho_predicate_2dx22dd95ed78b4d217_6 <= 3
 R794: x_6 + 1000 z_predicate_2dx5f1149c769efb91f_6
   + rho_predicate_2dx5f1149c769efb91f_6 <= 997
 R795: x_6 + 1000 z_predicate_2dx5f1149c769efb91f_6
   + rho_predicate_2dx5f1149c769efb91f_6 >= -3
 R796: y_6 - 1000 z_predicate_2bx955025411f5da14_6
   - rho_predicate_2bx955025411f5da14_6 >= -997
 R797: y_6 - 1000 z_predicate_2bx955025411f5da14_6
   - rho_predicate_2bx955025411f5da14_6 <= 3
 R798: y_6 + 1000 z_predicate_2bx7f11325f1c65baf6_6
   + rho_predicate_2bx7f11325f1c65baf6_6 <= 997
 R799: y_6 + 1000 z_predicate_2bx7f11325f1c65baf6_6
   + rho_predicate_2bx7f11325f1c65baf6_6 >= -3
 R800: rho_||_2bx22f6bca85b580f1b_6 - rho_predicate_2dx22dd95ed78b4d217_6
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_6 <= 1000
 R801: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2dx22dd95ed78b4d217_6 >= 0
 R802: - z_predicate_2dx22dd95ed78b4d217_6
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_6 <= 0
 R803: rho_||_2bx22f6bca85b580f1b_6 - rho_predicate_2dx5f1149c769efb91f_6
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_6 <= 1000
 R804: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2dx5f1149c769efb91f_6 >= 0
 R805: - z_predicate_2dx5f1149c769efb91f_6
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_6 <= 0
 R806: rho_||_2bx22f6bca85b580f1b_6 - rho_predicate_2bx955025411f5da14_6
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_6 <= 1000
 R807: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2bx955025411f5da14_6 >= 0
 R808: - z_predicate_2bx955025411f5da14_6
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_6 <= 0
 R809: rho_||_2bx22f6bca85b580f1b_6 - rho_predicate_2bx7f11325f1c65baf6_6
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_6 <= 1000
 R810: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2bx7f11325f1c65baf6_6 >= 0
 R811: - z_predicate_2bx7f11325f1c65baf6_6
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_6 <= 0
 R812: z_||_2bx22f6bca85b580f1b_6 - z_predicate_2dx22dd95ed78b4d217_6
   - z_predicate_2dx5f1149c769efb91f_6 - z_predicate_2bx955025411f5da14_6
   - z_predicate_2bx7f11325f1c65baf6_6 <= 0
 R813: - z_||_2bx22f6bca85b580f1b_6
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_6
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_6
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_6
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_6 >= 0
 R814: x_7 - 1000 z_predicate_2dx22dd95ed78b4d217_7
   - rho_predicate_2dx22dd95ed78b4d217_7 >= -997
 R815: x_7 - 1000 z_predicate_2dx22dd95ed78b4d217_7
   - rho_predicate_2dx22dd95ed78b4d217_7 <= 3
 R816: x_7 + 1000 z_predicate_2dx5f1149c769efb91f_7
   + rho_predicate_2dx5f1149c769efb91f_7 <= 997
 R817: x_7 + 1000 z_predicate_2dx5f1149c769efb91f_7
   + rho_predicate_2dx5f1149c769efb91f_7 >= -3
 R818: y_7 - 1000 z_predicate_2bx955025411f5da14_7
   - rho_predicate_2bx955025411f5da14_7 >= -997
 R819: y_7 - 1000 z_predicate_2bx955025411f5da14_7
   - rho_predicate_2bx955025411f5da14_7 <= 3
 R820: y_7 + 1000 z_predicate_2bx7f11325f1c65baf6_7
   + rho_predicate_2bx7f11325f1c65baf6_7 <= 997
 R821: y_7 + 1000 z_predicate_2bx7f11325f1c65baf6_7
   + rho_predicate_2bx7f11325f1c65baf6_7 >= -3
 R822: rho_||_2bx22f6bca85b580f1b_7 - rho_predicate_2dx22dd95ed78b4d217_7
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_7 <= 1000
 R823: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2dx22dd95ed78b4d217_7 >= 0
 R824: - z_predicate_2dx22dd95ed78b4d217_7
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_7 <= 0
 R825: rho_||_2bx22f6bca85b580f1b_7 - rho_predicate_2dx5f1149c769efb91f_7
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_7 <= 1000
 R826: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2dx5f1149c769efb91f_7 >= 0
 R827: - z_predicate_2dx5f1149c769efb91f_7
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_7 <= 0
 R828: rho_||_2bx22f6bca85b580f1b_7 - rho_predicate_2bx955025411f5da14_7
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_7 <= 1000
 R829: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2bx955025411f5da14_7 >= 0
 R830: - z_predicate_2bx955025411f5da14_7
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_7 <= 0
 R831: rho_||_2bx22f6bca85b580f1b_7 - rho_predicate_2bx7f11325f1c65baf6_7
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_7 <= 1000
 R832: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2bx7f11325f1c65baf6_7 >= 0
 R833: - z_predicate_2bx7f11325f1c65baf6_7
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_7 <= 0
 R834: z_||_2bx22f6bca85b580f1b_7 - z_predicate_2dx22dd95ed78b4d217_7
   - z_predicate_2dx5f1149c769efb91f_7 - z_predicate_2bx955025411f5da14_7
   - z_predicate_2bx7f11325f1c65baf6_7 <= 0
 R835: - z_||_2bx22f6bca85b580f1b_7
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_7
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_7
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_7
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_7 >= 0
 R836: x_8 - 1000 z_predicate_2dx22dd95ed78b4d217_8
   - rho_predicate_2dx22dd95ed78b4d217_8 >= -997
 R837: x_8 - 1000 z_predicate_2dx22dd95ed78b4d217_8
   - rho_predicate_2dx22dd95ed78b4d217_8 <= 3
 R838: x_8 + 1000 z_predicate_2dx5f1149c769efb91f_8
   + rho_predicate_2dx5f1149c769efb91f_8 <= 997
 R839: x_8 + 1000 z_predicate_2dx5f1149c769efb91f_8
   + rho_predicate_2dx5f1149c769efb91f_8 >= -3
 R840: y_8 - 1000 z_predicate_2bx955025411f5da14_8
   - rho_predicate_2bx955025411f5da14_8 >= -997
 R841: y_8 - 1000 z_predicate_2bx955025411f5da14_8
   - rho_predicate_2bx955025411f5da14_8 <= 3
 R842: y_8 + 1000 z_predicate_2bx7f11325f1c65baf6_8
   + rho_predicate_2bx7f11325f1c65baf6_8 <= 997
 R843: y_8 + 1000 z_predicate_2bx7f11325f1c65baf6_8
   + rho_predicate_2bx7f11325f1c65baf6_8 >= -3
 R844: rho_||_2bx22f6bca85b580f1b_8 - rho_predicate_2dx22dd95ed78b4d217_8
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_8 <= 1000
 R845: z_||_2bx22f6bca85b580f1b_8 - z_predicate_2dx22dd95ed78b4d217_8 >= 0
 R846: - z_predicate_2dx22dd95ed78b4d217_8
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_8 <= 0
 R847: rho_||_2bx22f6bca85b580f1b_8 - rho_predicate_2dx5f1149c769efb91f_8
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_8 <= 1000
 R848: z_||_2bx22f6bca85b580f1b_8 - z_predicate_2dx5f1149c769efb91f_8 >= 0
 R849: - z_predicate_2dx5f1149c769efb91f_8
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_8 <= 0
 R850: rho_||_2bx22f6bca85b580f1b_8 - rho_predicate_2bx955025411f5da14_8
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_8 <= 1000
 R851: z_||_2bx22f6bca85b580f1b_8 - z_predicate_2bx955025411f5da14_8 >= 0
 R852: - z_predicate_2bx955025411f5da14_8
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_8 <= 0
 R853: rho_||_2bx22f6bca85b580f1b_8 - rho_predicate_2bx7f11325f1c65baf6_8
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_8 <= 1000
 R854: z_||_2bx22f6bca85b580f1b_8 - z_predicate_2bx7f11325f1c65baf6_8 >= 0
 R855: - z_predicate_2bx7f11325f1c65baf6_8
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_8 <= 0
 R856: z_||_2bx22f6bca85b580f1b_8 - z_predicate_2dx22dd95ed78b4d217_8
   - z_predicate_2dx5f1149c769efb91f_8 - z_predicate_2bx955025411f5da14_8
   - z_predicate_2bx7f11325f1c65baf6_8 <= 0
 R857: - z_||_2bx22f6bca85b580f1b_8
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_8
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_8
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_8
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_8 >= 0
 R858: x_9 - 1000 z_predicate_2dx22dd95ed78b4d217_9
   - rho_predicate_2dx22dd95ed78b4d217_9 >= -997
 R859: x_9 - 1000 z_predicate_2dx22dd95ed78b4d217_9
   - rho_predicate_2dx22dd95ed78b4d217_9 <= 3
 R860: x_9 + 1000 z_predicate_2dx5f1149c769efb91f_9
   + rho_predicate_2dx5f1149c769efb91f_9 <= 997
 R861: x_9 + 1000 z_predicate_2dx5f1149c769efb91f_9
   + rho_predicate_2dx5f1149c769efb91f_9 >= -3
 R862: y_9 - 1000 z_predicate_2bx955025411f5da14_9
   - rho_predicate_2bx955025411f5da14_9 >= -997
 R863: y_9 - 1000 z_predicate_2bx955025411f5da14_9
   - rho_predicate_2bx955025411f5da14_9 <= 3
 R864: y_9 + 1000 z_predicate_2bx7f11325f1c65baf6_9
   + rho_predicate_2bx7f11325f1c65baf6_9 <= 997
 R865: y_9 + 1000 z_predicate_2bx7f11325f1c65baf6_9
   + rho_predicate_2bx7f11325f1c65baf6_9 >= -3
 R866: rho_||_2bx22f6bca85b580f1b_9 - rho_predicate_2dx22dd95ed78b4d217_9
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_9 <= 1000
 R867: z_||_2bx22f6bca85b580f1b_9 - z_predicate_2dx22dd95ed78b4d217_9 >= 0
 R868: - z_predicate_2dx22dd95ed78b4d217_9
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_9 <= 0
 R869: rho_||_2bx22f6bca85b580f1b_9 - rho_predicate_2dx5f1149c769efb91f_9
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_9 <= 1000
 R870: z_||_2bx22f6bca85b580f1b_9 - z_predicate_2dx5f1149c769efb91f_9 >= 0
 R871: - z_predicate_2dx5f1149c769efb91f_9
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_9 <= 0
 R872: rho_||_2bx22f6bca85b580f1b_9 - rho_predicate_2bx955025411f5da14_9
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_9 <= 1000
 R873: z_||_2bx22f6bca85b580f1b_9 - z_predicate_2bx955025411f5da14_9 >= 0
 R874: - z_predicate_2bx955025411f5da14_9
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_9 <= 0
 R875: rho_||_2bx22f6bca85b580f1b_9 - rho_predicate_2bx7f11325f1c65baf6_9
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_9 <= 1000
 R876: z_||_2bx22f6bca85b580f1b_9 - z_predicate_2bx7f11325f1c65baf6_9 >= 0
 R877: - z_predicate_2bx7f11325f1c65baf6_9
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_9 <= 0
 R878: z_||_2bx22f6bca85b580f1b_9 - z_predicate_2dx22dd95ed78b4d217_9
   - z_predicate_2dx5f1149c769efb91f_9 - z_predicate_2bx955025411f5da14_9
   - z_predicate_2bx7f11325f1c65baf6_9 <= 0
 R879: - z_||_2bx22f6bca85b580f1b_9
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_9
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_9
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_9
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_9 >= 0
 R880: x_10 - 1000 z_predicate_2dx22dd95ed78b4d217_10
   - rho_predicate_2dx22dd95ed78b4d217_10 >= -997
 R881: x_10 - 1000 z_predicate_2dx22dd95ed78b4d217_10
   - rho_predicate_2dx22dd95ed78b4d217_10 <= 3
 R882: x_10 + 1000 z_predicate_2dx5f1149c769efb91f_10
   + rho_predicate_2dx5f1149c769efb91f_10 <= 997
 R883: x_10 + 1000 z_predicate_2dx5f1149c769efb91f_10
   + rho_predicate_2dx5f1149c769efb91f_10 >= -3
 R884: y_10 - 1000 z_predicate_2bx955025411f5da14_10
   - rho_predicate_2bx955025411f5da14_10 >= -997
 R885: y_10 - 1000 z_predicate_2bx955025411f5da14_10
   - rho_predicate_2bx955025411f5da14_10 <= 3
 R886: y_10 + 1000 z_predicate_2bx7f11325f1c65baf6_10
   + rho_predicate_2bx7f11325f1c65baf6_10 <= 997
 R887: y_10 + 1000 z_predicate_2bx7f11325f1c65baf6_10
   + rho_predicate_2bx7f11325f1c65baf6_10 >= -3
 R888: rho_||_2bx22f6bca85b580f1b_10 - rho_predicate_2dx22dd95ed78b4d217_10
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_10
   <= 1000
 R889: z_||_2bx22f6bca85b580f1b_10 - z_predicate_2dx22dd95ed78b4d217_10
   >= 0
 R890: - z_predicate_2dx22dd95ed78b4d217_10
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_10 <= 0
 R891: rho_||_2bx22f6bca85b580f1b_10 - rho_predicate_2dx5f1149c769efb91f_10
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_10
   <= 1000
 R892: z_||_2bx22f6bca85b580f1b_10 - z_predicate_2dx5f1149c769efb91f_10
   >= 0
 R893: - z_predicate_2dx5f1149c769efb91f_10
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_10 <= 0
 R894: rho_||_2bx22f6bca85b580f1b_10 - rho_predicate_2bx955025411f5da14_10
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_10 <= 1000
 R895: z_||_2bx22f6bca85b580f1b_10 - z_predicate_2bx955025411f5da14_10
   >= 0
 R896: - z_predicate_2bx955025411f5da14_10
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_10 <= 0
 R897: rho_||_2bx22f6bca85b580f1b_10 - rho_predicate_2bx7f11325f1c65baf6_10
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_10
   <= 1000
 R898: z_||_2bx22f6bca85b580f1b_10 - z_predicate_2bx7f11325f1c65baf6_10
   >= 0
 R899: - z_predicate_2bx7f11325f1c65baf6_10
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_10 <= 0
 R900: z_||_2bx22f6bca85b580f1b_10 - z_predicate_2dx22dd95ed78b4d217_10
   - z_predicate_2dx5f1149c769efb91f_10 - z_predicate_2bx955025411f5da14_10
   - z_predicate_2bx7f11325f1c65baf6_10 <= 0
 R901: - z_||_2bx22f6bca85b580f1b_10
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_10
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_10
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_10
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_10 >= 0
 R902: x_11 - 1000 z_predicate_2dx22dd95ed78b4d217_11
   - rho_predicate_2dx22dd95ed78b4d217_11 >= -997
 R903: x_11 - 1000 z_predicate_2dx22dd95ed78b4d217_11
   - rho_predicate_2dx22dd95ed78b4d217_11 <= 3
 R904: x_11 + 1000 z_predicate_2dx5f1149c769efb91f_11
   + rho_predicate_2dx5f1149c769efb91f_11 <= 997
 R905: x_11 + 1000 z_predicate_2dx5f1149c769efb91f_11
   + rho_predicate_2dx5f1149c769efb91f_11 >= -3
 R906: y_11 - 1000 z_predicate_2bx955025411f5da14_11
   - rho_predicate_2bx955025411f5da14_11 >= -997
 R907: y_11 - 1000 z_predicate_2bx955025411f5da14_11
   - rho_predicate_2bx955025411f5da14_11 <= 3
 R908: y_11 + 1000 z_predicate_2bx7f11325f1c65baf6_11
   + rho_predicate_2bx7f11325f1c65baf6_11 <= 997
 R909: y_11 + 1000 z_predicate_2bx7f11325f1c65baf6_11
   + rho_predicate_2bx7f11325f1c65baf6_11 >= -3
 R910: rho_||_2bx22f6bca85b580f1b_11 - rho_predicate_2dx22dd95ed78b4d217_11
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_11
   <= 1000
 R911: z_||_2bx22f6bca85b580f1b_11 - z_predicate_2dx22dd95ed78b4d217_11
   >= 0
 R912: - z_predicate_2dx22dd95ed78b4d217_11
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_11 <= 0
 R913: rho_||_2bx22f6bca85b580f1b_11 - rho_predicate_2dx5f1149c769efb91f_11
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_11
   <= 1000
 R914: z_||_2bx22f6bca85b580f1b_11 - z_predicate_2dx5f1149c769efb91f_11
   >= 0
 R915: - z_predicate_2dx5f1149c769efb91f_11
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_11 <= 0
 R916: rho_||_2bx22f6bca85b580f1b_11 - rho_predicate_2bx955025411f5da14_11
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_11 <= 1000
 R917: z_||_2bx22f6bca85b580f1b_11 - z_predicate_2bx955025411f5da14_11
   >= 0
 R918: - z_predicate_2bx955025411f5da14_11
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_11 <= 0
 R919: rho_||_2bx22f6bca85b580f1b_11 - rho_predicate_2bx7f11325f1c65baf6_11
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_11
   <= 1000
 R920: z_||_2bx22f6bca85b580f1b_11 - z_predicate_2bx7f11325f1c65baf6_11
   >= 0
 R921: - z_predicate_2bx7f11325f1c65baf6_11
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_11 <= 0
 R922: z_||_2bx22f6bca85b580f1b_11 - z_predicate_2dx22dd95ed78b4d217_11
   - z_predicate_2dx5f1149c769efb91f_11 - z_predicate_2bx955025411f5da14_11
   - z_predicate_2bx7f11325f1c65baf6_11 <= 0
 R923: - z_||_2bx22f6bca85b580f1b_11
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_11
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_11
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_11
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_11 >= 0
 R924: x_12 - 1000 z_predicate_2dx22dd95ed78b4d217_12
   - rho_predicate_2dx22dd95ed78b4d217_12 >= -997
 R925: x_12 - 1000 z_predicate_2dx22dd95ed78b4d217_12
   - rho_predicate_2dx22dd95ed78b4d217_12 <= 3
 R926: x_12 + 1000 z_predicate_2dx5f1149c769efb91f_12
   + rho_predicate_2dx5f1149c769efb91f_12 <= 997
 R927: x_12 + 1000 z_predicate_2dx5f1149c769efb91f_12
   + rho_predicate_2dx5f1149c769efb91f_12 >= -3
 R928: y_12 - 1000 z_predicate_2bx955025411f5da14_12
   - rho_predicate_2bx955025411f5da14_12 >= -997
 R929: y_12 - 1000 z_predicate_2bx955025411f5da14_12
   - rho_predicate_2bx955025411f5da14_12 <= 3
 R930: y_12 + 1000 z_predicate_2bx7f11325f1c65baf6_12
   + rho_predicate_2bx7f11325f1c65baf6_12 <= 997
 R931: y_12 + 1000 z_predicate_2bx7f11325f1c65baf6_12
   + rho_predicate_2bx7f11325f1c65baf6_12 >= -3
 R932: rho_||_2bx22f6bca85b580f1b_12 - rho_predicate_2dx22dd95ed78b4d217_12
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_12
   <= 1000
 R933: z_||_2bx22f6bca85b580f1b_12 - z_predicate_2dx22dd95ed78b4d217_12
   >= 0
 R934: - z_predicate_2dx22dd95ed78b4d217_12
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_12 <= 0
 R935: rho_||_2bx22f6bca85b580f1b_12 - rho_predicate_2dx5f1149c769efb91f_12
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_12
   <= 1000
 R936: z_||_2bx22f6bca85b580f1b_12 - z_predicate_2dx5f1149c769efb91f_12
   >= 0
 R937: - z_predicate_2dx5f1149c769efb91f_12
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_12 <= 0
 R938: rho_||_2bx22f6bca85b580f1b_12 - rho_predicate_2bx955025411f5da14_12
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_12 <= 1000
 R939: z_||_2bx22f6bca85b580f1b_12 - z_predicate_2bx955025411f5da14_12
   >= 0
 R940: - z_predicate_2bx955025411f5da14_12
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_12 <= 0
 R941: rho_||_2bx22f6bca85b580f1b_12 - rho_predicate_2bx7f11325f1c65baf6_12
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_12
   <= 1000
 R942: z_||_2bx22f6bca85b580f1b_12 - z_predicate_2bx7f11325f1c65baf6_12
   >= 0
 R943: - z_predicate_2bx7f11325f1c65baf6_12
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_12 <= 0
 R944: z_||_2bx22f6bca85b580f1b_12 - z_predicate_2dx22dd95ed78b4d217_12
   - z_predicate_2dx5f1149c769efb91f_12 - z_predicate_2bx955025411f5da14_12
   - z_predicate_2bx7f11325f1c65baf6_12 <= 0
 R945: - z_||_2bx22f6bca85b580f1b_12
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_12
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_12
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_12
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_12 >= 0
 R946: x_13 - 1000 z_predicate_2dx22dd95ed78b4d217_13
   - rho_predicate_2dx22dd95ed78b4d217_13 >= -997
 R947: x_13 - 1000 z_predicate_2dx22dd95ed78b4d217_13
   - rho_predicate_2dx22dd95ed78b4d217_13 <= 3
 R948: x_13 + 1000 z_predicate_2dx5f1149c769efb91f_13
   + rho_predicate_2dx5f1149c769efb91f_13 <= 997
 R949: x_13 + 1000 z_predicate_2dx5f1149c769efb91f_13
   + rho_predicate_2dx5f1149c769efb91f_13 >= -3
 R950: y_13 - 1000 z_predicate_2bx955025411f5da14_13
   - rho_predicate_2bx955025411f5da14_13 >= -997
 R951: y_13 - 1000 z_predicate_2bx955025411f5da14_13
   - rho_predicate_2bx955025411f5da14_13 <= 3
 R952: y_13 + 1000 z_predicate_2bx7f11325f1c65baf6_13
   + rho_predicate_2bx7f11325f1c65baf6_13 <= 997
 R953: y_13 + 1000 z_predicate_2bx7f11325f1c65baf6_13
   + rho_predicate_2bx7f11325f1c65baf6_13 >= -3
 R954: rho_||_2bx22f6bca85b580f1b_13 - rho_predicate_2dx22dd95ed78b4d217_13
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_13
   <= 1000
 R955: z_||_2bx22f6bca85b580f1b_13 - z_predicate_2dx22dd95ed78b4d217_13
   >= 0
 R956: - z_predicate_2dx22dd95ed78b4d217_13
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_13 <= 0
 R957: rho_||_2bx22f6bca85b580f1b_13 - rho_predicate_2dx5f1149c769efb91f_13
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_13
   <= 1000
 R958: z_||_2bx22f6bca85b580f1b_13 - z_predicate_2dx5f1149c769efb91f_13
   >= 0
 R959: - z_predicate_2dx5f1149c769efb91f_13
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_13 <= 0
 R960: rho_||_2bx22f6bca85b580f1b_13 - rho_predicate_2bx955025411f5da14_13
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_13 <= 1000
 R961: z_||_2bx22f6bca85b580f1b_13 - z_predicate_2bx955025411f5da14_13
   >= 0
 R962: - z_predicate_2bx955025411f5da14_13
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_13 <= 0
 R963: rho_||_2bx22f6bca85b580f1b_13 - rho_predicate_2bx7f11325f1c65baf6_13
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_13
   <= 1000
 R964: z_||_2bx22f6bca85b580f1b_13 - z_predicate_2bx7f11325f1c65baf6_13
   >= 0
 R965: - z_predicate_2bx7f11325f1c65baf6_13
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_13 <= 0
 R966: z_||_2bx22f6bca85b580f1b_13 - z_predicate_2dx22dd95ed78b4d217_13
   - z_predicate_2dx5f1149c769efb91f_13 - z_predicate_2bx955025411f5da14_13
   - z_predicate_2bx7f11325f1c65baf6_13 <= 0
 R967: - z_||_2bx22f6bca85b580f1b_13
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_13
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_13
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_13
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_13 >= 0
 R968: x_14 - 1000 z_predicate_2dx22dd95ed78b4d217_14
   - rho_predicate_2dx22dd95ed78b4d217_14 >= -997
 R969: x_14 - 1000 z_predicate_2dx22dd95ed78b4d217_14
   - rho_predicate_2dx22dd95ed78b4d217_14 <= 3
 R970: x_14 + 1000 z_predicate_2dx5f1149c769efb91f_14
   + rho_predicate_2dx5f1149c769efb91f_14 <= 997
 R971: x_14 + 1000 z_predicate_2dx5f1149c769efb91f_14
   + rho_predicate_2dx5f1149c769efb91f_14 >= -3
 R972: y_14 - 1000 z_predicate_2bx955025411f5da14_14
   - rho_predicate_2bx955025411f5da14_14 >= -997
 R973: y_14 - 1000 z_predicate_2bx955025411f5da14_14
   - rho_predicate_2bx955025411f5da14_14 <= 3
 R974: y_14 + 1000 z_predicate_2bx7f11325f1c65baf6_14
   + rho_predicate_2bx7f11325f1c65baf6_14 <= 997
 R975: y_14 + 1000 z_predicate_2bx7f11325f1c65baf6_14
   + rho_predicate_2bx7f11325f1c65baf6_14 >= -3
 R976: rho_||_2bx22f6bca85b580f1b_14 - rho_predicate_2dx22dd95ed78b4d217_14
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_14
   <= 1000
 R977: z_||_2bx22f6bca85b580f1b_14 - z_predicate_2dx22dd95ed78b4d217_14
   >= 0
 R978: - z_predicate_2dx22dd95ed78b4d217_14
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_14 <= 0
 R979: rho_||_2bx22f6bca85b580f1b_14 - rho_predicate_2dx5f1149c769efb91f_14
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_14
   <= 1000
 R980: z_||_2bx22f6bca85b580f1b_14 - z_predicate_2dx5f1149c769efb91f_14
   >= 0
 R981: - z_predicate_2dx5f1149c769efb91f_14
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_14 <= 0
 R982: rho_||_2bx22f6bca85b580f1b_14 - rho_predicate_2bx955025411f5da14_14
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_14 <= 1000
 R983: z_||_2bx22f6bca85b580f1b_14 - z_predicate_2bx955025411f5da14_14
   >= 0
 R984: - z_predicate_2bx955025411f5da14_14
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_14 <= 0
 R985: rho_||_2bx22f6bca85b580f1b_14 - rho_predicate_2bx7f11325f1c65baf6_14
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_14
   <= 1000
 R986: z_||_2bx22f6bca85b580f1b_14 - z_predicate_2bx7f11325f1c65baf6_14
   >= 0
 R987: - z_predicate_2bx7f11325f1c65baf6_14
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_14 <= 0
 R988: z_||_2bx22f6bca85b580f1b_14 - z_predicate_2dx22dd95ed78b4d217_14
   - z_predicate_2dx5f1149c769efb91f_14 - z_predicate_2bx955025411f5da14_14
   - z_predicate_2bx7f11325f1c65baf6_14 <= 0
 R989: - z_||_2bx22f6bca85b580f1b_14
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_14
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_14
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_14
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_14 >= 0
 R990: x_15 - 1000 z_predicate_2dx22dd95ed78b4d217_15
   - rho_predicate_2dx22dd95ed78b4d217_15 >= -997
 R991: x_15 - 1000 z_predicate_2dx22dd95ed78b4d217_15
   - rho_predicate_2dx22dd95ed78b4d217_15 <= 3
 R992: x_15 + 1000 z_predicate_2dx5f1149c769efb91f_15
   + rho_predicate_2dx5f1149c769efb91f_15 <= 997
 R993: x_15 + 1000 z_predicate_2dx5f1149c769efb91f_15
   + rho_predicate_2dx5f1149c769efb91f_15 >= -3
 R994: y_15 - 1000 z_predicate_2bx955025411f5da14_15
   - rho_predicate_2bx955025411f5da14_15 >= -997
 R995: y_15 - 1000 z_predicate_2bx955025411f5da14_15
   - rho_predicate_2bx955025411f5da14_15 <= 3
 R996: y_15 + 1000 z_predicate_2bx7f11325f1c65baf6_15
   + rho_predicate_2bx7f11325f1c65baf6_15 <= 997
 R997: y_15 + 1000 z_predicate_2bx7f11325f1c65baf6_15
   + rho_predicate_2bx7f11325f1c65baf6_15 >= -3
 R998: rho_||_2bx22f6bca85b580f1b_15 - rho_predicate_2dx22dd95ed78b4d217_15
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_15
   <= 1000
 R999: z_||_2bx22f6bca85b580f1b_15 - z_predicate_2dx22dd95ed78b4d217_15
   >= 0
 R1000: - z_predicate_2dx22dd95ed78b4d217_15
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_15 <= 0
 R1001: rho_||_2bx22f6bca85b580f1b_15
   - rho_predicate_2dx5f1149c769efb91f_15
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_15
   <= 1000
 R1002: z_||_2bx22f6bca85b580f1b_15 - z_predicate_2dx5f1149c769efb91f_15
   >= 0
 R1003: - z_predicate_2dx5f1149c769efb91f_15
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_15 <= 0
 R1004: rho_||_2bx22f6bca85b580f1b_15 - rho_predicate_2bx955025411f5da14_15
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_15 <= 1000
 R1005: z_||_2bx22f6bca85b580f1b_15 - z_predicate_2bx955025411f5da14_15
   >= 0
 R1006: - z_predicate_2bx955025411f5da14_15
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_15 <= 0
 R1007: rho_||_2bx22f6bca85b580f1b_15
   - rho_predicate_2bx7f11325f1c65baf6_15
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_15
   <= 1000
 R1008: z_||_2bx22f6bca85b580f1b_15 - z_predicate_2bx7f11325f1c65baf6_15
   >= 0
 R1009: - z_predicate_2bx7f11325f1c65baf6_15
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_15 <= 0
 R1010: z_||_2bx22f6bca85b580f1b_15 - z_predicate_2dx22dd95ed78b4d217_15
   - z_predicate_2dx5f1149c769efb91f_15 - z_predicate_2bx955025411f5da14_15
   - z_predicate_2bx7f11325f1c65baf6_15 <= 0
 R1011: - z_||_2bx22f6bca85b580f1b_15
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_15
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_15
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_15
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_15 >= 0
 R1012: x_16 - 1000 z_predicate_2dx22dd95ed78b4d217_16
   - rho_predicate_2dx22dd95ed78b4d217_16 >= -997
 R1013: x_16 - 1000 z_predicate_2dx22dd95ed78b4d217_16
   - rho_predicate_2dx22dd95ed78b4d217_16 <= 3
 R1014: x_16 + 1000 z_predicate_2dx5f1149c769efb91f_16
   + rho_predicate_2dx5f1149c769efb91f_16 <= 997
 R1015: x_16 + 1000 z_predicate_2dx5f1149c769efb91f_16
   + rho_predicate_2dx5f1149c769efb91f_16 >= -3
 R1016: y_16 - 1000 z_predicate_2bx955025411f5da14_16
   - rho_predicate_2bx955025411f5da14_16 >= -997
 R1017: y_16 - 1000 z_predicate_2bx955025411f5da14_16
   - rho_predicate_2bx955025411f5da14_16 <= 3
 R1018: y_16 + 1000 z_predicate_2bx7f11325f1c65baf6_16
   + rho_predicate_2bx7f11325f1c65baf6_16 <= 997
 R1019: y_16 + 1000 z_predicate_2bx7f11325f1c65baf6_16
   + rho_predicate_2bx7f11325f1c65baf6_16 >= -3
 R1020: rho_||_2bx22f6bca85b580f1b_16
   - rho_predicate_2dx22dd95ed78b4d217_16
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_16
   <= 1000
 R1021: z_||_2bx22f6bca85b580f1b_16 - z_predicate_2dx22dd95ed78b4d217_16
   >= 0
 R1022: - z_predicate_2dx22dd95ed78b4d217_16
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_16 <= 0
 R1023: rho_||_2bx22f6bca85b580f1b_16
   - rho_predicate_2dx5f1149c769efb91f_16
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_16
   <= 1000
 R1024: z_||_2bx22f6bca85b580f1b_16 - z_predicate_2dx5f1149c769efb91f_16
   >= 0
 R1025: - z_predicate_2dx5f1149c769efb91f_16
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_16 <= 0
 R1026: rho_||_2bx22f6bca85b580f1b_16 - rho_predicate_2bx955025411f5da14_16
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_16 <= 1000
 R1027: z_||_2bx22f6bca85b580f1b_16 - z_predicate_2bx955025411f5da14_16
   >= 0
 R1028: - z_predicate_2bx955025411f5da14_16
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_16 <= 0
 R1029: rho_||_2bx22f6bca85b580f1b_16
   - rho_predicate_2bx7f11325f1c65baf6_16
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_16
   <= 1000
 R1030: z_||_2bx22f6bca85b580f1b_16 - z_predicate_2bx7f11325f1c65baf6_16
   >= 0
 R1031: - z_predicate_2bx7f11325f1c65baf6_16
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_16 <= 0
 R1032: z_||_2bx22f6bca85b580f1b_16 - z_predicate_2dx22dd95ed78b4d217_16
   - z_predicate_2dx5f1149c769efb91f_16 - z_predicate_2bx955025411f5da14_16
   - z_predicate_2bx7f11325f1c65baf6_16 <= 0
 R1033: - z_||_2bx22f6bca85b580f1b_16
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_16
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_16
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_16
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_16 >= 0
 R1034: x_17 - 1000 z_predicate_2dx22dd95ed78b4d217_17
   - rho_predicate_2dx22dd95ed78b4d217_17 >= -997
 R1035: x_17 - 1000 z_predicate_2dx22dd95ed78b4d217_17
   - rho_predicate_2dx22dd95ed78b4d217_17 <= 3
 R1036: x_17 + 1000 z_predicate_2dx5f1149c769efb91f_17
   + rho_predicate_2dx5f1149c769efb91f_17 <= 997
 R1037: x_17 + 1000 z_predicate_2dx5f1149c769efb91f_17
   + rho_predicate_2dx5f1149c769efb91f_17 >= -3
 R1038: y_17 - 1000 z_predicate_2bx955025411f5da14_17
   - rho_predicate_2bx955025411f5da14_17 >= -997
 R1039: y_17 - 1000 z_predicate_2bx955025411f5da14_17
   - rho_predicate_2bx955025411f5da14_17 <= 3
 R1040: y_17 + 1000 z_predicate_2bx7f11325f1c65baf6_17
   + rho_predicate_2bx7f11325f1c65baf6_17 <= 997
 R1041: y_17 + 1000 z_predicate_2bx7f11325f1c65baf6_17
   + rho_predicate_2bx7f11325f1c65baf6_17 >= -3
 R1042: rho_||_2bx22f6bca85b580f1b_17
   - rho_predicate_2dx22dd95ed78b4d217_17
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_17
   <= 1000
 R1043: z_||_2bx22f6bca85b580f1b_17 - z_predicate_2dx22dd95ed78b4d217_17
   >= 0
 R1044: - z_predicate_2dx22dd95ed78b4d217_17
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_17 <= 0
 R1045: rho_||_2bx22f6bca85b580f1b_17
   - rho_predicate_2dx5f1149c769efb91f_17
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_17
   <= 1000
 R1046: z_||_2bx22f6bca85b580f1b_17 - z_predicate_2dx5f1149c769efb91f_17
   >= 0
 R1047: - z_predicate_2dx5f1149c769efb91f_17
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_17 <= 0
 R1048: rho_||_2bx22f6bca85b580f1b_17 - rho_predicate_2bx955025411f5da14_17
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_17 <= 1000
 R1049: z_||_2bx22f6bca85b580f1b_17 - z_predicate_2bx955025411f5da14_17
   >= 0
 R1050: - z_predicate_2bx955025411f5da14_17
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_17 <= 0
 R1051: rho_||_2bx22f6bca85b580f1b_17
   - rho_predicate_2bx7f11325f1c65baf6_17
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_17
   <= 1000
 R1052: z_||_2bx22f6bca85b580f1b_17 - z_predicate_2bx7f11325f1c65baf6_17
   >= 0
 R1053: - z_predicate_2bx7f11325f1c65baf6_17
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_17 <= 0
 R1054: z_||_2bx22f6bca85b580f1b_17 - z_predicate_2dx22dd95ed78b4d217_17
   - z_predicate_2dx5f1149c769efb91f_17 - z_predicate_2bx955025411f5da14_17
   - z_predicate_2bx7f11325f1c65baf6_17 <= 0
 R1055: - z_||_2bx22f6bca85b580f1b_17
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_17
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_17
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_17
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_17 >= 0
 R1056: x_18 - 1000 z_predicate_2dx22dd95ed78b4d217_18
   - rho_predicate_2dx22dd95ed78b4d217_18 >= -997
 R1057: x_18 - 1000 z_predicate_2dx22dd95ed78b4d217_18
   - rho_predicate_2dx22dd95ed78b4d217_18 <= 3
 R1058: x_18 + 1000 z_predicate_2dx5f1149c769efb91f_18
   + rho_predicate_2dx5f1149c769efb91f_18 <= 997
 R1059: x_18 + 1000 z_predicate_2dx5f1149c769efb91f_18
   + rho_predicate_2dx5f1149c769efb91f_18 >= -3
 R1060: y_18 - 1000 z_predicate_2bx955025411f5da14_18
   - rho_predicate_2bx955025411f5da14_18 >= -997
 R1061: y_18 - 1000 z_predicate_2bx955025411f5da14_18
   - rho_predicate_2bx955025411f5da14_18 <= 3
 R1062: y_18 + 1000 z_predicate_2bx7f11325f1c65baf6_18
   + rho_predicate_2bx7f11325f1c65baf6_18 <= 997
 R1063: y_18 + 1000 z_predicate_2bx7f11325f1c65baf6_18
   + rho_predicate_2bx7f11325f1c65baf6_18 >= -3
 R1064: rho_||_2bx22f6bca85b580f1b_18
   - rho_predicate_2dx22dd95ed78b4d217_18
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_18
   <= 1000
 R1065: z_||_2bx22f6bca85b580f1b_18 - z_predicate_2dx22dd95ed78b4d217_18
   >= 0
 R1066: - z_predicate_2dx22dd95ed78b4d217_18
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_18 <= 0
 R1067: rho_||_2bx22f6bca85b580f1b_18
   - rho_predicate_2dx5f1149c769efb91f_18
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_18
   <= 1000
 R1068: z_||_2bx22f6bca85b580f1b_18 - z_predicate_2dx5f1149c769efb91f_18
   >= 0
 R1069: - z_predicate_2dx5f1149c769efb91f_18
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_18 <= 0
 R1070: rho_||_2bx22f6bca85b580f1b_18 - rho_predicate_2bx955025411f5da14_18
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_18 <= 1000
 R1071: z_||_2bx22f6bca85b580f1b_18 - z_predicate_2bx955025411f5da14_18
   >= 0
 R1072: - z_predicate_2bx955025411f5da14_18
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_18 <= 0
 R1073: rho_||_2bx22f6bca85b580f1b_18
   - rho_predicate_2bx7f11325f1c65baf6_18
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_18
   <= 1000
 R1074: z_||_2bx22f6bca85b580f1b_18 - z_predicate_2bx7f11325f1c65baf6_18
   >= 0
 R1075: - z_predicate_2bx7f11325f1c65baf6_18
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_18 <= 0
 R1076: z_||_2bx22f6bca85b580f1b_18 - z_predicate_2dx22dd95ed78b4d217_18
   - z_predicate_2dx5f1149c769efb91f_18 - z_predicate_2bx955025411f5da14_18
   - z_predicate_2bx7f11325f1c65baf6_18 <= 0
 R1077: - z_||_2bx22f6bca85b580f1b_18
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_18
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_18
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_18
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_18 >= 0
 R1078: x_19 - 1000 z_predicate_2dx22dd95ed78b4d217_19
   - rho_predicate_2dx22dd95ed78b4d217_19 >= -997
 R1079: x_19 - 1000 z_predicate_2dx22dd95ed78b4d217_19
   - rho_predicate_2dx22dd95ed78b4d217_19 <= 3
 R1080: x_19 + 1000 z_predicate_2dx5f1149c769efb91f_19
   + rho_predicate_2dx5f1149c769efb91f_19 <= 997
 R1081: x_19 + 1000 z_predicate_2dx5f1149c769efb91f_19
   + rho_predicate_2dx5f1149c769efb91f_19 >= -3
 R1082: y_19 - 1000 z_predicate_2bx955025411f5da14_19
   - rho_predicate_2bx955025411f5da14_19 >= -997
 R1083: y_19 - 1000 z_predicate_2bx955025411f5da14_19
   - rho_predicate_2bx955025411f5da14_19 <= 3
 R1084: y_19 + 1000 z_predicate_2bx7f11325f1c65baf6_19
   + rho_predicate_2bx7f11325f1c65baf6_19 <= 997
 R1085: y_19 + 1000 z_predicate_2bx7f11325f1c65baf6_19
   + rho_predicate_2bx7f11325f1c65baf6_19 >= -3
 R1086: rho_||_2bx22f6bca85b580f1b_19
   - rho_predicate_2dx22dd95ed78b4d217_19
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_19
   <= 1000
 R1087: z_||_2bx22f6bca85b580f1b_19 - z_predicate_2dx22dd95ed78b4d217_19
   >= 0
 R1088: - z_predicate_2dx22dd95ed78b4d217_19
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_19 <= 0
 R1089: rho_||_2bx22f6bca85b580f1b_19
   - rho_predicate_2dx5f1149c769efb91f_19
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_19
   <= 1000
 R1090: z_||_2bx22f6bca85b580f1b_19 - z_predicate_2dx5f1149c769efb91f_19
   >= 0
 R1091: - z_predicate_2dx5f1149c769efb91f_19
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_19 <= 0
 R1092: rho_||_2bx22f6bca85b580f1b_19 - rho_predicate_2bx955025411f5da14_19
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_19 <= 1000
 R1093: z_||_2bx22f6bca85b580f1b_19 - z_predicate_2bx955025411f5da14_19
   >= 0
 R1094: - z_predicate_2bx955025411f5da14_19
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_19 <= 0
 R1095: rho_||_2bx22f6bca85b580f1b_19
   - rho_predicate_2bx7f11325f1c65baf6_19
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_19
   <= 1000
 R1096: z_||_2bx22f6bca85b580f1b_19 - z_predicate_2bx7f11325f1c65baf6_19
   >= 0
 R1097: - z_predicate_2bx7f11325f1c65baf6_19
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_19 <= 0
 R1098: z_||_2bx22f6bca85b580f1b_19 - z_predicate_2dx22dd95ed78b4d217_19
   - z_predicate_2dx5f1149c769efb91f_19 - z_predicate_2bx955025411f5da14_19
   - z_predicate_2bx7f11325f1c65baf6_19 <= 0
 R1099: - z_||_2bx22f6bca85b580f1b_19
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_19
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_19
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_19
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_19 >= 0
 R1100: x_20 - 1000 z_predicate_2dx22dd95ed78b4d217_20
   - rho_predicate_2dx22dd95ed78b4d217_20 >= -997
 R1101: x_20 - 1000 z_predicate_2dx22dd95ed78b4d217_20
   - rho_predicate_2dx22dd95ed78b4d217_20 <= 3
 R1102: x_20 + 1000 z_predicate_2dx5f1149c769efb91f_20
   + rho_predicate_2dx5f1149c769efb91f_20 <= 997
 R1103: x_20 + 1000 z_predicate_2dx5f1149c769efb91f_20
   + rho_predicate_2dx5f1149c769efb91f_20 >= -3
 R1104: y_20 - 1000 z_predicate_2bx955025411f5da14_20
   - rho_predicate_2bx955025411f5da14_20 >= -997
 R1105: y_20 - 1000 z_predicate_2bx955025411f5da14_20
   - rho_predicate_2bx955025411f5da14_20 <= 3
 R1106: y_20 + 1000 z_predicate_2bx7f11325f1c65baf6_20
   + rho_predicate_2bx7f11325f1c65baf6_20 <= 997
 R1107: y_20 + 1000 z_predicate_2bx7f11325f1c65baf6_20
   + rho_predicate_2bx7f11325f1c65baf6_20 >= -3
 R1108: rho_||_2bx22f6bca85b580f1b_20
   - rho_predicate_2dx22dd95ed78b4d217_20
   + 1000 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_20
   <= 1000
 R1109: z_||_2bx22f6bca85b580f1b_20 - z_predicate_2dx22dd95ed78b4d217_20
   >= 0
 R1110: - z_predicate_2dx22dd95ed78b4d217_20
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_20 <= 0
 R1111: rho_||_2bx22f6bca85b580f1b_20
   - rho_predicate_2dx5f1149c769efb91f_20
   + 1000 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_20
   <= 1000
 R1112: z_||_2bx22f6bca85b580f1b_20 - z_predicate_2dx5f1149c769efb91f_20
   >= 0
 R1113: - z_predicate_2dx5f1149c769efb91f_20
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_20 <= 0
 R1114: rho_||_2bx22f6bca85b580f1b_20 - rho_predicate_2bx955025411f5da14_20
   + 1000 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_20 <= 1000
 R1115: z_||_2bx22f6bca85b580f1b_20 - z_predicate_2bx955025411f5da14_20
   >= 0
 R1116: - z_predicate_2bx955025411f5da14_20
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_20 <= 0
 R1117: rho_||_2bx22f6bca85b580f1b_20
   - rho_predicate_2bx7f11325f1c65baf6_20
   + 1000 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_20
   <= 1000
 R1118: z_||_2bx22f6bca85b580f1b_20 - z_predicate_2bx7f11325f1c65baf6_20
   >= 0
 R1119: - z_predicate_2bx7f11325f1c65baf6_20
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_20 <= 0
 R1120: z_||_2bx22f6bca85b580f1b_20 - z_predicate_2dx22dd95ed78b4d217_20
   - z_predicate_2dx5f1149c769efb91f_20 - z_predicate_2bx955025411f5da14_20
   - z_predicate_2bx7f11325f1c65baf6_20 <= 0
 R1121: - z_||_2bx22f6bca85b580f1b_20
   + zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_20
   + zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_20
   + zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_20
   + zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_20 >= 0
 R1122: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_0 <= 0
 R1123: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_0 <= 0
 R1124: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_1 <= 0
 R1125: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_1 <= 0
 R1126: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_2 <= 0
 R1127: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_2 <= 0
 R1128: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_3 <= 0
 R1129: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_3 <= 0
 R1130: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_4 <= 0
 R1131: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_4 <= 0
 R1132: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_5 <= 0
 R1133: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_5 <= 0
 R1134: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_6 <= 0
 R1135: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_6 <= 0
 R1136: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_7 <= 0
 R1137: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_7 <= 0
 R1138: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_8 <= 0
 R1139: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_8 <= 0
 R1140: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_9 <= 0
 R1141: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_9 <= 0
 R1142: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_10 <= 0
 R1143: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_10 <= 0
 R1144: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_11 <= 0
 R1145: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_11 <= 0
 R1146: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_12 <= 0
 R1147: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_12 <= 0
 R1148: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_13 <= 0
 R1149: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_13 <= 0
 R1150: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_14 <= 0
 R1151: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_14 <= 0
 R1152: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_15 <= 0
 R1153: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_15 <= 0
 R1154: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_16 <= 0
 R1155: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_16 <= 0
 R1156: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_17 <= 0
 R1157: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_17 <= 0
 R1158: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_18 <= 0
 R1159: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_18 <= 0
 R1160: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_19 <= 0
 R1161: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_19 <= 0
 R1162: rho_G_2bx1e250240efa087ae_0 - rho_||_2bx22f6bca85b580f1b_20 <= 0
 R1163: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_20 <= 0
 R1164: z_G_2bx1e250240efa087ae_0 - z_||_2bx22f6bca85b580f1b_0
   - z_||_2bx22f6bca85b580f1b_1 - z_||_2bx22f6bca85b580f1b_2
   - z_||_2bx22f6bca85b580f1b_3 - z_||_2bx22f6bca85b580f1b_4
   - z_||_2bx22f6bca85b580f1b_5 - z_||_2bx22f6bca85b580f1b_6
   - z_||_2bx22f6bca85b580f1b_7 - z_||_2bx22f6bca85b580f1b_8
   - z_||_2bx22f6bca85b580f1b_9 - z_||_2bx22f6bca85b580f1b_10
   - z_||_2bx22f6bca85b580f1b_11 - z_||_2bx22f6bca85b580f1b_12
   - z_||_2bx22f6bca85b580f1b_13 - z_||_2bx22f6bca85b580f1b_14
   - z_||_2bx22f6bca85b580f1b_15 - z_||_2bx22f6bca85b580f1b_16
   - z_||_2bx22f6bca85b580f1b_17 - z_||_2bx22f6bca85b580f1b_18
   - z_||_2bx22f6bca85b580f1b_19 - z_||_2bx22f6bca85b580f1b_20 >= -20
 R1165: x_0 - 1000 z_predicate_2dx68411627ea61c0e0_0
   - rho_predicate_2dx68411627ea61c0e0_0 >= -992
 R1166: x_0 - 1000 z_predicate_2dx68411627ea61c0e0_0
   - rho_predicate_2dx68411627ea61c0e0_0 <= 8
 R1167: x_0 + 1000 z_predicate_2dx5dba1e6a7b84e365_0
   + rho_predicate_2dx5dba1e6a7b84e365_0 <= 1003
 R1168: x_0 + 1000 z_predicate_2dx5dba1e6a7b84e365_0
   + rho_predicate_2dx5dba1e6a7b84e365_0 >= 3
 R1169: y_0 - 1000 z_predicate_2bx4c3942499adecf48_0
   - rho_predicate_2bx4c3942499adecf48_0 >= -1003
 R1170: y_0 - 1000 z_predicate_2bx4c3942499adecf48_0
   - rho_predicate_2bx4c3942499adecf48_0 <= -3
 R1171: y_0 + 1000 z_predicate_2bx22a3ae6fed0097b_0
   + rho_predicate_2bx22a3ae6fed0097b_0 <= 992
 R1172: y_0 + 1000 z_predicate_2bx22a3ae6fed0097b_0
   + rho_predicate_2bx22a3ae6fed0097b_0 >= -8
 R1173: rho_||_2dx1cb8c284b4383193_0 - rho_predicate_2dx68411627ea61c0e0_0
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_0 <= 1000
 R1174: z_||_2dx1cb8c284b4383193_0 - z_predicate_2dx68411627ea61c0e0_0
   >= 0
 R1175: - z_predicate_2dx68411627ea61c0e0_0
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_0 <= 0
 R1176: rho_||_2dx1cb8c284b4383193_0 - rho_predicate_2dx5dba1e6a7b84e365_0
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_0 <= 1000
 R1177: z_||_2dx1cb8c284b4383193_0 - z_predicate_2dx5dba1e6a7b84e365_0
   >= 0
 R1178: - z_predicate_2dx5dba1e6a7b84e365_0
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_0 <= 0
 R1179: rho_||_2dx1cb8c284b4383193_0 - rho_predicate_2bx4c3942499adecf48_0
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_0 <= 1000
 R1180: z_||_2dx1cb8c284b4383193_0 - z_predicate_2bx4c3942499adecf48_0
   >= 0
 R1181: - z_predicate_2bx4c3942499adecf48_0
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_0 <= 0
 R1182: rho_||_2dx1cb8c284b4383193_0 - rho_predicate_2bx22a3ae6fed0097b_0
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_0 <= 1000
 R1183: z_||_2dx1cb8c284b4383193_0 - z_predicate_2bx22a3ae6fed0097b_0 >= 0
 R1184: - z_predicate_2bx22a3ae6fed0097b_0
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_0 <= 0
 R1185: z_||_2dx1cb8c284b4383193_0 - z_predicate_2dx68411627ea61c0e0_0
   - z_predicate_2dx5dba1e6a7b84e365_0 - z_predicate_2bx4c3942499adecf48_0
   - z_predicate_2bx22a3ae6fed0097b_0 <= 0
 R1186: - z_||_2dx1cb8c284b4383193_0
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_0
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_0
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_0
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_0 >= 0
 R1187: x_1 - 1000 z_predicate_2dx68411627ea61c0e0_1
   - rho_predicate_2dx68411627ea61c0e0_1 >= -992
 R1188: x_1 - 1000 z_predicate_2dx68411627ea61c0e0_1
   - rho_predicate_2dx68411627ea61c0e0_1 <= 8
 R1189: x_1 + 1000 z_predicate_2dx5dba1e6a7b84e365_1
   + rho_predicate_2dx5dba1e6a7b84e365_1 <= 1003
 R1190: x_1 + 1000 z_predicate_2dx5dba1e6a7b84e365_1
   + rho_predicate_2dx5dba1e6a7b84e365_1 >= 3
 R1191: y_1 - 1000 z_predicate_2bx4c3942499adecf48_1
   - rho_predicate_2bx4c3942499adecf48_1 >= -1003
 R1192: y_1 - 1000 z_predicate_2bx4c3942499adecf48_1
   - rho_predicate_2bx4c3942499adecf48_1 <= -3
 R1193: y_1 + 1000 z_predicate_2bx22a3ae6fed0097b_1
   + rho_predicate_2bx22a3ae6fed0097b_1 <= 992
 R1194: y_1 + 1000 z_predicate_2bx22a3ae6fed0097b_1
   + rho_predicate_2bx22a3ae6fed0097b_1 >= -8
 R1195: rho_||_2dx1cb8c284b4383193_1 - rho_predicate_2dx68411627ea61c0e0_1
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_1 <= 1000
 R1196: z_||_2dx1cb8c284b4383193_1 - z_predicate_2dx68411627ea61c0e0_1
   >= 0
 R1197: - z_predicate_2dx68411627ea61c0e0_1
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_1 <= 0
 R1198: rho_||_2dx1cb8c284b4383193_1 - rho_predicate_2dx5dba1e6a7b84e365_1
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_1 <= 1000
 R1199: z_||_2dx1cb8c284b4383193_1 - z_predicate_2dx5dba1e6a7b84e365_1
   >= 0
 R1200: - z_predicate_2dx5dba1e6a7b84e365_1
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_1 <= 0
 R1201: rho_||_2dx1cb8c284b4383193_1 - rho_predicate_2bx4c3942499adecf48_1
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_1 <= 1000
 R1202: z_||_2dx1cb8c284b4383193_1 - z_predicate_2bx4c3942499adecf48_1
   >= 0
 R1203: - z_predicate_2bx4c3942499adecf48_1
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_1 <= 0
 R1204: rho_||_2dx1cb8c284b4383193_1 - rho_predicate_2bx22a3ae6fed0097b_1
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_1 <= 1000
 R1205: z_||_2dx1cb8c284b4383193_1 - z_predicate_2bx22a3ae6fed0097b_1 >= 0
 R1206: - z_predicate_2bx22a3ae6fed0097b_1
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_1 <= 0
 R1207: z_||_2dx1cb8c284b4383193_1 - z_predicate_2dx68411627ea61c0e0_1
   - z_predicate_2dx5dba1e6a7b84e365_1 - z_predicate_2bx4c3942499adecf48_1
   - z_predicate_2bx22a3ae6fed0097b_1 <= 0
 R1208: - z_||_2dx1cb8c284b4383193_1
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_1
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_1
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_1
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_1 >= 0
 R1209: x_2 - 1000 z_predicate_2dx68411627ea61c0e0_2
   - rho_predicate_2dx68411627ea61c0e0_2 >= -992
 R1210: x_2 - 1000 z_predicate_2dx68411627ea61c0e0_2
   - rho_predicate_2dx68411627ea61c0e0_2 <= 8
 R1211: x_2 + 1000 z_predicate_2dx5dba1e6a7b84e365_2
   + rho_predicate_2dx5dba1e6a7b84e365_2 <= 1003
 R1212: x_2 + 1000 z_predicate_2dx5dba1e6a7b84e365_2
   + rho_predicate_2dx5dba1e6a7b84e365_2 >= 3
 R1213: y_2 - 1000 z_predicate_2bx4c3942499adecf48_2
   - rho_predicate_2bx4c3942499adecf48_2 >= -1003
 R1214: y_2 - 1000 z_predicate_2bx4c3942499adecf48_2
   - rho_predicate_2bx4c3942499adecf48_2 <= -3
 R1215: y_2 + 1000 z_predicate_2bx22a3ae6fed0097b_2
   + rho_predicate_2bx22a3ae6fed0097b_2 <= 992
 R1216: y_2 + 1000 z_predicate_2bx22a3ae6fed0097b_2
   + rho_predicate_2bx22a3ae6fed0097b_2 >= -8
 R1217: rho_||_2dx1cb8c284b4383193_2 - rho_predicate_2dx68411627ea61c0e0_2
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_2 <= 1000
 R1218: z_||_2dx1cb8c284b4383193_2 - z_predicate_2dx68411627ea61c0e0_2
   >= 0
 R1219: - z_predicate_2dx68411627ea61c0e0_2
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_2 <= 0
 R1220: rho_||_2dx1cb8c284b4383193_2 - rho_predicate_2dx5dba1e6a7b84e365_2
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_2 <= 1000
 R1221: z_||_2dx1cb8c284b4383193_2 - z_predicate_2dx5dba1e6a7b84e365_2
   >= 0
 R1222: - z_predicate_2dx5dba1e6a7b84e365_2
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_2 <= 0
 R1223: rho_||_2dx1cb8c284b4383193_2 - rho_predicate_2bx4c3942499adecf48_2
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_2 <= 1000
 R1224: z_||_2dx1cb8c284b4383193_2 - z_predicate_2bx4c3942499adecf48_2
   >= 0
 R1225: - z_predicate_2bx4c3942499adecf48_2
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_2 <= 0
 R1226: rho_||_2dx1cb8c284b4383193_2 - rho_predicate_2bx22a3ae6fed0097b_2
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_2 <= 1000
 R1227: z_||_2dx1cb8c284b4383193_2 - z_predicate_2bx22a3ae6fed0097b_2 >= 0
 R1228: - z_predicate_2bx22a3ae6fed0097b_2
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_2 <= 0
 R1229: z_||_2dx1cb8c284b4383193_2 - z_predicate_2dx68411627ea61c0e0_2
   - z_predicate_2dx5dba1e6a7b84e365_2 - z_predicate_2bx4c3942499adecf48_2
   - z_predicate_2bx22a3ae6fed0097b_2 <= 0
 R1230: - z_||_2dx1cb8c284b4383193_2
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_2
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_2
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_2
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_2 >= 0
 R1231: x_3 - 1000 z_predicate_2dx68411627ea61c0e0_3
   - rho_predicate_2dx68411627ea61c0e0_3 >= -992
 R1232: x_3 - 1000 z_predicate_2dx68411627ea61c0e0_3
   - rho_predicate_2dx68411627ea61c0e0_3 <= 8
 R1233: x_3 + 1000 z_predicate_2dx5dba1e6a7b84e365_3
   + rho_predicate_2dx5dba1e6a7b84e365_3 <= 1003
 R1234: x_3 + 1000 z_predicate_2dx5dba1e6a7b84e365_3
   + rho_predicate_2dx5dba1e6a7b84e365_3 >= 3
 R1235: y_3 - 1000 z_predicate_2bx4c3942499adecf48_3
   - rho_predicate_2bx4c3942499adecf48_3 >= -1003
 R1236: y_3 - 1000 z_predicate_2bx4c3942499adecf48_3
   - rho_predicate_2bx4c3942499adecf48_3 <= -3
 R1237: y_3 + 1000 z_predicate_2bx22a3ae6fed0097b_3
   + rho_predicate_2bx22a3ae6fed0097b_3 <= 992
 R1238: y_3 + 1000 z_predicate_2bx22a3ae6fed0097b_3
   + rho_predicate_2bx22a3ae6fed0097b_3 >= -8
 R1239: rho_||_2dx1cb8c284b4383193_3 - rho_predicate_2dx68411627ea61c0e0_3
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_3 <= 1000
 R1240: z_||_2dx1cb8c284b4383193_3 - z_predicate_2dx68411627ea61c0e0_3
   >= 0
 R1241: - z_predicate_2dx68411627ea61c0e0_3
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_3 <= 0
 R1242: rho_||_2dx1cb8c284b4383193_3 - rho_predicate_2dx5dba1e6a7b84e365_3
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_3 <= 1000
 R1243: z_||_2dx1cb8c284b4383193_3 - z_predicate_2dx5dba1e6a7b84e365_3
   >= 0
 R1244: - z_predicate_2dx5dba1e6a7b84e365_3
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_3 <= 0
 R1245: rho_||_2dx1cb8c284b4383193_3 - rho_predicate_2bx4c3942499adecf48_3
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_3 <= 1000
 R1246: z_||_2dx1cb8c284b4383193_3 - z_predicate_2bx4c3942499adecf48_3
   >= 0
 R1247: - z_predicate_2bx4c3942499adecf48_3
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_3 <= 0
 R1248: rho_||_2dx1cb8c284b4383193_3 - rho_predicate_2bx22a3ae6fed0097b_3
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_3 <= 1000
 R1249: z_||_2dx1cb8c284b4383193_3 - z_predicate_2bx22a3ae6fed0097b_3 >= 0
 R1250: - z_predicate_2bx22a3ae6fed0097b_3
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_3 <= 0
 R1251: z_||_2dx1cb8c284b4383193_3 - z_predicate_2dx68411627ea61c0e0_3
   - z_predicate_2dx5dba1e6a7b84e365_3 - z_predicate_2bx4c3942499adecf48_3
   - z_predicate_2bx22a3ae6fed0097b_3 <= 0
 R1252: - z_||_2dx1cb8c284b4383193_3
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_3
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_3
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_3
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_3 >= 0
 R1253: x_4 - 1000 z_predicate_2dx68411627ea61c0e0_4
   - rho_predicate_2dx68411627ea61c0e0_4 >= -992
 R1254: x_4 - 1000 z_predicate_2dx68411627ea61c0e0_4
   - rho_predicate_2dx68411627ea61c0e0_4 <= 8
 R1255: x_4 + 1000 z_predicate_2dx5dba1e6a7b84e365_4
   + rho_predicate_2dx5dba1e6a7b84e365_4 <= 1003
 R1256: x_4 + 1000 z_predicate_2dx5dba1e6a7b84e365_4
   + rho_predicate_2dx5dba1e6a7b84e365_4 >= 3
 R1257: y_4 - 1000 z_predicate_2bx4c3942499adecf48_4
   - rho_predicate_2bx4c3942499adecf48_4 >= -1003
 R1258: y_4 - 1000 z_predicate_2bx4c3942499adecf48_4
   - rho_predicate_2bx4c3942499adecf48_4 <= -3
 R1259: y_4 + 1000 z_predicate_2bx22a3ae6fed0097b_4
   + rho_predicate_2bx22a3ae6fed0097b_4 <= 992
 R1260: y_4 + 1000 z_predicate_2bx22a3ae6fed0097b_4
   + rho_predicate_2bx22a3ae6fed0097b_4 >= -8
 R1261: rho_||_2dx1cb8c284b4383193_4 - rho_predicate_2dx68411627ea61c0e0_4
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_4 <= 1000
 R1262: z_||_2dx1cb8c284b4383193_4 - z_predicate_2dx68411627ea61c0e0_4
   >= 0
 R1263: - z_predicate_2dx68411627ea61c0e0_4
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_4 <= 0
 R1264: rho_||_2dx1cb8c284b4383193_4 - rho_predicate_2dx5dba1e6a7b84e365_4
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_4 <= 1000
 R1265: z_||_2dx1cb8c284b4383193_4 - z_predicate_2dx5dba1e6a7b84e365_4
   >= 0
 R1266: - z_predicate_2dx5dba1e6a7b84e365_4
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_4 <= 0
 R1267: rho_||_2dx1cb8c284b4383193_4 - rho_predicate_2bx4c3942499adecf48_4
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_4 <= 1000
 R1268: z_||_2dx1cb8c284b4383193_4 - z_predicate_2bx4c3942499adecf48_4
   >= 0
 R1269: - z_predicate_2bx4c3942499adecf48_4
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_4 <= 0
 R1270: rho_||_2dx1cb8c284b4383193_4 - rho_predicate_2bx22a3ae6fed0097b_4
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_4 <= 1000
 R1271: z_||_2dx1cb8c284b4383193_4 - z_predicate_2bx22a3ae6fed0097b_4 >= 0
 R1272: - z_predicate_2bx22a3ae6fed0097b_4
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_4 <= 0
 R1273: z_||_2dx1cb8c284b4383193_4 - z_predicate_2dx68411627ea61c0e0_4
   - z_predicate_2dx5dba1e6a7b84e365_4 - z_predicate_2bx4c3942499adecf48_4
   - z_predicate_2bx22a3ae6fed0097b_4 <= 0
 R1274: - z_||_2dx1cb8c284b4383193_4
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_4
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_4
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_4
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_4 >= 0
 R1275: x_5 - 1000 z_predicate_2dx68411627ea61c0e0_5
   - rho_predicate_2dx68411627ea61c0e0_5 >= -992
 R1276: x_5 - 1000 z_predicate_2dx68411627ea61c0e0_5
   - rho_predicate_2dx68411627ea61c0e0_5 <= 8
 R1277: x_5 + 1000 z_predicate_2dx5dba1e6a7b84e365_5
   + rho_predicate_2dx5dba1e6a7b84e365_5 <= 1003
 R1278: x_5 + 1000 z_predicate_2dx5dba1e6a7b84e365_5
   + rho_predicate_2dx5dba1e6a7b84e365_5 >= 3
 R1279: y_5 - 1000 z_predicate_2bx4c3942499adecf48_5
   - rho_predicate_2bx4c3942499adecf48_5 >= -1003
 R1280: y_5 - 1000 z_predicate_2bx4c3942499adecf48_5
   - rho_predicate_2bx4c3942499adecf48_5 <= -3
 R1281: y_5 + 1000 z_predicate_2bx22a3ae6fed0097b_5
   + rho_predicate_2bx22a3ae6fed0097b_5 <= 992
 R1282: y_5 + 1000 z_predicate_2bx22a3ae6fed0097b_5
   + rho_predicate_2bx22a3ae6fed0097b_5 >= -8
 R1283: rho_||_2dx1cb8c284b4383193_5 - rho_predicate_2dx68411627ea61c0e0_5
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_5 <= 1000
 R1284: z_||_2dx1cb8c284b4383193_5 - z_predicate_2dx68411627ea61c0e0_5
   >= 0
 R1285: - z_predicate_2dx68411627ea61c0e0_5
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_5 <= 0
 R1286: rho_||_2dx1cb8c284b4383193_5 - rho_predicate_2dx5dba1e6a7b84e365_5
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_5 <= 1000
 R1287: z_||_2dx1cb8c284b4383193_5 - z_predicate_2dx5dba1e6a7b84e365_5
   >= 0
 R1288: - z_predicate_2dx5dba1e6a7b84e365_5
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_5 <= 0
 R1289: rho_||_2dx1cb8c284b4383193_5 - rho_predicate_2bx4c3942499adecf48_5
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_5 <= 1000
 R1290: z_||_2dx1cb8c284b4383193_5 - z_predicate_2bx4c3942499adecf48_5
   >= 0
 R1291: - z_predicate_2bx4c3942499adecf48_5
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_5 <= 0
 R1292: rho_||_2dx1cb8c284b4383193_5 - rho_predicate_2bx22a3ae6fed0097b_5
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_5 <= 1000
 R1293: z_||_2dx1cb8c284b4383193_5 - z_predicate_2bx22a3ae6fed0097b_5 >= 0
 R1294: - z_predicate_2bx22a3ae6fed0097b_5
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_5 <= 0
 R1295: z_||_2dx1cb8c284b4383193_5 - z_predicate_2dx68411627ea61c0e0_5
   - z_predicate_2dx5dba1e6a7b84e365_5 - z_predicate_2bx4c3942499adecf48_5
   - z_predicate_2bx22a3ae6fed0097b_5 <= 0
 R1296: - z_||_2dx1cb8c284b4383193_5
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_5
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_5
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_5
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_5 >= 0
 R1297: x_6 - 1000 z_predicate_2dx68411627ea61c0e0_6
   - rho_predicate_2dx68411627ea61c0e0_6 >= -992
 R1298: x_6 - 1000 z_predicate_2dx68411627ea61c0e0_6
   - rho_predicate_2dx68411627ea61c0e0_6 <= 8
 R1299: x_6 + 1000 z_predicate_2dx5dba1e6a7b84e365_6
   + rho_predicate_2dx5dba1e6a7b84e365_6 <= 1003
 R1300: x_6 + 1000 z_predicate_2dx5dba1e6a7b84e365_6
   + rho_predicate_2dx5dba1e6a7b84e365_6 >= 3
 R1301: y_6 - 1000 z_predicate_2bx4c3942499adecf48_6
   - rho_predicate_2bx4c3942499adecf48_6 >= -1003
 R1302: y_6 - 1000 z_predicate_2bx4c3942499adecf48_6
   - rho_predicate_2bx4c3942499adecf48_6 <= -3
 R1303: y_6 + 1000 z_predicate_2bx22a3ae6fed0097b_6
   + rho_predicate_2bx22a3ae6fed0097b_6 <= 992
 R1304: y_6 + 1000 z_predicate_2bx22a3ae6fed0097b_6
   + rho_predicate_2bx22a3ae6fed0097b_6 >= -8
 R1305: rho_||_2dx1cb8c284b4383193_6 - rho_predicate_2dx68411627ea61c0e0_6
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_6 <= 1000
 R1306: z_||_2dx1cb8c284b4383193_6 - z_predicate_2dx68411627ea61c0e0_6
   >= 0
 R1307: - z_predicate_2dx68411627ea61c0e0_6
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_6 <= 0
 R1308: rho_||_2dx1cb8c284b4383193_6 - rho_predicate_2dx5dba1e6a7b84e365_6
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_6 <= 1000
 R1309: z_||_2dx1cb8c284b4383193_6 - z_predicate_2dx5dba1e6a7b84e365_6
   >= 0
 R1310: - z_predicate_2dx5dba1e6a7b84e365_6
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_6 <= 0
 R1311: rho_||_2dx1cb8c284b4383193_6 - rho_predicate_2bx4c3942499adecf48_6
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_6 <= 1000
 R1312: z_||_2dx1cb8c284b4383193_6 - z_predicate_2bx4c3942499adecf48_6
   >= 0
 R1313: - z_predicate_2bx4c3942499adecf48_6
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_6 <= 0
 R1314: rho_||_2dx1cb8c284b4383193_6 - rho_predicate_2bx22a3ae6fed0097b_6
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_6 <= 1000
 R1315: z_||_2dx1cb8c284b4383193_6 - z_predicate_2bx22a3ae6fed0097b_6 >= 0
 R1316: - z_predicate_2bx22a3ae6fed0097b_6
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_6 <= 0
 R1317: z_||_2dx1cb8c284b4383193_6 - z_predicate_2dx68411627ea61c0e0_6
   - z_predicate_2dx5dba1e6a7b84e365_6 - z_predicate_2bx4c3942499adecf48_6
   - z_predicate_2bx22a3ae6fed0097b_6 <= 0
 R1318: - z_||_2dx1cb8c284b4383193_6
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_6
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_6
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_6
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_6 >= 0
 R1319: x_7 - 1000 z_predicate_2dx68411627ea61c0e0_7
   - rho_predicate_2dx68411627ea61c0e0_7 >= -992
 R1320: x_7 - 1000 z_predicate_2dx68411627ea61c0e0_7
   - rho_predicate_2dx68411627ea61c0e0_7 <= 8
 R1321: x_7 + 1000 z_predicate_2dx5dba1e6a7b84e365_7
   + rho_predicate_2dx5dba1e6a7b84e365_7 <= 1003
 R1322: x_7 + 1000 z_predicate_2dx5dba1e6a7b84e365_7
   + rho_predicate_2dx5dba1e6a7b84e365_7 >= 3
 R1323: y_7 - 1000 z_predicate_2bx4c3942499adecf48_7
   - rho_predicate_2bx4c3942499adecf48_7 >= -1003
 R1324: y_7 - 1000 z_predicate_2bx4c3942499adecf48_7
   - rho_predicate_2bx4c3942499adecf48_7 <= -3
 R1325: y_7 + 1000 z_predicate_2bx22a3ae6fed0097b_7
   + rho_predicate_2bx22a3ae6fed0097b_7 <= 992
 R1326: y_7 + 1000 z_predicate_2bx22a3ae6fed0097b_7
   + rho_predicate_2bx22a3ae6fed0097b_7 >= -8
 R1327: rho_||_2dx1cb8c284b4383193_7 - rho_predicate_2dx68411627ea61c0e0_7
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_7 <= 1000
 R1328: z_||_2dx1cb8c284b4383193_7 - z_predicate_2dx68411627ea61c0e0_7
   >= 0
 R1329: - z_predicate_2dx68411627ea61c0e0_7
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_7 <= 0
 R1330: rho_||_2dx1cb8c284b4383193_7 - rho_predicate_2dx5dba1e6a7b84e365_7
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_7 <= 1000
 R1331: z_||_2dx1cb8c284b4383193_7 - z_predicate_2dx5dba1e6a7b84e365_7
   >= 0
 R1332: - z_predicate_2dx5dba1e6a7b84e365_7
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_7 <= 0
 R1333: rho_||_2dx1cb8c284b4383193_7 - rho_predicate_2bx4c3942499adecf48_7
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_7 <= 1000
 R1334: z_||_2dx1cb8c284b4383193_7 - z_predicate_2bx4c3942499adecf48_7
   >= 0
 R1335: - z_predicate_2bx4c3942499adecf48_7
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_7 <= 0
 R1336: rho_||_2dx1cb8c284b4383193_7 - rho_predicate_2bx22a3ae6fed0097b_7
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_7 <= 1000
 R1337: z_||_2dx1cb8c284b4383193_7 - z_predicate_2bx22a3ae6fed0097b_7 >= 0
 R1338: - z_predicate_2bx22a3ae6fed0097b_7
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_7 <= 0
 R1339: z_||_2dx1cb8c284b4383193_7 - z_predicate_2dx68411627ea61c0e0_7
   - z_predicate_2dx5dba1e6a7b84e365_7 - z_predicate_2bx4c3942499adecf48_7
   - z_predicate_2bx22a3ae6fed0097b_7 <= 0
 R1340: - z_||_2dx1cb8c284b4383193_7
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_7
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_7
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_7
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_7 >= 0
 R1341: x_8 - 1000 z_predicate_2dx68411627ea61c0e0_8
   - rho_predicate_2dx68411627ea61c0e0_8 >= -992
 R1342: x_8 - 1000 z_predicate_2dx68411627ea61c0e0_8
   - rho_predicate_2dx68411627ea61c0e0_8 <= 8
 R1343: x_8 + 1000 z_predicate_2dx5dba1e6a7b84e365_8
   + rho_predicate_2dx5dba1e6a7b84e365_8 <= 1003
 R1344: x_8 + 1000 z_predicate_2dx5dba1e6a7b84e365_8
   + rho_predicate_2dx5dba1e6a7b84e365_8 >= 3
 R1345: y_8 - 1000 z_predicate_2bx4c3942499adecf48_8
   - rho_predicate_2bx4c3942499adecf48_8 >= -1003
 R1346: y_8 - 1000 z_predicate_2bx4c3942499adecf48_8
   - rho_predicate_2bx4c3942499adecf48_8 <= -3
 R1347: y_8 + 1000 z_predicate_2bx22a3ae6fed0097b_8
   + rho_predicate_2bx22a3ae6fed0097b_8 <= 992
 R1348: y_8 + 1000 z_predicate_2bx22a3ae6fed0097b_8
   + rho_predicate_2bx22a3ae6fed0097b_8 >= -8
 R1349: rho_||_2dx1cb8c284b4383193_8 - rho_predicate_2dx68411627ea61c0e0_8
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_8 <= 1000
 R1350: z_||_2dx1cb8c284b4383193_8 - z_predicate_2dx68411627ea61c0e0_8
   >= 0
 R1351: - z_predicate_2dx68411627ea61c0e0_8
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_8 <= 0
 R1352: rho_||_2dx1cb8c284b4383193_8 - rho_predicate_2dx5dba1e6a7b84e365_8
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_8 <= 1000
 R1353: z_||_2dx1cb8c284b4383193_8 - z_predicate_2dx5dba1e6a7b84e365_8
   >= 0
 R1354: - z_predicate_2dx5dba1e6a7b84e365_8
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_8 <= 0
 R1355: rho_||_2dx1cb8c284b4383193_8 - rho_predicate_2bx4c3942499adecf48_8
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_8 <= 1000
 R1356: z_||_2dx1cb8c284b4383193_8 - z_predicate_2bx4c3942499adecf48_8
   >= 0
 R1357: - z_predicate_2bx4c3942499adecf48_8
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_8 <= 0
 R1358: rho_||_2dx1cb8c284b4383193_8 - rho_predicate_2bx22a3ae6fed0097b_8
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_8 <= 1000
 R1359: z_||_2dx1cb8c284b4383193_8 - z_predicate_2bx22a3ae6fed0097b_8 >= 0
 R1360: - z_predicate_2bx22a3ae6fed0097b_8
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_8 <= 0
 R1361: z_||_2dx1cb8c284b4383193_8 - z_predicate_2dx68411627ea61c0e0_8
   - z_predicate_2dx5dba1e6a7b84e365_8 - z_predicate_2bx4c3942499adecf48_8
   - z_predicate_2bx22a3ae6fed0097b_8 <= 0
 R1362: - z_||_2dx1cb8c284b4383193_8
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_8
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_8
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_8
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_8 >= 0
 R1363: x_9 - 1000 z_predicate_2dx68411627ea61c0e0_9
   - rho_predicate_2dx68411627ea61c0e0_9 >= -992
 R1364: x_9 - 1000 z_predicate_2dx68411627ea61c0e0_9
   - rho_predicate_2dx68411627ea61c0e0_9 <= 8
 R1365: x_9 + 1000 z_predicate_2dx5dba1e6a7b84e365_9
   + rho_predicate_2dx5dba1e6a7b84e365_9 <= 1003
 R1366: x_9 + 1000 z_predicate_2dx5dba1e6a7b84e365_9
   + rho_predicate_2dx5dba1e6a7b84e365_9 >= 3
 R1367: y_9 - 1000 z_predicate_2bx4c3942499adecf48_9
   - rho_predicate_2bx4c3942499adecf48_9 >= -1003
 R1368: y_9 - 1000 z_predicate_2bx4c3942499adecf48_9
   - rho_predicate_2bx4c3942499adecf48_9 <= -3
 R1369: y_9 + 1000 z_predicate_2bx22a3ae6fed0097b_9
   + rho_predicate_2bx22a3ae6fed0097b_9 <= 992
 R1370: y_9 + 1000 z_predicate_2bx22a3ae6fed0097b_9
   + rho_predicate_2bx22a3ae6fed0097b_9 >= -8
 R1371: rho_||_2dx1cb8c284b4383193_9 - rho_predicate_2dx68411627ea61c0e0_9
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_9 <= 1000
 R1372: z_||_2dx1cb8c284b4383193_9 - z_predicate_2dx68411627ea61c0e0_9
   >= 0
 R1373: - z_predicate_2dx68411627ea61c0e0_9
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_9 <= 0
 R1374: rho_||_2dx1cb8c284b4383193_9 - rho_predicate_2dx5dba1e6a7b84e365_9
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_9 <= 1000
 R1375: z_||_2dx1cb8c284b4383193_9 - z_predicate_2dx5dba1e6a7b84e365_9
   >= 0
 R1376: - z_predicate_2dx5dba1e6a7b84e365_9
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_9 <= 0
 R1377: rho_||_2dx1cb8c284b4383193_9 - rho_predicate_2bx4c3942499adecf48_9
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_9 <= 1000
 R1378: z_||_2dx1cb8c284b4383193_9 - z_predicate_2bx4c3942499adecf48_9
   >= 0
 R1379: - z_predicate_2bx4c3942499adecf48_9
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_9 <= 0
 R1380: rho_||_2dx1cb8c284b4383193_9 - rho_predicate_2bx22a3ae6fed0097b_9
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_9 <= 1000
 R1381: z_||_2dx1cb8c284b4383193_9 - z_predicate_2bx22a3ae6fed0097b_9 >= 0
 R1382: - z_predicate_2bx22a3ae6fed0097b_9
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_9 <= 0
 R1383: z_||_2dx1cb8c284b4383193_9 - z_predicate_2dx68411627ea61c0e0_9
   - z_predicate_2dx5dba1e6a7b84e365_9 - z_predicate_2bx4c3942499adecf48_9
   - z_predicate_2bx22a3ae6fed0097b_9 <= 0
 R1384: - z_||_2dx1cb8c284b4383193_9
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_9
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_9
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_9
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_9 >= 0
 R1385: x_10 - 1000 z_predicate_2dx68411627ea61c0e0_10
   - rho_predicate_2dx68411627ea61c0e0_10 >= -992
 R1386: x_10 - 1000 z_predicate_2dx68411627ea61c0e0_10
   - rho_predicate_2dx68411627ea61c0e0_10 <= 8
 R1387: x_10 + 1000 z_predicate_2dx5dba1e6a7b84e365_10
   + rho_predicate_2dx5dba1e6a7b84e365_10 <= 1003
 R1388: x_10 + 1000 z_predicate_2dx5dba1e6a7b84e365_10
   + rho_predicate_2dx5dba1e6a7b84e365_10 >= 3
 R1389: y_10 - 1000 z_predicate_2bx4c3942499adecf48_10
   - rho_predicate_2bx4c3942499adecf48_10 >= -1003
 R1390: y_10 - 1000 z_predicate_2bx4c3942499adecf48_10
   - rho_predicate_2bx4c3942499adecf48_10 <= -3
 R1391: y_10 + 1000 z_predicate_2bx22a3ae6fed0097b_10
   + rho_predicate_2bx22a3ae6fed0097b_10 <= 992
 R1392: y_10 + 1000 z_predicate_2bx22a3ae6fed0097b_10
   + rho_predicate_2bx22a3ae6fed0097b_10 >= -8
 R1393: rho_||_2dx1cb8c284b4383193_10
   - rho_predicate_2dx68411627ea61c0e0_10
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_10
   <= 1000
 R1394: z_||_2dx1cb8c284b4383193_10 - z_predicate_2dx68411627ea61c0e0_10
   >= 0
 R1395: - z_predicate_2dx68411627ea61c0e0_10
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_10 <= 0
 R1396: rho_||_2dx1cb8c284b4383193_10
   - rho_predicate_2dx5dba1e6a7b84e365_10
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_10
   <= 1000
 R1397: z_||_2dx1cb8c284b4383193_10 - z_predicate_2dx5dba1e6a7b84e365_10
   >= 0
 R1398: - z_predicate_2dx5dba1e6a7b84e365_10
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_10 <= 0
 R1399: rho_||_2dx1cb8c284b4383193_10
   - rho_predicate_2bx4c3942499adecf48_10
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_10
   <= 1000
 R1400: z_||_2dx1cb8c284b4383193_10 - z_predicate_2bx4c3942499adecf48_10
   >= 0
 R1401: - z_predicate_2bx4c3942499adecf48_10
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_10 <= 0
 R1402: rho_||_2dx1cb8c284b4383193_10 - rho_predicate_2bx22a3ae6fed0097b_10
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_10 <= 1000
 R1403: z_||_2dx1cb8c284b4383193_10 - z_predicate_2bx22a3ae6fed0097b_10
   >= 0
 R1404: - z_predicate_2bx22a3ae6fed0097b_10
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_10 <= 0
 R1405: z_||_2dx1cb8c284b4383193_10 - z_predicate_2dx68411627ea61c0e0_10
   - z_predicate_2dx5dba1e6a7b84e365_10
   - z_predicate_2bx4c3942499adecf48_10 - z_predicate_2bx22a3ae6fed0097b_10
   <= 0
 R1406: - z_||_2dx1cb8c284b4383193_10
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_10
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_10
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_10
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_10 >= 0
 R1407: x_11 - 1000 z_predicate_2dx68411627ea61c0e0_11
   - rho_predicate_2dx68411627ea61c0e0_11 >= -992
 R1408: x_11 - 1000 z_predicate_2dx68411627ea61c0e0_11
   - rho_predicate_2dx68411627ea61c0e0_11 <= 8
 R1409: x_11 + 1000 z_predicate_2dx5dba1e6a7b84e365_11
   + rho_predicate_2dx5dba1e6a7b84e365_11 <= 1003
 R1410: x_11 + 1000 z_predicate_2dx5dba1e6a7b84e365_11
   + rho_predicate_2dx5dba1e6a7b84e365_11 >= 3
 R1411: y_11 - 1000 z_predicate_2bx4c3942499adecf48_11
   - rho_predicate_2bx4c3942499adecf48_11 >= -1003
 R1412: y_11 - 1000 z_predicate_2bx4c3942499adecf48_11
   - rho_predicate_2bx4c3942499adecf48_11 <= -3
 R1413: y_11 + 1000 z_predicate_2bx22a3ae6fed0097b_11
   + rho_predicate_2bx22a3ae6fed0097b_11 <= 992
 R1414: y_11 + 1000 z_predicate_2bx22a3ae6fed0097b_11
   + rho_predicate_2bx22a3ae6fed0097b_11 >= -8
 R1415: rho_||_2dx1cb8c284b4383193_11
   - rho_predicate_2dx68411627ea61c0e0_11
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_11
   <= 1000
 R1416: z_||_2dx1cb8c284b4383193_11 - z_predicate_2dx68411627ea61c0e0_11
   >= 0
 R1417: - z_predicate_2dx68411627ea61c0e0_11
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_11 <= 0
 R1418: rho_||_2dx1cb8c284b4383193_11
   - rho_predicate_2dx5dba1e6a7b84e365_11
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_11
   <= 1000
 R1419: z_||_2dx1cb8c284b4383193_11 - z_predicate_2dx5dba1e6a7b84e365_11
   >= 0
 R1420: - z_predicate_2dx5dba1e6a7b84e365_11
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_11 <= 0
 R1421: rho_||_2dx1cb8c284b4383193_11
   - rho_predicate_2bx4c3942499adecf48_11
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_11
   <= 1000
 R1422: z_||_2dx1cb8c284b4383193_11 - z_predicate_2bx4c3942499adecf48_11
   >= 0
 R1423: - z_predicate_2bx4c3942499adecf48_11
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_11 <= 0
 R1424: rho_||_2dx1cb8c284b4383193_11 - rho_predicate_2bx22a3ae6fed0097b_11
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_11 <= 1000
 R1425: z_||_2dx1cb8c284b4383193_11 - z_predicate_2bx22a3ae6fed0097b_11
   >= 0
 R1426: - z_predicate_2bx22a3ae6fed0097b_11
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_11 <= 0
 R1427: z_||_2dx1cb8c284b4383193_11 - z_predicate_2dx68411627ea61c0e0_11
   - z_predicate_2dx5dba1e6a7b84e365_11
   - z_predicate_2bx4c3942499adecf48_11 - z_predicate_2bx22a3ae6fed0097b_11
   <= 0
 R1428: - z_||_2dx1cb8c284b4383193_11
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_11
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_11
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_11
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_11 >= 0
 R1429: x_12 - 1000 z_predicate_2dx68411627ea61c0e0_12
   - rho_predicate_2dx68411627ea61c0e0_12 >= -992
 R1430: x_12 - 1000 z_predicate_2dx68411627ea61c0e0_12
   - rho_predicate_2dx68411627ea61c0e0_12 <= 8
 R1431: x_12 + 1000 z_predicate_2dx5dba1e6a7b84e365_12
   + rho_predicate_2dx5dba1e6a7b84e365_12 <= 1003
 R1432: x_12 + 1000 z_predicate_2dx5dba1e6a7b84e365_12
   + rho_predicate_2dx5dba1e6a7b84e365_12 >= 3
 R1433: y_12 - 1000 z_predicate_2bx4c3942499adecf48_12
   - rho_predicate_2bx4c3942499adecf48_12 >= -1003
 R1434: y_12 - 1000 z_predicate_2bx4c3942499adecf48_12
   - rho_predicate_2bx4c3942499adecf48_12 <= -3
 R1435: y_12 + 1000 z_predicate_2bx22a3ae6fed0097b_12
   + rho_predicate_2bx22a3ae6fed0097b_12 <= 992
 R1436: y_12 + 1000 z_predicate_2bx22a3ae6fed0097b_12
   + rho_predicate_2bx22a3ae6fed0097b_12 >= -8
 R1437: rho_||_2dx1cb8c284b4383193_12
   - rho_predicate_2dx68411627ea61c0e0_12
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_12
   <= 1000
 R1438: z_||_2dx1cb8c284b4383193_12 - z_predicate_2dx68411627ea61c0e0_12
   >= 0
 R1439: - z_predicate_2dx68411627ea61c0e0_12
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_12 <= 0
 R1440: rho_||_2dx1cb8c284b4383193_12
   - rho_predicate_2dx5dba1e6a7b84e365_12
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_12
   <= 1000
 R1441: z_||_2dx1cb8c284b4383193_12 - z_predicate_2dx5dba1e6a7b84e365_12
   >= 0
 R1442: - z_predicate_2dx5dba1e6a7b84e365_12
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_12 <= 0
 R1443: rho_||_2dx1cb8c284b4383193_12
   - rho_predicate_2bx4c3942499adecf48_12
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_12
   <= 1000
 R1444: z_||_2dx1cb8c284b4383193_12 - z_predicate_2bx4c3942499adecf48_12
   >= 0
 R1445: - z_predicate_2bx4c3942499adecf48_12
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_12 <= 0
 R1446: rho_||_2dx1cb8c284b4383193_12 - rho_predicate_2bx22a3ae6fed0097b_12
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_12 <= 1000
 R1447: z_||_2dx1cb8c284b4383193_12 - z_predicate_2bx22a3ae6fed0097b_12
   >= 0
 R1448: - z_predicate_2bx22a3ae6fed0097b_12
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_12 <= 0
 R1449: z_||_2dx1cb8c284b4383193_12 - z_predicate_2dx68411627ea61c0e0_12
   - z_predicate_2dx5dba1e6a7b84e365_12
   - z_predicate_2bx4c3942499adecf48_12 - z_predicate_2bx22a3ae6fed0097b_12
   <= 0
 R1450: - z_||_2dx1cb8c284b4383193_12
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_12
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_12
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_12
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_12 >= 0
 R1451: x_13 - 1000 z_predicate_2dx68411627ea61c0e0_13
   - rho_predicate_2dx68411627ea61c0e0_13 >= -992
 R1452: x_13 - 1000 z_predicate_2dx68411627ea61c0e0_13
   - rho_predicate_2dx68411627ea61c0e0_13 <= 8
 R1453: x_13 + 1000 z_predicate_2dx5dba1e6a7b84e365_13
   + rho_predicate_2dx5dba1e6a7b84e365_13 <= 1003
 R1454: x_13 + 1000 z_predicate_2dx5dba1e6a7b84e365_13
   + rho_predicate_2dx5dba1e6a7b84e365_13 >= 3
 R1455: y_13 - 1000 z_predicate_2bx4c3942499adecf48_13
   - rho_predicate_2bx4c3942499adecf48_13 >= -1003
 R1456: y_13 - 1000 z_predicate_2bx4c3942499adecf48_13
   - rho_predicate_2bx4c3942499adecf48_13 <= -3
 R1457: y_13 + 1000 z_predicate_2bx22a3ae6fed0097b_13
   + rho_predicate_2bx22a3ae6fed0097b_13 <= 992
 R1458: y_13 + 1000 z_predicate_2bx22a3ae6fed0097b_13
   + rho_predicate_2bx22a3ae6fed0097b_13 >= -8
 R1459: rho_||_2dx1cb8c284b4383193_13
   - rho_predicate_2dx68411627ea61c0e0_13
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_13
   <= 1000
 R1460: z_||_2dx1cb8c284b4383193_13 - z_predicate_2dx68411627ea61c0e0_13
   >= 0
 R1461: - z_predicate_2dx68411627ea61c0e0_13
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_13 <= 0
 R1462: rho_||_2dx1cb8c284b4383193_13
   - rho_predicate_2dx5dba1e6a7b84e365_13
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_13
   <= 1000
 R1463: z_||_2dx1cb8c284b4383193_13 - z_predicate_2dx5dba1e6a7b84e365_13
   >= 0
 R1464: - z_predicate_2dx5dba1e6a7b84e365_13
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_13 <= 0
 R1465: rho_||_2dx1cb8c284b4383193_13
   - rho_predicate_2bx4c3942499adecf48_13
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_13
   <= 1000
 R1466: z_||_2dx1cb8c284b4383193_13 - z_predicate_2bx4c3942499adecf48_13
   >= 0
 R1467: - z_predicate_2bx4c3942499adecf48_13
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_13 <= 0
 R1468: rho_||_2dx1cb8c284b4383193_13 - rho_predicate_2bx22a3ae6fed0097b_13
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_13 <= 1000
 R1469: z_||_2dx1cb8c284b4383193_13 - z_predicate_2bx22a3ae6fed0097b_13
   >= 0
 R1470: - z_predicate_2bx22a3ae6fed0097b_13
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_13 <= 0
 R1471: z_||_2dx1cb8c284b4383193_13 - z_predicate_2dx68411627ea61c0e0_13
   - z_predicate_2dx5dba1e6a7b84e365_13
   - z_predicate_2bx4c3942499adecf48_13 - z_predicate_2bx22a3ae6fed0097b_13
   <= 0
 R1472: - z_||_2dx1cb8c284b4383193_13
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_13
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_13
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_13
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_13 >= 0
 R1473: x_14 - 1000 z_predicate_2dx68411627ea61c0e0_14
   - rho_predicate_2dx68411627ea61c0e0_14 >= -992
 R1474: x_14 - 1000 z_predicate_2dx68411627ea61c0e0_14
   - rho_predicate_2dx68411627ea61c0e0_14 <= 8
 R1475: x_14 + 1000 z_predicate_2dx5dba1e6a7b84e365_14
   + rho_predicate_2dx5dba1e6a7b84e365_14 <= 1003
 R1476: x_14 + 1000 z_predicate_2dx5dba1e6a7b84e365_14
   + rho_predicate_2dx5dba1e6a7b84e365_14 >= 3
 R1477: y_14 - 1000 z_predicate_2bx4c3942499adecf48_14
   - rho_predicate_2bx4c3942499adecf48_14 >= -1003
 R1478: y_14 - 1000 z_predicate_2bx4c3942499adecf48_14
   - rho_predicate_2bx4c3942499adecf48_14 <= -3
 R1479: y_14 + 1000 z_predicate_2bx22a3ae6fed0097b_14
   + rho_predicate_2bx22a3ae6fed0097b_14 <= 992
 R1480: y_14 + 1000 z_predicate_2bx22a3ae6fed0097b_14
   + rho_predicate_2bx22a3ae6fed0097b_14 >= -8
 R1481: rho_||_2dx1cb8c284b4383193_14
   - rho_predicate_2dx68411627ea61c0e0_14
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_14
   <= 1000
 R1482: z_||_2dx1cb8c284b4383193_14 - z_predicate_2dx68411627ea61c0e0_14
   >= 0
 R1483: - z_predicate_2dx68411627ea61c0e0_14
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_14 <= 0
 R1484: rho_||_2dx1cb8c284b4383193_14
   - rho_predicate_2dx5dba1e6a7b84e365_14
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_14
   <= 1000
 R1485: z_||_2dx1cb8c284b4383193_14 - z_predicate_2dx5dba1e6a7b84e365_14
   >= 0
 R1486: - z_predicate_2dx5dba1e6a7b84e365_14
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_14 <= 0
 R1487: rho_||_2dx1cb8c284b4383193_14
   - rho_predicate_2bx4c3942499adecf48_14
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_14
   <= 1000
 R1488: z_||_2dx1cb8c284b4383193_14 - z_predicate_2bx4c3942499adecf48_14
   >= 0
 R1489: - z_predicate_2bx4c3942499adecf48_14
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_14 <= 0
 R1490: rho_||_2dx1cb8c284b4383193_14 - rho_predicate_2bx22a3ae6fed0097b_14
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_14 <= 1000
 R1491: z_||_2dx1cb8c284b4383193_14 - z_predicate_2bx22a3ae6fed0097b_14
   >= 0
 R1492: - z_predicate_2bx22a3ae6fed0097b_14
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_14 <= 0
 R1493: z_||_2dx1cb8c284b4383193_14 - z_predicate_2dx68411627ea61c0e0_14
   - z_predicate_2dx5dba1e6a7b84e365_14
   - z_predicate_2bx4c3942499adecf48_14 - z_predicate_2bx22a3ae6fed0097b_14
   <= 0
 R1494: - z_||_2dx1cb8c284b4383193_14
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_14
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_14
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_14
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_14 >= 0
 R1495: x_15 - 1000 z_predicate_2dx68411627ea61c0e0_15
   - rho_predicate_2dx68411627ea61c0e0_15 >= -992
 R1496: x_15 - 1000 z_predicate_2dx68411627ea61c0e0_15
   - rho_predicate_2dx68411627ea61c0e0_15 <= 8
 R1497: x_15 + 1000 z_predicate_2dx5dba1e6a7b84e365_15
   + rho_predicate_2dx5dba1e6a7b84e365_15 <= 1003
 R1498: x_15 + 1000 z_predicate_2dx5dba1e6a7b84e365_15
   + rho_predicate_2dx5dba1e6a7b84e365_15 >= 3
 R1499: y_15 - 1000 z_predicate_2bx4c3942499adecf48_15
   - rho_predicate_2bx4c3942499adecf48_15 >= -1003
 R1500: y_15 - 1000 z_predicate_2bx4c3942499adecf48_15
   - rho_predicate_2bx4c3942499adecf48_15 <= -3
 R1501: y_15 + 1000 z_predicate_2bx22a3ae6fed0097b_15
   + rho_predicate_2bx22a3ae6fed0097b_15 <= 992
 R1502: y_15 + 1000 z_predicate_2bx22a3ae6fed0097b_15
   + rho_predicate_2bx22a3ae6fed0097b_15 >= -8
 R1503: rho_||_2dx1cb8c284b4383193_15
   - rho_predicate_2dx68411627ea61c0e0_15
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_15
   <= 1000
 R1504: z_||_2dx1cb8c284b4383193_15 - z_predicate_2dx68411627ea61c0e0_15
   >= 0
 R1505: - z_predicate_2dx68411627ea61c0e0_15
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_15 <= 0
 R1506: rho_||_2dx1cb8c284b4383193_15
   - rho_predicate_2dx5dba1e6a7b84e365_15
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_15
   <= 1000
 R1507: z_||_2dx1cb8c284b4383193_15 - z_predicate_2dx5dba1e6a7b84e365_15
   >= 0
 R1508: - z_predicate_2dx5dba1e6a7b84e365_15
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_15 <= 0
 R1509: rho_||_2dx1cb8c284b4383193_15
   - rho_predicate_2bx4c3942499adecf48_15
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_15
   <= 1000
 R1510: z_||_2dx1cb8c284b4383193_15 - z_predicate_2bx4c3942499adecf48_15
   >= 0
 R1511: - z_predicate_2bx4c3942499adecf48_15
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_15 <= 0
 R1512: rho_||_2dx1cb8c284b4383193_15 - rho_predicate_2bx22a3ae6fed0097b_15
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_15 <= 1000
 R1513: z_||_2dx1cb8c284b4383193_15 - z_predicate_2bx22a3ae6fed0097b_15
   >= 0
 R1514: - z_predicate_2bx22a3ae6fed0097b_15
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_15 <= 0
 R1515: z_||_2dx1cb8c284b4383193_15 - z_predicate_2dx68411627ea61c0e0_15
   - z_predicate_2dx5dba1e6a7b84e365_15
   - z_predicate_2bx4c3942499adecf48_15 - z_predicate_2bx22a3ae6fed0097b_15
   <= 0
 R1516: - z_||_2dx1cb8c284b4383193_15
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_15
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_15
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_15
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_15 >= 0
 R1517: x_16 - 1000 z_predicate_2dx68411627ea61c0e0_16
   - rho_predicate_2dx68411627ea61c0e0_16 >= -992
 R1518: x_16 - 1000 z_predicate_2dx68411627ea61c0e0_16
   - rho_predicate_2dx68411627ea61c0e0_16 <= 8
 R1519: x_16 + 1000 z_predicate_2dx5dba1e6a7b84e365_16
   + rho_predicate_2dx5dba1e6a7b84e365_16 <= 1003
 R1520: x_16 + 1000 z_predicate_2dx5dba1e6a7b84e365_16
   + rho_predicate_2dx5dba1e6a7b84e365_16 >= 3
 R1521: y_16 - 1000 z_predicate_2bx4c3942499adecf48_16
   - rho_predicate_2bx4c3942499adecf48_16 >= -1003
 R1522: y_16 - 1000 z_predicate_2bx4c3942499adecf48_16
   - rho_predicate_2bx4c3942499adecf48_16 <= -3
 R1523: y_16 + 1000 z_predicate_2bx22a3ae6fed0097b_16
   + rho_predicate_2bx22a3ae6fed0097b_16 <= 992
 R1524: y_16 + 1000 z_predicate_2bx22a3ae6fed0097b_16
   + rho_predicate_2bx22a3ae6fed0097b_16 >= -8
 R1525: rho_||_2dx1cb8c284b4383193_16
   - rho_predicate_2dx68411627ea61c0e0_16
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_16
   <= 1000
 R1526: z_||_2dx1cb8c284b4383193_16 - z_predicate_2dx68411627ea61c0e0_16
   >= 0
 R1527: - z_predicate_2dx68411627ea61c0e0_16
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_16 <= 0
 R1528: rho_||_2dx1cb8c284b4383193_16
   - rho_predicate_2dx5dba1e6a7b84e365_16
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_16
   <= 1000
 R1529: z_||_2dx1cb8c284b4383193_16 - z_predicate_2dx5dba1e6a7b84e365_16
   >= 0
 R1530: - z_predicate_2dx5dba1e6a7b84e365_16
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_16 <= 0
 R1531: rho_||_2dx1cb8c284b4383193_16
   - rho_predicate_2bx4c3942499adecf48_16
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_16
   <= 1000
 R1532: z_||_2dx1cb8c284b4383193_16 - z_predicate_2bx4c3942499adecf48_16
   >= 0
 R1533: - z_predicate_2bx4c3942499adecf48_16
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_16 <= 0
 R1534: rho_||_2dx1cb8c284b4383193_16 - rho_predicate_2bx22a3ae6fed0097b_16
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_16 <= 1000
 R1535: z_||_2dx1cb8c284b4383193_16 - z_predicate_2bx22a3ae6fed0097b_16
   >= 0
 R1536: - z_predicate_2bx22a3ae6fed0097b_16
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_16 <= 0
 R1537: z_||_2dx1cb8c284b4383193_16 - z_predicate_2dx68411627ea61c0e0_16
   - z_predicate_2dx5dba1e6a7b84e365_16
   - z_predicate_2bx4c3942499adecf48_16 - z_predicate_2bx22a3ae6fed0097b_16
   <= 0
 R1538: - z_||_2dx1cb8c284b4383193_16
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_16
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_16
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_16
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_16 >= 0
 R1539: x_17 - 1000 z_predicate_2dx68411627ea61c0e0_17
   - rho_predicate_2dx68411627ea61c0e0_17 >= -992
 R1540: x_17 - 1000 z_predicate_2dx68411627ea61c0e0_17
   - rho_predicate_2dx68411627ea61c0e0_17 <= 8
 R1541: x_17 + 1000 z_predicate_2dx5dba1e6a7b84e365_17
   + rho_predicate_2dx5dba1e6a7b84e365_17 <= 1003
 R1542: x_17 + 1000 z_predicate_2dx5dba1e6a7b84e365_17
   + rho_predicate_2dx5dba1e6a7b84e365_17 >= 3
 R1543: y_17 - 1000 z_predicate_2bx4c3942499adecf48_17
   - rho_predicate_2bx4c3942499adecf48_17 >= -1003
 R1544: y_17 - 1000 z_predicate_2bx4c3942499adecf48_17
   - rho_predicate_2bx4c3942499adecf48_17 <= -3
 R1545: y_17 + 1000 z_predicate_2bx22a3ae6fed0097b_17
   + rho_predicate_2bx22a3ae6fed0097b_17 <= 992
 R1546: y_17 + 1000 z_predicate_2bx22a3ae6fed0097b_17
   + rho_predicate_2bx22a3ae6fed0097b_17 >= -8
 R1547: rho_||_2dx1cb8c284b4383193_17
   - rho_predicate_2dx68411627ea61c0e0_17
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_17
   <= 1000
 R1548: z_||_2dx1cb8c284b4383193_17 - z_predicate_2dx68411627ea61c0e0_17
   >= 0
 R1549: - z_predicate_2dx68411627ea61c0e0_17
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_17 <= 0
 R1550: rho_||_2dx1cb8c284b4383193_17
   - rho_predicate_2dx5dba1e6a7b84e365_17
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_17
   <= 1000
 R1551: z_||_2dx1cb8c284b4383193_17 - z_predicate_2dx5dba1e6a7b84e365_17
   >= 0
 R1552: - z_predicate_2dx5dba1e6a7b84e365_17
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_17 <= 0
 R1553: rho_||_2dx1cb8c284b4383193_17
   - rho_predicate_2bx4c3942499adecf48_17
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_17
   <= 1000
 R1554: z_||_2dx1cb8c284b4383193_17 - z_predicate_2bx4c3942499adecf48_17
   >= 0
 R1555: - z_predicate_2bx4c3942499adecf48_17
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_17 <= 0
 R1556: rho_||_2dx1cb8c284b4383193_17 - rho_predicate_2bx22a3ae6fed0097b_17
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_17 <= 1000
 R1557: z_||_2dx1cb8c284b4383193_17 - z_predicate_2bx22a3ae6fed0097b_17
   >= 0
 R1558: - z_predicate_2bx22a3ae6fed0097b_17
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_17 <= 0
 R1559: z_||_2dx1cb8c284b4383193_17 - z_predicate_2dx68411627ea61c0e0_17
   - z_predicate_2dx5dba1e6a7b84e365_17
   - z_predicate_2bx4c3942499adecf48_17 - z_predicate_2bx22a3ae6fed0097b_17
   <= 0
 R1560: - z_||_2dx1cb8c284b4383193_17
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_17
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_17
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_17
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_17 >= 0
 R1561: x_18 - 1000 z_predicate_2dx68411627ea61c0e0_18
   - rho_predicate_2dx68411627ea61c0e0_18 >= -992
 R1562: x_18 - 1000 z_predicate_2dx68411627ea61c0e0_18
   - rho_predicate_2dx68411627ea61c0e0_18 <= 8
 R1563: x_18 + 1000 z_predicate_2dx5dba1e6a7b84e365_18
   + rho_predicate_2dx5dba1e6a7b84e365_18 <= 1003
 R1564: x_18 + 1000 z_predicate_2dx5dba1e6a7b84e365_18
   + rho_predicate_2dx5dba1e6a7b84e365_18 >= 3
 R1565: y_18 - 1000 z_predicate_2bx4c3942499adecf48_18
   - rho_predicate_2bx4c3942499adecf48_18 >= -1003
 R1566: y_18 - 1000 z_predicate_2bx4c3942499adecf48_18
   - rho_predicate_2bx4c3942499adecf48_18 <= -3
 R1567: y_18 + 1000 z_predicate_2bx22a3ae6fed0097b_18
   + rho_predicate_2bx22a3ae6fed0097b_18 <= 992
 R1568: y_18 + 1000 z_predicate_2bx22a3ae6fed0097b_18
   + rho_predicate_2bx22a3ae6fed0097b_18 >= -8
 R1569: rho_||_2dx1cb8c284b4383193_18
   - rho_predicate_2dx68411627ea61c0e0_18
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_18
   <= 1000
 R1570: z_||_2dx1cb8c284b4383193_18 - z_predicate_2dx68411627ea61c0e0_18
   >= 0
 R1571: - z_predicate_2dx68411627ea61c0e0_18
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_18 <= 0
 R1572: rho_||_2dx1cb8c284b4383193_18
   - rho_predicate_2dx5dba1e6a7b84e365_18
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_18
   <= 1000
 R1573: z_||_2dx1cb8c284b4383193_18 - z_predicate_2dx5dba1e6a7b84e365_18
   >= 0
 R1574: - z_predicate_2dx5dba1e6a7b84e365_18
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_18 <= 0
 R1575: rho_||_2dx1cb8c284b4383193_18
   - rho_predicate_2bx4c3942499adecf48_18
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_18
   <= 1000
 R1576: z_||_2dx1cb8c284b4383193_18 - z_predicate_2bx4c3942499adecf48_18
   >= 0
 R1577: - z_predicate_2bx4c3942499adecf48_18
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_18 <= 0
 R1578: rho_||_2dx1cb8c284b4383193_18 - rho_predicate_2bx22a3ae6fed0097b_18
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_18 <= 1000
 R1579: z_||_2dx1cb8c284b4383193_18 - z_predicate_2bx22a3ae6fed0097b_18
   >= 0
 R1580: - z_predicate_2bx22a3ae6fed0097b_18
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_18 <= 0
 R1581: z_||_2dx1cb8c284b4383193_18 - z_predicate_2dx68411627ea61c0e0_18
   - z_predicate_2dx5dba1e6a7b84e365_18
   - z_predicate_2bx4c3942499adecf48_18 - z_predicate_2bx22a3ae6fed0097b_18
   <= 0
 R1582: - z_||_2dx1cb8c284b4383193_18
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_18
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_18
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_18
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_18 >= 0
 R1583: x_19 - 1000 z_predicate_2dx68411627ea61c0e0_19
   - rho_predicate_2dx68411627ea61c0e0_19 >= -992
 R1584: x_19 - 1000 z_predicate_2dx68411627ea61c0e0_19
   - rho_predicate_2dx68411627ea61c0e0_19 <= 8
 R1585: x_19 + 1000 z_predicate_2dx5dba1e6a7b84e365_19
   + rho_predicate_2dx5dba1e6a7b84e365_19 <= 1003
 R1586: x_19 + 1000 z_predicate_2dx5dba1e6a7b84e365_19
   + rho_predicate_2dx5dba1e6a7b84e365_19 >= 3
 R1587: y_19 - 1000 z_predicate_2bx4c3942499adecf48_19
   - rho_predicate_2bx4c3942499adecf48_19 >= -1003
 R1588: y_19 - 1000 z_predicate_2bx4c3942499adecf48_19
   - rho_predicate_2bx4c3942499adecf48_19 <= -3
 R1589: y_19 + 1000 z_predicate_2bx22a3ae6fed0097b_19
   + rho_predicate_2bx22a3ae6fed0097b_19 <= 992
 R1590: y_19 + 1000 z_predicate_2bx22a3ae6fed0097b_19
   + rho_predicate_2bx22a3ae6fed0097b_19 >= -8
 R1591: rho_||_2dx1cb8c284b4383193_19
   - rho_predicate_2dx68411627ea61c0e0_19
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_19
   <= 1000
 R1592: z_||_2dx1cb8c284b4383193_19 - z_predicate_2dx68411627ea61c0e0_19
   >= 0
 R1593: - z_predicate_2dx68411627ea61c0e0_19
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_19 <= 0
 R1594: rho_||_2dx1cb8c284b4383193_19
   - rho_predicate_2dx5dba1e6a7b84e365_19
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_19
   <= 1000
 R1595: z_||_2dx1cb8c284b4383193_19 - z_predicate_2dx5dba1e6a7b84e365_19
   >= 0
 R1596: - z_predicate_2dx5dba1e6a7b84e365_19
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_19 <= 0
 R1597: rho_||_2dx1cb8c284b4383193_19
   - rho_predicate_2bx4c3942499adecf48_19
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_19
   <= 1000
 R1598: z_||_2dx1cb8c284b4383193_19 - z_predicate_2bx4c3942499adecf48_19
   >= 0
 R1599: - z_predicate_2bx4c3942499adecf48_19
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_19 <= 0
 R1600: rho_||_2dx1cb8c284b4383193_19 - rho_predicate_2bx22a3ae6fed0097b_19
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_19 <= 1000
 R1601: z_||_2dx1cb8c284b4383193_19 - z_predicate_2bx22a3ae6fed0097b_19
   >= 0
 R1602: - z_predicate_2bx22a3ae6fed0097b_19
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_19 <= 0
 R1603: z_||_2dx1cb8c284b4383193_19 - z_predicate_2dx68411627ea61c0e0_19
   - z_predicate_2dx5dba1e6a7b84e365_19
   - z_predicate_2bx4c3942499adecf48_19 - z_predicate_2bx22a3ae6fed0097b_19
   <= 0
 R1604: - z_||_2dx1cb8c284b4383193_19
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_19
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_19
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_19
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_19 >= 0
 R1605: x_20 - 1000 z_predicate_2dx68411627ea61c0e0_20
   - rho_predicate_2dx68411627ea61c0e0_20 >= -992
 R1606: x_20 - 1000 z_predicate_2dx68411627ea61c0e0_20
   - rho_predicate_2dx68411627ea61c0e0_20 <= 8
 R1607: x_20 + 1000 z_predicate_2dx5dba1e6a7b84e365_20
   + rho_predicate_2dx5dba1e6a7b84e365_20 <= 1003
 R1608: x_20 + 1000 z_predicate_2dx5dba1e6a7b84e365_20
   + rho_predicate_2dx5dba1e6a7b84e365_20 >= 3
 R1609: y_20 - 1000 z_predicate_2bx4c3942499adecf48_20
   - rho_predicate_2bx4c3942499adecf48_20 >= -1003
 R1610: y_20 - 1000 z_predicate_2bx4c3942499adecf48_20
   - rho_predicate_2bx4c3942499adecf48_20 <= -3
 R1611: y_20 + 1000 z_predicate_2bx22a3ae6fed0097b_20
   + rho_predicate_2bx22a3ae6fed0097b_20 <= 992
 R1612: y_20 + 1000 z_predicate_2bx22a3ae6fed0097b_20
   + rho_predicate_2bx22a3ae6fed0097b_20 >= -8
 R1613: rho_||_2dx1cb8c284b4383193_20
   - rho_predicate_2dx68411627ea61c0e0_20
   + 1000 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_20
   <= 1000
 R1614: z_||_2dx1cb8c284b4383193_20 - z_predicate_2dx68411627ea61c0e0_20
   >= 0
 R1615: - z_predicate_2dx68411627ea61c0e0_20
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_20 <= 0
 R1616: rho_||_2dx1cb8c284b4383193_20
   - rho_predicate_2dx5dba1e6a7b84e365_20
   + 1000 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_20
   <= 1000
 R1617: z_||_2dx1cb8c284b4383193_20 - z_predicate_2dx5dba1e6a7b84e365_20
   >= 0
 R1618: - z_predicate_2dx5dba1e6a7b84e365_20
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_20 <= 0
 R1619: rho_||_2dx1cb8c284b4383193_20
   - rho_predicate_2bx4c3942499adecf48_20
   + 1000 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_20
   <= 1000
 R1620: z_||_2dx1cb8c284b4383193_20 - z_predicate_2bx4c3942499adecf48_20
   >= 0
 R1621: - z_predicate_2bx4c3942499adecf48_20
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_20 <= 0
 R1622: rho_||_2dx1cb8c284b4383193_20 - rho_predicate_2bx22a3ae6fed0097b_20
   + 1000 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_20 <= 1000
 R1623: z_||_2dx1cb8c284b4383193_20 - z_predicate_2bx22a3ae6fed0097b_20
   >= 0
 R1624: - z_predicate_2bx22a3ae6fed0097b_20
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_20 <= 0
 R1625: z_||_2dx1cb8c284b4383193_20 - z_predicate_2dx68411627ea61c0e0_20
   - z_predicate_2dx5dba1e6a7b84e365_20
   - z_predicate_2bx4c3942499adecf48_20 - z_predicate_2bx22a3ae6fed0097b_20
   <= 0
 R1626: - z_||_2dx1cb8c284b4383193_20
   + zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_20
   + zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_20
   + zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_20
   + zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_20 >= 0
 R1627: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_0 <= 0
 R1628: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_0 <= 0
 R1629: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_1 <= 0
 R1630: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_1 <= 0
 R1631: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_2 <= 0
 R1632: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_2 <= 0
 R1633: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_3 <= 0
 R1634: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_3 <= 0
 R1635: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_4 <= 0
 R1636: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_4 <= 0
 R1637: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_5 <= 0
 R1638: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_5 <= 0
 R1639: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_6 <= 0
 R1640: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_6 <= 0
 R1641: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_7 <= 0
 R1642: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_7 <= 0
 R1643: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_8 <= 0
 R1644: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_8 <= 0
 R1645: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_9 <= 0
 R1646: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_9 <= 0
 R1647: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_10 <= 0
 R1648: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_10 <= 0
 R1649: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_11 <= 0
 R1650: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_11 <= 0
 R1651: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_12 <= 0
 R1652: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_12 <= 0
 R1653: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_13 <= 0
 R1654: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_13 <= 0
 R1655: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_14 <= 0
 R1656: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_14 <= 0
 R1657: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_15 <= 0
 R1658: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_15 <= 0
 R1659: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_16 <= 0
 R1660: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_16 <= 0
 R1661: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_17 <= 0
 R1662: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_17 <= 0
 R1663: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_18 <= 0
 R1664: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_18 <= 0
 R1665: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_19 <= 0
 R1666: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_19 <= 0
 R1667: rho_G_2bx7d3b4be48ae7738c_0 - rho_||_2dx1cb8c284b4383193_20 <= 0
 R1668: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_20 <= 0
 R1669: z_G_2bx7d3b4be48ae7738c_0 - z_||_2dx1cb8c284b4383193_0
   - z_||_2dx1cb8c284b4383193_1 - z_||_2dx1cb8c284b4383193_2
   - z_||_2dx1cb8c284b4383193_3 - z_||_2dx1cb8c284b4383193_4
   - z_||_2dx1cb8c284b4383193_5 - z_||_2dx1cb8c284b4383193_6
   - z_||_2dx1cb8c284b4383193_7 - z_||_2dx1cb8c284b4383193_8
   - z_||_2dx1cb8c284b4383193_9 - z_||_2dx1cb8c284b4383193_10
   - z_||_2dx1cb8c284b4383193_11 - z_||_2dx1cb8c284b4383193_12
   - z_||_2dx1cb8c284b4383193_13 - z_||_2dx1cb8c284b4383193_14
   - z_||_2dx1cb8c284b4383193_15 - z_||_2dx1cb8c284b4383193_16
   - z_||_2dx1cb8c284b4383193_17 - z_||_2dx1cb8c284b4383193_18
   - z_||_2dx1cb8c284b4383193_19 - z_||_2dx1cb8c284b4383193_20 >= -20
 R1670: rho_&&_2bx41f61981721fa2dd_0 - 0.5 rho_G_2bx1635c42e821daeea_0
   <= 0
 R1671: z_&&_2bx41f61981721fa2dd_0 - z_G_2bx1635c42e821daeea_0 <= 0
 R1672: rho_&&_2bx41f61981721fa2dd_0 - 0.1 rho_G_2bx1fbb236baa38c772_0
   <= 0
 R1673: z_&&_2bx41f61981721fa2dd_0 - z_G_2bx1fbb236baa38c772_0 <= 0
 R1674: rho_&&_2bx41f61981721fa2dd_0 - 0.5 rho_G_2bx1e250240efa087ae_0
   <= 0
 R1675: z_&&_2bx41f61981721fa2dd_0 - z_G_2bx1e250240efa087ae_0 <= 0
 R1676: rho_&&_2bx41f61981721fa2dd_0 - 0.5 rho_G_2bx7d3b4be48ae7738c_0
   <= 0
 R1677: z_&&_2bx41f61981721fa2dd_0 - z_G_2bx7d3b4be48ae7738c_0 <= 0
 R1678: z_&&_2bx41f61981721fa2dd_0 - z_G_2bx1635c42e821daeea_0
   - z_G_2bx1fbb236baa38c772_0 - z_G_2bx1e250240efa087ae_0
   - z_G_2bx7d3b4be48ae7738c_0 >= -3
 formula_satisfaction: z_&&_2bx41f61981721fa2dd_0 = 1
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
 -9 <= x_19 <= 9
 -9 <= y_19 <= 9
 -9 <= z_19 <= 9
 -3 <= u_19 <= 3
 -3 <= v_19 <= 3
 -3 <= w_19 <= 3
 -9 <= x_20 <= 9
 -9 <= y_20 <= 9
 -9 <= z_20 <= 9
 -3 <= u_20 <= 3
 -3 <= v_20 <= 3
 -3 <= w_20 <= 3
 z_&&_2bx41f61981721fa2dd_0 <= 1
 rho_&&_2bx41f61981721fa2dd_0 free
 z_G_2bx1635c42e821daeea_0 <= 1
 rho_G_2bx1635c42e821daeea_0 free
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
 z_&&_2bx47d4d1370e9d7522_19 <= 1
 rho_&&_2bx47d4d1370e9d7522_19 free
 rho_predicate_2dx4c7fa34b9cfd78d2_19 free
 rho_predicate_2bx32f72cccd281a177_19 free
 z_&&_2bx47d4d1370e9d7522_20 <= 1
 rho_&&_2bx47d4d1370e9d7522_20 free
 rho_predicate_2dx4c7fa34b9cfd78d2_20 free
 rho_predicate_2bx32f72cccd281a177_20 free
 z_G_2bx1fbb236baa38c772_0 <= 1
 rho_G_2bx1fbb236baa38c772_0 free
 z_||_2dx6fafc74611e76e89_0 <= 1
 rho_||_2dx6fafc74611e76e89_0 free
 rho_predicate_2bx454ca952238e72db_0 free
 rho_predicate_2dx19adc98cf842ca58_0 free
 rho_predicate_2bx70ac945c4f28d9ed_0 free
 rho_predicate_2dx7894b0affacefa_0 free
 z_||_2dx6fafc74611e76e89_1 <= 1
 rho_||_2dx6fafc74611e76e89_1 free
 rho_predicate_2bx454ca952238e72db_1 free
 rho_predicate_2dx19adc98cf842ca58_1 free
 rho_predicate_2bx70ac945c4f28d9ed_1 free
 rho_predicate_2dx7894b0affacefa_1 free
 z_||_2dx6fafc74611e76e89_2 <= 1
 rho_||_2dx6fafc74611e76e89_2 free
 rho_predicate_2bx454ca952238e72db_2 free
 rho_predicate_2dx19adc98cf842ca58_2 free
 rho_predicate_2bx70ac945c4f28d9ed_2 free
 rho_predicate_2dx7894b0affacefa_2 free
 z_||_2dx6fafc74611e76e89_3 <= 1
 rho_||_2dx6fafc74611e76e89_3 free
 rho_predicate_2bx454ca952238e72db_3 free
 rho_predicate_2dx19adc98cf842ca58_3 free
 rho_predicate_2bx70ac945c4f28d9ed_3 free
 rho_predicate_2dx7894b0affacefa_3 free
 z_||_2dx6fafc74611e76e89_4 <= 1
 rho_||_2dx6fafc74611e76e89_4 free
 rho_predicate_2bx454ca952238e72db_4 free
 rho_predicate_2dx19adc98cf842ca58_4 free
 rho_predicate_2bx70ac945c4f28d9ed_4 free
 rho_predicate_2dx7894b0affacefa_4 free
 z_||_2dx6fafc74611e76e89_5 <= 1
 rho_||_2dx6fafc74611e76e89_5 free
 rho_predicate_2bx454ca952238e72db_5 free
 rho_predicate_2dx19adc98cf842ca58_5 free
 rho_predicate_2bx70ac945c4f28d9ed_5 free
 rho_predicate_2dx7894b0affacefa_5 free
 z_||_2dx6fafc74611e76e89_6 <= 1
 rho_||_2dx6fafc74611e76e89_6 free
 rho_predicate_2bx454ca952238e72db_6 free
 rho_predicate_2dx19adc98cf842ca58_6 free
 rho_predicate_2bx70ac945c4f28d9ed_6 free
 rho_predicate_2dx7894b0affacefa_6 free
 z_||_2dx6fafc74611e76e89_7 <= 1
 rho_||_2dx6fafc74611e76e89_7 free
 rho_predicate_2bx454ca952238e72db_7 free
 rho_predicate_2dx19adc98cf842ca58_7 free
 rho_predicate_2bx70ac945c4f28d9ed_7 free
 rho_predicate_2dx7894b0affacefa_7 free
 z_||_2dx6fafc74611e76e89_8 <= 1
 rho_||_2dx6fafc74611e76e89_8 free
 rho_predicate_2bx454ca952238e72db_8 free
 rho_predicate_2dx19adc98cf842ca58_8 free
 rho_predicate_2bx70ac945c4f28d9ed_8 free
 rho_predicate_2dx7894b0affacefa_8 free
 z_||_2dx6fafc74611e76e89_9 <= 1
 rho_||_2dx6fafc74611e76e89_9 free
 rho_predicate_2bx454ca952238e72db_9 free
 rho_predicate_2dx19adc98cf842ca58_9 free
 rho_predicate_2bx70ac945c4f28d9ed_9 free
 rho_predicate_2dx7894b0affacefa_9 free
 z_||_2dx6fafc74611e76e89_10 <= 1
 rho_||_2dx6fafc74611e76e89_10 free
 rho_predicate_2bx454ca952238e72db_10 free
 rho_predicate_2dx19adc98cf842ca58_10 free
 rho_predicate_2bx70ac945c4f28d9ed_10 free
 rho_predicate_2dx7894b0affacefa_10 free
 z_||_2dx6fafc74611e76e89_11 <= 1
 rho_||_2dx6fafc74611e76e89_11 free
 rho_predicate_2bx454ca952238e72db_11 free
 rho_predicate_2dx19adc98cf842ca58_11 free
 rho_predicate_2bx70ac945c4f28d9ed_11 free
 rho_predicate_2dx7894b0affacefa_11 free
 z_||_2dx6fafc74611e76e89_12 <= 1
 rho_||_2dx6fafc74611e76e89_12 free
 rho_predicate_2bx454ca952238e72db_12 free
 rho_predicate_2dx19adc98cf842ca58_12 free
 rho_predicate_2bx70ac945c4f28d9ed_12 free
 rho_predicate_2dx7894b0affacefa_12 free
 z_||_2dx6fafc74611e76e89_13 <= 1
 rho_||_2dx6fafc74611e76e89_13 free
 rho_predicate_2bx454ca952238e72db_13 free
 rho_predicate_2dx19adc98cf842ca58_13 free
 rho_predicate_2bx70ac945c4f28d9ed_13 free
 rho_predicate_2dx7894b0affacefa_13 free
 z_||_2dx6fafc74611e76e89_14 <= 1
 rho_||_2dx6fafc74611e76e89_14 free
 rho_predicate_2bx454ca952238e72db_14 free
 rho_predicate_2dx19adc98cf842ca58_14 free
 rho_predicate_2bx70ac945c4f28d9ed_14 free
 rho_predicate_2dx7894b0affacefa_14 free
 z_||_2dx6fafc74611e76e89_15 <= 1
 rho_||_2dx6fafc74611e76e89_15 free
 rho_predicate_2bx454ca952238e72db_15 free
 rho_predicate_2dx19adc98cf842ca58_15 free
 rho_predicate_2bx70ac945c4f28d9ed_15 free
 rho_predicate_2dx7894b0affacefa_15 free
 z_||_2dx6fafc74611e76e89_16 <= 1
 rho_||_2dx6fafc74611e76e89_16 free
 rho_predicate_2bx454ca952238e72db_16 free
 rho_predicate_2dx19adc98cf842ca58_16 free
 rho_predicate_2bx70ac945c4f28d9ed_16 free
 rho_predicate_2dx7894b0affacefa_16 free
 z_||_2dx6fafc74611e76e89_17 <= 1
 rho_||_2dx6fafc74611e76e89_17 free
 rho_predicate_2bx454ca952238e72db_17 free
 rho_predicate_2dx19adc98cf842ca58_17 free
 rho_predicate_2bx70ac945c4f28d9ed_17 free
 rho_predicate_2dx7894b0affacefa_17 free
 z_||_2dx6fafc74611e76e89_18 <= 1
 rho_||_2dx6fafc74611e76e89_18 free
 rho_predicate_2bx454ca952238e72db_18 free
 rho_predicate_2dx19adc98cf842ca58_18 free
 rho_predicate_2bx70ac945c4f28d9ed_18 free
 rho_predicate_2dx7894b0affacefa_18 free
 z_||_2dx6fafc74611e76e89_19 <= 1
 rho_||_2dx6fafc74611e76e89_19 free
 rho_predicate_2bx454ca952238e72db_19 free
 rho_predicate_2dx19adc98cf842ca58_19 free
 rho_predicate_2bx70ac945c4f28d9ed_19 free
 rho_predicate_2dx7894b0affacefa_19 free
 z_||_2dx6fafc74611e76e89_20 <= 1
 rho_||_2dx6fafc74611e76e89_20 free
 rho_predicate_2bx454ca952238e72db_20 free
 rho_predicate_2dx19adc98cf842ca58_20 free
 rho_predicate_2bx70ac945c4f28d9ed_20 free
 rho_predicate_2dx7894b0affacefa_20 free
 z_G_2bx1e250240efa087ae_0 <= 1
 rho_G_2bx1e250240efa087ae_0 free
 z_||_2bx22f6bca85b580f1b_0 <= 1
 rho_||_2bx22f6bca85b580f1b_0 free
 rho_predicate_2dx22dd95ed78b4d217_0 free
 rho_predicate_2dx5f1149c769efb91f_0 free
 rho_predicate_2bx955025411f5da14_0 free
 rho_predicate_2bx7f11325f1c65baf6_0 free
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
 z_||_2bx22f6bca85b580f1b_8 <= 1
 rho_||_2bx22f6bca85b580f1b_8 free
 rho_predicate_2dx22dd95ed78b4d217_8 free
 rho_predicate_2dx5f1149c769efb91f_8 free
 rho_predicate_2bx955025411f5da14_8 free
 rho_predicate_2bx7f11325f1c65baf6_8 free
 z_||_2bx22f6bca85b580f1b_9 <= 1
 rho_||_2bx22f6bca85b580f1b_9 free
 rho_predicate_2dx22dd95ed78b4d217_9 free
 rho_predicate_2dx5f1149c769efb91f_9 free
 rho_predicate_2bx955025411f5da14_9 free
 rho_predicate_2bx7f11325f1c65baf6_9 free
 z_||_2bx22f6bca85b580f1b_10 <= 1
 rho_||_2bx22f6bca85b580f1b_10 free
 rho_predicate_2dx22dd95ed78b4d217_10 free
 rho_predicate_2dx5f1149c769efb91f_10 free
 rho_predicate_2bx955025411f5da14_10 free
 rho_predicate_2bx7f11325f1c65baf6_10 free
 z_||_2bx22f6bca85b580f1b_11 <= 1
 rho_||_2bx22f6bca85b580f1b_11 free
 rho_predicate_2dx22dd95ed78b4d217_11 free
 rho_predicate_2dx5f1149c769efb91f_11 free
 rho_predicate_2bx955025411f5da14_11 free
 rho_predicate_2bx7f11325f1c65baf6_11 free
 z_||_2bx22f6bca85b580f1b_12 <= 1
 rho_||_2bx22f6bca85b580f1b_12 free
 rho_predicate_2dx22dd95ed78b4d217_12 free
 rho_predicate_2dx5f1149c769efb91f_12 free
 rho_predicate_2bx955025411f5da14_12 free
 rho_predicate_2bx7f11325f1c65baf6_12 free
 z_||_2bx22f6bca85b580f1b_13 <= 1
 rho_||_2bx22f6bca85b580f1b_13 free
 rho_predicate_2dx22dd95ed78b4d217_13 free
 rho_predicate_2dx5f1149c769efb91f_13 free
 rho_predicate_2bx955025411f5da14_13 free
 rho_predicate_2bx7f11325f1c65baf6_13 free
 z_||_2bx22f6bca85b580f1b_14 <= 1
 rho_||_2bx22f6bca85b580f1b_14 free
 rho_predicate_2dx22dd95ed78b4d217_14 free
 rho_predicate_2dx5f1149c769efb91f_14 free
 rho_predicate_2bx955025411f5da14_14 free
 rho_predicate_2bx7f11325f1c65baf6_14 free
 z_||_2bx22f6bca85b580f1b_15 <= 1
 rho_||_2bx22f6bca85b580f1b_15 free
 rho_predicate_2dx22dd95ed78b4d217_15 free
 rho_predicate_2dx5f1149c769efb91f_15 free
 rho_predicate_2bx955025411f5da14_15 free
 rho_predicate_2bx7f11325f1c65baf6_15 free
 z_||_2bx22f6bca85b580f1b_16 <= 1
 rho_||_2bx22f6bca85b580f1b_16 free
 rho_predicate_2dx22dd95ed78b4d217_16 free
 rho_predicate_2dx5f1149c769efb91f_16 free
 rho_predicate_2bx955025411f5da14_16 free
 rho_predicate_2bx7f11325f1c65baf6_16 free
 z_||_2bx22f6bca85b580f1b_17 <= 1
 rho_||_2bx22f6bca85b580f1b_17 free
 rho_predicate_2dx22dd95ed78b4d217_17 free
 rho_predicate_2dx5f1149c769efb91f_17 free
 rho_predicate_2bx955025411f5da14_17 free
 rho_predicate_2bx7f11325f1c65baf6_17 free
 z_||_2bx22f6bca85b580f1b_18 <= 1
 rho_||_2bx22f6bca85b580f1b_18 free
 rho_predicate_2dx22dd95ed78b4d217_18 free
 rho_predicate_2dx5f1149c769efb91f_18 free
 rho_predicate_2bx955025411f5da14_18 free
 rho_predicate_2bx7f11325f1c65baf6_18 free
 z_||_2bx22f6bca85b580f1b_19 <= 1
 rho_||_2bx22f6bca85b580f1b_19 free
 rho_predicate_2dx22dd95ed78b4d217_19 free
 rho_predicate_2dx5f1149c769efb91f_19 free
 rho_predicate_2bx955025411f5da14_19 free
 rho_predicate_2bx7f11325f1c65baf6_19 free
 z_||_2bx22f6bca85b580f1b_20 <= 1
 rho_||_2bx22f6bca85b580f1b_20 free
 rho_predicate_2dx22dd95ed78b4d217_20 free
 rho_predicate_2dx5f1149c769efb91f_20 free
 rho_predicate_2bx955025411f5da14_20 free
 rho_predicate_2bx7f11325f1c65baf6_20 free
 z_G_2bx7d3b4be48ae7738c_0 <= 1
 rho_G_2bx7d3b4be48ae7738c_0 free
 z_||_2dx1cb8c284b4383193_0 <= 1
 rho_||_2dx1cb8c284b4383193_0 free
 rho_predicate_2dx68411627ea61c0e0_0 free
 rho_predicate_2dx5dba1e6a7b84e365_0 free
 rho_predicate_2bx4c3942499adecf48_0 free
 rho_predicate_2bx22a3ae6fed0097b_0 free
 z_||_2dx1cb8c284b4383193_1 <= 1
 rho_||_2dx1cb8c284b4383193_1 free
 rho_predicate_2dx68411627ea61c0e0_1 free
 rho_predicate_2dx5dba1e6a7b84e365_1 free
 rho_predicate_2bx4c3942499adecf48_1 free
 rho_predicate_2bx22a3ae6fed0097b_1 free
 z_||_2dx1cb8c284b4383193_2 <= 1
 rho_||_2dx1cb8c284b4383193_2 free
 rho_predicate_2dx68411627ea61c0e0_2 free
 rho_predicate_2dx5dba1e6a7b84e365_2 free
 rho_predicate_2bx4c3942499adecf48_2 free
 rho_predicate_2bx22a3ae6fed0097b_2 free
 z_||_2dx1cb8c284b4383193_3 <= 1
 rho_||_2dx1cb8c284b4383193_3 free
 rho_predicate_2dx68411627ea61c0e0_3 free
 rho_predicate_2dx5dba1e6a7b84e365_3 free
 rho_predicate_2bx4c3942499adecf48_3 free
 rho_predicate_2bx22a3ae6fed0097b_3 free
 z_||_2dx1cb8c284b4383193_4 <= 1
 rho_||_2dx1cb8c284b4383193_4 free
 rho_predicate_2dx68411627ea61c0e0_4 free
 rho_predicate_2dx5dba1e6a7b84e365_4 free
 rho_predicate_2bx4c3942499adecf48_4 free
 rho_predicate_2bx22a3ae6fed0097b_4 free
 z_||_2dx1cb8c284b4383193_5 <= 1
 rho_||_2dx1cb8c284b4383193_5 free
 rho_predicate_2dx68411627ea61c0e0_5 free
 rho_predicate_2dx5dba1e6a7b84e365_5 free
 rho_predicate_2bx4c3942499adecf48_5 free
 rho_predicate_2bx22a3ae6fed0097b_5 free
 z_||_2dx1cb8c284b4383193_6 <= 1
 rho_||_2dx1cb8c284b4383193_6 free
 rho_predicate_2dx68411627ea61c0e0_6 free
 rho_predicate_2dx5dba1e6a7b84e365_6 free
 rho_predicate_2bx4c3942499adecf48_6 free
 rho_predicate_2bx22a3ae6fed0097b_6 free
 z_||_2dx1cb8c284b4383193_7 <= 1
 rho_||_2dx1cb8c284b4383193_7 free
 rho_predicate_2dx68411627ea61c0e0_7 free
 rho_predicate_2dx5dba1e6a7b84e365_7 free
 rho_predicate_2bx4c3942499adecf48_7 free
 rho_predicate_2bx22a3ae6fed0097b_7 free
 z_||_2dx1cb8c284b4383193_8 <= 1
 rho_||_2dx1cb8c284b4383193_8 free
 rho_predicate_2dx68411627ea61c0e0_8 free
 rho_predicate_2dx5dba1e6a7b84e365_8 free
 rho_predicate_2bx4c3942499adecf48_8 free
 rho_predicate_2bx22a3ae6fed0097b_8 free
 z_||_2dx1cb8c284b4383193_9 <= 1
 rho_||_2dx1cb8c284b4383193_9 free
 rho_predicate_2dx68411627ea61c0e0_9 free
 rho_predicate_2dx5dba1e6a7b84e365_9 free
 rho_predicate_2bx4c3942499adecf48_9 free
 rho_predicate_2bx22a3ae6fed0097b_9 free
 z_||_2dx1cb8c284b4383193_10 <= 1
 rho_||_2dx1cb8c284b4383193_10 free
 rho_predicate_2dx68411627ea61c0e0_10 free
 rho_predicate_2dx5dba1e6a7b84e365_10 free
 rho_predicate_2bx4c3942499adecf48_10 free
 rho_predicate_2bx22a3ae6fed0097b_10 free
 z_||_2dx1cb8c284b4383193_11 <= 1
 rho_||_2dx1cb8c284b4383193_11 free
 rho_predicate_2dx68411627ea61c0e0_11 free
 rho_predicate_2dx5dba1e6a7b84e365_11 free
 rho_predicate_2bx4c3942499adecf48_11 free
 rho_predicate_2bx22a3ae6fed0097b_11 free
 z_||_2dx1cb8c284b4383193_12 <= 1
 rho_||_2dx1cb8c284b4383193_12 free
 rho_predicate_2dx68411627ea61c0e0_12 free
 rho_predicate_2dx5dba1e6a7b84e365_12 free
 rho_predicate_2bx4c3942499adecf48_12 free
 rho_predicate_2bx22a3ae6fed0097b_12 free
 z_||_2dx1cb8c284b4383193_13 <= 1
 rho_||_2dx1cb8c284b4383193_13 free
 rho_predicate_2dx68411627ea61c0e0_13 free
 rho_predicate_2dx5dba1e6a7b84e365_13 free
 rho_predicate_2bx4c3942499adecf48_13 free
 rho_predicate_2bx22a3ae6fed0097b_13 free
 z_||_2dx1cb8c284b4383193_14 <= 1
 rho_||_2dx1cb8c284b4383193_14 free
 rho_predicate_2dx68411627ea61c0e0_14 free
 rho_predicate_2dx5dba1e6a7b84e365_14 free
 rho_predicate_2bx4c3942499adecf48_14 free
 rho_predicate_2bx22a3ae6fed0097b_14 free
 z_||_2dx1cb8c284b4383193_15 <= 1
 rho_||_2dx1cb8c284b4383193_15 free
 rho_predicate_2dx68411627ea61c0e0_15 free
 rho_predicate_2dx5dba1e6a7b84e365_15 free
 rho_predicate_2bx4c3942499adecf48_15 free
 rho_predicate_2bx22a3ae6fed0097b_15 free
 z_||_2dx1cb8c284b4383193_16 <= 1
 rho_||_2dx1cb8c284b4383193_16 free
 rho_predicate_2dx68411627ea61c0e0_16 free
 rho_predicate_2dx5dba1e6a7b84e365_16 free
 rho_predicate_2bx4c3942499adecf48_16 free
 rho_predicate_2bx22a3ae6fed0097b_16 free
 z_||_2dx1cb8c284b4383193_17 <= 1
 rho_||_2dx1cb8c284b4383193_17 free
 rho_predicate_2dx68411627ea61c0e0_17 free
 rho_predicate_2dx5dba1e6a7b84e365_17 free
 rho_predicate_2bx4c3942499adecf48_17 free
 rho_predicate_2bx22a3ae6fed0097b_17 free
 z_||_2dx1cb8c284b4383193_18 <= 1
 rho_||_2dx1cb8c284b4383193_18 free
 rho_predicate_2dx68411627ea61c0e0_18 free
 rho_predicate_2dx5dba1e6a7b84e365_18 free
 rho_predicate_2bx4c3942499adecf48_18 free
 rho_predicate_2bx22a3ae6fed0097b_18 free
 z_||_2dx1cb8c284b4383193_19 <= 1
 rho_||_2dx1cb8c284b4383193_19 free
 rho_predicate_2dx68411627ea61c0e0_19 free
 rho_predicate_2dx5dba1e6a7b84e365_19 free
 rho_predicate_2bx4c3942499adecf48_19 free
 rho_predicate_2bx22a3ae6fed0097b_19 free
 z_||_2dx1cb8c284b4383193_20 <= 1
 rho_||_2dx1cb8c284b4383193_20 free
 rho_predicate_2dx68411627ea61c0e0_20 free
 rho_predicate_2dx5dba1e6a7b84e365_20 free
 rho_predicate_2bx4c3942499adecf48_20 free
 rho_predicate_2bx22a3ae6fed0097b_20 free
Binaries
 z_predicate_2dx4c7fa34b9cfd78d2_13 z_predicate_2bx32f72cccd281a177_13
 z_predicate_2dx4c7fa34b9cfd78d2_14 z_predicate_2bx32f72cccd281a177_14
 z_predicate_2dx4c7fa34b9cfd78d2_15 z_predicate_2bx32f72cccd281a177_15
 z_predicate_2dx4c7fa34b9cfd78d2_16 z_predicate_2bx32f72cccd281a177_16
 z_predicate_2dx4c7fa34b9cfd78d2_17 z_predicate_2bx32f72cccd281a177_17
 z_predicate_2dx4c7fa34b9cfd78d2_18 z_predicate_2bx32f72cccd281a177_18
 z_predicate_2dx4c7fa34b9cfd78d2_19 z_predicate_2bx32f72cccd281a177_19
 z_predicate_2dx4c7fa34b9cfd78d2_20 z_predicate_2bx32f72cccd281a177_20
 z_predicate_2bx454ca952238e72db_0 z_predicate_2dx19adc98cf842ca58_0
 z_predicate_2bx70ac945c4f28d9ed_0 z_predicate_2dx7894b0affacefa_0
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_0
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_0
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_0
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_0
 z_predicate_2bx454ca952238e72db_1 z_predicate_2dx19adc98cf842ca58_1
 z_predicate_2bx70ac945c4f28d9ed_1 z_predicate_2dx7894b0affacefa_1
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_1
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_1
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_1
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_1
 z_predicate_2bx454ca952238e72db_2 z_predicate_2dx19adc98cf842ca58_2
 z_predicate_2bx70ac945c4f28d9ed_2 z_predicate_2dx7894b0affacefa_2
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_2
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_2
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_2
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_2
 z_predicate_2bx454ca952238e72db_3 z_predicate_2dx19adc98cf842ca58_3
 z_predicate_2bx70ac945c4f28d9ed_3 z_predicate_2dx7894b0affacefa_3
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_3
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_3
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_3
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_3
 z_predicate_2bx454ca952238e72db_4 z_predicate_2dx19adc98cf842ca58_4
 z_predicate_2bx70ac945c4f28d9ed_4 z_predicate_2dx7894b0affacefa_4
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_4
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_4
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_4
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_4
 z_predicate_2bx454ca952238e72db_5 z_predicate_2dx19adc98cf842ca58_5
 z_predicate_2bx70ac945c4f28d9ed_5 z_predicate_2dx7894b0affacefa_5
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_5
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_5
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_5
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_5
 z_predicate_2bx454ca952238e72db_6 z_predicate_2dx19adc98cf842ca58_6
 z_predicate_2bx70ac945c4f28d9ed_6 z_predicate_2dx7894b0affacefa_6
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_6
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_6
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_6
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_6
 z_predicate_2bx454ca952238e72db_7 z_predicate_2dx19adc98cf842ca58_7
 z_predicate_2bx70ac945c4f28d9ed_7 z_predicate_2dx7894b0affacefa_7
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_7
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_7
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_7
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_7
 z_predicate_2bx454ca952238e72db_8 z_predicate_2dx19adc98cf842ca58_8
 z_predicate_2bx70ac945c4f28d9ed_8 z_predicate_2dx7894b0affacefa_8
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_8
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_8
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_8
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_8
 z_predicate_2bx454ca952238e72db_9 z_predicate_2dx19adc98cf842ca58_9
 z_predicate_2bx70ac945c4f28d9ed_9 z_predicate_2dx7894b0affacefa_9
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_9
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_9
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_9
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_9
 z_predicate_2bx454ca952238e72db_10 z_predicate_2dx19adc98cf842ca58_10
 z_predicate_2bx70ac945c4f28d9ed_10 z_predicate_2dx7894b0affacefa_10
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_10
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_10
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_10
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_10
 z_predicate_2bx454ca952238e72db_11 z_predicate_2dx19adc98cf842ca58_11
 z_predicate_2bx70ac945c4f28d9ed_11 z_predicate_2dx7894b0affacefa_11
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_11
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_11
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_11
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_11
 z_predicate_2bx454ca952238e72db_12 z_predicate_2dx19adc98cf842ca58_12
 z_predicate_2bx70ac945c4f28d9ed_12 z_predicate_2dx7894b0affacefa_12
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_12
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_12
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_12
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_12
 z_predicate_2bx454ca952238e72db_13 z_predicate_2dx19adc98cf842ca58_13
 z_predicate_2bx70ac945c4f28d9ed_13 z_predicate_2dx7894b0affacefa_13
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_13
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_13
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_13
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_13
 z_predicate_2bx454ca952238e72db_14 z_predicate_2dx19adc98cf842ca58_14
 z_predicate_2bx70ac945c4f28d9ed_14 z_predicate_2dx7894b0affacefa_14
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_14
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_14
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_14
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_14
 z_predicate_2bx454ca952238e72db_15 z_predicate_2dx19adc98cf842ca58_15
 z_predicate_2bx70ac945c4f28d9ed_15 z_predicate_2dx7894b0affacefa_15
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_15
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_15
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_15
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_15
 z_predicate_2bx454ca952238e72db_16 z_predicate_2dx19adc98cf842ca58_16
 z_predicate_2bx70ac945c4f28d9ed_16 z_predicate_2dx7894b0affacefa_16
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_16
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_16
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_16
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_16
 z_predicate_2bx454ca952238e72db_17 z_predicate_2dx19adc98cf842ca58_17
 z_predicate_2bx70ac945c4f28d9ed_17 z_predicate_2dx7894b0affacefa_17
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_17
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_17
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_17
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_17
 z_predicate_2bx454ca952238e72db_18 z_predicate_2dx19adc98cf842ca58_18
 z_predicate_2bx70ac945c4f28d9ed_18 z_predicate_2dx7894b0affacefa_18
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_18
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_18
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_18
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_18
 z_predicate_2bx454ca952238e72db_19 z_predicate_2dx19adc98cf842ca58_19
 z_predicate_2bx70ac945c4f28d9ed_19 z_predicate_2dx7894b0affacefa_19
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_19
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_19
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_19
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_19
 z_predicate_2bx454ca952238e72db_20 z_predicate_2dx19adc98cf842ca58_20
 z_predicate_2bx70ac945c4f28d9ed_20 z_predicate_2dx7894b0affacefa_20
 zhat_predicate_2bx454ca952238e72db_2dx6fafc74611e76e89_20
 zhat_predicate_2dx19adc98cf842ca58_2dx6fafc74611e76e89_20
 zhat_predicate_2bx70ac945c4f28d9ed_2dx6fafc74611e76e89_20
 zhat_predicate_2dx7894b0affacefa_2dx6fafc74611e76e89_20
 z_predicate_2dx22dd95ed78b4d217_0 z_predicate_2dx5f1149c769efb91f_0
 z_predicate_2bx955025411f5da14_0 z_predicate_2bx7f11325f1c65baf6_0
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_0
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_0
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_0
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_0
 z_predicate_2dx22dd95ed78b4d217_1 z_predicate_2dx5f1149c769efb91f_1
 z_predicate_2bx955025411f5da14_1 z_predicate_2bx7f11325f1c65baf6_1
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_1
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_1
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_1
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_1
 z_predicate_2dx22dd95ed78b4d217_2 z_predicate_2dx5f1149c769efb91f_2
 z_predicate_2bx955025411f5da14_2 z_predicate_2bx7f11325f1c65baf6_2
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_2
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_2
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_2
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_2
 z_predicate_2dx22dd95ed78b4d217_3 z_predicate_2dx5f1149c769efb91f_3
 z_predicate_2bx955025411f5da14_3 z_predicate_2bx7f11325f1c65baf6_3
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_3
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_3
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_3
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_3
 z_predicate_2dx22dd95ed78b4d217_4 z_predicate_2dx5f1149c769efb91f_4
 z_predicate_2bx955025411f5da14_4 z_predicate_2bx7f11325f1c65baf6_4
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_4
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_4
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_4
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_4
 z_predicate_2dx22dd95ed78b4d217_5 z_predicate_2dx5f1149c769efb91f_5
 z_predicate_2bx955025411f5da14_5 z_predicate_2bx7f11325f1c65baf6_5
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_5
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_5
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_5
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_5
 z_predicate_2dx22dd95ed78b4d217_6 z_predicate_2dx5f1149c769efb91f_6
 z_predicate_2bx955025411f5da14_6 z_predicate_2bx7f11325f1c65baf6_6
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_6
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_6
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_6
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_6
 z_predicate_2dx22dd95ed78b4d217_7 z_predicate_2dx5f1149c769efb91f_7
 z_predicate_2bx955025411f5da14_7 z_predicate_2bx7f11325f1c65baf6_7
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_7
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_7
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_7
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_7
 z_predicate_2dx22dd95ed78b4d217_8 z_predicate_2dx5f1149c769efb91f_8
 z_predicate_2bx955025411f5da14_8 z_predicate_2bx7f11325f1c65baf6_8
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_8
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_8
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_8
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_8
 z_predicate_2dx22dd95ed78b4d217_9 z_predicate_2dx5f1149c769efb91f_9
 z_predicate_2bx955025411f5da14_9 z_predicate_2bx7f11325f1c65baf6_9
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_9
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_9
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_9
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_9
 z_predicate_2dx22dd95ed78b4d217_10 z_predicate_2dx5f1149c769efb91f_10
 z_predicate_2bx955025411f5da14_10 z_predicate_2bx7f11325f1c65baf6_10
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_10
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_10
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_10
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_10
 z_predicate_2dx22dd95ed78b4d217_11 z_predicate_2dx5f1149c769efb91f_11
 z_predicate_2bx955025411f5da14_11 z_predicate_2bx7f11325f1c65baf6_11
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_11
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_11
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_11
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_11
 z_predicate_2dx22dd95ed78b4d217_12 z_predicate_2dx5f1149c769efb91f_12
 z_predicate_2bx955025411f5da14_12 z_predicate_2bx7f11325f1c65baf6_12
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_12
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_12
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_12
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_12
 z_predicate_2dx22dd95ed78b4d217_13 z_predicate_2dx5f1149c769efb91f_13
 z_predicate_2bx955025411f5da14_13 z_predicate_2bx7f11325f1c65baf6_13
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_13
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_13
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_13
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_13
 z_predicate_2dx22dd95ed78b4d217_14 z_predicate_2dx5f1149c769efb91f_14
 z_predicate_2bx955025411f5da14_14 z_predicate_2bx7f11325f1c65baf6_14
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_14
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_14
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_14
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_14
 z_predicate_2dx22dd95ed78b4d217_15 z_predicate_2dx5f1149c769efb91f_15
 z_predicate_2bx955025411f5da14_15 z_predicate_2bx7f11325f1c65baf6_15
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_15
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_15
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_15
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_15
 z_predicate_2dx22dd95ed78b4d217_16 z_predicate_2dx5f1149c769efb91f_16
 z_predicate_2bx955025411f5da14_16 z_predicate_2bx7f11325f1c65baf6_16
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_16
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_16
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_16
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_16
 z_predicate_2dx22dd95ed78b4d217_17 z_predicate_2dx5f1149c769efb91f_17
 z_predicate_2bx955025411f5da14_17 z_predicate_2bx7f11325f1c65baf6_17
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_17
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_17
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_17
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_17
 z_predicate_2dx22dd95ed78b4d217_18 z_predicate_2dx5f1149c769efb91f_18
 z_predicate_2bx955025411f5da14_18 z_predicate_2bx7f11325f1c65baf6_18
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_18
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_18
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_18
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_18
 z_predicate_2dx22dd95ed78b4d217_19 z_predicate_2dx5f1149c769efb91f_19
 z_predicate_2bx955025411f5da14_19 z_predicate_2bx7f11325f1c65baf6_19
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_19
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_19
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_19
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_19
 z_predicate_2dx22dd95ed78b4d217_20 z_predicate_2dx5f1149c769efb91f_20
 z_predicate_2bx955025411f5da14_20 z_predicate_2bx7f11325f1c65baf6_20
 zhat_predicate_2dx22dd95ed78b4d217_2bx22f6bca85b580f1b_20
 zhat_predicate_2dx5f1149c769efb91f_2bx22f6bca85b580f1b_20
 zhat_predicate_2bx955025411f5da14_2bx22f6bca85b580f1b_20
 zhat_predicate_2bx7f11325f1c65baf6_2bx22f6bca85b580f1b_20
 z_predicate_2dx68411627ea61c0e0_0 z_predicate_2dx5dba1e6a7b84e365_0
 z_predicate_2bx4c3942499adecf48_0 z_predicate_2bx22a3ae6fed0097b_0
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_0
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_0
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_0
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_0
 z_predicate_2dx68411627ea61c0e0_1 z_predicate_2dx5dba1e6a7b84e365_1
 z_predicate_2bx4c3942499adecf48_1 z_predicate_2bx22a3ae6fed0097b_1
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_1
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_1
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_1
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_1
 z_predicate_2dx68411627ea61c0e0_2 z_predicate_2dx5dba1e6a7b84e365_2
 z_predicate_2bx4c3942499adecf48_2 z_predicate_2bx22a3ae6fed0097b_2
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_2
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_2
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_2
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_2
 z_predicate_2dx68411627ea61c0e0_3 z_predicate_2dx5dba1e6a7b84e365_3
 z_predicate_2bx4c3942499adecf48_3 z_predicate_2bx22a3ae6fed0097b_3
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_3
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_3
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_3
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_3
 z_predicate_2dx68411627ea61c0e0_4 z_predicate_2dx5dba1e6a7b84e365_4
 z_predicate_2bx4c3942499adecf48_4 z_predicate_2bx22a3ae6fed0097b_4
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_4
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_4
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_4
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_4
 z_predicate_2dx68411627ea61c0e0_5 z_predicate_2dx5dba1e6a7b84e365_5
 z_predicate_2bx4c3942499adecf48_5 z_predicate_2bx22a3ae6fed0097b_5
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_5
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_5
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_5
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_5
 z_predicate_2dx68411627ea61c0e0_6 z_predicate_2dx5dba1e6a7b84e365_6
 z_predicate_2bx4c3942499adecf48_6 z_predicate_2bx22a3ae6fed0097b_6
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_6
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_6
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_6
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_6
 z_predicate_2dx68411627ea61c0e0_7 z_predicate_2dx5dba1e6a7b84e365_7
 z_predicate_2bx4c3942499adecf48_7 z_predicate_2bx22a3ae6fed0097b_7
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_7
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_7
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_7
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_7
 z_predicate_2dx68411627ea61c0e0_8 z_predicate_2dx5dba1e6a7b84e365_8
 z_predicate_2bx4c3942499adecf48_8 z_predicate_2bx22a3ae6fed0097b_8
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_8
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_8
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_8
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_8
 z_predicate_2dx68411627ea61c0e0_9 z_predicate_2dx5dba1e6a7b84e365_9
 z_predicate_2bx4c3942499adecf48_9 z_predicate_2bx22a3ae6fed0097b_9
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_9
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_9
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_9
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_9
 z_predicate_2dx68411627ea61c0e0_10 z_predicate_2dx5dba1e6a7b84e365_10
 z_predicate_2bx4c3942499adecf48_10 z_predicate_2bx22a3ae6fed0097b_10
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_10
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_10
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_10
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_10
 z_predicate_2dx68411627ea61c0e0_11 z_predicate_2dx5dba1e6a7b84e365_11
 z_predicate_2bx4c3942499adecf48_11 z_predicate_2bx22a3ae6fed0097b_11
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_11
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_11
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_11
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_11
 z_predicate_2dx68411627ea61c0e0_12 z_predicate_2dx5dba1e6a7b84e365_12
 z_predicate_2bx4c3942499adecf48_12 z_predicate_2bx22a3ae6fed0097b_12
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_12
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_12
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_12
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_12
 z_predicate_2dx68411627ea61c0e0_13 z_predicate_2dx5dba1e6a7b84e365_13
 z_predicate_2bx4c3942499adecf48_13 z_predicate_2bx22a3ae6fed0097b_13
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_13
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_13
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_13
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_13
 z_predicate_2dx68411627ea61c0e0_14 z_predicate_2dx5dba1e6a7b84e365_14
 z_predicate_2bx4c3942499adecf48_14 z_predicate_2bx22a3ae6fed0097b_14
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_14
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_14
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_14
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_14
 z_predicate_2dx68411627ea61c0e0_15 z_predicate_2dx5dba1e6a7b84e365_15
 z_predicate_2bx4c3942499adecf48_15 z_predicate_2bx22a3ae6fed0097b_15
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_15
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_15
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_15
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_15
 z_predicate_2dx68411627ea61c0e0_16 z_predicate_2dx5dba1e6a7b84e365_16
 z_predicate_2bx4c3942499adecf48_16 z_predicate_2bx22a3ae6fed0097b_16
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_16
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_16
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_16
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_16
 z_predicate_2dx68411627ea61c0e0_17 z_predicate_2dx5dba1e6a7b84e365_17
 z_predicate_2bx4c3942499adecf48_17 z_predicate_2bx22a3ae6fed0097b_17
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_17
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_17
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_17
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_17
 z_predicate_2dx68411627ea61c0e0_18 z_predicate_2dx5dba1e6a7b84e365_18
 z_predicate_2bx4c3942499adecf48_18 z_predicate_2bx22a3ae6fed0097b_18
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_18
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_18
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_18
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_18
 z_predicate_2dx68411627ea61c0e0_19 z_predicate_2dx5dba1e6a7b84e365_19
 z_predicate_2bx4c3942499adecf48_19 z_predicate_2bx22a3ae6fed0097b_19
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_19
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_19
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_19
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_19
 z_predicate_2dx68411627ea61c0e0_20 z_predicate_2dx5dba1e6a7b84e365_20
 z_predicate_2bx4c3942499adecf48_20 z_predicate_2bx22a3ae6fed0097b_20
 zhat_predicate_2dx68411627ea61c0e0_2dx1cb8c284b4383193_20
 zhat_predicate_2dx5dba1e6a7b84e365_2dx1cb8c284b4383193_20
 zhat_predicate_2bx4c3942499adecf48_2dx1cb8c284b4383193_20
 zhat_predicate_2bx22a3ae6fed0097b_2dx1cb8c284b4383193_20
End
