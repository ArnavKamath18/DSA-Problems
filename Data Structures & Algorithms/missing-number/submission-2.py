class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = 0
        nums.sort()

        for num in nums:
            if num != target:
                return target
            target += 1

        return target