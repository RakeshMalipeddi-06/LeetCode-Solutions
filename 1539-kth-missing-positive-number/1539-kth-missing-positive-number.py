class Solution:
    def findKthPositive(self, arr, k):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            # Missing numbers before arr[mid]
            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k