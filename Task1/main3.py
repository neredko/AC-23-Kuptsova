#Задача3
print("Введите строку:")
a = str(input())
summ = 0
#strr = "а,е,ё,и,о,у,ы,э,ы,я"
strr = "eyuioa"
for i in a:
    for j in strr:
        if i == j:
            summ += 1
print(summ)
    
    