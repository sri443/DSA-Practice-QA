'''You are given an integer array nums and an integer k.

Return true if there exists a subarray of length k where all elements are distinct. Otherwise return false.

Example
Input: nums = [1,2,3,1,4,5], k = 3
Output: True
'''

def hasDistinctSubarray(nums, k):
    freq = set()
    start = 0

    for end in range(len(nums)):

        while nums[end] in freq:
            freq.remove(nums[start])
            start += 1

        freq.add(nums[end])

        if end - start + 1 == k:
            return True

    return False
