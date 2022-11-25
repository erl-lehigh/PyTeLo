\ Model pswSTL formula: ((F[3.0, 6.0]^<lambda> ((x >= -9.0) &&^<lambda> (y >= 4.0))) &^<lambda> (F[3.0, 6.0]^<lambda> ((x >= 4.0) &&^<lambda> (y >= -9.0))))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0 u_6 + 0 v_6 + 0 w_6 + z_&_2bxbb488d6087ec2fa_0
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
 R18: x_0 = 0
 R19: y_0 = 0
 R20: z_0 = 0
 R21: u_0 = 0
 R22: v_0 = 0
 R23: w_0 = 0
 R24: x_3 - 1000 z_predicate_2dx2fec186068be67f7_3 <= -9
 R25: x_3 - 1000 z_predicate_2dx2fec186068be67f7_3 >= -1009
 R26: y_3 - 1000 z_predicate_2bx1735b9f08705a189_3 <= 4
 R27: y_3 - 1000 z_predicate_2bx1735b9f08705a189_3 >= -996
 R28: z_&&_2bx3af5ec8d6ce1b795_3 - 0.5 z_predicate_2dx2fec186068be67f7_3
   - 0.5 z_predicate_2bx1735b9f08705a189_3 = 0
 R29: x_4 - 1000 z_predicate_2dx2fec186068be67f7_4 <= -9
 R30: x_4 - 1000 z_predicate_2dx2fec186068be67f7_4 >= -1009
 R31: y_4 - 1000 z_predicate_2bx1735b9f08705a189_4 <= 4
 R32: y_4 - 1000 z_predicate_2bx1735b9f08705a189_4 >= -996
 R33: z_&&_2bx3af5ec8d6ce1b795_4 - 0.5 z_predicate_2dx2fec186068be67f7_4
   - 0.5 z_predicate_2bx1735b9f08705a189_4 = 0
 R34: x_5 - 1000 z_predicate_2dx2fec186068be67f7_5 <= -9
 R35: x_5 - 1000 z_predicate_2dx2fec186068be67f7_5 >= -1009
 R36: y_5 - 1000 z_predicate_2bx1735b9f08705a189_5 <= 4
 R37: y_5 - 1000 z_predicate_2bx1735b9f08705a189_5 >= -996
 R38: z_&&_2bx3af5ec8d6ce1b795_5 - 0.5 z_predicate_2dx2fec186068be67f7_5
   - 0.5 z_predicate_2bx1735b9f08705a189_5 = 0
 R39: x_6 - 1000 z_predicate_2dx2fec186068be67f7_6 <= -9
 R40: x_6 - 1000 z_predicate_2dx2fec186068be67f7_6 >= -1009
 R41: y_6 - 1000 z_predicate_2bx1735b9f08705a189_6 <= 4
 R42: y_6 - 1000 z_predicate_2bx1735b9f08705a189_6 >= -996
 R43: z_&&_2bx3af5ec8d6ce1b795_6 - 0.5 z_predicate_2dx2fec186068be67f7_6
   - 0.5 z_predicate_2bx1735b9f08705a189_6 = 0
 R44: - z_&&_2bx3af5ec8d6ce1b795_3 + y_event_3 = 0
 R45: - z_&&_2bx3af5ec8d6ce1b795_4 + y_event_4 = 0
 R46: - z_&&_2bx3af5ec8d6ce1b795_5 + y_event_5 = 0
 R47: - z_&&_2bx3af5ec8d6ce1b795_6 + y_event_6 = 0
 R48: x_3 - 1000 z_predicate_2dx30be4d89f565bb0c_3 <= 4
 R49: x_3 - 1000 z_predicate_2dx30be4d89f565bb0c_3 >= -996
 R50: y_3 - 1000 z_predicate_2dx70b6d9b1e46d932_3 <= -9
 R51: y_3 - 1000 z_predicate_2dx70b6d9b1e46d932_3 >= -1009
 R52: z_&&_2dx19b616a5a0da4d87_3 - 0.5 z_predicate_2dx30be4d89f565bb0c_3
   - 0.5 z_predicate_2dx70b6d9b1e46d932_3 = 0
 R53: x_4 - 1000 z_predicate_2dx30be4d89f565bb0c_4 <= 4
 R54: x_4 - 1000 z_predicate_2dx30be4d89f565bb0c_4 >= -996
 R55: y_4 - 1000 z_predicate_2dx70b6d9b1e46d932_4 <= -9
 R56: y_4 - 1000 z_predicate_2dx70b6d9b1e46d932_4 >= -1009
 R57: z_&&_2dx19b616a5a0da4d87_4 - 0.5 z_predicate_2dx30be4d89f565bb0c_4
   - 0.5 z_predicate_2dx70b6d9b1e46d932_4 = 0
 R58: x_5 - 1000 z_predicate_2dx30be4d89f565bb0c_5 <= 4
 R59: x_5 - 1000 z_predicate_2dx30be4d89f565bb0c_5 >= -996
 R60: y_5 - 1000 z_predicate_2dx70b6d9b1e46d932_5 <= -9
 R61: y_5 - 1000 z_predicate_2dx70b6d9b1e46d932_5 >= -1009
 R62: z_&&_2dx19b616a5a0da4d87_5 - 0.5 z_predicate_2dx30be4d89f565bb0c_5
   - 0.5 z_predicate_2dx70b6d9b1e46d932_5 = 0
 R63: x_6 - 1000 z_predicate_2dx30be4d89f565bb0c_6 <= 4
 R64: x_6 - 1000 z_predicate_2dx30be4d89f565bb0c_6 >= -996
 R65: y_6 - 1000 z_predicate_2dx70b6d9b1e46d932_6 <= -9
 R66: y_6 - 1000 z_predicate_2dx70b6d9b1e46d932_6 >= -1009
 R67: z_&&_2dx19b616a5a0da4d87_6 - 0.5 z_predicate_2dx30be4d89f565bb0c_6
   - 0.5 z_predicate_2dx70b6d9b1e46d932_6 = 0
 R68: - z_&&_2dx19b616a5a0da4d87_3 + y_event_3 = 0
 R69: - z_&&_2dx19b616a5a0da4d87_4 + y_event_4 = 0
 R70: - z_&&_2dx19b616a5a0da4d87_5 + y_event_5 = 0
 R71: - z_&&_2dx19b616a5a0da4d87_6 + y_event_6 = 0
 R72: z_&_2bxbb488d6087ec2fa_0 - 0.5 z_F_2dx2a7c43dd7bfa01_0
   - 0.5 z_F_2dx190d055ee88ccfb5_0 = 0
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
 z_F_2dx2a7c43dd7bfa01_0 <= 1
 z_&&_2bx3af5ec8d6ce1b795_3 <= 1
 z_&&_2bx3af5ec8d6ce1b795_4 <= 1
 z_&&_2bx3af5ec8d6ce1b795_5 <= 1
 z_&&_2bx3af5ec8d6ce1b795_6 <= 1
 y_event_3 <= 1
 y_event_4 <= 1
 y_event_5 <= 1
 y_event_6 <= 1
 z_F_2dx190d055ee88ccfb5_0 <= 1
 z_&&_2dx19b616a5a0da4d87_3 <= 1
 z_&&_2dx19b616a5a0da4d87_4 <= 1
 z_&&_2dx19b616a5a0da4d87_5 <= 1
 z_&&_2dx19b616a5a0da4d87_6 <= 1
 y_event_3 <= 1
 y_event_4 <= 1
 y_event_5 <= 1
 y_event_6 <= 1
Binaries
 z_&_2bxbb488d6087ec2fa_0 z_predicate_2dx2fec186068be67f7_3
 z_predicate_2bx1735b9f08705a189_3 z_predicate_2dx2fec186068be67f7_4
 z_predicate_2bx1735b9f08705a189_4 z_predicate_2dx2fec186068be67f7_5
 z_predicate_2bx1735b9f08705a189_5 z_predicate_2dx2fec186068be67f7_6
 z_predicate_2bx1735b9f08705a189_6 z_predicate_2dx30be4d89f565bb0c_3
 z_predicate_2dx70b6d9b1e46d932_3 z_predicate_2dx30be4d89f565bb0c_4
 z_predicate_2dx70b6d9b1e46d932_4 z_predicate_2dx30be4d89f565bb0c_5
 z_predicate_2dx70b6d9b1e46d932_5 z_predicate_2dx30be4d89f565bb0c_6
 z_predicate_2dx70b6d9b1e46d932_6
General Constraints
 GC0: z_F_2dx2a7c43dd7bfa01_0 = MAX ( y_event_3 , y_event_4 , y_event_5 ,
   y_event_6 )
 GC1: z_F_2dx190d055ee88ccfb5_0 = MAX ( y_event_3 , y_event_4 , y_event_5 ,
   y_event_6 )
End
