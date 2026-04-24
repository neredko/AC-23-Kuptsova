 #T6 Шифр Цезаря
print("Введите слово(только латинские буквы)")
word = input().strip()
print("Введите сдвиг(целое число от 1 до 10)")
sdv = int(input().strip())
al_low = "abcdefghijklmnopqrstuvwxyz"
al_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

if sdv < 1 or sdv > 10:
    print("Ошибка: сдвиг должен быть от 1 до 10")
else:
    for i in word:
        if 'a' <= i <= 'z':                  
            n_c = (ord(i) - ord('a') + sdv) % 26 + ord('a')
            result += chr(n_c)
        elif 'A' <= i <= 'Z':               
            n_c = (ord(i) - ord('A') + sdv) % 26 + ord('A')
            result += chr(n_c)
            
        else:
            print("Ошибка: можно вводить только латинские буквы!")
            result = ""   
            break        

    if result:
        print("Зашифрованное слово:", result)