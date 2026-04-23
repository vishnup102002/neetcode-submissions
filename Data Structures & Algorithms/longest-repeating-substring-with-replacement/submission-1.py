class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp={}
        l,res=0,0
        m_f=0
        for r in range(len(s)):
            mapp[s[r]] = 1+mapp.get(s[r],0)
            m_f=max(m_f,mapp[s[r]])
            while (r-l+1)-m_f>k:
                mapp[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
