class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(n2, n1, op):
            if op == "+":
                return n1 + n2
            elif op == "-":
                return n1 - n2
            elif op == "*":
                return n1 * n2
            elif op == "/":
                return int(n1 / n2)

        ops = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in ops:
                a,b = stack.pop(), stack.pop()
                res = calc(a, b, token)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack.pop()

