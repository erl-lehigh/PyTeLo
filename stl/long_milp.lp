\ Model L-WSTL formula: ((F[0.0, 2.0]^<lambda> (x <= 5.0)) &&^<lambda> (F[0.0, 2.0]^<lambda> (x <= 2.0)) &&^<lambda> (F[0.0, 4.0]^<lambda> (x >= 9.0)))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  rho_&&_2dx6e0404ace59dfaca_0
Subject To
 R0: 1000 z_predicate_2dx41f8ab8e3008e3bf_0
   + rho_predicate_2dx41f8ab8e3008e3bf_0 + x_0 >= 5
 R1: 1000 z_predicate_2dx41f8ab8e3008e3bf_0
   + rho_predicate_2dx41f8ab8e3008e3bf_0 + x_0 <= 1005
 R2: 1000 z_predicate_2dx41f8ab8e3008e3bf_1
   + rho_predicate_2dx41f8ab8e3008e3bf_1 + x_1 >= 5
 R3: 1000 z_predicate_2dx41f8ab8e3008e3bf_1
   + rho_predicate_2dx41f8ab8e3008e3bf_1 + x_1 <= 1005
 R4: 1000 z_predicate_2dx41f8ab8e3008e3bf_2
   + rho_predicate_2dx41f8ab8e3008e3bf_2 + x_2 >= 5
 R5: 1000 z_predicate_2dx41f8ab8e3008e3bf_2
   + rho_predicate_2dx41f8ab8e3008e3bf_2 + x_2 <= 1005
 R6: 1000 z_F_2dx600f19d3f244bc16_0 + rho_F_2dx600f19d3f244bc16_0
   - 10 rho_predicate_2dx41f8ab8e3008e3bf_0
   + 1000 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_0 <= 2000
 R7: - 1000 z_F_2dx600f19d3f244bc16_0 + rho_F_2dx600f19d3f244bc16_0
   + 9 rho_predicate_2dx41f8ab8e3008e3bf_0
   + 1000 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_0 <= 1000
 R8: 1000 z_F_2dx600f19d3f244bc16_0 + rho_F_2dx600f19d3f244bc16_0
   - 10 rho_predicate_2dx41f8ab8e3008e3bf_1
   + 1000 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_1 <= 2000
 R9: - 1000 z_F_2dx600f19d3f244bc16_0 + rho_F_2dx600f19d3f244bc16_0
   + 9 rho_predicate_2dx41f8ab8e3008e3bf_1
   + 1000 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_1 <= 1000
 R10: 1000 z_F_2dx600f19d3f244bc16_0 + rho_F_2dx600f19d3f244bc16_0
   - 10 rho_predicate_2dx41f8ab8e3008e3bf_2
   + 1000 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_2 <= 2000
 R11: - 1000 z_F_2dx600f19d3f244bc16_0 + rho_F_2dx600f19d3f244bc16_0
   + 9 rho_predicate_2dx41f8ab8e3008e3bf_2
   + 1000 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_2 <= 1000
 R12: z_F_2dx600f19d3f244bc16_0 - z_predicate_2dx41f8ab8e3008e3bf_0
   - z_predicate_2dx41f8ab8e3008e3bf_1 - z_predicate_2dx41f8ab8e3008e3bf_2
   <= 0
 R13: zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_0
   + zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_1
   + zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_2 >= 1
 R14: x_0 + 1000 z_predicate_2dx4fd9632aacb9ccb4_0
   + rho_predicate_2dx4fd9632aacb9ccb4_0 >= 2
 R15: x_0 + 1000 z_predicate_2dx4fd9632aacb9ccb4_0
   + rho_predicate_2dx4fd9632aacb9ccb4_0 <= 1002
 R16: x_1 + 1000 z_predicate_2dx4fd9632aacb9ccb4_1
   + rho_predicate_2dx4fd9632aacb9ccb4_1 >= 2
 R17: x_1 + 1000 z_predicate_2dx4fd9632aacb9ccb4_1
   + rho_predicate_2dx4fd9632aacb9ccb4_1 <= 1002
 R18: x_2 + 1000 z_predicate_2dx4fd9632aacb9ccb4_2
   + rho_predicate_2dx4fd9632aacb9ccb4_2 >= 2
 R19: x_2 + 1000 z_predicate_2dx4fd9632aacb9ccb4_2
   + rho_predicate_2dx4fd9632aacb9ccb4_2 <= 1002
 R20: 1000 z_F_2dxcbdd9c68ce83a47_0 + rho_F_2dxcbdd9c68ce83a47_0
   - 5 rho_predicate_2dx4fd9632aacb9ccb4_0
   + 1000 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_0 <= 2000
 R21: - 1000 z_F_2dxcbdd9c68ce83a47_0 + rho_F_2dxcbdd9c68ce83a47_0
   + 4 rho_predicate_2dx4fd9632aacb9ccb4_0
   + 1000 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_0 <= 1000
 R22: 1000 z_F_2dxcbdd9c68ce83a47_0 + rho_F_2dxcbdd9c68ce83a47_0
   - 5 rho_predicate_2dx4fd9632aacb9ccb4_1
   + 1000 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_1 <= 2000
 R23: - 1000 z_F_2dxcbdd9c68ce83a47_0 + rho_F_2dxcbdd9c68ce83a47_0
   + 4 rho_predicate_2dx4fd9632aacb9ccb4_1
   + 1000 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_1 <= 1000
 R24: 1000 z_F_2dxcbdd9c68ce83a47_0 + rho_F_2dxcbdd9c68ce83a47_0
   - 5 rho_predicate_2dx4fd9632aacb9ccb4_2
   + 1000 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_2 <= 2000
 R25: - 1000 z_F_2dxcbdd9c68ce83a47_0 + rho_F_2dxcbdd9c68ce83a47_0
   + 4 rho_predicate_2dx4fd9632aacb9ccb4_2
   + 1000 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_2 <= 1000
 R26: z_F_2dxcbdd9c68ce83a47_0 - z_predicate_2dx4fd9632aacb9ccb4_0
   - z_predicate_2dx4fd9632aacb9ccb4_1 - z_predicate_2dx4fd9632aacb9ccb4_2
   <= 0
 R27: zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_0
   + zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_1
   + zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_2 >= 1
 R28: x_0 - 1000 z_predicate_2dx7621d167b92cd791_0
   - rho_predicate_2dx7621d167b92cd791_0 <= 9
 R29: x_0 - 1000 z_predicate_2dx7621d167b92cd791_0
   - rho_predicate_2dx7621d167b92cd791_0 >= -991
 R30: x_1 - 1000 z_predicate_2dx7621d167b92cd791_1
   - rho_predicate_2dx7621d167b92cd791_1 <= 9
 R31: x_1 - 1000 z_predicate_2dx7621d167b92cd791_1
   - rho_predicate_2dx7621d167b92cd791_1 >= -991
 R32: x_2 - 1000 z_predicate_2dx7621d167b92cd791_2
   - rho_predicate_2dx7621d167b92cd791_2 <= 9
 R33: x_2 - 1000 z_predicate_2dx7621d167b92cd791_2
   - rho_predicate_2dx7621d167b92cd791_2 >= -991
 R34: - 1000 z_predicate_2dx7621d167b92cd791_3
   - rho_predicate_2dx7621d167b92cd791_3 + x_3 <= 9
 R35: - 1000 z_predicate_2dx7621d167b92cd791_3
   - rho_predicate_2dx7621d167b92cd791_3 + x_3 >= -991
 R36: - 1000 z_predicate_2dx7621d167b92cd791_4
   - rho_predicate_2dx7621d167b92cd791_4 + x_4 <= 9
 R37: - 1000 z_predicate_2dx7621d167b92cd791_4
   - rho_predicate_2dx7621d167b92cd791_4 + x_4 >= -991
 R38: 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   - 5 rho_predicate_2dx7621d167b92cd791_0
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_0 <= 2000
 R39: - 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   + 4 rho_predicate_2dx7621d167b92cd791_0
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_0 <= 1000
 R40: 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   - 5 rho_predicate_2dx7621d167b92cd791_1
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_1 <= 2000
 R41: - 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   + 4 rho_predicate_2dx7621d167b92cd791_1
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_1 <= 1000
 R42: 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   - 5 rho_predicate_2dx7621d167b92cd791_2
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_2 <= 2000
 R43: - 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   + 4 rho_predicate_2dx7621d167b92cd791_2
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_2 <= 1000
 R44: 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   - 5 rho_predicate_2dx7621d167b92cd791_3
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_3 <= 2000
 R45: - 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   + 4 rho_predicate_2dx7621d167b92cd791_3
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_3 <= 1000
 R46: 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   - 5 rho_predicate_2dx7621d167b92cd791_4
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_4 <= 2000
 R47: - 1000 z_F_2bx458975d0c31dd2fe_0 + rho_F_2bx458975d0c31dd2fe_0
   + 4 rho_predicate_2dx7621d167b92cd791_4
   + 1000 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_4 <= 1000
 R48: z_F_2bx458975d0c31dd2fe_0 - z_predicate_2dx7621d167b92cd791_0
   - z_predicate_2dx7621d167b92cd791_1 - z_predicate_2dx7621d167b92cd791_2
   - z_predicate_2dx7621d167b92cd791_3 - z_predicate_2dx7621d167b92cd791_4
   <= 0
 R49: zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_0
   + zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_1
   + zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_2
   + zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_3
   + zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_4 >= 1
 R50: 1000 z_&&_2dx6e0404ace59dfaca_0 + rho_&&_2dx6e0404ace59dfaca_0
   <= 1000
 R51: - 1000 z_&&_2dx6e0404ace59dfaca_0 + rho_&&_2dx6e0404ace59dfaca_0
   - rho_F_2dx600f19d3f244bc16_0 <= 0
 R52: z_&&_2dx6e0404ace59dfaca_0 - z_F_2dx600f19d3f244bc16_0 <= 0
 R53: 1000 z_&&_2dx6e0404ace59dfaca_0 + rho_&&_2dx6e0404ace59dfaca_0
   + rho_F_2dxcbdd9c68ce83a47_0 <= 1000
 R54: - 1000 z_&&_2dx6e0404ace59dfaca_0 + rho_&&_2dx6e0404ace59dfaca_0
   - 2 rho_F_2dxcbdd9c68ce83a47_0 <= 0
 R55: z_&&_2dx6e0404ace59dfaca_0 - z_F_2dxcbdd9c68ce83a47_0 <= 0
 R56: 1000 z_&&_2dx6e0404ace59dfaca_0 + rho_&&_2dx6e0404ace59dfaca_0
   + 2 rho_F_2bx458975d0c31dd2fe_0 <= 1000
 R57: - 1000 z_&&_2dx6e0404ace59dfaca_0 + rho_&&_2dx6e0404ace59dfaca_0
   - 3 rho_F_2bx458975d0c31dd2fe_0 <= 0
 R58: z_&&_2dx6e0404ace59dfaca_0 - z_F_2bx458975d0c31dd2fe_0 <= 0
 formula_satisfaction: z_&&_2dx6e0404ace59dfaca_0 = 1
Bounds
 z_&&_2dx6e0404ace59dfaca_0 <= 1
 rho_&&_2dx6e0404ace59dfaca_0 free
 z_F_2dx600f19d3f244bc16_0 <= 1
 rho_F_2dx600f19d3f244bc16_0 free
 rho_predicate_2dx41f8ab8e3008e3bf_0 free
 x_0 <= 10
 rho_predicate_2dx41f8ab8e3008e3bf_1 free
 x_1 <= 10
 rho_predicate_2dx41f8ab8e3008e3bf_2 free
 x_2 <= 10
 z_F_2dxcbdd9c68ce83a47_0 <= 1
 rho_F_2dxcbdd9c68ce83a47_0 free
 rho_predicate_2dx4fd9632aacb9ccb4_0 free
 rho_predicate_2dx4fd9632aacb9ccb4_1 free
 rho_predicate_2dx4fd9632aacb9ccb4_2 free
 z_F_2bx458975d0c31dd2fe_0 <= 1
 rho_F_2bx458975d0c31dd2fe_0 free
 rho_predicate_2dx7621d167b92cd791_0 free
 rho_predicate_2dx7621d167b92cd791_1 free
 rho_predicate_2dx7621d167b92cd791_2 free
 rho_predicate_2dx7621d167b92cd791_3 free
 x_3 <= 10
 rho_predicate_2dx7621d167b92cd791_4 free
 x_4 <= 10
Binaries
 z_predicate_2dx41f8ab8e3008e3bf_0 z_predicate_2dx41f8ab8e3008e3bf_1
 z_predicate_2dx41f8ab8e3008e3bf_2
 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_0
 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_1
 zhat_predicate_2dx41f8ab8e3008e3bf_2dx600f19d3f244bc16_2
 z_predicate_2dx4fd9632aacb9ccb4_0 z_predicate_2dx4fd9632aacb9ccb4_1
 z_predicate_2dx4fd9632aacb9ccb4_2
 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_0
 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_1
 zhat_predicate_2dx4fd9632aacb9ccb4_2dxcbdd9c68ce83a47_2
 z_predicate_2dx7621d167b92cd791_0 z_predicate_2dx7621d167b92cd791_1
 z_predicate_2dx7621d167b92cd791_2 z_predicate_2dx7621d167b92cd791_3
 z_predicate_2dx7621d167b92cd791_4
 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_0
 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_1
 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_2
 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_3
 zhat_predicate_2dx7621d167b92cd791_2bx458975d0c31dd2fe_4
End
