#task 4. Объединение словарей с суммированием

d1 = {"яблоки":10,"груши":5,"бананы":3}
d2 = {"груши":7,"бананы":4,"апельсины":8}

merged = {}

for i in d1:
    merged[i] = d1[i] #копирование d1

#добавление d2
for i in d2:

    if i in merged:
        merged[i] += d2[i]

    else:
        merged[i] = d2[i]

print(merged)