class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ops = '+-*/'
        _ops = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b),
        }
        stack = []
        for i in tokens:
            if i not in _ops:
                stack.append(i)
            else:
                val1 = int(stack[-2])
                val2 = int(stack[-1])
                new = _ops[i](val1,val2)
                # pop last 2 things    
                stack.pop(-1)
                stack.pop(-1)
                stack.append(new)
        
        return int(stack[0])