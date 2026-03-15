''' You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        start=0
        max_avg=float("-inf")
        window_sum=float("0")
      
        for end in range(len(nums)):
            window_sum+=nums[end]
          
            while end-start+1>k:
                window_sum-=nums[start]
                start+=1
              
            if end-start+1==k:
                max_avg=max(max_avg,window_sum/k)
              
        return max_avg


'''Solution 2'''

class Solution(object):
    def findMaxAverage(self, nums, k):
      
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum += nums[i]     #Can combine addition and subtraction in same step
            window_sum -= nums[i-k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / float(k)
