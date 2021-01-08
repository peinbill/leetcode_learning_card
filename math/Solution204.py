import math
class Solution:
    # 暴力破解，注意 i 遍历到最大 \sqrt{n}
    def countPrimes1(self, n: int) -> int:
        def isPrime(n):
            max_n = int(math.sqrt(n))
            for i in range(2,max_n+1):
                if n%i==0:
                    return False
            return True
        cnt = 0
        for i in range(2,n):
            if isPrime(i):
                cnt+=1
                # print(i)
        return cnt



    # 埃氏筛_重点掌握
    # 初始化长度 O(n)的标记数组，表示这个数组是否为质数。数组初始化所有的数都是质数
    # 从 2 开始将当前数字的倍数全都标记为合数。标记到 \sqrt{n} 时停止
    def countPrimes(self,n:int)->int:
        isPrime = [True for i in range(n)]
        i = 2
        while i*i<n:
            if isPrime[i]:
                for j in range(i*i,n,i):
                    isPrime[j] = False

            i+=1

        cnt=0
        for i in range(2,n):
            if isPrime[i]:
                cnt+=1
        return cnt


if __name__=="__main__":
    solution = Solution()
    print(solution.countPrimes1(10))