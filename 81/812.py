class Stas:
    def __init__(self,n):
        self.n = n
    def caps(self):
        print ('>>>', self.n.upper())

n=str(input("Введите слово ---> "))
a = Stas(n)
a.caps()
