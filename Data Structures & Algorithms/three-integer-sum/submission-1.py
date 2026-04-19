class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r=[]
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            s=i+1
            e=len(nums)-1
            while  s<e:
                target = -(nums[s] + nums[e])
                if a < target:
                    s += 1
                elif a > target:
                    e -= 1
                else:
                    r.append([a, nums[s], nums[e]])
                    s += 1
                    e -= 1
                    while s<e and nums[s]==nums[s-1]:
                        s+=1
                    while s<e and nums[e]==nums[e+1]:
                        e-=1
        return r
                    


            


        