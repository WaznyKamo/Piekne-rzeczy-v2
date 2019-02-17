file = open("zadanie_4_triangle_big.txt", "r")
data = []

for line in file:
    for i in line:
        if i.isdigit():
            data.append(line)
            break

for i in range(len(data)):
    data[i] = data[i].split()

for i in range(len(data)):
    for j in range(i+1):
        data[i][j] = int(data[i][j])

for i in range(len(data)-2, -1, -1):
    for j in range(i+1):
        if data[i+1][j] > data[i+1][j+1]:
            data[i][j] += data[i+1][j]
        else:
            data[i][j] += data[i + 1][j+1]
print('Najwyższa suma wynosi: {}'.format(data[0][0]))
