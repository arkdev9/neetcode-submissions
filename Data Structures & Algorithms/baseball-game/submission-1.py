class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                op1 = int(stack[-1])
                op2 = int(stack[-2])
                stack.append(op1 + op2)

            elif op == "C":
                stack.pop()

            elif op == "D":
                stack.append(int(stack[-1]) * 2)
            
            else:
                stack.append(op)
        
        res = 0

        for i in stack:
            res += int(i)

        return res
