from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = 0
        n = len(nums)
        res = [0] * n  # Initializes output array of size n with zeros
        
        # Step 1: Calculate product of non-zero numbers and count total zeros
        for num in nums:
            if num == 0:
                zero += 1
                continue
            prod *= num
            
        # Case 1: More than 1 zero -> everything is 0 (res is already [0] * n)
        if zero > 1:
            return res
        
        # Case 2: Exactly 1 zero -> only the zero position gets non-zero product
        elif zero == 1:
            for i in range(n):
                if nums[i] == 0:
                    res[i] = prod
                    
        # Case 3: No zeros -> standard division using integer division '//'
        else:
            for i in range(n):
                res[i] = prod // nums[i]  # Use // to keep integers (avoid floats like 24.0)

        return res