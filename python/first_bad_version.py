# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(min, max, vers):
            if min > max:
                return min
            mid = (min + max) // 2
            vers[n] = isBadVersion(mid)
            if vers[n] and (n - 1) in vers and not vers[n - 1]:
                return mid
            elif vers[n]:
                return helper(min, mid - 1, vers)
            else:
                return helper(mid + 1, max, vers)
            
        vers = {}
        return helper(0, n, vers)