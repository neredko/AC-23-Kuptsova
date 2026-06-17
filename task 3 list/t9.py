#task 9. Сортировка таблицы по нескольким столбцам

table = [
    ["B", 100, 4.5],
    ["A", 100, 4.5],
    ["C", 50, 5.0],
    ["D", 100, 5.0],
]

def sort_key(row):
    return (row[1], -row[2], row[0])

sorted_table = sorted(table, key=sort_key)

print(sorted_table) # [['C', 50, 5.0], ['D', 100, 5.0], ['A', 100, 4.5], ['B', 100, 4.5]]

