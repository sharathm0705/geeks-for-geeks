class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        arr.sort()

        def countLessThanOrEqual(val):
            count = 0
            n = len(arr)
            for i in range(n - 2):
                left = i + 1
                right = n - 1
                while left < right:
                    current_sum = arr[i] + arr[left] + arr[right]
                    if current_sum <= val:
                        count += (right - left)
                        left += 1
                    else:
                        right -= 1
            return count

        return countLessThanOrEqual(r) - countLessThanOrEqual(l - 1)