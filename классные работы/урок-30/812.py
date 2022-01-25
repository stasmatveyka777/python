class UpperTitle():
    def __init__(self,string):
        self.string = string
    def strUppertitle(self):
        a = ""
        for i in self.string:
            a+=str(i).title()
        print(a)
text = UpperTitle('python')
text.strUppertitle()