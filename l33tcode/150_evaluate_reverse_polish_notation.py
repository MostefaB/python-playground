class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        print(tokens)
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        ans = 0
        for i, val in enumerate(tokens):
            stack.append(val)
            if val in ['+', '-', '*', '/']:
                operation = stack.pop()
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                if val == '+':
                    ans = operand_1 + operand_2
                elif val == '*':
                    ans = operand_1 * operand_2
                elif val == '-':
                    ans = operand_1 - operand_2
                elif val == '/':
                    ans = operand_1 / operand_2
                stack.append(ans)
        return int(stack[0])