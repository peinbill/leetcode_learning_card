class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n==0:
            return 0
        dp = [1 for i in range(n)]
        dp[0]=1
        i2,i3,i5 = 0,0,0
        for i in range(1,n):
            min_num= min(2*dp[i2],3*dp[i3],5*dp[i5])
            dp[i]= min_num
            if min_num==2*dp[i2]:
                i2+=1
            if min_num==3*dp[i3]:
                i3+=1
            if min_num==5*dp[i5]:
                i5+=1
        return dp[-1]

if __name__=="__main__":
    solution = Solution()
    print(solution.nthUglyNumber(7))