class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        current = x
        m = -n if n < 0 else n
        while m > 0:
            
            if m & 1:
                result *= current
            current *= current
            m >>= 1

        return 1 / result if n < 0 else result
