def subarraySum(arr, n, s):
    curr_sum = arr[0]
    start = 0
    for i in range(1, n+1):
        while curr_sum > s and start < i-1:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == s:
            return [start+1, i]
        if i < n:
            curr_sum += arr[i]
    return [-1]