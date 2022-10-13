\ Model STL formula: ((x <= 8.0) && (x >= 4.0) && (x >= 3.0))
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - rho + 0 C6 + 0 C7 + 0 C8 + 0 C9 + 0 C10 + 0 C11 + 0 C12 + 0 C13 + 0 C14
   + 0 C15 + 0 C16 + 0 C17 + 0 C18 + 0 C19 + 0 C20 + 0 C21
Subject To
 R0: rho + 1000 predicate_2bx36b1284cc44798e_0 + x_0 >= 8
 R1: rho + 1000 predicate_2bx36b1284cc44798e_0 + x_0 <= 1008
 R2: - rho + x_0 - 1000 predicate_2dx30be4d89f565bb0c_0 <= 4
 R3: - rho + x_0 - 1000 predicate_2dx30be4d89f565bb0c_0 >= -996
 R4: - rho + x_0 - 1000 predicate_2dx22dd95ed78b4d217_0 <= 3
 R5: - rho + x_0 - 1000 predicate_2dx22dd95ed78b4d217_0 >= -997
 R6: &&_2bx13091e873a7b1722_0 - predicate_2bx36b1284cc44798e_0 <= 0
 R7: &&_2bx13091e873a7b1722_0 - predicate_2dx30be4d89f565bb0c_0 <= 0
 R8: &&_2bx13091e873a7b1722_0 - predicate_2dx22dd95ed78b4d217_0 <= 0
 R9: &&_2bx13091e873a7b1722_0 - predicate_2bx36b1284cc44798e_0
   - predicate_2dx30be4d89f565bb0c_0 - predicate_2dx22dd95ed78b4d217_0
   >= -2
 formula_satisfaction: &&_2bx13091e873a7b1722_0 = 1
Bounds
 -infinity <= rho <= 999
 x_0 <= 10
 C6 free
 C7 free
 C8 free
 C9 free
 C10 free
 C11 free
 C12 free
 C13 free
 C14 free
 C15 free
 C16 free
 C17 free
 C18 free
 C19 free
 C20 free
 C21 free
Binaries
 &&_2bx13091e873a7b1722_0 predicate_2bx36b1284cc44798e_0
 predicate_2dx30be4d89f565bb0c_0 predicate_2dx22dd95ed78b4d217_0
End
