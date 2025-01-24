print("Pažaiskime X 0 žaidimą!")
lenta = [" "] * 9
zaidejas = "X"

while True:
    print(f"{lenta[0]}|{lenta[1]}|{lenta[2]}\n-+-+-\n"
          f"{lenta[3]}|{lenta[4]}|{lenta[5]}\n-+-+-\n"
          f"{lenta[6]}|{lenta[7]}|{lenta[8]}")

    ejimas = input("Kur norėtumete eiti? (Rinkites skaičių nuo 1 iki 9): \n")
    if not ejimas.isdigit():
        print("Bloga įvestis. Įveskite skaičių nuo 1 iki 9!")
        continue
    elif not int(ejimas):
        print("Bloga įvestis. Įveskite skaičių nuo 1 iki 9!")
        continue
    elif int(ejimas) < 1 or int(ejimas) > 9:
        print("Bloga įvestis. Įveskite skaičių nuo 1 iki 9!")
        continue

    ejimas = int(ejimas) - 1

    if lenta[ejimas] == " ":
        lenta[ejimas] = zaidejas
    else:
        print("Langelis jau užimtas. Rinkites kita langelį")
        continue

    if (lenta[0] == lenta[1] == lenta[2] == zaidejas or
        lenta[3] == lenta[4] == lenta[5] == zaidejas or
        lenta[6] == lenta[7] == lenta[8] == zaidejas or
        lenta[0] == lenta[3] == lenta[6] == zaidejas or
        lenta[1] == lenta[4] == lenta[7] == zaidejas or
        lenta[2] == lenta[5] == lenta[8] == zaidejas or
        lenta[0] == lenta[4] == lenta[8] == zaidejas or
        lenta[2] == lenta[4] == lenta[6] == zaidejas):
        print(f"{lenta[0]}|{lenta[1]}|{lenta[2]}\n-+-+-\n"
              f"{lenta[3]}|{lenta[4]}|{lenta[5]}\n-+-+-\n"
              f"{lenta[6]}|{lenta[7]}|{lenta[8]}")
        print(f"Žaidėjas {zaidejas} laimėjo!")
        break

    if " " not in lenta:
        print("Lygesios!")
        break

    if zaidejas == "X":
        zaidejas = "O"
    else:
        zaidejas = "X"
