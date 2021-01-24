from random import randint



Suit = ["Gunting", "Batu", "Kertas"]

komputer = Suit[randint(0,2)]

pemain = False

while pemain == False:
    pemain = input("Gunting, Batu, Kertas ? : ")
    if pemain == komputer:
        print("Seri!")
    elif pemain == "Batu":
        if komputer == "Kertas":
            print("Kamu Kalah!", komputer, "membungkus", pemain)
        else:
            print("Kamu Menang!", pemain, "menghancurkan", komputer)
    elif pemain == "Kertas":
        if komputer == "Gunting":
            print("Kamu Kalah!", komputer, "memotong", pemain)
        else:
            print("Kamu Menang!", pemain, "membungkus", komputer)
    elif pemain == "Gunting":
        if komputer == "Batu":
            print("Kamu Kalah!", komputer, "menghancurkan", pemain)
        else:
            print("Kamu Menang!", pemain, "momotong", komputer)
    else:
        print("Pilihan yang kamu masukan salah...")

  

    pemain = False
komputer = Suit[randint(0,2)]