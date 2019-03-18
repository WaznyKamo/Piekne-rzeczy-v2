# Proszę znaleźć ścieżkę z największą sumą elementów w "trójkącie".
# Przechodzić można tylko z góry na dół w lewo lub na dół w prawo. Każda liczba
# w trójkącie jest z zakresu od 10 do 99.
# Trójkąt jest w pliku zadanie_4_triangle_big.txt

file = open("zadanie_4_triangle_big.txt", "r")
data = []

# utworzenie listy zawierającej kolejne linie z pliku, które zawierają liczby (nie są puste)
for line in file:
    for i in line:
        if i.isdigit():
            data.append(line)
            break

# zamiana linii(kolejnych elementów listy) w listy składające się z liczb znajdujących się w pliku
# dane = [[lista_liczb_1_rzędu], [lista_liczb_2_rzędu], (...)]
for i in range(len(data)):
    data[i] = data[i].split()

# zamiana liczb zapisanych jako string na inty
for i in range(len(data)):
    for j in range(i+1):
        data[i][j] = int(data[i][j])

# rozpoczęcie dodawania liczb "od dołu", decydując która z liczb w ostatnim rzędzie daje większą sume sąsiadującej
# liczbie w rzędzie wyżej, na tej podstawie przyjmowanie wartości tych większych i zmniejszanie listy linia po linii
for i in range(len(data)-2, -1, -1):
    for j in range(i+1):
        if data[i+1][j] > data[i+1][j+1]:
            data[i][j] += data[i+1][j]
        else:
            data[i][j] += data[i + 1][j+1]

print('Najwyższa suma wynosi: {}'.format(data[0][0]))
