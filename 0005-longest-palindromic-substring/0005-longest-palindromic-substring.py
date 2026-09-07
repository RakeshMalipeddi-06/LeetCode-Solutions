class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        result = ""

        for i in range(n):

            # Odd-length palindrome
            l = i
            r = i

            while l >= 0 and r < n and s[l] == s[r]:
                if len(result) < r - l + 1:
                    result = s[l:r + 1]

                l = l - 1
                r = r + 1

            # Even-length palindrome
            l = i
            r = i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                if len(result) < r - l + 1:
                    result = s[l:r + 1]

                l = l - 1
                r = r + 1

        return result