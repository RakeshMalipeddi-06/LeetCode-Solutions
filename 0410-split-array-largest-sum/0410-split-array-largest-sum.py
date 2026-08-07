class Solution:
    def splitArray(self, nums, k):

        # Search Space
        left = max(nums)
        right = sum(nums)
        ans = right

        while left <= right:

            mid = (left + right) // 2

            # Count subarrays required
            subarrays = self.countSubarrays(nums, mid)

            if subarrays <= k:
                ans = mid
                right = mid - 1      # Try smaller largest sum
            else:
                left = mid + 1       # Increase largest sum

        return ans

    # Helper Function
    def countSubarrays(self, nums, limit):

        subarrays = 1
        currentSum = 0

        for num in nums:

            if currentSum + num <= limit:
                currentSum += num
            else:
                subarrays += 1
                currentSum = num

        return subarrays



        