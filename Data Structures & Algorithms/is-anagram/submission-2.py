class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        acc = []
        for i, word in enumerate([s, t]):
            d = {}
            for char in word:
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
            acc.append(d)
        
        return acc[0] == acc[1]