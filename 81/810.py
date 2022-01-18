class Rectangle:
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def plosha(self):
        return self.a * self.b
 
a = Rectangle(2, 3)
print(a.plosha())

