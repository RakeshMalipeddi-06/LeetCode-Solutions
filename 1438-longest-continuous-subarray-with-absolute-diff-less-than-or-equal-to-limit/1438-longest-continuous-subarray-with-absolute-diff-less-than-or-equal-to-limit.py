from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        max_dq = deque()  # Indices in decreasing value order
        min_dq = deque()  # Indices in increasing value order

        left = 0
        result = 0

        for right in range(len(nums)):

            # Maintain maximum deque
            while max_dq and nums[max_dq[-1]] < nums[right]:
                max_dq.pop()
            max_dq.append(right)

            # Maintain minimum deque
            while min_dq and nums[min_dq[-1]] > nums[right]:
                min_dq.pop()
            min_dq.append(right)

            # Shrink window while invalid
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                if max_dq[0] == left:
                    max_dq.popleft()

                if min_dq[0] == left:
                    min_dq.popleft()

                left += 1

            # Update longest valid window
            result = max(result, right - left + 1)

        return result
        