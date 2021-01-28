from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix==None or len(matrix)==0:
            return []
        if len(matrix)==1:
            return matrix[0]

        row_num = len(matrix)
        col_num = len(matrix[0])
        num_count = row_num*col_num

        start = 1

        top,bottom = 0,row_num-1
        left,right = 0,col_num-1

        result = []

        while start<=num_count:
            # top
            for i in range(left,right+1):
                result.append(matrix[top][i])
                start+=1

            # right
            for i in range(top+1,bottom+1):
                result.append(matrix[i][right])
                start+=1

            if top!=bottom:
                # bottom
                for i in range(right-1,left-1,-1):
                    result.append(matrix[bottom][i])
                    start += 1

            if left!=right:
                # left
                for i in range(bottom-1,top,-1):
                    result.append(matrix[i][left])
                    start += 1

            left+=1
            right-=1
            top+=1
            bottom-=1
        return result

if __name__=="__main__":
    solution = Solution()
    print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))