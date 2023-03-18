class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        else:
            countS, countT = {}, {}
            for c in s:
                countS[c] = 1 + countS.get(c, 0)
            for c in t:
                countT[c] = 1 + countT.get(c, 0)
        return countS == countT
