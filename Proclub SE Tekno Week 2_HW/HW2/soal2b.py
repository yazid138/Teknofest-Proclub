data_menang = []

def cekMenang(skor1, skor2):
    if skor1 > skor2:
        data_menang.append(klubA)
    elif skor1 < skor2:
        data_menang.append(klubB)
    else:
        data_menang.append('Draw')

klubA = input('Klub A : ')
klubB = input('Klub B : ')

hitung = 0
while True:
    hitung += 1
    skor1, skor2 = map(int, input(f'Pertandingan {hitung} : ').split())
    if skor1 < 0 or skor2 < 0:
        break

    cekMenang(skor1, skor2)

hitung = 0
for hasil in data_menang:
    hitung += 1
    print(f'Hasil {hitung} : {hasil}')

print('Pertandingan Selesai')