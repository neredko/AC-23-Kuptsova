#task 2. Частотный словарь символов

s = "программирование"

freq = {}

for i in s:
    
    if i in freq:
        freq[i] += 1
        
    else:
        freq[i] = 1

print(freq)
