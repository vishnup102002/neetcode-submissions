class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr=[0]*len(temperatures)
        for i in range(len(temperatures)):
            a=temperatures[i]
            for j in range(i + 1, len(temperatures)):
                b=temperatures[j]
                if a<b:
                    arr[i] = j - i
                    break
                
        return arr
                