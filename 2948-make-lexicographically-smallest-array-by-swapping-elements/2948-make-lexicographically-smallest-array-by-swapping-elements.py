class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted((value, index) for index, value in enumerate(nums))

        start = 0
        ans = [0] * len(nums)

        for i in range(1, len(arr) + 1):
            if i == len(arr) or arr[i][0] - arr[i - 1][0] > limit:

                group = arr[start:i]

                values = sorted(value for value, index in group)
                indices = sorted(index for value, index in group)

                for j in range(len(group)):
                    ans[indices[j]] = values[j]

                start = i

        return ans

        