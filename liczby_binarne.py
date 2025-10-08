def same_len_num(s1, s2):
    if s1 > s2:
        return 1
    elif s1 < s2:
        return 2
    else:
        return 3
def sortowanie_po_len(gl):
    koncowa_tablica= []
    gl.sort(key=lambda x: len(x[1]), reverse=True)
    while len(gl) >= 1:
        if len(gl) == 1:
            koncowa_tablica.append(gl[0])
            gl.pop(0)
        else:
            if len(gl[0][1]) > len(gl[1][1]):
                koncowa_tablica.append(gl[0])
                gl.pop(0)
            elif len(gl[0][1]) < len(gl[1][1]):
                koncowa_tablica.append(gl[0])
                gl.pop(1)
            elif len(gl[0][1]) == len(gl[1][1]):
                if gl[0][1].find('1') < gl[1][1].find('1'):
                    koncowa_tablica.append(gl[0])
                    gl.pop(0)
                elif gl[0][1].find('1') > gl[1][1].find('1'):
                    koncowa_tablica.append(gl[1])
                    gl.pop(1)
                if gl[0][1].find('1') == gl[1][1].find('1'):
                    wynik = same_len_num(gl[0][1],gl[1][1])
                    if wynik == 3:
                        koncowa_tablica.append(gl[0])
                        koncowa_tablica.append(gl[1])
                        gl.pop(0)
                        gl.pop(0)
                    elif wynik == 2:
                        koncowa_tablica.append(gl[1])
                        gl.pop(1)
                    elif wynik == 1:
                        koncowa_tablica.append(gl[0])
                        gl.pop(0)
    print(f"najwieksza: {koncowa_tablica[0][0]} najmniejsza: {koncowa_tablica[-1][0]}")
tablica = []
for i in range(1000):
    tablica.append((i, input("binarna do podania: ")))
sortowanie_po_len(tablica)