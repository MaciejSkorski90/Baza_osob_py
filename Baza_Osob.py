#-------------------------------------------------------------------------------
# Name:        lista_adresow_baza
# Purpose:
#
# Author:      Maciej Skórski
#
# Created:     23-12-2019
# Copyright:   Maciej Skórski 2019
# Licence:     -
#-------------------------------------------------------------------------------

lista_adresow = []

def dodaj_adres():
    print("dodaj")
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    uzytkownik = imie + " " + nazwisko
    lista_adresow.append(uzytkownik)

def kasuj_adres():
    print("kasuj")
    index = int(input("Podaj index: "))
    lista_adresow.remove(lista_adresow[index-1])

def wyswietl_dane():
    print("wyswietl")
    for index in range(len(lista_adresow)):
        print(f'{index+1}: {lista_adresow[index]}')

opcja = 1

while opcja != 0:
    print("1 - Dodaj imie i nazwisko")
    print("2 - Kasuj imie i nazwisko")
    print("3 - Wyswietl dane")
    print("0 - Koniec programu")
    opcja = int(input("Wybierz opcje: "))
    if opcja == 1:
        dodaj_adres()
    elif opcja == 2:
        kasuj_adres()
    elif opcja == 3:
        wyswietl_dane()
    elif opcja == 0:
        print("Koniec programu")
    else:
        print("Nie ma takiej opcji!")
