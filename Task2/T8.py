#T8 Индикатор загрузки
import time
print("Загрузка: [] 0%", end='', flush=True)

for i in range(1, 11):
    time.sleep(1)  
    print(f"\rЗагрузка: [{'#' * i}] {i * 10}%", end='', flush=True)

print()