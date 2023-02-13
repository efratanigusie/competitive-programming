class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        summation = 0
        cur = 0
        myDict = {0:1}
        for n in nums:
            cur+=n
            dif = cur-k
            summation+= myDict.get(dif,0)
            myDict[cur] = myDict.get(cur,0) + 1
        return summation
