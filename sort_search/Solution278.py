class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left+1 < right:
            mid = left + (right - left) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        # 要考虑第一个是错的的情况
        if isBadVersion(left):
            return left
        else:
            return right


def isBadVersion(n):
    return True