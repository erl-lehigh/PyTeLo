\ Model S-WSTL formula: (((G[1.0, 5.0]^<lambda> (x >= 7.0)) ||^<lambda> (G[1.0, 5.0]^<lambda> (y <= 2.0))) &&^<lambda> ((G[5.0, 10.0]^<lambda> (x <= 3.0)) ||^<lambda> (G[5.0, 10.0]^<lambda> (y >= 8.0))))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  rho_&&_2dx57a890f3b8d44acd_0
Subject To
 R0: x_0 = 0
 R1: y_0 = 0
 R2: x_1 - 1000 z_predicate_2dx5a605e8b6db0d82b_1
   - rho_predicate_2dx5a605e8b6db0d82b_1 >= -993
 R3: x_1 - 1000 z_predicate_2dx5a605e8b6db0d82b_1
   - rho_predicate_2dx5a605e8b6db0d82b_1 <= 7
 R4: x_2 - 1000 z_predicate_2dx5a605e8b6db0d82b_2
   - rho_predicate_2dx5a605e8b6db0d82b_2 >= -993
 R5: x_2 - 1000 z_predicate_2dx5a605e8b6db0d82b_2
   - rho_predicate_2dx5a605e8b6db0d82b_2 <= 7
 R6: x_3 - 1000 z_predicate_2dx5a605e8b6db0d82b_3
   - rho_predicate_2dx5a605e8b6db0d82b_3 >= -993
 R7: x_3 - 1000 z_predicate_2dx5a605e8b6db0d82b_3
   - rho_predicate_2dx5a605e8b6db0d82b_3 <= 7
 R8: x_4 - 1000 z_predicate_2dx5a605e8b6db0d82b_4
   - rho_predicate_2dx5a605e8b6db0d82b_4 >= -993
 R9: x_4 - 1000 z_predicate_2dx5a605e8b6db0d82b_4
   - rho_predicate_2dx5a605e8b6db0d82b_4 <= 7
 R10: x_5 - 1000 z_predicate_2dx5a605e8b6db0d82b_5
   - rho_predicate_2dx5a605e8b6db0d82b_5 >= -993
 R11: x_5 - 1000 z_predicate_2dx5a605e8b6db0d82b_5
   - rho_predicate_2dx5a605e8b6db0d82b_5 <= 7
 R12: rho_G_2dx1a8a6556e9e7f9b3_0 - 0.1 rho_predicate_2dx5a605e8b6db0d82b_1
   <= 0
 R13: z_G_2dx1a8a6556e9e7f9b3_0 - z_predicate_2dx5a605e8b6db0d82b_1 <= 0
 R14: rho_G_2dx1a8a6556e9e7f9b3_0 - 0.2 rho_predicate_2dx5a605e8b6db0d82b_2
   <= 0
 R15: z_G_2dx1a8a6556e9e7f9b3_0 - z_predicate_2dx5a605e8b6db0d82b_2 <= 0
 R16: rho_G_2dx1a8a6556e9e7f9b3_0 - 0.3 rho_predicate_2dx5a605e8b6db0d82b_3
   <= 0
 R17: z_G_2dx1a8a6556e9e7f9b3_0 - z_predicate_2dx5a605e8b6db0d82b_3 <= 0
 R18: rho_G_2dx1a8a6556e9e7f9b3_0 - 0.4 rho_predicate_2dx5a605e8b6db0d82b_4
   <= 0
 R19: z_G_2dx1a8a6556e9e7f9b3_0 - z_predicate_2dx5a605e8b6db0d82b_4 <= 0
 R20: rho_G_2dx1a8a6556e9e7f9b3_0 - 0.5 rho_predicate_2dx5a605e8b6db0d82b_5
   <= 0
 R21: z_G_2dx1a8a6556e9e7f9b3_0 - z_predicate_2dx5a605e8b6db0d82b_5 <= 0
 R22: z_G_2dx1a8a6556e9e7f9b3_0 - z_predicate_2dx5a605e8b6db0d82b_1
   - z_predicate_2dx5a605e8b6db0d82b_2 - z_predicate_2dx5a605e8b6db0d82b_3
   - z_predicate_2dx5a605e8b6db0d82b_4 - z_predicate_2dx5a605e8b6db0d82b_5
   >= -4
 R23: y_1 + 1000 z_predicate_2dxe594ff07ec5e5b3_1
   + rho_predicate_2dxe594ff07ec5e5b3_1 <= 1002
 R24: y_1 + 1000 z_predicate_2dxe594ff07ec5e5b3_1
   + rho_predicate_2dxe594ff07ec5e5b3_1 >= 2
 R25: y_2 + 1000 z_predicate_2dxe594ff07ec5e5b3_2
   + rho_predicate_2dxe594ff07ec5e5b3_2 <= 1002
 R26: y_2 + 1000 z_predicate_2dxe594ff07ec5e5b3_2
   + rho_predicate_2dxe594ff07ec5e5b3_2 >= 2
 R27: y_3 + 1000 z_predicate_2dxe594ff07ec5e5b3_3
   + rho_predicate_2dxe594ff07ec5e5b3_3 <= 1002
 R28: y_3 + 1000 z_predicate_2dxe594ff07ec5e5b3_3
   + rho_predicate_2dxe594ff07ec5e5b3_3 >= 2
 R29: y_4 + 1000 z_predicate_2dxe594ff07ec5e5b3_4
   + rho_predicate_2dxe594ff07ec5e5b3_4 <= 1002
 R30: y_4 + 1000 z_predicate_2dxe594ff07ec5e5b3_4
   + rho_predicate_2dxe594ff07ec5e5b3_4 >= 2
 R31: y_5 + 1000 z_predicate_2dxe594ff07ec5e5b3_5
   + rho_predicate_2dxe594ff07ec5e5b3_5 <= 1002
 R32: y_5 + 1000 z_predicate_2dxe594ff07ec5e5b3_5
   + rho_predicate_2dxe594ff07ec5e5b3_5 >= 2
 R33: rho_G_2dx51f88492ab40220b_0 - 0.1 rho_predicate_2dxe594ff07ec5e5b3_1
   <= 0
 R34: z_G_2dx51f88492ab40220b_0 - z_predicate_2dxe594ff07ec5e5b3_1 <= 0
 R35: rho_G_2dx51f88492ab40220b_0 - 0.2 rho_predicate_2dxe594ff07ec5e5b3_2
   <= 0
 R36: z_G_2dx51f88492ab40220b_0 - z_predicate_2dxe594ff07ec5e5b3_2 <= 0
 R37: rho_G_2dx51f88492ab40220b_0 - 0.3 rho_predicate_2dxe594ff07ec5e5b3_3
   <= 0
 R38: z_G_2dx51f88492ab40220b_0 - z_predicate_2dxe594ff07ec5e5b3_3 <= 0
 R39: rho_G_2dx51f88492ab40220b_0 - 0.4 rho_predicate_2dxe594ff07ec5e5b3_4
   <= 0
 R40: z_G_2dx51f88492ab40220b_0 - z_predicate_2dxe594ff07ec5e5b3_4 <= 0
 R41: rho_G_2dx51f88492ab40220b_0 - 0.5 rho_predicate_2dxe594ff07ec5e5b3_5
   <= 0
 R42: z_G_2dx51f88492ab40220b_0 - z_predicate_2dxe594ff07ec5e5b3_5 <= 0
 R43: z_G_2dx51f88492ab40220b_0 - z_predicate_2dxe594ff07ec5e5b3_1
   - z_predicate_2dxe594ff07ec5e5b3_2 - z_predicate_2dxe594ff07ec5e5b3_3
   - z_predicate_2dxe594ff07ec5e5b3_4 - z_predicate_2dxe594ff07ec5e5b3_5
   >= -4
 R44: rho_||_2dx3c2c7ee4adbd2f8b_0 - 0.2 rho_G_2dx1a8a6556e9e7f9b3_0
   + 1000 zhat_G_2dx1a8a6556e9e7f9b3_2dx3c2c7ee4adbd2f8b_0 <= 1000
 R45: z_||_2dx3c2c7ee4adbd2f8b_0 - z_G_2dx1a8a6556e9e7f9b3_0 >= 0
 R46: - z_G_2dx1a8a6556e9e7f9b3_0
   + zhat_G_2dx1a8a6556e9e7f9b3_2dx3c2c7ee4adbd2f8b_0 <= 0
 R47: rho_||_2dx3c2c7ee4adbd2f8b_0 - 0.8 rho_G_2dx51f88492ab40220b_0
   + 1000 zhat_G_2dx51f88492ab40220b_2dx3c2c7ee4adbd2f8b_0 <= 1000
 R48: z_||_2dx3c2c7ee4adbd2f8b_0 - z_G_2dx51f88492ab40220b_0 >= 0
 R49: - z_G_2dx51f88492ab40220b_0
   + zhat_G_2dx51f88492ab40220b_2dx3c2c7ee4adbd2f8b_0 <= 0
 R50: z_||_2dx3c2c7ee4adbd2f8b_0 - z_G_2dx1a8a6556e9e7f9b3_0
   - z_G_2dx51f88492ab40220b_0 <= 0
 R51: zhat_G_2dx1a8a6556e9e7f9b3_2dx3c2c7ee4adbd2f8b_0
   + zhat_G_2dx51f88492ab40220b_2dx3c2c7ee4adbd2f8b_0 >= 1
 R52: x_5 + 1000 z_predicate_2dx5dba1e6a7b84e365_5
   + rho_predicate_2dx5dba1e6a7b84e365_5 <= 1003
 R53: x_5 + 1000 z_predicate_2dx5dba1e6a7b84e365_5
   + rho_predicate_2dx5dba1e6a7b84e365_5 >= 3
 R54: x_6 + 1000 z_predicate_2dx5dba1e6a7b84e365_6
   + rho_predicate_2dx5dba1e6a7b84e365_6 <= 1003
 R55: x_6 + 1000 z_predicate_2dx5dba1e6a7b84e365_6
   + rho_predicate_2dx5dba1e6a7b84e365_6 >= 3
 R56: x_7 + 1000 z_predicate_2dx5dba1e6a7b84e365_7
   + rho_predicate_2dx5dba1e6a7b84e365_7 <= 1003
 R57: x_7 + 1000 z_predicate_2dx5dba1e6a7b84e365_7
   + rho_predicate_2dx5dba1e6a7b84e365_7 >= 3
 R58: x_8 + 1000 z_predicate_2dx5dba1e6a7b84e365_8
   + rho_predicate_2dx5dba1e6a7b84e365_8 <= 1003
 R59: x_8 + 1000 z_predicate_2dx5dba1e6a7b84e365_8
   + rho_predicate_2dx5dba1e6a7b84e365_8 >= 3
 R60: x_9 + 1000 z_predicate_2dx5dba1e6a7b84e365_9
   + rho_predicate_2dx5dba1e6a7b84e365_9 <= 1003
 R61: x_9 + 1000 z_predicate_2dx5dba1e6a7b84e365_9
   + rho_predicate_2dx5dba1e6a7b84e365_9 >= 3
 R62: x_10 + 1000 z_predicate_2dx5dba1e6a7b84e365_10
   + rho_predicate_2dx5dba1e6a7b84e365_10 <= 1003
 R63: x_10 + 1000 z_predicate_2dx5dba1e6a7b84e365_10
   + rho_predicate_2dx5dba1e6a7b84e365_10 >= 3
 R64: rho_G_2bx4e1862dbc1242c7c_0 - 0.5 rho_predicate_2dx5dba1e6a7b84e365_5
   <= 0
 R65: z_G_2bx4e1862dbc1242c7c_0 - z_predicate_2dx5dba1e6a7b84e365_5 <= 0
 R66: rho_G_2bx4e1862dbc1242c7c_0 - 0.5 rho_predicate_2dx5dba1e6a7b84e365_6
   <= 0
 R67: z_G_2bx4e1862dbc1242c7c_0 - z_predicate_2dx5dba1e6a7b84e365_6 <= 0
 R68: rho_G_2bx4e1862dbc1242c7c_0 - 0.4 rho_predicate_2dx5dba1e6a7b84e365_7
   <= 0
 R69: z_G_2bx4e1862dbc1242c7c_0 - z_predicate_2dx5dba1e6a7b84e365_7 <= 0
 R70: rho_G_2bx4e1862dbc1242c7c_0 - 0.3 rho_predicate_2dx5dba1e6a7b84e365_8
   <= 0
 R71: z_G_2bx4e1862dbc1242c7c_0 - z_predicate_2dx5dba1e6a7b84e365_8 <= 0
 R72: rho_G_2bx4e1862dbc1242c7c_0 - 0.2 rho_predicate_2dx5dba1e6a7b84e365_9
   <= 0
 R73: z_G_2bx4e1862dbc1242c7c_0 - z_predicate_2dx5dba1e6a7b84e365_9 <= 0
 R74: rho_G_2bx4e1862dbc1242c7c_0
   - 0.1 rho_predicate_2dx5dba1e6a7b84e365_10 <= 0
 R75: z_G_2bx4e1862dbc1242c7c_0 - z_predicate_2dx5dba1e6a7b84e365_10 <= 0
 R76: z_G_2bx4e1862dbc1242c7c_0 - z_predicate_2dx5dba1e6a7b84e365_5
   - z_predicate_2dx5dba1e6a7b84e365_6 - z_predicate_2dx5dba1e6a7b84e365_7
   - z_predicate_2dx5dba1e6a7b84e365_8 - z_predicate_2dx5dba1e6a7b84e365_9
   - z_predicate_2dx5dba1e6a7b84e365_10 >= -5
 R77: y_5 - 1000 z_predicate_2bx70ac945c4f28d9ed_5
   - rho_predicate_2bx70ac945c4f28d9ed_5 >= -992
 R78: y_5 - 1000 z_predicate_2bx70ac945c4f28d9ed_5
   - rho_predicate_2bx70ac945c4f28d9ed_5 <= 8
 R79: y_6 - 1000 z_predicate_2bx70ac945c4f28d9ed_6
   - rho_predicate_2bx70ac945c4f28d9ed_6 >= -992
 R80: y_6 - 1000 z_predicate_2bx70ac945c4f28d9ed_6
   - rho_predicate_2bx70ac945c4f28d9ed_6 <= 8
 R81: y_7 - 1000 z_predicate_2bx70ac945c4f28d9ed_7
   - rho_predicate_2bx70ac945c4f28d9ed_7 >= -992
 R82: y_7 - 1000 z_predicate_2bx70ac945c4f28d9ed_7
   - rho_predicate_2bx70ac945c4f28d9ed_7 <= 8
 R83: y_8 - 1000 z_predicate_2bx70ac945c4f28d9ed_8
   - rho_predicate_2bx70ac945c4f28d9ed_8 >= -992
 R84: y_8 - 1000 z_predicate_2bx70ac945c4f28d9ed_8
   - rho_predicate_2bx70ac945c4f28d9ed_8 <= 8
 R85: y_9 - 1000 z_predicate_2bx70ac945c4f28d9ed_9
   - rho_predicate_2bx70ac945c4f28d9ed_9 >= -992
 R86: y_9 - 1000 z_predicate_2bx70ac945c4f28d9ed_9
   - rho_predicate_2bx70ac945c4f28d9ed_9 <= 8
 R87: y_10 - 1000 z_predicate_2bx70ac945c4f28d9ed_10
   - rho_predicate_2bx70ac945c4f28d9ed_10 >= -992
 R88: y_10 - 1000 z_predicate_2bx70ac945c4f28d9ed_10
   - rho_predicate_2bx70ac945c4f28d9ed_10 <= 8
 R89: rho_G_2bx213d83069bb0ad12_0 - 0.5 rho_predicate_2bx70ac945c4f28d9ed_5
   <= 0
 R90: z_G_2bx213d83069bb0ad12_0 - z_predicate_2bx70ac945c4f28d9ed_5 <= 0
 R91: rho_G_2bx213d83069bb0ad12_0 - 0.5 rho_predicate_2bx70ac945c4f28d9ed_6
   <= 0
 R92: z_G_2bx213d83069bb0ad12_0 - z_predicate_2bx70ac945c4f28d9ed_6 <= 0
 R93: rho_G_2bx213d83069bb0ad12_0 - 0.4 rho_predicate_2bx70ac945c4f28d9ed_7
   <= 0
 R94: z_G_2bx213d83069bb0ad12_0 - z_predicate_2bx70ac945c4f28d9ed_7 <= 0
 R95: rho_G_2bx213d83069bb0ad12_0 - 0.3 rho_predicate_2bx70ac945c4f28d9ed_8
   <= 0
 R96: z_G_2bx213d83069bb0ad12_0 - z_predicate_2bx70ac945c4f28d9ed_8 <= 0
 R97: rho_G_2bx213d83069bb0ad12_0 - 0.2 rho_predicate_2bx70ac945c4f28d9ed_9
   <= 0
 R98: z_G_2bx213d83069bb0ad12_0 - z_predicate_2bx70ac945c4f28d9ed_9 <= 0
 R99: rho_G_2bx213d83069bb0ad12_0
   - 0.1 rho_predicate_2bx70ac945c4f28d9ed_10 <= 0
 R100: z_G_2bx213d83069bb0ad12_0 - z_predicate_2bx70ac945c4f28d9ed_10 <= 0
 R101: z_G_2bx213d83069bb0ad12_0 - z_predicate_2bx70ac945c4f28d9ed_5
   - z_predicate_2bx70ac945c4f28d9ed_6 - z_predicate_2bx70ac945c4f28d9ed_7
   - z_predicate_2bx70ac945c4f28d9ed_8 - z_predicate_2bx70ac945c4f28d9ed_9
   - z_predicate_2bx70ac945c4f28d9ed_10 >= -5
 R102: rho_||_2dx18de549da475245d_0 - 0.2 rho_G_2bx4e1862dbc1242c7c_0
   + 1000 zhat_G_2bx4e1862dbc1242c7c_2dx18de549da475245d_0 <= 1000
 R103: z_||_2dx18de549da475245d_0 - z_G_2bx4e1862dbc1242c7c_0 >= 0
 R104: - z_G_2bx4e1862dbc1242c7c_0
   + zhat_G_2bx4e1862dbc1242c7c_2dx18de549da475245d_0 <= 0
 R105: rho_||_2dx18de549da475245d_0 - 0.8 rho_G_2bx213d83069bb0ad12_0
   + 1000 zhat_G_2bx213d83069bb0ad12_2dx18de549da475245d_0 <= 1000
 R106: z_||_2dx18de549da475245d_0 - z_G_2bx213d83069bb0ad12_0 >= 0
 R107: - z_G_2bx213d83069bb0ad12_0
   + zhat_G_2bx213d83069bb0ad12_2dx18de549da475245d_0 <= 0
 R108: z_||_2dx18de549da475245d_0 - z_G_2bx4e1862dbc1242c7c_0
   - z_G_2bx213d83069bb0ad12_0 <= 0
 R109: zhat_G_2bx4e1862dbc1242c7c_2dx18de549da475245d_0
   + zhat_G_2bx213d83069bb0ad12_2dx18de549da475245d_0 >= 1
 R110: rho_&&_2dx57a890f3b8d44acd_0 - 0.5 rho_||_2dx3c2c7ee4adbd2f8b_0
   <= 0
 R111: z_&&_2dx57a890f3b8d44acd_0 - z_||_2dx3c2c7ee4adbd2f8b_0 <= 0
 R112: rho_&&_2dx57a890f3b8d44acd_0 - 0.5 rho_||_2dx18de549da475245d_0
   <= 0
 R113: z_&&_2dx57a890f3b8d44acd_0 - z_||_2dx18de549da475245d_0 <= 0
 R114: z_&&_2dx57a890f3b8d44acd_0 - z_||_2dx3c2c7ee4adbd2f8b_0
   - z_||_2dx18de549da475245d_0 >= -1
 formula_satisfaction: z_&&_2dx57a890f3b8d44acd_0 = 1
Bounds
 x_0 <= 10
 y_0 <= 10
 x_1 <= 10
 y_1 <= 10
 x_2 <= 10
 y_2 <= 10
 x_3 <= 10
 y_3 <= 10
 x_4 <= 10
 y_4 <= 10
 x_5 <= 10
 y_5 <= 10
 x_6 <= 10
 y_6 <= 10
 x_7 <= 10
 y_7 <= 10
 x_8 <= 10
 y_8 <= 10
 x_9 <= 10
 y_9 <= 10
 x_10 <= 10
 y_10 <= 10
 z_&&_2dx57a890f3b8d44acd_0 <= 1
 rho_&&_2dx57a890f3b8d44acd_0 free
 z_||_2dx3c2c7ee4adbd2f8b_0 <= 1
 rho_||_2dx3c2c7ee4adbd2f8b_0 free
 z_G_2dx1a8a6556e9e7f9b3_0 <= 1
 rho_G_2dx1a8a6556e9e7f9b3_0 free
 rho_predicate_2dx5a605e8b6db0d82b_1 free
 rho_predicate_2dx5a605e8b6db0d82b_2 free
 rho_predicate_2dx5a605e8b6db0d82b_3 free
 rho_predicate_2dx5a605e8b6db0d82b_4 free
 rho_predicate_2dx5a605e8b6db0d82b_5 free
 z_G_2dx51f88492ab40220b_0 <= 1
 rho_G_2dx51f88492ab40220b_0 free
 rho_predicate_2dxe594ff07ec5e5b3_1 free
 rho_predicate_2dxe594ff07ec5e5b3_2 free
 rho_predicate_2dxe594ff07ec5e5b3_3 free
 rho_predicate_2dxe594ff07ec5e5b3_4 free
 rho_predicate_2dxe594ff07ec5e5b3_5 free
 z_||_2dx18de549da475245d_0 <= 1
 rho_||_2dx18de549da475245d_0 free
 z_G_2bx4e1862dbc1242c7c_0 <= 1
 rho_G_2bx4e1862dbc1242c7c_0 free
 rho_predicate_2dx5dba1e6a7b84e365_5 free
 rho_predicate_2dx5dba1e6a7b84e365_6 free
 rho_predicate_2dx5dba1e6a7b84e365_7 free
 rho_predicate_2dx5dba1e6a7b84e365_8 free
 rho_predicate_2dx5dba1e6a7b84e365_9 free
 rho_predicate_2dx5dba1e6a7b84e365_10 free
 z_G_2bx213d83069bb0ad12_0 <= 1
 rho_G_2bx213d83069bb0ad12_0 free
 rho_predicate_2bx70ac945c4f28d9ed_5 free
 rho_predicate_2bx70ac945c4f28d9ed_6 free
 rho_predicate_2bx70ac945c4f28d9ed_7 free
 rho_predicate_2bx70ac945c4f28d9ed_8 free
 rho_predicate_2bx70ac945c4f28d9ed_9 free
 rho_predicate_2bx70ac945c4f28d9ed_10 free
Binaries
 z_predicate_2dx5a605e8b6db0d82b_1 z_predicate_2dx5a605e8b6db0d82b_2
 z_predicate_2dx5a605e8b6db0d82b_3 z_predicate_2dx5a605e8b6db0d82b_4
 z_predicate_2dx5a605e8b6db0d82b_5 z_predicate_2dxe594ff07ec5e5b3_1
 z_predicate_2dxe594ff07ec5e5b3_2 z_predicate_2dxe594ff07ec5e5b3_3
 z_predicate_2dxe594ff07ec5e5b3_4 z_predicate_2dxe594ff07ec5e5b3_5
 zhat_G_2dx1a8a6556e9e7f9b3_2dx3c2c7ee4adbd2f8b_0
 zhat_G_2dx51f88492ab40220b_2dx3c2c7ee4adbd2f8b_0
 z_predicate_2dx5dba1e6a7b84e365_5 z_predicate_2dx5dba1e6a7b84e365_6
 z_predicate_2dx5dba1e6a7b84e365_7 z_predicate_2dx5dba1e6a7b84e365_8
 z_predicate_2dx5dba1e6a7b84e365_9 z_predicate_2dx5dba1e6a7b84e365_10
 z_predicate_2bx70ac945c4f28d9ed_5 z_predicate_2bx70ac945c4f28d9ed_6
 z_predicate_2bx70ac945c4f28d9ed_7 z_predicate_2bx70ac945c4f28d9ed_8
 z_predicate_2bx70ac945c4f28d9ed_9 z_predicate_2bx70ac945c4f28d9ed_10
 zhat_G_2bx4e1862dbc1242c7c_2dx18de549da475245d_0
 zhat_G_2bx213d83069bb0ad12_2dx18de549da475245d_0
End
