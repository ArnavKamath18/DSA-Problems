class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        temp = n

        while temp != 1:
            summ = 0
            if temp in seen:
                return False
            else:
                seen.add(temp)
            while temp > 0:
                summ += (temp%10)**2
                temp //= 10
            temp = summ

        return True