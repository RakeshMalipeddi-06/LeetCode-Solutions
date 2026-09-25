class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[-1]
        max_area=0

        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    l=i-stack[-1]
                    max_area=max(max_area,l)
        
        return max_area

        