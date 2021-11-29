#                                       8.4
def make_shirt(text,r):
   print(f'Текст:"I love Python", размер:L')
   a=f'Текст:"{text.title()}", размер:{r}'
   return a
text=str(input("Введите текст на футболке: "))
r=int(input("Введите размер футболки: "))
b=make_shirt(text,r)
print(b)