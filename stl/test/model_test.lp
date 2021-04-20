\ Model STL formula: ((G[0.0, 2.0] (x >= 3.0)) && (F[0.0, 6.0] (y >= 4.0)) && (G[0.0, 2.0] (z >= 1.0)))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - rho + 0 u_0 + 0 v_0 + 0 w_0 + 0 u_1 + 0 v_1 + 0 w_1 + 0 u_2 + 0 v_2
   + 0 w_2 + 0 u_3 + 0 v_3 + 0 w_3 + 0 u_4 + 0 v_4 + 0 w_4 + 0 u_5 + 0 v_5
   + 0 w_5 + 0 u_6 + 0 v_6 + 0 w_6 + 0 u_14 + 0 v_14 + 0 w_14
Subject To
 R0: x_0 = 0
 R1: y_0 = 2
 R2: z_0 = -1
 R3: x_1 = 2
 R4: y_1 = 2
 R5: z_1 = -1
 R6: x_2 = 4
 R7: y_2 = 2
 R8: z_2 = -1
 R9: x_3 = 1
 R10: y_3 = 2
 R11: z_3 = -1
 R12: x_4 = 3
 R13: y_4 = 2
 R14: z_4 = -1
 R15: x_5 = 0
 R16: y_5 = 2
 R17: z_5 = -1
 R18: x_6 = 2
 R19: y_6 = 2
 R20: z_6 = -1
 R21: x_7 = 4
 R22: y_7 = 2
 R23: z_7 = -1
 R24: - x_7 - u_7 + x_8 = 0
 R25: - y_7 - v_7 + y_8 = 0
 R26: - z_7 - w_7 + z_8 = 0
 R27: - x_8 - u_8 + x_9 = 0
 R28: - y_8 - v_8 + y_9 = 0
 R29: - z_8 - w_8 + z_9 = 0
 R30: - x_9 - u_9 + x_10 = 0
 R31: - y_9 - v_9 + y_10 = 0
 R32: - z_9 - w_9 + z_10 = 0
 R33: - x_10 - u_10 + x_11 = 0
 R34: - y_10 - v_10 + y_11 = 0
 R35: - z_10 - w_10 + z_11 = 0
 R36: - x_11 - u_11 + x_12 = 0
 R37: - y_11 - v_11 + y_12 = 0
 R38: - z_11 - w_11 + z_12 = 0
 R39: - x_12 - u_12 + x_13 = 0
 R40: - y_12 - v_12 + y_13 = 0
 R41: - z_12 - w_12 + z_13 = 0
 R42: - x_13 - u_13 + x_14 = 0
 R43: - y_13 - v_13 + y_14 = 0
 R44: - z_13 - w_13 + z_14 = 0
 R45: - rho + x_0 - 20 predicate_2dx22dd95ed78b4d217_0 <= 3
 R46: - rho + x_0 - 20 predicate_2dx22dd95ed78b4d217_0 >= -17
 R47: - rho + x_1 - 20 predicate_2dx22dd95ed78b4d217_1 <= 3
 R48: - rho + x_1 - 20 predicate_2dx22dd95ed78b4d217_1 >= -17
 R49: - rho + x_2 - 20 predicate_2dx22dd95ed78b4d217_2 <= 3
 R50: - rho + x_2 - 20 predicate_2dx22dd95ed78b4d217_2 >= -17
 R51: always_2dx69bcdd71a3ff42e3_0 - predicate_2dx22dd95ed78b4d217_0 <= 0
 R52: always_2dx69bcdd71a3ff42e3_0 - predicate_2dx22dd95ed78b4d217_1 <= 0
 R53: always_2dx69bcdd71a3ff42e3_0 - predicate_2dx22dd95ed78b4d217_2 <= 0
 R54: always_2dx69bcdd71a3ff42e3_0 - predicate_2dx22dd95ed78b4d217_0
   - predicate_2dx22dd95ed78b4d217_1 - predicate_2dx22dd95ed78b4d217_2
   >= -2
 R55: - rho + y_0 - 20 predicate_2bx1735b9f08705a189_0 <= 4
 R56: - rho + y_0 - 20 predicate_2bx1735b9f08705a189_0 >= -16
 R57: - rho + y_1 - 20 predicate_2bx1735b9f08705a189_1 <= 4
 R58: - rho + y_1 - 20 predicate_2bx1735b9f08705a189_1 >= -16
 R59: - rho + y_2 - 20 predicate_2bx1735b9f08705a189_2 <= 4
 R60: - rho + y_2 - 20 predicate_2bx1735b9f08705a189_2 >= -16
 R61: - rho + y_3 - 20 predicate_2bx1735b9f08705a189_3 <= 4
 R62: - rho + y_3 - 20 predicate_2bx1735b9f08705a189_3 >= -16
 R63: - rho + y_4 - 20 predicate_2bx1735b9f08705a189_4 <= 4
 R64: - rho + y_4 - 20 predicate_2bx1735b9f08705a189_4 >= -16
 R65: - rho + y_5 - 20 predicate_2bx1735b9f08705a189_5 <= 4
 R66: - rho + y_5 - 20 predicate_2bx1735b9f08705a189_5 >= -16
 R67: - rho + y_6 - 20 predicate_2bx1735b9f08705a189_6 <= 4
 R68: - rho + y_6 - 20 predicate_2bx1735b9f08705a189_6 >= -16
 R69: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_0 >= 0
 R70: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_1 >= 0
 R71: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_2 >= 0
 R72: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_3 >= 0
 R73: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_4 >= 0
 R74: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_5 >= 0
 R75: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_6 >= 0
 R76: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_0
   - predicate_2bx1735b9f08705a189_1 - predicate_2bx1735b9f08705a189_2
   - predicate_2bx1735b9f08705a189_3 - predicate_2bx1735b9f08705a189_4
   - predicate_2bx1735b9f08705a189_5 - predicate_2bx1735b9f08705a189_6
   <= 0
 R77: - rho + z_0 - 20 predicate_2dx33b18e258c171243_0 <= 1
 R78: - rho + z_0 - 20 predicate_2dx33b18e258c171243_0 >= -19
 R79: - rho + z_1 - 20 predicate_2dx33b18e258c171243_1 <= 1
 R80: - rho + z_1 - 20 predicate_2dx33b18e258c171243_1 >= -19
 R81: - rho + z_2 - 20 predicate_2dx33b18e258c171243_2 <= 1
 R82: - rho + z_2 - 20 predicate_2dx33b18e258c171243_2 >= -19
 R83: always_2dx7c33fe6ba9ff9e2b_0 - predicate_2dx33b18e258c171243_0 <= 0
 R84: always_2dx7c33fe6ba9ff9e2b_0 - predicate_2dx33b18e258c171243_1 <= 0
 R85: always_2dx7c33fe6ba9ff9e2b_0 - predicate_2dx33b18e258c171243_2 <= 0
 R86: always_2dx7c33fe6ba9ff9e2b_0 - predicate_2dx33b18e258c171243_0
   - predicate_2dx33b18e258c171243_1 - predicate_2dx33b18e258c171243_2
   >= -2
 R87: and_2bx118e22bf358da4df_0 - always_2dx69bcdd71a3ff42e3_0 <= 0
 R88: and_2bx118e22bf358da4df_0 - event_2bx21312f0771487ac4_0 <= 0
 R89: and_2bx118e22bf358da4df_0 - always_2dx7c33fe6ba9ff9e2b_0 <= 0
 R90: and_2bx118e22bf358da4df_0 - always_2dx69bcdd71a3ff42e3_0
   - event_2bx21312f0771487ac4_0 - always_2dx7c33fe6ba9ff9e2b_0 >= -2
 formula_satisfaction: and_2bx118e22bf358da4df_0 = 1
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
Binaries
 and_2bx118e22bf358da4df_0 always_2dx69bcdd71a3ff42e3_0
 predicate_2dx22dd95ed78b4d217_0 predicate_2dx22dd95ed78b4d217_1
 predicate_2dx22dd95ed78b4d217_2 event_2bx21312f0771487ac4_0
 predicate_2bx1735b9f08705a189_0 predicate_2bx1735b9f08705a189_1
 predicate_2bx1735b9f08705a189_2 predicate_2bx1735b9f08705a189_3
 predicate_2bx1735b9f08705a189_4 predicate_2bx1735b9f08705a189_5
 predicate_2bx1735b9f08705a189_6 always_2dx7c33fe6ba9ff9e2b_0
 predicate_2dx33b18e258c171243_0 predicate_2dx33b18e258c171243_1
 predicate_2dx33b18e258c171243_2
End
