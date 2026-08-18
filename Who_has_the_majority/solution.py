class Solution:
    def moreFrequent(self, arr, x, y):
        #code here
        count_x = arr.count(x)
        count_y = arr.count(y)
        
        if count_x > count_y:
            return x
        elif count_y > count_x:
            return y
        else:
            return min(x, y)