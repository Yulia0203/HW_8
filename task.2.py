# Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.


import random
rows = columns = 5
sumDiagonal = 0
count = 0
numbers = [0] * rows 
beautyText = 1

for i in range(len(numbers)):
    numbers[i] = list(0 for _ in range(columns))

for i in range(rows):
    for j in range(columns):
        current_number = random.randint(0,30)
        numbers[i][j] = random.randint(0,30)
        if i == j:
            sumDiagonal += numbers[i][j]
        
print("\nKвадратная матрица, заполненная случайными числами")
for row in numbers:
    print(row)

print(f'\nсуммa главной диагонали: {sumDiagonal}')  

for i in range(rows):
    for j in range(columns):
        count += numbers[i][j]
    if count > sumDiagonal:
        print(f'Суума элементов {beautyText} строки: {count} - больше суммы диагонали')
    count = 0
    beautyText += 1