class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed)%2:
            return []

        changed.sort()

        i = 1
        j = 0
        k = 0
        while i<len(changed):

            if changed[i]%2==0:

                while j<i-1 and changed[j]<(changed[i]//2):
                    j+=1

                if changed[j]==(changed[i]//2):
                    changed[ k ] , changed[ j ] = changed[ j ] , changed[ k ]
                    k+=1
                    j+=1
                    changed[i]=-1
            i+=1

        if k==len(changed)//2:
            return changed[:k]
        return []
