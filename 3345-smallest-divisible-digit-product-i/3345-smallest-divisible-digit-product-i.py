class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:

            product = 1
            num = n

            # Find product of digits
            while num > 0:
                digit = num % 10
                product *= digit
                num //= 10

            # Check divisibility
            if product % t == 0:
                return n

            # Try next number
            n += 1
        