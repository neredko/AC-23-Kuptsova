#task 7. Проверка вложенности (является ли один словарь подмножеством другого)

small = {"a":1,"c":3}
big = {"a":1,"b":2,"c":3}

is_subset = True

for i in small:

    if i not in big or big[i] != small[i]:
        is_subset = False
        break

print(is_subset) 