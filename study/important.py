# def complicated():
#     print('fuck uuu!!')

# KEY = 'fuckyou'

# if __name__ == '__main__':
#     print('I was being processed')

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, o):
        return Vector(self.a + o.a, self.b + o.b)

    def __str__(self):
        return '('+str(self.a)+', '+str(self.b)+')'

    def print(self):
        print(f'({self.a}, {self.b})')


v1 = Vector(5, 10)
v2 = Vector(1, 2)
v3 = v1 + v2
# v3.print()
print(str(v3))