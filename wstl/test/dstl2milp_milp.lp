\ Model STL formula: ((x <= 2.0) || (x > 3.0))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - rho
Subject To
 R0: rho + 1000 predicate_2dx4fd9632aacb9ccb4_0 + x_0 >= 2
 R1: rho + 1000 predicate_2dx4fd9632aacb9ccb4_0 + x_0 <= 1002
 R2: - rho + x_0 - 1000 predicate_2dx3f86447cf37d038f_0 <= 3
 R3: - rho + x_0 - 1000 predicate_2dx3f86447cf37d038f_0 >= -997
 R4: ||_2dx501e5e412dfc71be_0 - predicate_2dx4fd9632aacb9ccb4_0 >= 0
 R5: ||_2dx501e5e412dfc71be_0 - predicate_2dx3f86447cf37d038f_0 >= 0
 R6: ||_2dx501e5e412dfc71be_0 - predicate_2dx4fd9632aacb9ccb4_0
   - predicate_2dx3f86447cf37d038f_0 <= 0
 formula_satisfaction: ||_2dx501e5e412dfc71be_0 = 1
Bounds
 -infinity <= rho <= 999
 -10 <= x_0 <= 10
Binaries
 ||_2dx501e5e412dfc71be_0 predicate_2dx4fd9632aacb9ccb4_0
 predicate_2dx3f86447cf37d038f_0
End
