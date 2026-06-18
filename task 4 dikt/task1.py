#task 1. Слияние двух списков в словарь

keys = ["имя","возраст","город"]
values =["Анна","25","Москва"]

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]
    
print(result)