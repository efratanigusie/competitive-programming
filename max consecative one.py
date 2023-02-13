class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxx = max(0, k)
        i, j = 0, 0
        while j < len(nums):

            if k < 1:
                # print(nums[i:j], k)
                if nums[j] == 1:
                    j += 1
                    maxx = max(maxx, j-i)
                    continue
                if nums[i] == 0:
                    k += 1
                i += 1
            else:
                if nums[j] == 0:
                    k -= 1
                j += 1
            maxx = max(maxx, j-i)
        return (maxx)
