#                                       8.3
def make_shirt(text,r):
   a=f'Текст:"{text.title()}", размер:{r}'
   return a
text=str(input("Введите текст на футболке: "))
r=int(input("Введите размер футболки: "))
b=make_shirt(text,r)
print(b)