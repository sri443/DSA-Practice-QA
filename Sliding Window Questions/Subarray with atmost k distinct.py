'''Return the number of subarrays with at most k distinct integers.'''


def subarraysWithAtMostKDistinct(nums, k):
    start = 0
    freq = {}
    count = 0

    for end in range(len(nums)):
        freq[nums[end]] = freq.get(nums[end], 0) + 1

        while len(freq) > k:
            freq[nums[start]] -= 1
            if freq[nums[start]] == 0:
                del freq[nums[start]]
            start += 1

        count += end - start + 1

    return count
