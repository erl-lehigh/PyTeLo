\ Model S-WSTL formula: ((G[8.0, 10.0]^<lambda> ((x >= 6.0) &&^<lambda> (y <= -6.0))) &&^<lambda> (G[8.0, 10.0]^<lambda> ((x <= -6.0) &&^<lambda> (y >= 6.0))) &&^<lambda> (G[0.0, 1.0]^<lambda> ((x <= -6.0) &&^<lambda> (y <= -6.0))))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0 u_10 + 0 v_10 + 0 w_10 + rho_&&_2dx357e49ca96a6d288_0
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
 R30: x_0 = -9
 R31: y_0 = -9
 R32: z_0 = 0
 R33: u_0 = 0
 R34: v_0 = 0
 R35: w_0 = 0
 R36: x_8 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_8
   - rho_predicate_2dx4c7fa34b9cfd78d2_8 >= -994
 R37: x_8 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_8
   - rho_predicate_2dx4c7fa34b9cfd78d2_8 <= 6
 R38: y_8 + 1000 z_predicate_2bx556f07e65bd9f395_8
   + rho_predicate_2bx556f07e65bd9f395_8 <= 994
 R39: y_8 + 1000 z_predicate_2bx556f07e65bd9f395_8
   + rho_predicate_2bx556f07e65bd9f395_8 >= -6
 R40: rho_&&_2dx77c13656f83eed1e_8 - rho_predicate_2dx4c7fa34b9cfd78d2_8
   <= 0
 R41: z_&&_2dx77c13656f83eed1e_8 - z_predicate_2dx4c7fa34b9cfd78d2_8 <= 0
 R42: rho_&&_2dx77c13656f83eed1e_8 - rho_predicate_2bx556f07e65bd9f395_8
   <= 0
 R43: z_&&_2dx77c13656f83eed1e_8 - z_predicate_2bx556f07e65bd9f395_8 <= 0
 R44: z_&&_2dx77c13656f83eed1e_8 - z_predicate_2dx4c7fa34b9cfd78d2_8
   - z_predicate_2bx556f07e65bd9f395_8 >= -1
 R45: x_9 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_9
   - rho_predicate_2dx4c7fa34b9cfd78d2_9 >= -994
 R46: x_9 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_9
   - rho_predicate_2dx4c7fa34b9cfd78d2_9 <= 6
 R47: y_9 + 1000 z_predicate_2bx556f07e65bd9f395_9
   + rho_predicate_2bx556f07e65bd9f395_9 <= 994
 R48: y_9 + 1000 z_predicate_2bx556f07e65bd9f395_9
   + rho_predicate_2bx556f07e65bd9f395_9 >= -6
 R49: rho_&&_2dx77c13656f83eed1e_9 - rho_predicate_2dx4c7fa34b9cfd78d2_9
   <= 0
 R50: z_&&_2dx77c13656f83eed1e_9 - z_predicate_2dx4c7fa34b9cfd78d2_9 <= 0
 R51: rho_&&_2dx77c13656f83eed1e_9 - rho_predicate_2bx556f07e65bd9f395_9
   <= 0
 R52: z_&&_2dx77c13656f83eed1e_9 - z_predicate_2bx556f07e65bd9f395_9 <= 0
 R53: z_&&_2dx77c13656f83eed1e_9 - z_predicate_2dx4c7fa34b9cfd78d2_9
   - z_predicate_2bx556f07e65bd9f395_9 >= -1
 R54: x_10 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_10
   - rho_predicate_2dx4c7fa34b9cfd78d2_10 >= -994
 R55: x_10 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_10
   - rho_predicate_2dx4c7fa34b9cfd78d2_10 <= 6
 R56: y_10 + 1000 z_predicate_2bx556f07e65bd9f395_10
   + rho_predicate_2bx556f07e65bd9f395_10 <= 994
 R57: y_10 + 1000 z_predicate_2bx556f07e65bd9f395_10
   + rho_predicate_2bx556f07e65bd9f395_10 >= -6
 R58: rho_&&_2dx77c13656f83eed1e_10 - rho_predicate_2dx4c7fa34b9cfd78d2_10
   <= 0
 R59: z_&&_2dx77c13656f83eed1e_10 - z_predicate_2dx4c7fa34b9cfd78d2_10
   <= 0
 R60: rho_&&_2dx77c13656f83eed1e_10 - rho_predicate_2bx556f07e65bd9f395_10
   <= 0
 R61: z_&&_2dx77c13656f83eed1e_10 - z_predicate_2bx556f07e65bd9f395_10
   <= 0
 R62: z_&&_2dx77c13656f83eed1e_10 - z_predicate_2dx4c7fa34b9cfd78d2_10
   - z_predicate_2bx556f07e65bd9f395_10 >= -1
 R63: rho_G_2bx3126109403624376_0 - rho_&&_2dx77c13656f83eed1e_8 <= 0
 R64: z_G_2bx3126109403624376_0 - z_&&_2dx77c13656f83eed1e_8 <= 0
 R65: rho_G_2bx3126109403624376_0 - rho_&&_2dx77c13656f83eed1e_9 <= 0
 R66: z_G_2bx3126109403624376_0 - z_&&_2dx77c13656f83eed1e_9 <= 0
 R67: rho_G_2bx3126109403624376_0 - rho_&&_2dx77c13656f83eed1e_10 <= 0
 R68: z_G_2bx3126109403624376_0 - z_&&_2dx77c13656f83eed1e_10 <= 0
 R69: z_G_2bx3126109403624376_0 - z_&&_2dx77c13656f83eed1e_8
   - z_&&_2dx77c13656f83eed1e_9 - z_&&_2dx77c13656f83eed1e_10 >= -2
 R70: x_8 + 1000 z_predicate_2bx5b8af825940a107a_8
   + rho_predicate_2bx5b8af825940a107a_8 <= 994
 R71: x_8 + 1000 z_predicate_2bx5b8af825940a107a_8
   + rho_predicate_2bx5b8af825940a107a_8 >= -6
 R72: y_8 - 1000 z_predicate_2bx32f72cccd281a177_8
   - rho_predicate_2bx32f72cccd281a177_8 >= -994
 R73: y_8 - 1000 z_predicate_2bx32f72cccd281a177_8
   - rho_predicate_2bx32f72cccd281a177_8 <= 6
 R74: rho_&&_2dx64e60b01d1682750_8 - rho_predicate_2bx5b8af825940a107a_8
   <= 0
 R75: z_&&_2dx64e60b01d1682750_8 - z_predicate_2bx5b8af825940a107a_8 <= 0
 R76: rho_&&_2dx64e60b01d1682750_8 - rho_predicate_2bx32f72cccd281a177_8
   <= 0
 R77: z_&&_2dx64e60b01d1682750_8 - z_predicate_2bx32f72cccd281a177_8 <= 0
 R78: z_&&_2dx64e60b01d1682750_8 - z_predicate_2bx5b8af825940a107a_8
   - z_predicate_2bx32f72cccd281a177_8 >= -1
 R79: x_9 + 1000 z_predicate_2bx5b8af825940a107a_9
   + rho_predicate_2bx5b8af825940a107a_9 <= 994
 R80: x_9 + 1000 z_predicate_2bx5b8af825940a107a_9
   + rho_predicate_2bx5b8af825940a107a_9 >= -6
 R81: y_9 - 1000 z_predicate_2bx32f72cccd281a177_9
   - rho_predicate_2bx32f72cccd281a177_9 >= -994
 R82: y_9 - 1000 z_predicate_2bx32f72cccd281a177_9
   - rho_predicate_2bx32f72cccd281a177_9 <= 6
 R83: rho_&&_2dx64e60b01d1682750_9 - rho_predicate_2bx5b8af825940a107a_9
   <= 0
 R84: z_&&_2dx64e60b01d1682750_9 - z_predicate_2bx5b8af825940a107a_9 <= 0
 R85: rho_&&_2dx64e60b01d1682750_9 - rho_predicate_2bx32f72cccd281a177_9
   <= 0
 R86: z_&&_2dx64e60b01d1682750_9 - z_predicate_2bx32f72cccd281a177_9 <= 0
 R87: z_&&_2dx64e60b01d1682750_9 - z_predicate_2bx5b8af825940a107a_9
   - z_predicate_2bx32f72cccd281a177_9 >= -1
 R88: x_10 + 1000 z_predicate_2bx5b8af825940a107a_10
   + rho_predicate_2bx5b8af825940a107a_10 <= 994
 R89: x_10 + 1000 z_predicate_2bx5b8af825940a107a_10
   + rho_predicate_2bx5b8af825940a107a_10 >= -6
 R90: y_10 - 1000 z_predicate_2bx32f72cccd281a177_10
   - rho_predicate_2bx32f72cccd281a177_10 >= -994
 R91: y_10 - 1000 z_predicate_2bx32f72cccd281a177_10
   - rho_predicate_2bx32f72cccd281a177_10 <= 6
 R92: rho_&&_2dx64e60b01d1682750_10 - rho_predicate_2bx5b8af825940a107a_10
   <= 0
 R93: z_&&_2dx64e60b01d1682750_10 - z_predicate_2bx5b8af825940a107a_10
   <= 0
 R94: rho_&&_2dx64e60b01d1682750_10 - rho_predicate_2bx32f72cccd281a177_10
   <= 0
 R95: z_&&_2dx64e60b01d1682750_10 - z_predicate_2bx32f72cccd281a177_10
   <= 0
 R96: z_&&_2dx64e60b01d1682750_10 - z_predicate_2bx5b8af825940a107a_10
   - z_predicate_2bx32f72cccd281a177_10 >= -1
 R97: rho_G_2bx2dc176d942bfc648_0 - rho_&&_2dx64e60b01d1682750_8 <= 0
 R98: z_G_2bx2dc176d942bfc648_0 - z_&&_2dx64e60b01d1682750_8 <= 0
 R99: rho_G_2bx2dc176d942bfc648_0 - rho_&&_2dx64e60b01d1682750_9 <= 0
 R100: z_G_2bx2dc176d942bfc648_0 - z_&&_2dx64e60b01d1682750_9 <= 0
 R101: rho_G_2bx2dc176d942bfc648_0 - rho_&&_2dx64e60b01d1682750_10 <= 0
 R102: z_G_2bx2dc176d942bfc648_0 - z_&&_2dx64e60b01d1682750_10 <= 0
 R103: z_G_2bx2dc176d942bfc648_0 - z_&&_2dx64e60b01d1682750_8
   - z_&&_2dx64e60b01d1682750_9 - z_&&_2dx64e60b01d1682750_10 >= -2
 R104: x_0 + 1000 z_predicate_2bx5b8af825940a107a_0
   + rho_predicate_2bx5b8af825940a107a_0 <= 994
 R105: x_0 + 1000 z_predicate_2bx5b8af825940a107a_0
   + rho_predicate_2bx5b8af825940a107a_0 >= -6
 R106: y_0 + 1000 z_predicate_2bx556f07e65bd9f395_0
   + rho_predicate_2bx556f07e65bd9f395_0 <= 994
 R107: y_0 + 1000 z_predicate_2bx556f07e65bd9f395_0
   + rho_predicate_2bx556f07e65bd9f395_0 >= -6
 R108: rho_&&_2bx4d9a906c9b43dcf4_0 - rho_predicate_2bx5b8af825940a107a_0
   <= 0
 R109: z_&&_2bx4d9a906c9b43dcf4_0 - z_predicate_2bx5b8af825940a107a_0 <= 0
 R110: rho_&&_2bx4d9a906c9b43dcf4_0 - rho_predicate_2bx556f07e65bd9f395_0
   <= 0
 R111: z_&&_2bx4d9a906c9b43dcf4_0 - z_predicate_2bx556f07e65bd9f395_0 <= 0
 R112: z_&&_2bx4d9a906c9b43dcf4_0 - z_predicate_2bx5b8af825940a107a_0
   - z_predicate_2bx556f07e65bd9f395_0 >= -1
 R113: x_1 + 1000 z_predicate_2bx5b8af825940a107a_1
   + rho_predicate_2bx5b8af825940a107a_1 <= 994
 R114: x_1 + 1000 z_predicate_2bx5b8af825940a107a_1
   + rho_predicate_2bx5b8af825940a107a_1 >= -6
 R115: y_1 + 1000 z_predicate_2bx556f07e65bd9f395_1
   + rho_predicate_2bx556f07e65bd9f395_1 <= 994
 R116: y_1 + 1000 z_predicate_2bx556f07e65bd9f395_1
   + rho_predicate_2bx556f07e65bd9f395_1 >= -6
 R117: rho_&&_2bx4d9a906c9b43dcf4_1 - rho_predicate_2bx5b8af825940a107a_1
   <= 0
 R118: z_&&_2bx4d9a906c9b43dcf4_1 - z_predicate_2bx5b8af825940a107a_1 <= 0
 R119: rho_&&_2bx4d9a906c9b43dcf4_1 - rho_predicate_2bx556f07e65bd9f395_1
   <= 0
 R120: z_&&_2bx4d9a906c9b43dcf4_1 - z_predicate_2bx556f07e65bd9f395_1 <= 0
 R121: z_&&_2bx4d9a906c9b43dcf4_1 - z_predicate_2bx5b8af825940a107a_1
   - z_predicate_2bx556f07e65bd9f395_1 >= -1
 R122: rho_G_2dx60319af456428e09_0 - rho_&&_2bx4d9a906c9b43dcf4_0 <= 0
 R123: z_G_2dx60319af456428e09_0 - z_&&_2bx4d9a906c9b43dcf4_0 <= 0
 R124: rho_G_2dx60319af456428e09_0 - rho_&&_2bx4d9a906c9b43dcf4_1 <= 0
 R125: z_G_2dx60319af456428e09_0 - z_&&_2bx4d9a906c9b43dcf4_1 <= 0
 R126: z_G_2dx60319af456428e09_0 - z_&&_2bx4d9a906c9b43dcf4_0
   - z_&&_2bx4d9a906c9b43dcf4_1 >= -1
 R127: rho_&&_2dx357e49ca96a6d288_0 - rho_G_2bx3126109403624376_0 <= 0
 R128: z_&&_2dx357e49ca96a6d288_0 - z_G_2bx3126109403624376_0 <= 0
 R129: rho_&&_2dx357e49ca96a6d288_0 - 20 rho_G_2bx2dc176d942bfc648_0 <= 0
 R130: z_&&_2dx357e49ca96a6d288_0 - z_G_2bx2dc176d942bfc648_0 <= 0
 R131: rho_&&_2dx357e49ca96a6d288_0 - rho_G_2dx60319af456428e09_0 <= 0
 R132: z_&&_2dx357e49ca96a6d288_0 - z_G_2dx60319af456428e09_0 <= 0
 R133: z_&&_2dx357e49ca96a6d288_0 - z_G_2bx3126109403624376_0
   - z_G_2bx2dc176d942bfc648_0 - z_G_2dx60319af456428e09_0 >= -2
 formula_satisfaction: z_&&_2dx357e49ca96a6d288_0 = 1
Bounds
 -9 <= x_0 <= 9
 -9 <= y_0 <= 9
 -9 <= z_0 <= 9
 -2 <= u_0 <= 2
 -2 <= v_0 <= 2
 -2 <= w_0 <= 2
 -9 <= x_1 <= 9
 -9 <= y_1 <= 9
 -9 <= z_1 <= 9
 -2 <= u_1 <= 2
 -2 <= v_1 <= 2
 -2 <= w_1 <= 2
 -9 <= x_2 <= 9
 -9 <= y_2 <= 9
 -9 <= z_2 <= 9
 -2 <= u_2 <= 2
 -2 <= v_2 <= 2
 -2 <= w_2 <= 2
 -9 <= x_3 <= 9
 -9 <= y_3 <= 9
 -9 <= z_3 <= 9
 -2 <= u_3 <= 2
 -2 <= v_3 <= 2
 -2 <= w_3 <= 2
 -9 <= x_4 <= 9
 -9 <= y_4 <= 9
 -9 <= z_4 <= 9
 -2 <= u_4 <= 2
 -2 <= v_4 <= 2
 -2 <= w_4 <= 2
 -9 <= x_5 <= 9
 -9 <= y_5 <= 9
 -9 <= z_5 <= 9
 -2 <= u_5 <= 2
 -2 <= v_5 <= 2
 -2 <= w_5 <= 2
 -9 <= x_6 <= 9
 -9 <= y_6 <= 9
 -9 <= z_6 <= 9
 -2 <= u_6 <= 2
 -2 <= v_6 <= 2
 -2 <= w_6 <= 2
 -9 <= x_7 <= 9
 -9 <= y_7 <= 9
 -9 <= z_7 <= 9
 -2 <= u_7 <= 2
 -2 <= v_7 <= 2
 -2 <= w_7 <= 2
 -9 <= x_8 <= 9
 -9 <= y_8 <= 9
 -9 <= z_8 <= 9
 -2 <= u_8 <= 2
 -2 <= v_8 <= 2
 -2 <= w_8 <= 2
 -9 <= x_9 <= 9
 -9 <= y_9 <= 9
 -9 <= z_9 <= 9
 -2 <= u_9 <= 2
 -2 <= v_9 <= 2
 -2 <= w_9 <= 2
 -9 <= x_10 <= 9
 -9 <= y_10 <= 9
 -9 <= z_10 <= 9
 -2 <= u_10 <= 2
 -2 <= v_10 <= 2
 -2 <= w_10 <= 2
 z_&&_2dx357e49ca96a6d288_0 <= 1
 rho_&&_2dx357e49ca96a6d288_0 free
 z_G_2bx3126109403624376_0 <= 1
 rho_G_2bx3126109403624376_0 free
 z_&&_2dx77c13656f83eed1e_8 <= 1
 rho_&&_2dx77c13656f83eed1e_8 free
 rho_predicate_2dx4c7fa34b9cfd78d2_8 free
 rho_predicate_2bx556f07e65bd9f395_8 free
 z_&&_2dx77c13656f83eed1e_9 <= 1
 rho_&&_2dx77c13656f83eed1e_9 free
 rho_predicate_2dx4c7fa34b9cfd78d2_9 free
 rho_predicate_2bx556f07e65bd9f395_9 free
 z_&&_2dx77c13656f83eed1e_10 <= 1
 rho_&&_2dx77c13656f83eed1e_10 free
 rho_predicate_2dx4c7fa34b9cfd78d2_10 free
 rho_predicate_2bx556f07e65bd9f395_10 free
 z_G_2bx2dc176d942bfc648_0 <= 1
 rho_G_2bx2dc176d942bfc648_0 free
 z_&&_2dx64e60b01d1682750_8 <= 1
 rho_&&_2dx64e60b01d1682750_8 free
 rho_predicate_2bx5b8af825940a107a_8 free
 rho_predicate_2bx32f72cccd281a177_8 free
 z_&&_2dx64e60b01d1682750_9 <= 1
 rho_&&_2dx64e60b01d1682750_9 free
 rho_predicate_2bx5b8af825940a107a_9 free
 rho_predicate_2bx32f72cccd281a177_9 free
 z_&&_2dx64e60b01d1682750_10 <= 1
 rho_&&_2dx64e60b01d1682750_10 free
 rho_predicate_2bx5b8af825940a107a_10 free
 rho_predicate_2bx32f72cccd281a177_10 free
 z_G_2dx60319af456428e09_0 <= 1
 rho_G_2dx60319af456428e09_0 free
 z_&&_2bx4d9a906c9b43dcf4_0 <= 1
 rho_&&_2bx4d9a906c9b43dcf4_0 free
 rho_predicate_2bx5b8af825940a107a_0 free
 rho_predicate_2bx556f07e65bd9f395_0 free
 z_&&_2bx4d9a906c9b43dcf4_1 <= 1
 rho_&&_2bx4d9a906c9b43dcf4_1 free
 rho_predicate_2bx5b8af825940a107a_1 free
 rho_predicate_2bx556f07e65bd9f395_1 free
Binaries
 z_predicate_2dx4c7fa34b9cfd78d2_8 z_predicate_2bx556f07e65bd9f395_8
 z_predicate_2dx4c7fa34b9cfd78d2_9 z_predicate_2bx556f07e65bd9f395_9
 z_predicate_2dx4c7fa34b9cfd78d2_10 z_predicate_2bx556f07e65bd9f395_10
 z_predicate_2bx5b8af825940a107a_8 z_predicate_2bx32f72cccd281a177_8
 z_predicate_2bx5b8af825940a107a_9 z_predicate_2bx32f72cccd281a177_9
 z_predicate_2bx5b8af825940a107a_10 z_predicate_2bx32f72cccd281a177_10
 z_predicate_2bx5b8af825940a107a_0 z_predicate_2bx556f07e65bd9f395_0
 z_predicate_2bx5b8af825940a107a_1 z_predicate_2bx556f07e65bd9f395_1
End
