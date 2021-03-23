\ Model STL formula: ((G[0.0, 2.0] (x >= 3.0)) && (F[0.0, 6.0] (y >= 4.0)) && (G[0.0, 2.0] (z >= 1.0)))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - rho + 0 u_7 + 0 v_7 + 0 w_7
Subject To
 R0: x_0 = 3
 R1: y_0 = -1
 R2: z_0 = 1
 R3: - x_0 - u_0 + x_1 = 0
 R4: - y_0 - v_0 + y_1 = 0
 R5: - z_0 - w_0 + z_1 = 0
 R6: - x_1 - u_1 + x_2 = 0
 R7: - y_1 - v_1 + y_2 = 0
 R8: - z_1 - w_1 + z_2 = 0
 R9: - x_2 - u_2 + x_3 = 0
 R10: - y_2 - v_2 + y_3 = 0
 R11: - z_2 - w_2 + z_3 = 0
 R12: - x_3 - u_3 + x_4 = 0
 R13: - y_3 - v_3 + y_4 = 0
 R14: - z_3 - w_3 + z_4 = 0
 R15: - x_4 - u_4 + x_5 = 0
 R16: - y_4 - v_4 + y_5 = 0
 R17: - z_4 - w_4 + z_5 = 0
 R18: - x_5 - u_5 + x_6 = 0
 R19: - y_5 - v_5 + y_6 = 0
 R20: - z_5 - w_5 + z_6 = 0
 R21: - x_6 - u_6 + x_7 = 0
 R22: - y_6 - v_6 + y_7 = 0
 R23: - z_6 - w_6 + z_7 = 0
 R24: - rho + x_0 - 20 predicate_2dx22dd95ed78b4d217_0 <= 3
 R25: - rho + x_0 - 20 predicate_2dx22dd95ed78b4d217_0 >= -17
 R26: - rho + x_1 - 20 predicate_2dx22dd95ed78b4d217_1 <= 3
 R27: - rho + x_1 - 20 predicate_2dx22dd95ed78b4d217_1 >= -17
 R28: - rho + x_2 - 20 predicate_2dx22dd95ed78b4d217_2 <= 3
 R29: - rho + x_2 - 20 predicate_2dx22dd95ed78b4d217_2 >= -17
 R30: always_2dx69bcdd71a3ff42e3_0 - predicate_2dx22dd95ed78b4d217_0 <= 0
 R31: always_2dx69bcdd71a3ff42e3_0 - predicate_2dx22dd95ed78b4d217_1 <= 0
 R32: always_2dx69bcdd71a3ff42e3_0 - predicate_2dx22dd95ed78b4d217_2 <= 0
 R33: always_2dx69bcdd71a3ff42e3_0 - predicate_2dx22dd95ed78b4d217_0
   - predicate_2dx22dd95ed78b4d217_1 - predicate_2dx22dd95ed78b4d217_2
   >= -2
 R34: - rho + y_0 - 20 predicate_2bx1735b9f08705a189_0 <= 4
 R35: - rho + y_0 - 20 predicate_2bx1735b9f08705a189_0 >= -16
 R36: - rho + y_1 - 20 predicate_2bx1735b9f08705a189_1 <= 4
 R37: - rho + y_1 - 20 predicate_2bx1735b9f08705a189_1 >= -16
 R38: - rho + y_2 - 20 predicate_2bx1735b9f08705a189_2 <= 4
 R39: - rho + y_2 - 20 predicate_2bx1735b9f08705a189_2 >= -16
 R40: - rho + y_3 - 20 predicate_2bx1735b9f08705a189_3 <= 4
 R41: - rho + y_3 - 20 predicate_2bx1735b9f08705a189_3 >= -16
 R42: - rho + y_4 - 20 predicate_2bx1735b9f08705a189_4 <= 4
 R43: - rho + y_4 - 20 predicate_2bx1735b9f08705a189_4 >= -16
 R44: - rho + y_5 - 20 predicate_2bx1735b9f08705a189_5 <= 4
 R45: - rho + y_5 - 20 predicate_2bx1735b9f08705a189_5 >= -16
 R46: - rho + y_6 - 20 predicate_2bx1735b9f08705a189_6 <= 4
 R47: - rho + y_6 - 20 predicate_2bx1735b9f08705a189_6 >= -16
 R48: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_0 >= 0
 R49: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_1 >= 0
 R50: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_2 >= 0
 R51: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_3 >= 0
 R52: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_4 >= 0
 R53: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_5 >= 0
 R54: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_6 >= 0
 R55: event_2bx21312f0771487ac4_0 - predicate_2bx1735b9f08705a189_0
   - predicate_2bx1735b9f08705a189_1 - predicate_2bx1735b9f08705a189_2
   - predicate_2bx1735b9f08705a189_3 - predicate_2bx1735b9f08705a189_4
   - predicate_2bx1735b9f08705a189_5 - predicate_2bx1735b9f08705a189_6
   <= 0
 R56: - rho + z_0 - 20 predicate_2dx33b18e258c171243_0 <= 1
 R57: - rho + z_0 - 20 predicate_2dx33b18e258c171243_0 >= -19
 R58: - rho + z_1 - 20 predicate_2dx33b18e258c171243_1 <= 1
 R59: - rho + z_1 - 20 predicate_2dx33b18e258c171243_1 >= -19
 R60: - rho + z_2 - 20 predicate_2dx33b18e258c171243_2 <= 1
 R61: - rho + z_2 - 20 predicate_2dx33b18e258c171243_2 >= -19
 R62: always_2dx7c33fe6ba9ff9e2b_0 - predicate_2dx33b18e258c171243_0 <= 0
 R63: always_2dx7c33fe6ba9ff9e2b_0 - predicate_2dx33b18e258c171243_1 <= 0
 R64: always_2dx7c33fe6ba9ff9e2b_0 - predicate_2dx33b18e258c171243_2 <= 0
 R65: always_2dx7c33fe6ba9ff9e2b_0 - predicate_2dx33b18e258c171243_0
   - predicate_2dx33b18e258c171243_1 - predicate_2dx33b18e258c171243_2
   >= -2
 R66: and_2bx118e22bf358da4df_0 - always_2dx69bcdd71a3ff42e3_0 <= 0
 R67: and_2bx118e22bf358da4df_0 - event_2bx21312f0771487ac4_0 <= 0
 R68: and_2bx118e22bf358da4df_0 - always_2dx7c33fe6ba9ff9e2b_0 <= 0
 R69: and_2bx118e22bf358da4df_0 - always_2dx69bcdd71a3ff42e3_0
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
