class Solution:
    def maxArea(self, heights: List[int]) -> int:
        target = 0
        left = 0
        right = len(heights)-1
        while left<right:
            c_h = min(heights[left],heights[right])
            w = right- left
            c_a = c_h*w

            target = max(c_a,target)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return target
        