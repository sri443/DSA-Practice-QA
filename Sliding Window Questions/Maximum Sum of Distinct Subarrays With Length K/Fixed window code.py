#Time complexity O(n)
#Space complexity O(k)

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq =  {}
        output = sum(nums[:k])
        distinct = 0
        best = 0

        for i in range(k):
            x = nums[i]
            if nums[i] in freq:
                freq[x] += 1
            else:
                freq[x] = 1
                distinct += 1
        
        if distinct == k:
            best = output

        for i in range(k,len(nums)):
            add = nums[i]
            rem = nums[i-k]
            output = output + add - rem

            if add in freq:
                freq[add] += 1
            else:
                freq[add] = 1
                distinct += 1
            
            freq[rem] -= 1
            if freq[rem] == 0:
                del freq[rem]
                distinct -= 1
            
            if distinct == k and output>best:
                best = output
        return best
