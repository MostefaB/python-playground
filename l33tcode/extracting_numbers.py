class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        ans = 0
        i = 0
        j = 0
        numbers = []
        
        while i < len(A):
            print(f"i:{i}, j:{j}, numbers:{numbers}")
            # Check if number or char
            if ord(A[i]) - ord('a') >= 0:
                i += 1
                j += 1
                # continue
            else:
                # Move forward to parse the whole number
                while ord(A[j]) - ord('a') < 0 and j < len(A):
                    j +=1
                    if j == len(A):
                        break
                
                # if j == len(A): 
                #     print(f"Appending: {A[i:]} to {numbers}")
                #     numbers.append(A[i:])


                numbers.append(A[i:j])
                i = j
                
        for num in numbers:
            ans += int(num)
        print(f"Extracted numbers: {numbers}")
        print(f" --- ANSWER = {ans} --- ")
        return ans

# ret = Solution().solve("48n78hx95xur5")