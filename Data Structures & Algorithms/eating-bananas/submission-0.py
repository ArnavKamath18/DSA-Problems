import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kworks(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile/k)
            if total <= h:
                return True
            else:
                return False

        l = 1
        r = max(piles)

        while l <= r:
            m = (l+r)//2

            if kworks(m):
                r = m-1
            else:
                l = m+1
        
        if kworks(l):
            return l
        else:
            return r