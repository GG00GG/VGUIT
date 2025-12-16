# Вариант 5

input_file = "Zolotarev_Ilya_Ruslanovich_U-254_vvod.txt"
output_file = "Zolotarev_Ilya_Ruslanovich_U-254_vivod.txt"

with open(input_file, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]
  
# 1
n1, m1 = map(int, lines[0].split())
matrix1 = []
index = 1
for i in range(n1):
    row = list(map(int, lines[index].split()))
    matrix1.append(row)
    index += 1

for row in matrix1:
    row.sort()

# 2
n2 = int(lines[index])
index += 1
matrix2 = []
for i in range(n2):
    row = list(map(int, lines[index].split()))
    matrix2.append(row)
    index += 1

for i in range(n2):
    min_val = min(matrix2[i])
    for j in range(n2):
        if matrix2[i][j] == min_val:
            if min_val % 2 == 0:
                matrix2[i][j] = 0
            else:
                matrix2[i][j] = 1
            break

with open(output_file, 'w', encoding='utf-8') as f:
    for row in matrix1:
        f.write(' '.join(map(str, row)) + '\n')
    
    f.write('\n')
    
    for row in matrix2:
        f.write(' '.join(map(str, row)) + '\n')
