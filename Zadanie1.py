# W pliku rows.txt znajduje się tabela zawierająca liczby całkowite dla których
# trzeba policzyć sumę kontrolną.
# Twoim zadaniem jest dla każdego rzędu określić różnicę między największą
# wartością a najmniejszą wartością - suma kontrolna jest sumą wszystkich tych
# różnic.

file = open("rows.txt", "r+")
control_sum = 0
difference = []
for line in file:
    numbers = line.split()
    lowest_number = int(numbers[0])
    highest_number = int(numbers[0])
    for number in numbers:
        number = int(number)
        if number > highest_number:
            highest_number = number
        if number < lowest_number:
            lowest_number = number
    difference.append(highest_number - lowest_number)

for i in difference:
    control_sum += i
print("Suma kontrolna wynosi " + str(control_sum))
