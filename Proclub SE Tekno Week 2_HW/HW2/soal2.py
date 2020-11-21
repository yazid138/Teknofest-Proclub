"""
masukin klub 1
masukin klub 2

ulangin pertandingan == true
hitung + 1
pertandingan 1 : 1 3
pertandingan 2 : 3 1
pertandingan 3 : 1 1
pertandingan 4 : -1 1
jika data terdapat mines/kurang dari nol(0) keluar dari perulangan == false

data = [[1,3],[3,1],[1,1],[-1,1]]
cek data terdapat minus tidak kalo ada minus hapus datanya

data = [[1,3],[3,1],[1,1]]
ulangin/perulangan bercabang dan ambil datanya
hitung + 1
cek apakah data[0][0] == data[0][1]
    cetak draw
cek apakah data[0][0] > data[0][1]
    cetak klub 1 menang
cek apakah data[0][0] < data[0][1]
    cetak klub 2 menang
hapus data[0]

pertandingan selesai

"""

cek = True
data_skor = []
hitung = 0

def cekMenang(x):
    if data_skor[x][0] == data_skor[x][1]:
        print(f'hasil {hitung} : Draw')
    elif data_skor[x][0] > data_skor[x][1]:
        print(f'hasil {hitung} : {klubA}')
    elif data_skor[x][0] < data_skor[x][1]:
        print(f'hasil {hitung} : {klubB}')
    else:
        print('pertandingan tidak valid')

klubA = input('Klub A : ')
klubB = input('Klub B : ')

while cek:
    hitung += 1
    # inisialisasi input dan rubah ke int
    skor_string = input(f'Pertandingan {hitung} : ').split()
    # mengubah data_skor dari str ke int ke variabel skor
    skor = [int(i) for i in skor_string]
    # masukkan skor ke list
    data_skor.append(skor)
    # ambil nilai datanya dari skor
    for i in skor:
        data = i
        # cek apakah skor terdapat minus
        if data < 0:
            cek = False

# hapus data terakhir
del data_skor[len(data_skor)-1]

hitung = 0
for x in range(len(data_skor)):
    hitung += 1
    cekMenang(x)

print('Pertandingan selesai')

