class Solution:
    
    def getAllPossibilities(
            self, currentOpenBrackets:int,
            currentClosedBrackets:int, 
            limit:int,
            stack:list[str],
            possibilities:list[str]) -> list[str]:
        # Check whether we hit our goal n open and closed ()
        # Use a stack to store each possible combination
        if currentOpenBrackets == currentClosedBrackets == limit:
            possibilities.append("".join(stack))
            # print(f"to_return:{possibilities} and stack:{stack}")
            return possibilities
        # Check if we still can add open brackets
        if currentOpenBrackets < limit:
            stack.append("(")
            # print(f"stack after appending `(`: {stack}")
            # re-evaluate all possibilities given that we made this choice
            self.getAllPossibilities(currentOpenBrackets + 1, currentClosedBrackets, limit, stack,possibilities)
            # Undo 
            stack.pop()
            print(f"stack after poping `(`: {stack}")
        
        # Check if we still can add closed brackets
        if currentClosedBrackets < currentOpenBrackets:
            stack.append(")")
            # print(f"stack after appending `)`: {stack}")
            # re-evaluate all possibilities given that we made this choice
            self.getAllPossibilities(currentOpenBrackets, currentClosedBrackets + 1, limit, stack,possibilities)
            # Undo 
            stack.pop()
            # print(f"stack after poping `)`: {stack}")

    
    def generateParenthesis(self, n: int) -> list[str]:
        stack = list()
        possibilities = list()
        self.getAllPossibilities(0,0,n,stack,possibilities)
        return possibilities
