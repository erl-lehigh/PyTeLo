\ Model STL formula: ((G[4.0, 10.0] (x >= 3.0)) && (G[4.0, 10.0] (y >= 4.0)) && (G[4.0, 10.0] (z >= 1.0)))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - rho + 0 u_10 + 0 v_10 + 0 w_10
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
 R30: x_0 = 0
 R31: y_0 = 0
 R32: z_0 = 0
 R33: u_0 = 0
 R34: v_0 = 0
 R35: w_0 = 0
 R36: - rho + x_4 - 1000 predicate_2dx22dd95ed78b4d217_4 <= 3
 R37: - rho + x_4 - 1000 predicate_2dx22dd95ed78b4d217_4 >= -997
 R38: - rho + x_5 - 1000 predicate_2dx22dd95ed78b4d217_5 <= 3
 R39: - rho + x_5 - 1000 predicate_2dx22dd95ed78b4d217_5 >= -997
 R40: - rho + x_6 - 1000 predicate_2dx22dd95ed78b4d217_6 <= 3
 R41: - rho + x_6 - 1000 predicate_2dx22dd95ed78b4d217_6 >= -997
 R42: - rho + x_7 - 1000 predicate_2dx22dd95ed78b4d217_7 <= 3
 R43: - rho + x_7 - 1000 predicate_2dx22dd95ed78b4d217_7 >= -997
 R44: - rho + x_8 - 1000 predicate_2dx22dd95ed78b4d217_8 <= 3
 R45: - rho + x_8 - 1000 predicate_2dx22dd95ed78b4d217_8 >= -997
 R46: - rho + x_9 - 1000 predicate_2dx22dd95ed78b4d217_9 <= 3
 R47: - rho + x_9 - 1000 predicate_2dx22dd95ed78b4d217_9 >= -997
 R48: - rho + x_10 - 1000 predicate_2dx22dd95ed78b4d217_10 <= 3
 R49: - rho + x_10 - 1000 predicate_2dx22dd95ed78b4d217_10 >= -997
 R50: G_2bx36d55f653b5f6fb7_0 - predicate_2dx22dd95ed78b4d217_4 <= 0
 R51: G_2bx36d55f653b5f6fb7_0 - predicate_2dx22dd95ed78b4d217_5 <= 0
 R52: G_2bx36d55f653b5f6fb7_0 - predicate_2dx22dd95ed78b4d217_6 <= 0
 R53: G_2bx36d55f653b5f6fb7_0 - predicate_2dx22dd95ed78b4d217_7 <= 0
 R54: G_2bx36d55f653b5f6fb7_0 - predicate_2dx22dd95ed78b4d217_8 <= 0
 R55: G_2bx36d55f653b5f6fb7_0 - predicate_2dx22dd95ed78b4d217_9 <= 0
 R56: G_2bx36d55f653b5f6fb7_0 - predicate_2dx22dd95ed78b4d217_10 <= 0
 R57: G_2bx36d55f653b5f6fb7_0 - predicate_2dx22dd95ed78b4d217_4
   - predicate_2dx22dd95ed78b4d217_5 - predicate_2dx22dd95ed78b4d217_6
   - predicate_2dx22dd95ed78b4d217_7 - predicate_2dx22dd95ed78b4d217_8
   - predicate_2dx22dd95ed78b4d217_9 - predicate_2dx22dd95ed78b4d217_10
   >= -6
 R58: - rho + y_4 - 1000 predicate_2bx1735b9f08705a189_4 <= 4
 R59: - rho + y_4 - 1000 predicate_2bx1735b9f08705a189_4 >= -996
 R60: - rho + y_5 - 1000 predicate_2bx1735b9f08705a189_5 <= 4
 R61: - rho + y_5 - 1000 predicate_2bx1735b9f08705a189_5 >= -996
 R62: - rho + y_6 - 1000 predicate_2bx1735b9f08705a189_6 <= 4
 R63: - rho + y_6 - 1000 predicate_2bx1735b9f08705a189_6 >= -996
 R64: - rho + y_7 - 1000 predicate_2bx1735b9f08705a189_7 <= 4
 R65: - rho + y_7 - 1000 predicate_2bx1735b9f08705a189_7 >= -996
 R66: - rho + y_8 - 1000 predicate_2bx1735b9f08705a189_8 <= 4
 R67: - rho + y_8 - 1000 predicate_2bx1735b9f08705a189_8 >= -996
 R68: - rho + y_9 - 1000 predicate_2bx1735b9f08705a189_9 <= 4
 R69: - rho + y_9 - 1000 predicate_2bx1735b9f08705a189_9 >= -996
 R70: - rho + y_10 - 1000 predicate_2bx1735b9f08705a189_10 <= 4
 R71: - rho + y_10 - 1000 predicate_2bx1735b9f08705a189_10 >= -996
 R72: G_2bx53bdb62ba6d5f51b_0 - predicate_2bx1735b9f08705a189_4 <= 0
 R73: G_2bx53bdb62ba6d5f51b_0 - predicate_2bx1735b9f08705a189_5 <= 0
 R74: G_2bx53bdb62ba6d5f51b_0 - predicate_2bx1735b9f08705a189_6 <= 0
 R75: G_2bx53bdb62ba6d5f51b_0 - predicate_2bx1735b9f08705a189_7 <= 0
 R76: G_2bx53bdb62ba6d5f51b_0 - predicate_2bx1735b9f08705a189_8 <= 0
 R77: G_2bx53bdb62ba6d5f51b_0 - predicate_2bx1735b9f08705a189_9 <= 0
 R78: G_2bx53bdb62ba6d5f51b_0 - predicate_2bx1735b9f08705a189_10 <= 0
 R79: G_2bx53bdb62ba6d5f51b_0 - predicate_2bx1735b9f08705a189_4
   - predicate_2bx1735b9f08705a189_5 - predicate_2bx1735b9f08705a189_6
   - predicate_2bx1735b9f08705a189_7 - predicate_2bx1735b9f08705a189_8
   - predicate_2bx1735b9f08705a189_9 - predicate_2bx1735b9f08705a189_10
   >= -6
 R80: - rho + z_4 - 1000 predicate_2dx33b18e258c171243_4 <= 1
 R81: - rho + z_4 - 1000 predicate_2dx33b18e258c171243_4 >= -999
 R82: - rho + z_5 - 1000 predicate_2dx33b18e258c171243_5 <= 1
 R83: - rho + z_5 - 1000 predicate_2dx33b18e258c171243_5 >= -999
 R84: - rho + z_6 - 1000 predicate_2dx33b18e258c171243_6 <= 1
 R85: - rho + z_6 - 1000 predicate_2dx33b18e258c171243_6 >= -999
 R86: - rho + z_7 - 1000 predicate_2dx33b18e258c171243_7 <= 1
 R87: - rho + z_7 - 1000 predicate_2dx33b18e258c171243_7 >= -999
 R88: - rho + z_8 - 1000 predicate_2dx33b18e258c171243_8 <= 1
 R89: - rho + z_8 - 1000 predicate_2dx33b18e258c171243_8 >= -999
 R90: - rho + z_9 - 1000 predicate_2dx33b18e258c171243_9 <= 1
 R91: - rho + z_9 - 1000 predicate_2dx33b18e258c171243_9 >= -999
 R92: - rho + z_10 - 1000 predicate_2dx33b18e258c171243_10 <= 1
 R93: - rho + z_10 - 1000 predicate_2dx33b18e258c171243_10 >= -999
 R94: G_2bx72ac03a180647dbb_0 - predicate_2dx33b18e258c171243_4 <= 0
 R95: G_2bx72ac03a180647dbb_0 - predicate_2dx33b18e258c171243_5 <= 0
 R96: G_2bx72ac03a180647dbb_0 - predicate_2dx33b18e258c171243_6 <= 0
 R97: G_2bx72ac03a180647dbb_0 - predicate_2dx33b18e258c171243_7 <= 0
 R98: G_2bx72ac03a180647dbb_0 - predicate_2dx33b18e258c171243_8 <= 0
 R99: G_2bx72ac03a180647dbb_0 - predicate_2dx33b18e258c171243_9 <= 0
 R100: G_2bx72ac03a180647dbb_0 - predicate_2dx33b18e258c171243_10 <= 0
 R101: G_2bx72ac03a180647dbb_0 - predicate_2dx33b18e258c171243_4
   - predicate_2dx33b18e258c171243_5 - predicate_2dx33b18e258c171243_6
   - predicate_2dx33b18e258c171243_7 - predicate_2dx33b18e258c171243_8
   - predicate_2dx33b18e258c171243_9 - predicate_2dx33b18e258c171243_10
   >= -6
 R102: &&_2dx395c7d4d8c9136da_0 - G_2bx36d55f653b5f6fb7_0 <= 0
 R103: &&_2dx395c7d4d8c9136da_0 - G_2bx53bdb62ba6d5f51b_0 <= 0
 R104: &&_2dx395c7d4d8c9136da_0 - G_2bx72ac03a180647dbb_0 <= 0
 R105: &&_2dx395c7d4d8c9136da_0 - G_2bx36d55f653b5f6fb7_0
   - G_2bx53bdb62ba6d5f51b_0 - G_2bx72ac03a180647dbb_0 >= -2
 formula_satisfaction: &&_2dx395c7d4d8c9136da_0 = 1
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
Binaries
 &&_2dx395c7d4d8c9136da_0 G_2bx36d55f653b5f6fb7_0
 predicate_2dx22dd95ed78b4d217_4 predicate_2dx22dd95ed78b4d217_5
 predicate_2dx22dd95ed78b4d217_6 predicate_2dx22dd95ed78b4d217_7
 predicate_2dx22dd95ed78b4d217_8 predicate_2dx22dd95ed78b4d217_9
 predicate_2dx22dd95ed78b4d217_10 G_2bx53bdb62ba6d5f51b_0
 predicate_2bx1735b9f08705a189_4 predicate_2bx1735b9f08705a189_5
 predicate_2bx1735b9f08705a189_6 predicate_2bx1735b9f08705a189_7
 predicate_2bx1735b9f08705a189_8 predicate_2bx1735b9f08705a189_9
 predicate_2bx1735b9f08705a189_10 G_2bx72ac03a180647dbb_0
 predicate_2dx33b18e258c171243_4 predicate_2dx33b18e258c171243_5
 predicate_2dx33b18e258c171243_6 predicate_2dx33b18e258c171243_7
 predicate_2dx33b18e258c171243_8 predicate_2dx33b18e258c171243_9
 predicate_2dx33b18e258c171243_10
End
