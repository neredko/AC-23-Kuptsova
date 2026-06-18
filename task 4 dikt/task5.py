#task 5. Инвертирование словаря с повторяющимися значениями

original = {
    "Анна": "Python",
    "Борис": "Java",
    "Вера": "Python",
    "Глеб": "C++",
    "Даша": "Java"
}

inverted = {}

for i in original:

    language = original[i]

    if language in inverted:
        inverted[language].append(i)

    else:
        inverted[language] = [i]

print(inverted)