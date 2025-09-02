class Solution(object):
    def splitArray(self, nums, k):
        l, r = max(nums), sum(nums)
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2
            ansMax = self.func(mid, k, nums)
            if ansMax > 0:
                ans = ansMax
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def func(self, mid, k, nums):
        count, total, maxVal = 0, 0, -1
        for el in nums:
            total += el
            if total > mid:
                count += 1
                maxVal = max(maxVal, total - el)
                total = el
        if total > 0:
            count += 1
        maxVal = max(maxVal, total)
        return maxVal if count <= k else -1