#Задача6
import random
zag = random.randint(1,100)
print("Я загадал число от 1 до 100. Попробуй угадать!")
chis = 0 
p = 0 
while chis != zag:
    try:
        chis = input()
        p += 1 
        if int(chis) > 100 or int(chis) < 1 :
            print("Диапазон числа от 1 до 100")
        if int(chis) < zag:
            print(f"Твой вариант: {chis}")
            print(f"Загаданное число больше")
        if int(chis) > zag:
            print(f"Твой вариант: {chis}")
            print(f"Загаданное число меньше")
        if int(chis) == zag:
            print(f"Твой вариант: {chis}")
            print(f"Поздравляю! Ты угадал число {chis} за {p} попытки! ")
    except:
        print(f"Твой вариант: {chis}")
        print(f"Ошибка! Введите целое число!")
        
