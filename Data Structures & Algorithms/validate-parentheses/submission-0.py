class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesMap = {'}' : '{', ')' : '(', ']' : '['}

        for c in s:
            if c in parenthesesMap:
                if stack and stack[-1] == parenthesesMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True