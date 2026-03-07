#Time Complexity O(n)
#Space Complexity O(k)

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        curr_sum=0
        start=0
        ans=0
        freq=set()
      
        for end in range(len(nums)):
            while nums[end] in freq:
                freq.remove(nums[start])
                curr_sum-=nums[start]
                start+=1
              
            freq.add(nums[end])
            curr_sum+=nums[end]
          
            if end-start+1 == k:
                ans=max(curr_sum,ans)
                freq.remove(nums[start])
                curr_sum-=nums[start]
                start+=1
              
        return ans

            
