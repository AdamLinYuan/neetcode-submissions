class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calc(num1, num2, sign):
            num1, num2 = int(num1), int(num2)
            if sign == '+':
                return num1 + num2
            elif sign == '-':
                return num1 - num2
            elif sign == '*':
                return num1 * num2
            elif sign == '/':
                return num1 / num2

        stack = []
        signs = ['+', '-', '*', '/']
        res = 0
        for t in tokens:
            if t in signs:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(calc(num1, num2, t))
            else:
                stack.append(t)
            
        return int(stack[0])      