class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        res = []
        l,r = 0,0
        
        while r < len(popped):
            res.append(pushed[l])
            
            
            while res and res[-1] == popped[r]:
                res.pop()
                r += 1
            
            if res and l == len(pushed)-1 and res[-1] != popped[r]:
                return False
            l += 1
            
        return True
