\ Model pswSTL formula: ((x >= 5.0) &^<lambda> (x <= 1.0))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  z_&_2dx64a121e056f17e94_0
Subject To
 R0: - 1000 z_predicate_2dx3e9eebaf2234d87d_0 + x_0 <= 5
 R1: - 1000 z_predicate_2dx3e9eebaf2234d87d_0 + x_0 >= -995
 R2: x_0 + 1000 z_predicate_2dx797b9146c700e2d3_0 >= 1
 R3: x_0 + 1000 z_predicate_2dx797b9146c700e2d3_0 <= 1001
 R4: z_&_2dx64a121e056f17e94_0
   - 0.8333333333333334 z_predicate_2dx3e9eebaf2234d87d_0
   - 0.1666666666666667 z_predicate_2dx797b9146c700e2d3_0 = 0
Bounds
 z_&_2dx64a121e056f17e94_0 <= 1
 -10 <= x_0 <= 10
Binaries
 z_predicate_2dx3e9eebaf2234d87d_0 z_predicate_2dx797b9146c700e2d3_0
End
