class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur_area=0
        max_area=0
        left = 0
        right = len(heights)-1
        while left<right:
            width=right-left
            height=min(heights[left],heights[right])
            cur_area = width* height
            max_area = max(max_area,cur_area)
            if heights[left]<=heights[right]:
                left+=1
            elif heights[right]<heights[left]:
                right-=1
            
        return max_area
              


        