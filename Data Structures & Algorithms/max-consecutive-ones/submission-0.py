class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        acc = []
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                acc.append(tmp)
                tmp = 0
            else:
                tmp += 1
        acc.append(tmp)
        
        return max(acc)