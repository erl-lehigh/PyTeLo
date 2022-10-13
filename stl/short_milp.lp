\ Model S-WSTL formula: ((G[5.0, 10.0]^<lambda> (x >= 3.0)) &&^<lambda> (G[5.0, 10.0]^<lambda> (y <= -2.0)) &&^<lambda> (G[5.0, 10.0]^<lambda> (z >= 1.0)))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0 u_10 + 0 v_10 + 0 w_10 + rho_&&_2dx2db83bba55f505ef_0
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
 R36: x_5 - 1000 z_predicate_2dx22dd95ed78b4d217_5
   - rho_predicate_2dx22dd95ed78b4d217_5 <= 3
 R37: x_5 - 1000 z_predicate_2dx22dd95ed78b4d217_5
   - rho_predicate_2dx22dd95ed78b4d217_5 >= -997
 R38: x_6 - 1000 z_predicate_2dx22dd95ed78b4d217_6
   - rho_predicate_2dx22dd95ed78b4d217_6 <= 3
 R39: x_6 - 1000 z_predicate_2dx22dd95ed78b4d217_6
   - rho_predicate_2dx22dd95ed78b4d217_6 >= -997
 R40: x_7 - 1000 z_predicate_2dx22dd95ed78b4d217_7
   - rho_predicate_2dx22dd95ed78b4d217_7 <= 3
 R41: x_7 - 1000 z_predicate_2dx22dd95ed78b4d217_7
   - rho_predicate_2dx22dd95ed78b4d217_7 >= -997
 R42: x_8 - 1000 z_predicate_2dx22dd95ed78b4d217_8
   - rho_predicate_2dx22dd95ed78b4d217_8 <= 3
 R43: x_8 - 1000 z_predicate_2dx22dd95ed78b4d217_8
   - rho_predicate_2dx22dd95ed78b4d217_8 >= -997
 R44: x_9 - 1000 z_predicate_2dx22dd95ed78b4d217_9
   - rho_predicate_2dx22dd95ed78b4d217_9 <= 3
 R45: x_9 - 1000 z_predicate_2dx22dd95ed78b4d217_9
   - rho_predicate_2dx22dd95ed78b4d217_9 >= -997
 R46: x_10 - 1000 z_predicate_2dx22dd95ed78b4d217_10
   - rho_predicate_2dx22dd95ed78b4d217_10 <= 3
 R47: x_10 - 1000 z_predicate_2dx22dd95ed78b4d217_10
   - rho_predicate_2dx22dd95ed78b4d217_10 >= -997
 R48: rho_G_2dx706aecdda938fda_0 - 10 rho_predicate_2dx22dd95ed78b4d217_5
   <= 0
 R49: z_G_2dx706aecdda938fda_0 - z_predicate_2dx22dd95ed78b4d217_5 <= 0
 R50: rho_G_2dx706aecdda938fda_0 - 10 rho_predicate_2dx22dd95ed78b4d217_6
   <= 0
 R51: z_G_2dx706aecdda938fda_0 - z_predicate_2dx22dd95ed78b4d217_6 <= 0
 R52: rho_G_2dx706aecdda938fda_0 - 10 rho_predicate_2dx22dd95ed78b4d217_7
   <= 0
 R53: z_G_2dx706aecdda938fda_0 - z_predicate_2dx22dd95ed78b4d217_7 <= 0
 R54: rho_G_2dx706aecdda938fda_0 - 10 rho_predicate_2dx22dd95ed78b4d217_8
   <= 0
 R55: z_G_2dx706aecdda938fda_0 - z_predicate_2dx22dd95ed78b4d217_8 <= 0
 R56: rho_G_2dx706aecdda938fda_0 - 10 rho_predicate_2dx22dd95ed78b4d217_9
   <= 0
 R57: z_G_2dx706aecdda938fda_0 - z_predicate_2dx22dd95ed78b4d217_9 <= 0
 R58: rho_G_2dx706aecdda938fda_0 - 10 rho_predicate_2dx22dd95ed78b4d217_10
   <= 0
 R59: z_G_2dx706aecdda938fda_0 - z_predicate_2dx22dd95ed78b4d217_10 <= 0
 R60: y_5 + 1000 z_predicate_2dx730e126114cf2e57_5
   + rho_predicate_2dx730e126114cf2e57_5 >= -2
 R61: y_5 + 1000 z_predicate_2dx730e126114cf2e57_5
   + rho_predicate_2dx730e126114cf2e57_5 <= 998
 R62: y_6 + 1000 z_predicate_2dx730e126114cf2e57_6
   + rho_predicate_2dx730e126114cf2e57_6 >= -2
 R63: y_6 + 1000 z_predicate_2dx730e126114cf2e57_6
   + rho_predicate_2dx730e126114cf2e57_6 <= 998
 R64: y_7 + 1000 z_predicate_2dx730e126114cf2e57_7
   + rho_predicate_2dx730e126114cf2e57_7 >= -2
 R65: y_7 + 1000 z_predicate_2dx730e126114cf2e57_7
   + rho_predicate_2dx730e126114cf2e57_7 <= 998
 R66: y_8 + 1000 z_predicate_2dx730e126114cf2e57_8
   + rho_predicate_2dx730e126114cf2e57_8 >= -2
 R67: y_8 + 1000 z_predicate_2dx730e126114cf2e57_8
   + rho_predicate_2dx730e126114cf2e57_8 <= 998
 R68: y_9 + 1000 z_predicate_2dx730e126114cf2e57_9
   + rho_predicate_2dx730e126114cf2e57_9 >= -2
 R69: y_9 + 1000 z_predicate_2dx730e126114cf2e57_9
   + rho_predicate_2dx730e126114cf2e57_9 <= 998
 R70: y_10 + 1000 z_predicate_2dx730e126114cf2e57_10
   + rho_predicate_2dx730e126114cf2e57_10 >= -2
 R71: y_10 + 1000 z_predicate_2dx730e126114cf2e57_10
   + rho_predicate_2dx730e126114cf2e57_10 <= 998
 R72: rho_G_2dx1d1ff920146f2ed0_0 - 5 rho_predicate_2dx730e126114cf2e57_5
   <= 0
 R73: z_G_2dx1d1ff920146f2ed0_0 - z_predicate_2dx730e126114cf2e57_5 <= 0
 R74: rho_G_2dx1d1ff920146f2ed0_0 - 5 rho_predicate_2dx730e126114cf2e57_6
   <= 0
 R75: z_G_2dx1d1ff920146f2ed0_0 - z_predicate_2dx730e126114cf2e57_6 <= 0
 R76: rho_G_2dx1d1ff920146f2ed0_0 - 5 rho_predicate_2dx730e126114cf2e57_7
   <= 0
 R77: z_G_2dx1d1ff920146f2ed0_0 - z_predicate_2dx730e126114cf2e57_7 <= 0
 R78: rho_G_2dx1d1ff920146f2ed0_0 - 5 rho_predicate_2dx730e126114cf2e57_8
   <= 0
 R79: z_G_2dx1d1ff920146f2ed0_0 - z_predicate_2dx730e126114cf2e57_8 <= 0
 R80: rho_G_2dx1d1ff920146f2ed0_0 - 5 rho_predicate_2dx730e126114cf2e57_9
   <= 0
 R81: z_G_2dx1d1ff920146f2ed0_0 - z_predicate_2dx730e126114cf2e57_9 <= 0
 R82: rho_G_2dx1d1ff920146f2ed0_0 - 5 rho_predicate_2dx730e126114cf2e57_10
   <= 0
 R83: z_G_2dx1d1ff920146f2ed0_0 - z_predicate_2dx730e126114cf2e57_10 <= 0
 R84: z_5 - 1000 z_predicate_2dx33b18e258c171243_5
   - rho_predicate_2dx33b18e258c171243_5 <= 1
 R85: z_5 - 1000 z_predicate_2dx33b18e258c171243_5
   - rho_predicate_2dx33b18e258c171243_5 >= -999
 R86: z_6 - 1000 z_predicate_2dx33b18e258c171243_6
   - rho_predicate_2dx33b18e258c171243_6 <= 1
 R87: z_6 - 1000 z_predicate_2dx33b18e258c171243_6
   - rho_predicate_2dx33b18e258c171243_6 >= -999
 R88: z_7 - 1000 z_predicate_2dx33b18e258c171243_7
   - rho_predicate_2dx33b18e258c171243_7 <= 1
 R89: z_7 - 1000 z_predicate_2dx33b18e258c171243_7
   - rho_predicate_2dx33b18e258c171243_7 >= -999
 R90: z_8 - 1000 z_predicate_2dx33b18e258c171243_8
   - rho_predicate_2dx33b18e258c171243_8 <= 1
 R91: z_8 - 1000 z_predicate_2dx33b18e258c171243_8
   - rho_predicate_2dx33b18e258c171243_8 >= -999
 R92: z_9 - 1000 z_predicate_2dx33b18e258c171243_9
   - rho_predicate_2dx33b18e258c171243_9 <= 1
 R93: z_9 - 1000 z_predicate_2dx33b18e258c171243_9
   - rho_predicate_2dx33b18e258c171243_9 >= -999
 R94: z_10 - 1000 z_predicate_2dx33b18e258c171243_10
   - rho_predicate_2dx33b18e258c171243_10 <= 1
 R95: z_10 - 1000 z_predicate_2dx33b18e258c171243_10
   - rho_predicate_2dx33b18e258c171243_10 >= -999
 R96: rho_G_2bx732f4e90cfac6b2_0 - 5 rho_predicate_2dx33b18e258c171243_5
   <= 0
 R97: z_G_2bx732f4e90cfac6b2_0 - z_predicate_2dx33b18e258c171243_5 <= 0
 R98: rho_G_2bx732f4e90cfac6b2_0 - 5 rho_predicate_2dx33b18e258c171243_6
   <= 0
 R99: z_G_2bx732f4e90cfac6b2_0 - z_predicate_2dx33b18e258c171243_6 <= 0
 R100: rho_G_2bx732f4e90cfac6b2_0 - 5 rho_predicate_2dx33b18e258c171243_7
   <= 0
 R101: z_G_2bx732f4e90cfac6b2_0 - z_predicate_2dx33b18e258c171243_7 <= 0
 R102: rho_G_2bx732f4e90cfac6b2_0 - 5 rho_predicate_2dx33b18e258c171243_8
   <= 0
 R103: z_G_2bx732f4e90cfac6b2_0 - z_predicate_2dx33b18e258c171243_8 <= 0
 R104: rho_G_2bx732f4e90cfac6b2_0 - 5 rho_predicate_2dx33b18e258c171243_9
   <= 0
 R105: z_G_2bx732f4e90cfac6b2_0 - z_predicate_2dx33b18e258c171243_9 <= 0
 R106: rho_G_2bx732f4e90cfac6b2_0 - 5 rho_predicate_2dx33b18e258c171243_10
   <= 0
 R107: z_G_2bx732f4e90cfac6b2_0 - z_predicate_2dx33b18e258c171243_10 <= 0
 R108: rho_&&_2dx2db83bba55f505ef_0 - rho_G_2dx706aecdda938fda_0 <= 0
 R109: z_&&_2dx2db83bba55f505ef_0 - z_G_2dx706aecdda938fda_0 <= 0
 R110: rho_&&_2dx2db83bba55f505ef_0 - 2 rho_G_2dx1d1ff920146f2ed0_0 <= 0
 R111: z_&&_2dx2db83bba55f505ef_0 - z_G_2dx1d1ff920146f2ed0_0 <= 0
 R112: rho_&&_2dx2db83bba55f505ef_0 - 3 rho_G_2bx732f4e90cfac6b2_0 <= 0
 R113: z_&&_2dx2db83bba55f505ef_0 - z_G_2bx732f4e90cfac6b2_0 <= 0
 formula_satisfaction: z_&&_2dx2db83bba55f505ef_0 = 1
Bounds
 -10 <= x_0 <= 10
 -10 <= y_0 <= 10
 -10 <= z_0 <= 10
 -3 <= u_0 <= 3
 -3 <= v_0 <= 3
 -3 <= w_0 <= 3
 -10 <= x_1 <= 10
 -10 <= y_1 <= 10
 -10 <= z_1 <= 10
 -3 <= u_1 <= 3
 -3 <= v_1 <= 3
 -3 <= w_1 <= 3
 -10 <= x_2 <= 10
 -10 <= y_2 <= 10
 -10 <= z_2 <= 10
 -3 <= u_2 <= 3
 -3 <= v_2 <= 3
 -3 <= w_2 <= 3
 -10 <= x_3 <= 10
 -10 <= y_3 <= 10
 -10 <= z_3 <= 10
 -3 <= u_3 <= 3
 -3 <= v_3 <= 3
 -3 <= w_3 <= 3
 -10 <= x_4 <= 10
 -10 <= y_4 <= 10
 -10 <= z_4 <= 10
 -3 <= u_4 <= 3
 -3 <= v_4 <= 3
 -3 <= w_4 <= 3
 -10 <= x_5 <= 10
 -10 <= y_5 <= 10
 -10 <= z_5 <= 10
 -3 <= u_5 <= 3
 -3 <= v_5 <= 3
 -3 <= w_5 <= 3
 -10 <= x_6 <= 10
 -10 <= y_6 <= 10
 -10 <= z_6 <= 10
 -3 <= u_6 <= 3
 -3 <= v_6 <= 3
 -3 <= w_6 <= 3
 -10 <= x_7 <= 10
 -10 <= y_7 <= 10
 -10 <= z_7 <= 10
 -3 <= u_7 <= 3
 -3 <= v_7 <= 3
 -3 <= w_7 <= 3
 -10 <= x_8 <= 10
 -10 <= y_8 <= 10
 -10 <= z_8 <= 10
 -3 <= u_8 <= 3
 -3 <= v_8 <= 3
 -3 <= w_8 <= 3
 -10 <= x_9 <= 10
 -10 <= y_9 <= 10
 -10 <= z_9 <= 10
 -3 <= u_9 <= 3
 -3 <= v_9 <= 3
 -3 <= w_9 <= 3
 -10 <= x_10 <= 10
 -10 <= y_10 <= 10
 -10 <= z_10 <= 10
 -3 <= u_10 <= 3
 -3 <= v_10 <= 3
 -3 <= w_10 <= 3
 z_&&_2dx2db83bba55f505ef_0 <= 1
 rho_&&_2dx2db83bba55f505ef_0 free
 z_G_2dx706aecdda938fda_0 <= 1
 rho_G_2dx706aecdda938fda_0 free
 rho_predicate_2dx22dd95ed78b4d217_5 free
 rho_predicate_2dx22dd95ed78b4d217_6 free
 rho_predicate_2dx22dd95ed78b4d217_7 free
 rho_predicate_2dx22dd95ed78b4d217_8 free
 rho_predicate_2dx22dd95ed78b4d217_9 free
 rho_predicate_2dx22dd95ed78b4d217_10 free
 z_G_2dx1d1ff920146f2ed0_0 <= 1
 rho_G_2dx1d1ff920146f2ed0_0 free
 rho_predicate_2dx730e126114cf2e57_5 free
 rho_predicate_2dx730e126114cf2e57_6 free
 rho_predicate_2dx730e126114cf2e57_7 free
 rho_predicate_2dx730e126114cf2e57_8 free
 rho_predicate_2dx730e126114cf2e57_9 free
 rho_predicate_2dx730e126114cf2e57_10 free
 z_G_2bx732f4e90cfac6b2_0 <= 1
 rho_G_2bx732f4e90cfac6b2_0 free
 rho_predicate_2dx33b18e258c171243_5 free
 rho_predicate_2dx33b18e258c171243_6 free
 rho_predicate_2dx33b18e258c171243_7 free
 rho_predicate_2dx33b18e258c171243_8 free
 rho_predicate_2dx33b18e258c171243_9 free
 rho_predicate_2dx33b18e258c171243_10 free
Binaries
 z_predicate_2dx22dd95ed78b4d217_5 z_predicate_2dx22dd95ed78b4d217_6
 z_predicate_2dx22dd95ed78b4d217_7 z_predicate_2dx22dd95ed78b4d217_8
 z_predicate_2dx22dd95ed78b4d217_9 z_predicate_2dx22dd95ed78b4d217_10
 z_predicate_2dx730e126114cf2e57_5 z_predicate_2dx730e126114cf2e57_6
 z_predicate_2dx730e126114cf2e57_7 z_predicate_2dx730e126114cf2e57_8
 z_predicate_2dx730e126114cf2e57_9 z_predicate_2dx730e126114cf2e57_10
 z_predicate_2dx33b18e258c171243_5 z_predicate_2dx33b18e258c171243_6
 z_predicate_2dx33b18e258c171243_7 z_predicate_2dx33b18e258c171243_8
 z_predicate_2dx33b18e258c171243_9 z_predicate_2dx33b18e258c171243_10
End
