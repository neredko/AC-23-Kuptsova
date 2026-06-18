#task 10. "Перекличка" – кто не сдал

students = {
    "Анна":True,
    "Борис":False,
    "Вера":True,
    "Арфа":False
}

all_names = ["Анна","Борис","Вера","Глеб","Диана","Елена"]

absent = []   #отсутствующие
failed = []   #должники

for name in all_names:

    if name in students:           

        if students[name] == False:   
            failed.append(name)
            
    else:                        
        absent.append(name)

print("Отсутствуют:", absent)   
print("Не сдали:", failed)     