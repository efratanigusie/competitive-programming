class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res, firstLen_max, secondLen_max = nums[firstLen + secondLen - 1],              nums        [firstLen - 1], nums[secondLen - 1]
        for i in range(firstLen + secondLen, len(nums)):
            firstLen_max = max(firstLen_max, nums[i - secondLen] - nums[i - firstLen - secondLen])
            secondLen_max = max(secondLen_max, nums[i - firstLen] - nums[i - firstLen - secondLen])
            res = max(res, firstLen_max + nums[i] - nums[i - secondLen], secondLen_max + nums[i] - nums[i - firstLen])
        return res
