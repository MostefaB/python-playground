class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = False
        length_s1 = len(s1) # Size of the window
        length_s2 = len(s2)

        counter_s1 = dict()
        
        for c in s1:
            counter_s1[c] = 1 + counter_s1.get(c,0)

        l, r = 0, length_s1 - 1
        while r < length_s2:
            counter_s2 = dict()
            for c in s2[l:r+1]:
                counter_s2[c] = 1 + counter_s2.get(c,0)
            if counter_s2 == counter_s1:
                return True
            else:
                l += 1
                r += 1
        return res

            