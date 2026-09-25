class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        n=0
        stack=[]
        sign=1

        for ch in s:
            if ch.isdigit():
                n=n*10+int(ch)
            elif ch=="+":
                result+=sign*n
                sign=+1
                n=0
            elif ch=="-":
                result+=sign*n
                sign=-1
                n=0
            elif ch=="(":
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1
                n=0
            elif ch==")":
                result+=sign*n
                n=0
                prevsign=stack.pop()
                prevres=stack.pop()
                result=prevres+prevsign*result
        result+=sign*n
        return result


            