from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m:m+n]=B[:]

        def exch(nums,i,j):
            nums[i],nums[j]=nums[j],nums[i]

        # 再使用插入排序
        for i in range(m,m+n):
            for j in range(i,0,-1):
                if A[j-1]>A[j]:
                    exch(A,j,j-1)
                else:
                    break

        return A

if __name__=="__main__":
    solution = Solution()
    solution.merge([2,0],1,[1],1)