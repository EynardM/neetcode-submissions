class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        acc = []
        for num in nums:
            if num not in acc:
                acc.append(num)
            else:
                return True
        return False