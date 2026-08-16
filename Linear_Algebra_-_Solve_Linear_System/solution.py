import numpy as np
class Solution:
    def solveLinearSystem(self, a, b):
        # code here
        return np.linalg.solve(a, b)