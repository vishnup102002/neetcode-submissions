class Solution:

    def encode(self, strs: List[str]) -> str:

        s1 = ""
        for w in strs:
            s1+=str(len(w))+"#"+w
        return s1
        
    def decode(self, s: str) -> List[str]:
        r=[]
        i=0
        while(i<len(s)):
            j = s.find("#", i)
            l = int(s[i:j])
            r.append(s[j+1 : j+1+l])
            i=j+1+l
        return r

        