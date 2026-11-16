class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def add(a,b):
            return a + b
        
        def subtract(a,b):
            return a - b
        
        def divide(a, b):
            return int(a / b)
        
        def multiply(a, b):
            return a * b
        
        operations = {
            "+" : add,
            "-" : subtract,
            "/" : divide,
            "*" : multiply
        }

        for val in tokens:
            if val in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[val](a,b))
            else:
                stack.append(int(val))
        
        return stack.pop()