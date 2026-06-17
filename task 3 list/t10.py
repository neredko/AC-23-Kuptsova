#task 10. Кольцевой буфер на списке (без класса) 

capacity = 3
actions = [1, 2, 3, 4, 5]

buffer = []  

for i in actions:
    
    if len(buffer) < capacity:
        buffer.append(i)

    else:
        buffer.pop(0)   
        buffer.append(i)  #если кончилось место, удаляем 0 элемент и добавляем новый в конец
    
    print(buffer)
