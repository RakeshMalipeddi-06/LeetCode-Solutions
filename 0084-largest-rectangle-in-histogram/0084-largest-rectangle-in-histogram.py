
class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]

            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1

            area = height * width
            max_area = max(max_area, area)

        return max_area
        