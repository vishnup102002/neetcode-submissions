class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)-1
        m1={}
        m2={}
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            m1[s1[i]]=1+m1.get(s1[i],0)
            m2[s2[i]]=1+m2.get(s2[i],0)
        if m1==m2:
            return True
        for r in range (len(s1),len(s2)):
            m2[s2[l]]-=1
            if m2[s2[l]]==0:
                del m2[s2[l]]
            l+=1
            m2[s2[r]]=1+m2.get(s2[r],0)
            if m1==m2:
                return True
            
        return False


            
        