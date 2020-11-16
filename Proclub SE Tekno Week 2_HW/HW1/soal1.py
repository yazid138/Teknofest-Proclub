arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    bMin = min(arrBerat)
    bMax = max(arrBerat)

def rerata(arrBerat):
    total = 0
    # Definisikan Proses Mencari Rerata Dari Total Berat
    for i in range(n):
        total += arrBerat[i]
    total /= n

    # Return Hasil Rerata
    return total

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    data_berat = float(input())
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(data_berat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print(f'Berat balita minimum: {bMin:.2f} kg');
print(f'Bera balita maximum: {bMax:.2f} kg');
print(f"Rerata berat balita: {rerata(arrBerat):.2f} kg");