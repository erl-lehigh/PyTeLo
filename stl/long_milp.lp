\ Model L-WSTL formula: ((x >= 7.0) ||^<lambda> (x <= -7.0))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  rho_||_2bx6a7065f683bd1413_0
Subject To
 R0: - 1000 z_predicate_2dx5a605e8b6db0d82b_0
   - rho_predicate_2dx5a605e8b6db0d82b_0 + x_0 <= 7
 R1: - 1000 z_predicate_2dx5a605e8b6db0d82b_0
   - rho_predicate_2dx5a605e8b6db0d82b_0 + x_0 >= -993
 R2: x_0 + 1000 z_predicate_2bx696bb36562d5272d_0
   + rho_predicate_2bx696bb36562d5272d_0 >= -7
 R3: x_0 + 1000 z_predicate_2bx696bb36562d5272d_0
   + rho_predicate_2bx696bb36562d5272d_0 <= 993
 R4: 1000 z_||_2bx6a7065f683bd1413_0 + rho_||_2bx6a7065f683bd1413_0
   - rho_predicate_2dx5a605e8b6db0d82b_0
   + 1000 zhat_predicate_2dx5a605e8b6db0d82b_2bx6a7065f683bd1413_0 <= 2000
 R5: - 1000 z_||_2bx6a7065f683bd1413_0 + rho_||_2bx6a7065f683bd1413_0
   + 1000 zhat_predicate_2dx5a605e8b6db0d82b_2bx6a7065f683bd1413_0 <= 1000
 R6: 1000 z_||_2bx6a7065f683bd1413_0 + rho_||_2bx6a7065f683bd1413_0
   - rho_predicate_2bx696bb36562d5272d_0
   + 1000 zhat_predicate_2bx696bb36562d5272d_2bx6a7065f683bd1413_0 <= 2000
 R7: - 1000 z_||_2bx6a7065f683bd1413_0 + rho_||_2bx6a7065f683bd1413_0
   + 1000 zhat_predicate_2bx696bb36562d5272d_2bx6a7065f683bd1413_0 <= 1000
 R8: z_||_2bx6a7065f683bd1413_0 - z_predicate_2dx5a605e8b6db0d82b_0
   - z_predicate_2bx696bb36562d5272d_0 <= 0
 R9: zhat_predicate_2dx5a605e8b6db0d82b_2bx6a7065f683bd1413_0
   + zhat_predicate_2bx696bb36562d5272d_2bx6a7065f683bd1413_0 >= 1
 formula_satisfaction: z_||_2bx6a7065f683bd1413_0 = 1
Bounds
 z_||_2bx6a7065f683bd1413_0 <= 1
 rho_||_2bx6a7065f683bd1413_0 free
 rho_predicate_2dx5a605e8b6db0d82b_0 free
 x_0 <= 10
 rho_predicate_2bx696bb36562d5272d_0 free
Binaries
 z_predicate_2dx5a605e8b6db0d82b_0 z_predicate_2bx696bb36562d5272d_0
 zhat_predicate_2dx5a605e8b6db0d82b_2bx6a7065f683bd1413_0
 zhat_predicate_2bx696bb36562d5272d_2bx6a7065f683bd1413_0
End
