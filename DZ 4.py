import random

class Encryptor:
    def __init__(self, a, b):
        op = random.randint(0, 3)
        if op == 0:
            self.result = a + b
        elif op == 1:
            self.result = a - b
        elif op == 2:
            self.result = a * b
        else:
            self.result = a / b if b != 0 else 0

    def __str__(self):
        return str(self.result)

x = int(input())
y = int(input())
obj = Encryptor(x, y)
print(obj)
