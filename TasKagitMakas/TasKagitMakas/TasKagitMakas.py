import random
from typing import ParamSpecArgs
secenek = "rock","paper","scissors"
rock = secenek[0] 
paper = secenek[1]
scissors = secenek[2]
print("cikmak icin lutfen e tusuna basiniz")
while True:
    print("lutfen bir secenek seciniz: ")
    secim = input(secenek)
    compChoice = random.choice.secenek
    if secim == rock :
        if compChoice == paper:
            print("bilgisayarin secimi tas oyunu kazandiniz")
        elif compChoice == scissors:
            print("bilgisayarin secimi tas oyunu kaybettiniz")
        else :
            print("bilgisayarin secimi tas oyun berabere")
    elif secim == paper:
        if(compChoice == rock):
            print("bilgisayarin secimi kagit oyunu kaybettiniz")
        elif(compChoice == paper):
            print("bilgisayarin secimi kagit oyun berabere")
        else:
            print("bilgisayarin secimi kagit oyunu kazandiniz")
    else:
        if compChoice == rock:
            print("bilgisayarin secimi kagit oyunu kaybettiniz")
        elif(compChoice == paper):
            print("bilgisayarin secimi kagit oyun berabere")
        else:
            print("bilgisayarin secimi kagit oyunu kazandiniz")
    if secim == "e":
        break;