class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        _map = {
            '}':'{', ']':'[',')':'('
        }
        for i in s:
            if i in '[({':
                stack.append(i)
            elif i in '])}':
                if stack != []:
                    if stack[-1] == _map[i]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        return stack == []
        