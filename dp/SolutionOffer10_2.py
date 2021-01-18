class Solution:
    def numWays(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        if n==0:
            return 1
        if n==1 or n==2:
            return n
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            dp[i]=dp[i]%1000000007
        return dp[i]