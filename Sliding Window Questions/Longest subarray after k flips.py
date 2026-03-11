'''You are given a binary array nums (only 0 and 1) and an integer k.

You may flip at most k zeros to 1s.

Return the length of the longest contiguous subarray containing only 1s after performing at most k flips.'''

def longestOnes(nums, k):

    start=0
    max_len=0
    count=0
  
    for end in range(len(nums)):
      
        if nums[end]==0:
            count+=1
          
        while count>k:
            if nums[start]==0:
                count-=1
            start+=1
          
        max_len=max(max_len,end-start+1)
      
    return max_len
