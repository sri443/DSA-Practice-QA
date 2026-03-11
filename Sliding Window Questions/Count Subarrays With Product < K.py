'''Given an array of positive integers nums and an integer k, 

return the number of contiguous subarrays where:

product < k'''

def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    start = 0
    prod = 1
    count = 0

    for end in range(len(nums)):
        prod *= nums[end]

        while prod >= k:
            prod //= nums[start]
            start += 1

        count += end - start + 1

    return count
