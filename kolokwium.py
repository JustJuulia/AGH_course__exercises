import math
def czy_liczba_zlozona(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return True
        return False
#  pseudokod z poolecenia
def algorytm(n):
    wynik = 0
    x = 1
    for i in range(1,n+1):
        x = x*i
        j = 1
        while x >= j:
            wynik = wynik + 1
            j = j*2
    print(x,j,wynik)

def nww_z_wartosci_enharmonicznej(dzwiek1, dzwiek2):
    def obliczenie_bazy(baza):
        if baza == 'C':
            baza = 0
        elif baza == 'D':
            baza = 2
        elif baza == 'E':
            baza = 4
        elif baza == 'F':
            baza = 5
        elif baza == 'G':
            baza = 7
        elif baza == 'A':
            baza = 9
        elif baza == 'B':
            baza = 11
        return baza
    def obliczanie_calkowitej_wartosci(dzwiek, baza):
        if len(dzwiek) == 2:
            # baza i oktawa
            oktawa = int(dzwiek[1])
            wynik_dzwiek = baza + 12 * oktawa
        elif len(dzwiek) == 3:
            # baza modyfikatopr oktawa
            if dzwiek[1] == '#':
                modyfikator = 1
            elif dzwiek[1] == 'b':
                modyfikator = -1
            oktawa = int(dzwiek[2])
            wynik_dzwiek = baza + modyfikator + (12 * oktawa)
        return wynik_dzwiek
    def obliczanie_nww(liczba1,liczba2):
        if liczba1 < liczba2:
            liczba1, liczba2 = liczba2, liczba1
        temp = liczba1
        while temp % liczba2 != 0:
            temp = temp + liczba1
        return temp
    # wartosckoncowa = baza + modyfikator + (12*oktawa)
    #C=0 D=2 E=4 F=5 G=7 A=9 B=11
    # modyfikatory #=+1 b=-1
    dzwiek1 = str(dzwiek1)
    dzwiek2 = str(dzwiek2)
    baza1 = dzwiek1[0]
    baza1 = obliczenie_bazy(baza1)
    baza2 = dzwiek2[0]
    baza2 = obliczenie_bazy(baza2)
    wartosc_dzwiek1 = int(obliczanie_calkowitej_wartosci(dzwiek1, baza1))
    wartosc_dzwiek2 = int(obliczanie_calkowitej_wartosci(dzwiek2, baza2))
    wynik = obliczanie_nww(wartosc_dzwiek1, wartosc_dzwiek2)
    return wynik
print(nww_z_wartosci_enharmonicznej("C#4","F3"))
