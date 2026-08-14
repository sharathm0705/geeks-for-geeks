class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n = len(arr)
    
        if n % 2 != 0:
            return arr[n // 2]