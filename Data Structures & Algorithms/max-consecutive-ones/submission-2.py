class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cpt = 0

        for num in nums:
            cpt = cpt + 1 if num else 0
            res = max(res, cpt)

        return res

