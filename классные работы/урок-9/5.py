prompt = "\nПривет! Меня зовут бот, я хочу узнать о тебе все:"
prompt += "\nВведите “out” для завершения программы"
 
active = True
while active:
  message = input(prompt)
  if message == "out":
    active = False
  else:
    print(message)