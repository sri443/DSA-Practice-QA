'''You are given an array of positive integers nums and an integer k.

Return the number of contiguous subarrays whose sum is ≤ k.'''

def countSubarraysAtMostK(nums, k):
  
    start=0
    sum1=0
    count=0
  
    for end in range(len(nums)):
        sum1+=nums[end]
      
        while sum1>k:
            sum1-=nums[start]
            start+=1
          
        count+=end-start+1
      
    return count
