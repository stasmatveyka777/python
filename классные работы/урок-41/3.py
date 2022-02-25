gre_score = int(input("Введите текущий лимит: "))
per_grad = int(input("Введите кредитный рейтинг: "))

if per_grad > 70:
        if gre_score > 150:
                print("Поздравляем, вам выдан кредит")
else:
    print("Извините, вы не имеете права на кредит")
