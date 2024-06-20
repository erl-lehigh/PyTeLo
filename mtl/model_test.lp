\ Model MTL formula: ((G[0.0, 2.0] y) && (G[0.0, 2.0] z))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize multi-objectives
  OBJ0: Priority=2 Weight=1 AbsTol=1e-06 RelTol=0
   - &&_2dx62c33bb76fd51fe0_0_zi
  OBJ1: Priority=1 Weight=1 AbsTol=1e-06 RelTol=0
   - G_2bx4cfcee3dc1ae1626_0_zi - G_2bx4cfcee3dc1dbdcef_0_zi
  OBJ2: Priority=0 Weight=1 AbsTol=1e-06 RelTol=0
   - predicate_2bx39b28d5f8_0_zi - predicate_2bx39b28d5f8_1_zi
   - predicate_2bx39b28d5f8_2_zi - predicate_2bx3a2c9f77b_0_zi
   - predicate_2bx3a2c9f77b_1_zi - predicate_2bx3a2c9f77b_2_zi
Subject To
 R0: - &&_2dx62c33bb76fd51fe0_0 + &&_2dx62c33bb76fd51fe0_0_zi <= 0
 R1: - G_2bx4cfcee3dc1ae1626_0 + G_2bx4cfcee3dc1ae1626_0_zi <= 0
 R2: &&_2dx62c33bb76fd51fe0_0_zi + G_2bx4cfcee3dc1ae1626_0_zi <= 1
 R3: - predicate_2bx39b28d5f8_0 + predicate_2bx39b28d5f8_0_zi <= 0
 R4: &&_2dx62c33bb76fd51fe0_0_zi + predicate_2bx39b28d5f8_0_zi <= 1
 R5: G_2bx4cfcee3dc1ae1626_0_zi + predicate_2bx39b28d5f8_0_zi <= 1
 R6: - predicate_2bx39b28d5f8_1 + predicate_2bx39b28d5f8_1_zi <= 0
 R7: &&_2dx62c33bb76fd51fe0_0_zi + predicate_2bx39b28d5f8_1_zi <= 1
 R8: G_2bx4cfcee3dc1ae1626_0_zi + predicate_2bx39b28d5f8_1_zi <= 1
 R9: - predicate_2bx39b28d5f8_2 + predicate_2bx39b28d5f8_2_zi <= 0
 R10: &&_2dx62c33bb76fd51fe0_0_zi + predicate_2bx39b28d5f8_2_zi <= 1
 R11: G_2bx4cfcee3dc1ae1626_0_zi + predicate_2bx39b28d5f8_2_zi <= 1
 R12: G_2bx4cfcee3dc1ae1626_0 - 0.3333333333333333 predicate_2bx39b28d5f8_0
   - 0.3333333333333333 predicate_2bx39b28d5f8_1
   - 0.3333333333333333 predicate_2bx39b28d5f8_2 = 0
 R13: - G_2bx4cfcee3dc1dbdcef_0 + G_2bx4cfcee3dc1dbdcef_0_zi <= 0
 R14: &&_2dx62c33bb76fd51fe0_0_zi + G_2bx4cfcee3dc1dbdcef_0_zi <= 1
 R15: - predicate_2bx3a2c9f77b_0 + predicate_2bx3a2c9f77b_0_zi <= 0
 R16: &&_2dx62c33bb76fd51fe0_0_zi + predicate_2bx3a2c9f77b_0_zi <= 1
 R17: G_2bx4cfcee3dc1dbdcef_0_zi + predicate_2bx3a2c9f77b_0_zi <= 1
 R18: - predicate_2bx3a2c9f77b_1 + predicate_2bx3a2c9f77b_1_zi <= 0
 R19: &&_2dx62c33bb76fd51fe0_0_zi + predicate_2bx3a2c9f77b_1_zi <= 1
 R20: G_2bx4cfcee3dc1dbdcef_0_zi + predicate_2bx3a2c9f77b_1_zi <= 1
 R21: - predicate_2bx3a2c9f77b_2 + predicate_2bx3a2c9f77b_2_zi <= 0
 R22: &&_2dx62c33bb76fd51fe0_0_zi + predicate_2bx3a2c9f77b_2_zi <= 1
 R23: G_2bx4cfcee3dc1dbdcef_0_zi + predicate_2bx3a2c9f77b_2_zi <= 1
 R24: G_2bx4cfcee3dc1dbdcef_0 - 0.3333333333333333 predicate_2bx3a2c9f77b_0
   - 0.3333333333333333 predicate_2bx3a2c9f77b_1
   - 0.3333333333333333 predicate_2bx3a2c9f77b_2 = 0
 R25: &&_2dx62c33bb76fd51fe0_0 - 0.5 G_2bx4cfcee3dc1ae1626_0
   - 0.5 G_2bx4cfcee3dc1dbdcef_0 = 0
 R26: predicate_2bx39b28d5f8_1 = 0
Bounds
 &&_2dx62c33bb76fd51fe0_0 <= 1
 G_2bx4cfcee3dc1ae1626_0 <= 1
 G_2bx4cfcee3dc1dbdcef_0 <= 1
Binaries
 &&_2dx62c33bb76fd51fe0_0_zi G_2bx4cfcee3dc1ae1626_0_zi
 predicate_2bx39b28d5f8_0 predicate_2bx39b28d5f8_0_zi
 predicate_2bx39b28d5f8_1 predicate_2bx39b28d5f8_1_zi
 predicate_2bx39b28d5f8_2 predicate_2bx39b28d5f8_2_zi
 G_2bx4cfcee3dc1dbdcef_0_zi predicate_2bx3a2c9f77b_0
 predicate_2bx3a2c9f77b_0_zi predicate_2bx3a2c9f77b_1
 predicate_2bx3a2c9f77b_1_zi predicate_2bx3a2c9f77b_2
 predicate_2bx3a2c9f77b_2_zi
End
