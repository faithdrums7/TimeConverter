# Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, 
# jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string 
# akan keluar notifikasi. Invalid Input

    
def timeConverter(seconds):
    
    HH = seconds // 3600 % 100  # kita konversikan detik kedalam jam, kemudian karena batasnya adalah 35999 detik yaitu 100 jam maka di mod 100
    MM = seconds % 3600 // 60   # pertama karena jika 3600 akan masuk ke 1 jam, maka kita mod terlebih dahulu kemudian sisanya kita bagi dengan 60 digunakan 2 garing agar tidak koma
    SS = (seconds % 3600) % 60  # untuk menemukan sisa detik maka sisa dari mod 3600 di mod kembali dengan 60

    if HH < 10:                 # if condition ini digunakan untuk menambah str 0 di depan setiap HH, MM dan SS yang nilainya dibawah 10
        HH = '0' + str(HH)
    else:
        HH = str(HH)
            
    if MM < 10:
        MM = '0' + str(MM)
    else:
        MM = str(MM)
            
    if SS < 10:
        SS = '0' + str(SS)
    else:
        SS = str(SS)
    4
    final = print(f'Konversi : {HH}:{MM}:{SS}')
    return final
    
    
seconds = input("Masukkan detik! ")  # function input untuk memasukkan value dari user
try:                                 # jika type dari seconds bukan int maka akan print invalid input!
    seconds = int(seconds)
except ValueError:
    print('Invalid Input!')
if seconds > 359999:                 # jika sudah benar inputnya merupakan integer maka akan di cek kembali apakah inputnya lebih dari 359999
    print('Input kelebihan!')
else:
    timeConverter(seconds)           # memanggil function jika kondisi kondisi diatasnya tidak termasuk