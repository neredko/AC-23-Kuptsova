#task 6. Безопасное удаление нескольких ключей

data = {"a": 1,"b": 2,"c": 3,"d": 4}
to_remove = ["b","e","c"]   

for i in to_remove:

    if i in data:         
        del data[i]        

print(data)  