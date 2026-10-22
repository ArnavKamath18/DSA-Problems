class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        candidates = []

        for num in nums:
            if num not in seen and num not in candidates:
                candidates.append(num)
            elif num not in seen:
                candidates.remove(num)
                seen.append(num)
        
        return candidates[-1]