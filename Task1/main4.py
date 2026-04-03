#Задача4
print("Введите верхнюю границу")
n = int(input())
for n in range(2, n + 1):
    is_prime = True
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n)