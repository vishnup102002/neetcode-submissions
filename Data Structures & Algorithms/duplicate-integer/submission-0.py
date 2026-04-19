class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=set(nums)
        return len(l)!=len(nums)
        