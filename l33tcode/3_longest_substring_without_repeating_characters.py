# 3. Longest Substring Without Repeating Characters
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We need a hashSet
        hash_set = set()
        ans = 0

        l = 0
        for r in range(len(s)):
            while s[r] in hash_set:
                # Remove the left side of the sliding window
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            ans = max(ans, r - l + 1)
        return ans



                

                

            




            
            


             
        





s = "pwwkew"
print(f" --- ANSWER: {Solution().lengthOfLongestSubstring(s)}")