from operator import add, sub, mul, truediv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": add, "-": sub, "*": mul, "/": truediv}
        operands = []

        for token in tokens:
            if token not in ops:
                operands.append(int(token))
            else:
                second = operands.pop()
                first = operands.pop()
                res = ops[token](first, second)
                operands.append(int(res))
        
        return operands.pop()