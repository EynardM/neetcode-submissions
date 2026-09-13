class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = [num for num in nums if num != val]
        nums[:] = tmp
        return len(nums)