\ Model S-WSTL formula: ((x >= 6.0) ||^<lambda> (x <= 6.0) ||^<lambda> (x <= 0.0))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  rho_||_2bx4a7ff530f20ef2bf_0
Subject To
 R0: - 1000 z_predicate_2dx4c7fa34b9cfd78d2_0
   - rho_predicate_2dx4c7fa34b9cfd78d2_0 + x_0 >= -994
 R1: - 1000 z_predicate_2dx4c7fa34b9cfd78d2_0
   - rho_predicate_2dx4c7fa34b9cfd78d2_0 + x_0 <= 6
 R2: x_0 + 1000 z_predicate_2dx18566057797ead00_0
   + rho_predicate_2dx18566057797ead00_0 <= 1006
 R3: x_0 + 1000 z_predicate_2dx18566057797ead00_0
   + rho_predicate_2dx18566057797ead00_0 >= 6
 R4: x_0 + 1000 z_predicate_2dx6b9ad606f835cc1a_0
   + rho_predicate_2dx6b9ad606f835cc1a_0 <= 1000
 R5: x_0 + 1000 z_predicate_2dx6b9ad606f835cc1a_0
   + rho_predicate_2dx6b9ad606f835cc1a_0 >= 0
 R6: rho_||_2bx4a7ff530f20ef2bf_0 + 1000 z_predicate_2dx4c7fa34b9cfd78d2_0
   - 6 rho_predicate_2dx4c7fa34b9cfd78d2_0 <= 1000
 R7: z_||_2bx4a7ff530f20ef2bf_0 - z_predicate_2dx4c7fa34b9cfd78d2_0 >= 0
 R8: rho_||_2bx4a7ff530f20ef2bf_0 + 1000 z_predicate_2dx18566057797ead00_0
   - rho_predicate_2dx18566057797ead00_0 <= 1000
 R9: z_||_2bx4a7ff530f20ef2bf_0 - z_predicate_2dx18566057797ead00_0 >= 0
 R10: rho_||_2bx4a7ff530f20ef2bf_0 + 1000 z_predicate_2dx6b9ad606f835cc1a_0
   - 10 rho_predicate_2dx6b9ad606f835cc1a_0 <= 1000
 R11: z_||_2bx4a7ff530f20ef2bf_0 - z_predicate_2dx6b9ad606f835cc1a_0 >= 0
 R12: z_||_2bx4a7ff530f20ef2bf_0 - z_predicate_2dx4c7fa34b9cfd78d2_0
   - z_predicate_2dx18566057797ead00_0 - z_predicate_2dx6b9ad606f835cc1a_0
   <= 0
 formula_satisfaction: z_||_2bx4a7ff530f20ef2bf_0 = 1
Bounds
 z_||_2bx4a7ff530f20ef2bf_0 <= 1
 rho_||_2bx4a7ff530f20ef2bf_0 free
 rho_predicate_2dx4c7fa34b9cfd78d2_0 free
 -9 <= x_0 <= 9
 rho_predicate_2dx18566057797ead00_0 free
 rho_predicate_2dx6b9ad606f835cc1a_0 free
Binaries
 z_predicate_2dx4c7fa34b9cfd78d2_0 z_predicate_2dx18566057797ead00_0
 z_predicate_2dx6b9ad606f835cc1a_0
End
