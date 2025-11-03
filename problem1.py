class Calculator:
    def __init__(self,a,d,operation):
        self.a=a
        self.b=b
        self.operation=operation.lower()
    def calculate(self):
        if self.operation=='addition':
            return self.a+self.b
        elif self.operation=='subtracion':
            return self.a-self.b
        elif self.operation=='multiplication':
            return self.a*self.b
        elif self.operation=='division':
            if self.b==0:
                return 'error! division by zero:'
            return self.a/self.b
        else:
            return 'invalid operation'
a=int(input('enter the first number(a):'))
b=int(input('enter second number(b)'))
operation=input('enter operation(Addition/Subtraction/Multiplication/Division):')
calc=Calculator(a,b,operation)
result=calc.calculate()
print(result)

1