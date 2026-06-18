#task 8. Построение вложенного словаря из списка кортежей

data = [
    ("фрукты","яблоки",10),
    ("фрукты","груши",5),
    ("овощи","морковь",7),
    ("фрукты","яблоки",12),  
    ("овощи","свёкла",4)
]

nested = {}  

for category, subcategory, value in data:

    if category not in nested:
        nested[category] = {}
    

    nested[category][subcategory] = value

print(nested)
