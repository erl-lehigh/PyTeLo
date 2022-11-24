\ Model pswSTL formula: ((G[4.0, 10.0]^<lambda> ((x <= -6.0) &&^<lambda> (y >= 6.0))) &&^<lambda> (G[4.0, 10.0]^<lambda> ((x >= 6.0) &&^<lambda> (y <= -6.0))))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0 u_10 + 0 v_10 + 0 w_10 + z_&&_2bx4313867a8ed6933_0
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
 R36: x_4 + 1000 z_predicate_2bx5b8af825940a107a_4 >= -6
 R37: x_4 + 1000 z_predicate_2bx5b8af825940a107a_4 <= 994
 R38: y_4 - 1000 z_predicate_2bx32f72cccd281a177_4 <= 6
 R39: y_4 - 1000 z_predicate_2bx32f72cccd281a177_4 >= -994
 R40: z_&&_2dx64e60b01d1682750_4 - 0.5 z_predicate_2bx5b8af825940a107a_4
   - 0.5 z_predicate_2bx32f72cccd281a177_4 = 0
 R41: x_5 + 1000 z_predicate_2bx5b8af825940a107a_5 >= -6
 R42: x_5 + 1000 z_predicate_2bx5b8af825940a107a_5 <= 994
 R43: y_5 - 1000 z_predicate_2bx32f72cccd281a177_5 <= 6
 R44: y_5 - 1000 z_predicate_2bx32f72cccd281a177_5 >= -994
 R45: z_&&_2dx64e60b01d1682750_5 - 0.5 z_predicate_2bx5b8af825940a107a_5
   - 0.5 z_predicate_2bx32f72cccd281a177_5 = 0
 R46: x_6 + 1000 z_predicate_2bx5b8af825940a107a_6 >= -6
 R47: x_6 + 1000 z_predicate_2bx5b8af825940a107a_6 <= 994
 R48: y_6 - 1000 z_predicate_2bx32f72cccd281a177_6 <= 6
 R49: y_6 - 1000 z_predicate_2bx32f72cccd281a177_6 >= -994
 R50: z_&&_2dx64e60b01d1682750_6 - 0.5 z_predicate_2bx5b8af825940a107a_6
   - 0.5 z_predicate_2bx32f72cccd281a177_6 = 0
 R51: x_7 + 1000 z_predicate_2bx5b8af825940a107a_7 >= -6
 R52: x_7 + 1000 z_predicate_2bx5b8af825940a107a_7 <= 994
 R53: y_7 - 1000 z_predicate_2bx32f72cccd281a177_7 <= 6
 R54: y_7 - 1000 z_predicate_2bx32f72cccd281a177_7 >= -994
 R55: z_&&_2dx64e60b01d1682750_7 - 0.5 z_predicate_2bx5b8af825940a107a_7
   - 0.5 z_predicate_2bx32f72cccd281a177_7 = 0
 R56: x_8 + 1000 z_predicate_2bx5b8af825940a107a_8 >= -6
 R57: x_8 + 1000 z_predicate_2bx5b8af825940a107a_8 <= 994
 R58: y_8 - 1000 z_predicate_2bx32f72cccd281a177_8 <= 6
 R59: y_8 - 1000 z_predicate_2bx32f72cccd281a177_8 >= -994
 R60: z_&&_2dx64e60b01d1682750_8 - 0.5 z_predicate_2bx5b8af825940a107a_8
   - 0.5 z_predicate_2bx32f72cccd281a177_8 = 0
 R61: x_9 + 1000 z_predicate_2bx5b8af825940a107a_9 >= -6
 R62: x_9 + 1000 z_predicate_2bx5b8af825940a107a_9 <= 994
 R63: y_9 - 1000 z_predicate_2bx32f72cccd281a177_9 <= 6
 R64: y_9 - 1000 z_predicate_2bx32f72cccd281a177_9 >= -994
 R65: z_&&_2dx64e60b01d1682750_9 - 0.5 z_predicate_2bx5b8af825940a107a_9
   - 0.5 z_predicate_2bx32f72cccd281a177_9 = 0
 R66: x_10 + 1000 z_predicate_2bx5b8af825940a107a_10 >= -6
 R67: x_10 + 1000 z_predicate_2bx5b8af825940a107a_10 <= 994
 R68: y_10 - 1000 z_predicate_2bx32f72cccd281a177_10 <= 6
 R69: y_10 - 1000 z_predicate_2bx32f72cccd281a177_10 >= -994
 R70: z_&&_2dx64e60b01d1682750_10 - 0.5 z_predicate_2bx5b8af825940a107a_10
   - 0.5 z_predicate_2bx32f72cccd281a177_10 = 0
 R71: z_G_2bx89381c2e19f4234_0
   - 0.1428571428571428 z_&&_2dx64e60b01d1682750_4
   - 0.1428571428571428 z_&&_2dx64e60b01d1682750_5
   - 0.1428571428571428 z_&&_2dx64e60b01d1682750_6
   - 0.1428571428571428 z_&&_2dx64e60b01d1682750_7
   - 0.1428571428571428 z_&&_2dx64e60b01d1682750_8
   - 0.1428571428571428 z_&&_2dx64e60b01d1682750_9
   - 0.1428571428571428 z_&&_2dx64e60b01d1682750_10 = 0
 R72: x_4 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_4 <= 6
 R73: x_4 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_4 >= -994
 R74: y_4 + 1000 z_predicate_2bx556f07e65bd9f395_4 >= -6
 R75: y_4 + 1000 z_predicate_2bx556f07e65bd9f395_4 <= 994
 R76: z_&&_2dx77c13656f83eed1e_4 - 0.5 z_predicate_2dx4c7fa34b9cfd78d2_4
   - 0.5 z_predicate_2bx556f07e65bd9f395_4 = 0
 R77: x_5 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_5 <= 6
 R78: x_5 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_5 >= -994
 R79: y_5 + 1000 z_predicate_2bx556f07e65bd9f395_5 >= -6
 R80: y_5 + 1000 z_predicate_2bx556f07e65bd9f395_5 <= 994
 R81: z_&&_2dx77c13656f83eed1e_5 - 0.5 z_predicate_2dx4c7fa34b9cfd78d2_5
   - 0.5 z_predicate_2bx556f07e65bd9f395_5 = 0
 R82: x_6 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_6 <= 6
 R83: x_6 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_6 >= -994
 R84: y_6 + 1000 z_predicate_2bx556f07e65bd9f395_6 >= -6
 R85: y_6 + 1000 z_predicate_2bx556f07e65bd9f395_6 <= 994
 R86: z_&&_2dx77c13656f83eed1e_6 - 0.5 z_predicate_2dx4c7fa34b9cfd78d2_6
   - 0.5 z_predicate_2bx556f07e65bd9f395_6 = 0
 R87: x_7 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_7 <= 6
 R88: x_7 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_7 >= -994
 R89: y_7 + 1000 z_predicate_2bx556f07e65bd9f395_7 >= -6
 R90: y_7 + 1000 z_predicate_2bx556f07e65bd9f395_7 <= 994
 R91: z_&&_2dx77c13656f83eed1e_7 - 0.5 z_predicate_2dx4c7fa34b9cfd78d2_7
   - 0.5 z_predicate_2bx556f07e65bd9f395_7 = 0
 R92: x_8 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_8 <= 6
 R93: x_8 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_8 >= -994
 R94: y_8 + 1000 z_predicate_2bx556f07e65bd9f395_8 >= -6
 R95: y_8 + 1000 z_predicate_2bx556f07e65bd9f395_8 <= 994
 R96: z_&&_2dx77c13656f83eed1e_8 - 0.5 z_predicate_2dx4c7fa34b9cfd78d2_8
   - 0.5 z_predicate_2bx556f07e65bd9f395_8 = 0
 R97: x_9 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_9 <= 6
 R98: x_9 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_9 >= -994
 R99: y_9 + 1000 z_predicate_2bx556f07e65bd9f395_9 >= -6
 R100: y_9 + 1000 z_predicate_2bx556f07e65bd9f395_9 <= 994
 R101: z_&&_2dx77c13656f83eed1e_9 - 0.5 z_predicate_2dx4c7fa34b9cfd78d2_9
   - 0.5 z_predicate_2bx556f07e65bd9f395_9 = 0
 R102: x_10 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_10 <= 6
 R103: x_10 - 1000 z_predicate_2dx4c7fa34b9cfd78d2_10 >= -994
 R104: y_10 + 1000 z_predicate_2bx556f07e65bd9f395_10 >= -6
 R105: y_10 + 1000 z_predicate_2bx556f07e65bd9f395_10 <= 994
 R106: z_&&_2dx77c13656f83eed1e_10 - 0.5 z_predicate_2dx4c7fa34b9cfd78d2_10
   - 0.5 z_predicate_2bx556f07e65bd9f395_10 = 0
 R107: z_G_2dx475cc33368ef13e_0
   - 0.1428571428571428 z_&&_2dx77c13656f83eed1e_4
   - 0.1428571428571428 z_&&_2dx77c13656f83eed1e_5
   - 0.1428571428571428 z_&&_2dx77c13656f83eed1e_6
   - 0.1428571428571428 z_&&_2dx77c13656f83eed1e_7
   - 0.1428571428571428 z_&&_2dx77c13656f83eed1e_8
   - 0.1428571428571428 z_&&_2dx77c13656f83eed1e_9
   - 0.1428571428571428 z_&&_2dx77c13656f83eed1e_10 = 0
 R108: z_&&_2bx4313867a8ed6933_0 - 0.4 z_G_2bx89381c2e19f4234_0
   - 0.6 z_G_2dx475cc33368ef13e_0 = 0
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
 z_&&_2bx4313867a8ed6933_0 <= 1
 z_G_2bx89381c2e19f4234_0 <= 1
 z_&&_2dx64e60b01d1682750_4 <= 1
 z_&&_2dx64e60b01d1682750_5 <= 1
 z_&&_2dx64e60b01d1682750_6 <= 1
 z_&&_2dx64e60b01d1682750_7 <= 1
 z_&&_2dx64e60b01d1682750_8 <= 1
 z_&&_2dx64e60b01d1682750_9 <= 1
 z_&&_2dx64e60b01d1682750_10 <= 1
 z_G_2dx475cc33368ef13e_0 <= 1
 z_&&_2dx77c13656f83eed1e_4 <= 1
 z_&&_2dx77c13656f83eed1e_5 <= 1
 z_&&_2dx77c13656f83eed1e_6 <= 1
 z_&&_2dx77c13656f83eed1e_7 <= 1
 z_&&_2dx77c13656f83eed1e_8 <= 1
 z_&&_2dx77c13656f83eed1e_9 <= 1
 z_&&_2dx77c13656f83eed1e_10 <= 1
Binaries
 z_predicate_2bx5b8af825940a107a_4 z_predicate_2bx32f72cccd281a177_4
 z_predicate_2bx5b8af825940a107a_5 z_predicate_2bx32f72cccd281a177_5
 z_predicate_2bx5b8af825940a107a_6 z_predicate_2bx32f72cccd281a177_6
 z_predicate_2bx5b8af825940a107a_7 z_predicate_2bx32f72cccd281a177_7
 z_predicate_2bx5b8af825940a107a_8 z_predicate_2bx32f72cccd281a177_8
 z_predicate_2bx5b8af825940a107a_9 z_predicate_2bx32f72cccd281a177_9
 z_predicate_2bx5b8af825940a107a_10 z_predicate_2bx32f72cccd281a177_10
 z_predicate_2dx4c7fa34b9cfd78d2_4 z_predicate_2bx556f07e65bd9f395_4
 z_predicate_2dx4c7fa34b9cfd78d2_5 z_predicate_2bx556f07e65bd9f395_5
 z_predicate_2dx4c7fa34b9cfd78d2_6 z_predicate_2bx556f07e65bd9f395_6
 z_predicate_2dx4c7fa34b9cfd78d2_7 z_predicate_2bx556f07e65bd9f395_7
 z_predicate_2dx4c7fa34b9cfd78d2_8 z_predicate_2bx556f07e65bd9f395_8
 z_predicate_2dx4c7fa34b9cfd78d2_9 z_predicate_2bx556f07e65bd9f395_9
 z_predicate_2dx4c7fa34b9cfd78d2_10 z_predicate_2bx556f07e65bd9f395_10
End
