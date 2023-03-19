class Solution:
    def isValid(self, s:str) -> bool:
        stack = [] # Use stack data structure represented as a list in Python
        # Use re represent the mirrored item, keys are closing items, values are opening items
        dict = {"]":"[", "}":"{", ")":"("}

        # Loop through the input `s`
        for char in s:
            
            # Test whether the item is an opening one
            if char in dict.values():
                # Add it to the stack
                stack.append(char)
            
            # Test whether the item is a closing one and is supported (e.g <> are not supported)
            elif char in dict.keys():
                # If the stack is empty (e.g. input string starts with `)`, then we know it is invalid) or 
                
                if stack == [] or \
                    dict[char] != stack.pop():
                    return False
            # Test whether the char is not supported
            else:
                return False
        # stack should be empty if all opening items have been properly closed (poped)
        return stack == []