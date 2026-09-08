class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        acc = []
        for num in nums:
            if num in acc:
                return True
            else : 
                acc.append(num)
        return False