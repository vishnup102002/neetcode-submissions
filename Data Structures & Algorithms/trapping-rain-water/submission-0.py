class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        maxl=0
        maxr=0
        res=0
        l,r=0,len(height)-1
        while l<r:
            maxl=max(height[l],maxl)
            maxr=max(height[r],maxr)
            if maxl <=maxr:
                if maxl-height[l]>=0:
                    res+=maxl-height[l]
                l+= 1
            else:
                if maxr-height[r]>=0:
                    res+=maxr-height[r]
                r-= 1
        return res



      
             

            
            
            

        