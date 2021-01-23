class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.count=0
        self.dfs(0,0,m,n,k)
        return self.count

    def dfs(self,i,j,m,n,k):
        if i>m-1 or j>n-1:
            return
        if not self.isVaild(i,j,k):
            return
        self.count+=1
        self.dfs(i+1,j,m,n,k)
        self.dfs(i,j+1,m,n,k)


    def isVaild(self,i,j,k)-> bool:
        sum_num=0
        while i/10!=0:
            sum_num+=i%10
            i = i/10
        sum_num+=i%10
        while j/10!=0:
            sum_num += j%10
            j=j/10
        sum_num += j%10
        return sum_num<=k

if __name__=="__main__":
    solution = Solution()
    solution.movingCount(1,2,1)