class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def square(self):
        print(f'Square: {self.width*self.height}')
rect1 = Rectangle(2,3)
rect1.square()