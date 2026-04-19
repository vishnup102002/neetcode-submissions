class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            s=0
            e=c-1
            while s<=e:
                mid =(s+e)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    e=mid-1
                else:
                    s=mid+1
        return False

        