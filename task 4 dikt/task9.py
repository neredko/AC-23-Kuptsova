#task 9. Группировка слов по первой букве

words = ["Анна","арбуз","Борис","банюк","Вера","арфа","Белка"]

groups = {}  

for word in words:

    first = word[0].upper()   
    

    if first not in groups:
        groups[first] = [word]

    else:
        groups[first].append(word)   

print(groups)