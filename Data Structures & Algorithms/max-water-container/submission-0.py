class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        l=0
        r=len(heights)-1
        while l<r:
            x=min(heights[r],heights[l])
            y=r-l
            a=x*y
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            m=max(m,a)
        return m      