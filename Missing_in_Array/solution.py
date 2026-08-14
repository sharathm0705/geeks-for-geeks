class Solution:
    def missingNum(self, n, arr):
        return n*(n+1)//2 - sum(arr)