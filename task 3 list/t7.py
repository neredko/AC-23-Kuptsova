#task 7. Транспонирование матрицы

matrix = [[1,2,3],[4,5,6]]

rows = len(matrix) # строки
cols = len(matrix[0]) # столбцы

transposed = []


for c in range(cols):
    new_row = [] # проходим по столбцу

    for r in range(rows):
        new_row.append(matrix[r][c]) # проходим по строке
    transposed.append(new_row)

print(transposed)  # [[1,4],[2,5],[3,6]]
