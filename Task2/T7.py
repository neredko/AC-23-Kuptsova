#T7 Характеристики числа
print("Введите целое положительное число")
intt = input()
summ=0
if intt.isdigit(): 
    if int(intt) < 0:
        print("Ошибка: введено отрицательно число")
    elif int(intt) == 0:
        print("Количество цифр в числе: 1")
        print("Сумма всех цифр числа: 0")
        print("Палиндром: да")
    else: 
        if "5" in str(intt):
            five = "цифра 5 найдена"
        else:
            five = "цифра 5 не найдена"
        if intt == intt[::-1]:
            pl = "да"
        else: 
            pl = "нет"
        for i in intt:
            summ += int(i) 
        print(f"Сумма всех цифр числа: {summ}, количество цифр в числе: {len(intt)}, {five},палиндром: {pl} ")
else: 
    print("Ошибка. Введены символы, которые не являются цифрами")
        