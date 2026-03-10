'''Given an array of positive integers nums and integer target, 

return the minimum length of a subarray whose sum >= target.

If no such subarray exists, return 0.'''

def minSubArrayLen(target, nums):
    start = 0
    window_sum = 0
    min_len = float("inf")

    for end in range(len(nums)):
        window_sum += nums[end]

        while window_sum >= target:
            min_len = min(min_len, end - start + 1)
            window_sum -= nums[start]
            start += 1

    return 0 if min_len == float("inf") else min_len
