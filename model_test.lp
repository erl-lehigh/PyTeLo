\ Model STL formula: ((x >= 6.0) && (F[0.0, 2.0] (y > 3.0)) && (G[1.0, 6.0] (z < 8.0)) && (G[1.0, 6.0] (z > 3.0)))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.2 rho0 + 0.8 rho1
Subject To
 R0: - rho0 - 1000 predicate_2dx4c7fa34b9cfd78d2_0 + x_0 <= 6
 R1: - rho0 - 1000 predicate_2dx4c7fa34b9cfd78d2_0 + x_0 >= -994
 R2: - rho0 - 1000 predicate_2dx312c4f7f0b611806_0 + y_0 <= 3
 R3: - rho0 - 1000 predicate_2dx312c4f7f0b611806_0 + y_0 >= -997
 R4: - rho0 - 1000 predicate_2dx312c4f7f0b611806_1 + y_1 <= 3
 R5: - rho0 - 1000 predicate_2dx312c4f7f0b611806_1 + y_1 >= -997
 R6: - rho0 - 1000 predicate_2dx312c4f7f0b611806_2 + y_2 <= 3
 R7: - rho0 - 1000 predicate_2dx312c4f7f0b611806_2 + y_2 >= -997
 R8: event_2dx79499ea35423ce39_0 - predicate_2dx312c4f7f0b611806_0 >= 0
 R9: event_2dx79499ea35423ce39_0 - predicate_2dx312c4f7f0b611806_1 >= 0
 R10: event_2dx79499ea35423ce39_0 - predicate_2dx312c4f7f0b611806_2 >= 0
 R11: event_2dx79499ea35423ce39_0 - predicate_2dx312c4f7f0b611806_0
   - predicate_2dx312c4f7f0b611806_1 - predicate_2dx312c4f7f0b611806_2
   <= 0
 R12: rho1 + 1000 predicate_2bx48972c4e06aa798c_1 + z_1 >= 8
 R13: rho1 + 1000 predicate_2bx48972c4e06aa798c_1 + z_1 <= 1008
 R14: rho1 + 1000 predicate_2bx48972c4e06aa798c_2 + z_2 >= 8
 R15: rho1 + 1000 predicate_2bx48972c4e06aa798c_2 + z_2 <= 1008
 R16: rho1 + 1000 predicate_2bx48972c4e06aa798c_3 + z_3 >= 8
 R17: rho1 + 1000 predicate_2bx48972c4e06aa798c_3 + z_3 <= 1008
 R18: rho1 + 1000 predicate_2bx48972c4e06aa798c_4 + z_4 >= 8
 R19: rho1 + 1000 predicate_2bx48972c4e06aa798c_4 + z_4 <= 1008
 R20: rho1 + 1000 predicate_2bx48972c4e06aa798c_5 + z_5 >= 8
 R21: rho1 + 1000 predicate_2bx48972c4e06aa798c_5 + z_5 <= 1008
 R22: rho1 + 1000 predicate_2bx48972c4e06aa798c_6 + z_6 >= 8
 R23: rho1 + 1000 predicate_2bx48972c4e06aa798c_6 + z_6 <= 1008
 R24: always_2bx456eb694edc28b4d_0 - predicate_2bx48972c4e06aa798c_1 <= 0
 R25: always_2bx456eb694edc28b4d_0 - predicate_2bx48972c4e06aa798c_2 <= 0
 R26: always_2bx456eb694edc28b4d_0 - predicate_2bx48972c4e06aa798c_3 <= 0
 R27: always_2bx456eb694edc28b4d_0 - predicate_2bx48972c4e06aa798c_4 <= 0
 R28: always_2bx456eb694edc28b4d_0 - predicate_2bx48972c4e06aa798c_5 <= 0
 R29: always_2bx456eb694edc28b4d_0 - predicate_2bx48972c4e06aa798c_6 <= 0
 R30: always_2bx456eb694edc28b4d_0 - predicate_2bx48972c4e06aa798c_1
   - predicate_2bx48972c4e06aa798c_2 - predicate_2bx48972c4e06aa798c_3
   - predicate_2bx48972c4e06aa798c_4 - predicate_2bx48972c4e06aa798c_5
   - predicate_2bx48972c4e06aa798c_6 >= -5
 R31: - rho1 + z_1 - 1000 predicate_2bxc2ee9246a8ee2bb_1 <= 3
 R32: - rho1 + z_1 - 1000 predicate_2bxc2ee9246a8ee2bb_1 >= -997
 R33: - rho1 + z_2 - 1000 predicate_2bxc2ee9246a8ee2bb_2 <= 3
 R34: - rho1 + z_2 - 1000 predicate_2bxc2ee9246a8ee2bb_2 >= -997
 R35: - rho1 + z_3 - 1000 predicate_2bxc2ee9246a8ee2bb_3 <= 3
 R36: - rho1 + z_3 - 1000 predicate_2bxc2ee9246a8ee2bb_3 >= -997
 R37: - rho1 + z_4 - 1000 predicate_2bxc2ee9246a8ee2bb_4 <= 3
 R38: - rho1 + z_4 - 1000 predicate_2bxc2ee9246a8ee2bb_4 >= -997
 R39: - rho1 + z_5 - 1000 predicate_2bxc2ee9246a8ee2bb_5 <= 3
 R40: - rho1 + z_5 - 1000 predicate_2bxc2ee9246a8ee2bb_5 >= -997
 R41: - rho1 + z_6 - 1000 predicate_2bxc2ee9246a8ee2bb_6 <= 3
 R42: - rho1 + z_6 - 1000 predicate_2bxc2ee9246a8ee2bb_6 >= -997
 R43: always_2bx617c596dba17ce34_0 - predicate_2bxc2ee9246a8ee2bb_1 <= 0
 R44: always_2bx617c596dba17ce34_0 - predicate_2bxc2ee9246a8ee2bb_2 <= 0
 R45: always_2bx617c596dba17ce34_0 - predicate_2bxc2ee9246a8ee2bb_3 <= 0
 R46: always_2bx617c596dba17ce34_0 - predicate_2bxc2ee9246a8ee2bb_4 <= 0
 R47: always_2bx617c596dba17ce34_0 - predicate_2bxc2ee9246a8ee2bb_5 <= 0
 R48: always_2bx617c596dba17ce34_0 - predicate_2bxc2ee9246a8ee2bb_6 <= 0
 R49: always_2bx617c596dba17ce34_0 - predicate_2bxc2ee9246a8ee2bb_1
   - predicate_2bxc2ee9246a8ee2bb_2 - predicate_2bxc2ee9246a8ee2bb_3
   - predicate_2bxc2ee9246a8ee2bb_4 - predicate_2bxc2ee9246a8ee2bb_5
   - predicate_2bxc2ee9246a8ee2bb_6 >= -5
 R50: and_2bx60b4b0235b99e3c3_0 - predicate_2dx4c7fa34b9cfd78d2_0 <= 0
 R51: and_2bx60b4b0235b99e3c3_0 - event_2dx79499ea35423ce39_0 <= 0
 R52: and_2bx60b4b0235b99e3c3_0 - always_2bx456eb694edc28b4d_0 <= 0
 R53: and_2bx60b4b0235b99e3c3_0 - always_2bx617c596dba17ce34_0 <= 0
 R54: and_2bx60b4b0235b99e3c3_0 - predicate_2dx4c7fa34b9cfd78d2_0
   - event_2dx79499ea35423ce39_0 - always_2bx456eb694edc28b4d_0
   - always_2bx617c596dba17ce34_0 >= -3
 formula_satisfaction: and_2bx60b4b0235b99e3c3_0 = 1
Bounds
 -infinity <= rho0 <= 999
 -infinity <= rho1 <= 999
 -4 <= x_0 <= 5
 -4 <= y_0 <= 1
 -4 <= y_1 <= 1
 -4 <= y_2 <= 1
 -10 <= z_1 <= 10
 -10 <= z_2 <= 10
 -10 <= z_3 <= 10
 -10 <= z_4 <= 10
 -10 <= z_5 <= 10
 -10 <= z_6 <= 10
Binaries
 and_2bx60b4b0235b99e3c3_0 predicate_2dx4c7fa34b9cfd78d2_0
 event_2dx79499ea35423ce39_0 predicate_2dx312c4f7f0b611806_0
 predicate_2dx312c4f7f0b611806_1 predicate_2dx312c4f7f0b611806_2
 always_2bx456eb694edc28b4d_0 predicate_2bx48972c4e06aa798c_1
 predicate_2bx48972c4e06aa798c_2 predicate_2bx48972c4e06aa798c_3
 predicate_2bx48972c4e06aa798c_4 predicate_2bx48972c4e06aa798c_5
 predicate_2bx48972c4e06aa798c_6 always_2bx617c596dba17ce34_0
 predicate_2bxc2ee9246a8ee2bb_1 predicate_2bxc2ee9246a8ee2bb_2
 predicate_2bxc2ee9246a8ee2bb_3 predicate_2bxc2ee9246a8ee2bb_4
 predicate_2bxc2ee9246a8ee2bb_5 predicate_2bxc2ee9246a8ee2bb_6
End
