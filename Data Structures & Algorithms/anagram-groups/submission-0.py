class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp=defaultdict(list)
        for s in strs:
            a="".join(sorted(s))
            mapp[a].append(s)
            l=list(mapp.values())
        return l