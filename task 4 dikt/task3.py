#task 3. Средний балл по словарю оценок

students = {
    "Анна": [5,4,5,4],
    "Борис": [3,3,4,5],
    "Вера": [5,5,5,4]
}

average_grades = {}

for name in students:         
    average_grades[name] = sum(students[name] ) / len(students[name] )  

print(average_grades)