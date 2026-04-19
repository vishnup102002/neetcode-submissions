class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lt=sorted(set(nums))
        n=0
        m=0
        for i in lt:
            if(i-1 not in lt):
                n=i
                l=1
            while n+1 in lt:
                l+=1
                n+=1
            m=max(m,l)
        return m







        