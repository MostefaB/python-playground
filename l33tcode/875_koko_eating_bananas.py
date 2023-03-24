import math
class Solution:
    def countPasses(self, k:int, piles:list[int]) -> int:
        passes = 0
        for val in piles:
            if val <= k:
                passes += 1
                # print(f"COUNTING PASSES: current_val:{val} requires {1} of passes using a speed of {k} passes/h ")
            else:
                if val % k == 0:
                    passes += val // k
                    # print(f"COUNTING PASSES: current_val:{val} requires {val // k} of passes using a speed of {k} passes/h ")
                else:
                    passes += (val // k) + 1
                    # print(f"COUNTING PASSES: current_val:{val} requires {(val // k) + 1} of passes using a speed of {k} passes/h ")
        return passes
    
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # n: piles of bananas
        # i-th pile: piles[i]
        # h: guards will come back in h hours
        # k: speed of eating (piles/h) -> we want the min speed

        max_piles = max(piles)
        n = len(piles)

        if h == n: return max_piles
        
        l, r = 1, max_piles

        while l <= r:
            middle = (r + l) // 2
            nb_passes = self.countPasses(middle,piles)
            # print(f"l:{l}, middle:{middle}, r:{r}, nb_passes:{nb_passes}, h:{h}")
            if nb_passes < h:
                r = middle - 1
            if nb_passes > h:
                l = middle + 1
            else:
                current_ans = middle
                r = middle -1

        return current_ans