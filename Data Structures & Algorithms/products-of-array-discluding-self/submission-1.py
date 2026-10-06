class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        post, pre = 1,1
        for i in range(n):
            res[i] = pre
            pre*=nums[i]
        
        for i in range(n-1,-1,-1):
            res[i] *=post
            post*=nums[i]
        
        return res
            
        