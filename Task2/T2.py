#Задача2 Процент выполнения теста 
print("Введите процент выполнения теста: целое число от 0 до 100")
procent = int(input())
if 90 <= procent <= 100:
    print("А(Отлично)")
elif 75 <= procent <= 89:
    print("В(Хорошо)")
elif 60 <= procent <= 74:
    print("С(Удовлетворительно)")
elif 50 <= procent <= 59:
    print("D(Неудовлетворительно)")
elif 0 <= procent <= 49:
    print("F(Провал)")
else: 
    print("Ошибка, введите число от 0 до 100")