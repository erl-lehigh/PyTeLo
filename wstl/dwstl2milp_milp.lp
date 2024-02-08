\ Model STL formula: ((x <= 6.0) ||^<lambda> (x >= 2.0))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  rho_||_2bx45dfd68d5bdd9a5b_0
Subject To
 R0: 1000 predicate_2dx18566057797ead00_0
   + rho_predicate_2dx18566057797ead00_0 + x_0 >= 6
 R1: 1000 predicate_2dx18566057797ead00_0
   + rho_predicate_2dx18566057797ead00_0 + x_0 <= 1006
 R2: x_0 - 1000 predicate_2dx14fcdaada9e9bb5e_0
   - rho_predicate_2dx14fcdaada9e9bb5e_0 <= 2
 R3: x_0 - 1000 predicate_2dx14fcdaada9e9bb5e_0
   - rho_predicate_2dx14fcdaada9e9bb5e_0 >= -998
 R4: rho_||_2bx45dfd68d5bdd9a5b_0 - rho_predicate_2dx18566057797ead00_0
   + 1000 zhat_predicate_2dx18566057797ead00_2bx45dfd68d5bdd9a5b_0 <= 1000
 R5: ||_2bx45dfd68d5bdd9a5b_0 - predicate_2dx18566057797ead00_0 >= 0
 R6: - predicate_2dx18566057797ead00_0
   + zhat_predicate_2dx18566057797ead00_2bx45dfd68d5bdd9a5b_0 <= 0
 R7: rho_||_2bx45dfd68d5bdd9a5b_0 - 4 rho_predicate_2dx14fcdaada9e9bb5e_0
   + 1000 zhat_predicate_2dx14fcdaada9e9bb5e_2bx45dfd68d5bdd9a5b_0 <= 1000
 R8: ||_2bx45dfd68d5bdd9a5b_0 - predicate_2dx14fcdaada9e9bb5e_0 >= 0
 R9: - predicate_2dx14fcdaada9e9bb5e_0
   + zhat_predicate_2dx14fcdaada9e9bb5e_2bx45dfd68d5bdd9a5b_0 <= 0
 R10: ||_2bx45dfd68d5bdd9a5b_0 - predicate_2dx18566057797ead00_0
   - predicate_2dx14fcdaada9e9bb5e_0 <= 0
 R11: - ||_2bx45dfd68d5bdd9a5b_0
   + zhat_predicate_2dx18566057797ead00_2bx45dfd68d5bdd9a5b_0
   + zhat_predicate_2dx14fcdaada9e9bb5e_2bx45dfd68d5bdd9a5b_0 >= 0
 formula_satisfaction: ||_2bx45dfd68d5bdd9a5b_0 = 1
Bounds
 rho_||_2bx45dfd68d5bdd9a5b_0 free
 rho_predicate_2dx18566057797ead00_0 free
 x_0 <= 10
 rho_predicate_2dx14fcdaada9e9bb5e_0 free
Binaries
 ||_2bx45dfd68d5bdd9a5b_0 predicate_2dx18566057797ead00_0
 predicate_2dx14fcdaada9e9bb5e_0
 zhat_predicate_2dx18566057797ead00_2bx45dfd68d5bdd9a5b_0
 zhat_predicate_2dx14fcdaada9e9bb5e_2bx45dfd68d5bdd9a5b_0
End
