#Задача3 Калькулятор
print("Введите первое число")
one_ch = int(input())
print("Введите операцию(+,-,*,/)")
operation = str(input())
print("Введите второе число")
two_ch = int(input())

if operation == "+":
    print(f"{one_ch}{operation}{two_ch}={one_ch + two_ch}")
elif operation == "-":
    print(f"{one_ch}{operation}{two_ch}={one_ch - two_ch}")
elif operation == "*":
    print(f"{one_ch}{operation}{two_ch}={one_ch * two_ch}")
elif operation == "/" and two_ch == 0:
    print("Ошибка: деление на ноль")
elif operation == "/" :
    print(f"{one_ch}{operation}{two_ch}={one_ch / two_ch}")
else:
    print("Неизвестная операция")