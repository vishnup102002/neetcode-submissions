class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        a=[]
        res=0
        for r in range(len(s)):
            while s[r] in a:
                a.pop(0)
            
            a.append(s[r])
            res=max(res,len(a))
        return res
            
        