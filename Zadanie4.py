import random
# 1 - Kamień
# 2 - Papier
# 3 - Nożyce

# liczniki wygranych, przegranych i remisów
win_count = 0
lose_count = 0
draw_count = 0


# funkcja określająca czy grać dalej
def continue_game():
    game_choice = input("Czy grać dalej? \n T - Tak \n N - Nie \n")
    if game_choice == "T":
        return 1
    elif game_choice == "N":
        return 2
    else:
        return 3


while True:
    choice = input("Wybierz: \n K - kamien \n P - papier \n N - nożyce \n")
    enemy = random.randint(1, 3)
    if choice == "K":
        if enemy == 1:
            print("Przeciwnik wybrał kamień")
            print("Remis")
            draw_count +=1
        elif enemy == 2:
            print("Przeciwnik wybrał papier")
            print("Przegrałeś! Spróbuj ponownie.")
            lose_count += 1
        elif enemy == 3:
            print("Przeciwnik wybrał nożyce")
            print("Gratulacje, wygrałeś!")
            win_count += 1
    elif choice == "P":
        if enemy == 1:
            print("Przeciwnik wybrał kamień")
            print("Gratulacje, wygrałeś!")
            win_count += 1
        elif enemy == 2:
            print("Przeciwnik wybrał papier")
            print("Remis")
            draw_count += 1
        elif enemy == 3:
            print("Przeciwnik wybrał nożyce")
            print("Przegrałeś! Spróbuj ponownie.")
            lose_count += 1
    elif choice == "N":
        if enemy == 1:
            print("Przeciwnik wybrał kamień")
            print("Przegrałeś! Spróbuj ponownie.")
            lose_count += 1
        elif enemy == 2:
            print("Przeciwnik wybrał papier")
            print("Remis")
            draw_count += 1
        elif enemy == 3:
            print("Przeciwnik wybrał nożyce")
            print("Gratulacje, wygrałeś!")
            win_count += 1
    else:
        print("Podano błędną wartość")

    i = continue_game()
    if i == 1:
        pass
    elif i == 2:
        break
    else:
        continue_game()

    print("Liczba wygranych: {0} \n"
          "Liczba przegranych: {1} \n"
          "Liczba remisów: {2} \n".format(win_count, lose_count, draw_count))
