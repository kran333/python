class Shapes:
    def __init__(self,lenght):
        self.lenght = lenght
        pass
    def area(self):
        return 0

class Square(Shapes):
    def area(self):
        return self.lenght * 2

obj = Square(10)
val = obj.area()
print val