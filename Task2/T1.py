# Задача1 Месяца
print("Введите число от 1 до 12")
vvod = int(input())
if vvod in [12,1,2]:
    print("Зима")
elif vvod in[3,4,5]:
    print("Весна")
elif vvod in[6,7,8]:
    print("Лето")
elif vvod in[9,10,11]:
    print("Осень")
elif vvod < 0 or vvod > 12:
    print("Ошибка: Введите число от 1 до 12")
