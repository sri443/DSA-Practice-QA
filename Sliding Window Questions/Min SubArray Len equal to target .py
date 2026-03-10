'''Given an array of positive integers nums and integer target, 

return the minimum length of a subarray whose sum = target.

If no such subarray exists, return 0.'''

def minSubArrayLen(target, nums):
    start=0
    min_len=float("inf")
    sum1=0
    for end in range(len(nums)):
        sum1+=nums[end]
        while sum1>target:
            sum1-=nums[start]
            start+=1
        if sum1==target:
            min_len=min(min_len,end-start+1)
    return min_len if min_len < float("inf") else 0
