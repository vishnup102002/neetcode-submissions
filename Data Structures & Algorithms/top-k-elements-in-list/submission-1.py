class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp={}
        f=[[] for i in range(len(nums)+1)]
        for n in nums:
            mapp[n]=mapp.get(n,0)+1
        for a,b in mapp.items():
            f[b].append(a)
        res=[]
        for i in range(len(f)-1,0,-1):
            for j in f[i]:
                res.append(j)
            if len(res)==k:
                return res