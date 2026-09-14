class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)-1):
            if isinstance(arr[i+1],int):
                res.append(max([arr[j] for j in range(i+1, len(arr))]))
        res.append(-1)
        return res
            