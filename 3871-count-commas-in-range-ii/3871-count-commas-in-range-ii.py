class Solution(object):
    def countCommas(self, n):

        answer = 0
        start = 1000
        commas = 1

        while start <= n:

            end = min(n, start * 1000 - 1)

            count = end - start + 1

            answer += count * commas

            start *= 1000
            commas += 1

        return answer
        