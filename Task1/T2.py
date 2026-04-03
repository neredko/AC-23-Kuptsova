#Задача 2: Таблица умножения для числа
print("Введите число:")
a = int(input())
for i in range(1,11):
    ymn = i*a
    print(f"{a}*{i} = {ymn} ")
