class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
            x *= -1
        else:
            negative = False
        res = int((str(x)[::-1]))

        if res > 2**31-1 or res < -2**31:
            return 0
        else:
            if negative:
                return res*-1
            else:
                return res