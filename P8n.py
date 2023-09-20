import cv2


def HitungP8N(gambar,x,y):
    f1 = gambar[(x-1),(y-1)]
    f2 = gambar[(x,y-1)]
    f3 = gambar[(x+1),(y-1)]
    f4 = gambar[(y+1),y]
    f5 = gambar[(x+1),(y+1)]
    f6 = gambar[x,(y+1)]
    f7 = gambar[(x-1),(y+1)]
    f8 = gambar[(x-1),y]

    print(f"Himpunan Nilai Intensitas N8P adalah ({f1,f2,f3,f4,f5,f6,f7,f8}")
Gambarnya = cv2.imread('blackping.jpeg',cv2.IMREAD_GRAYSCALE)

#mengambil ukuran gambar
baris, kolom = Gambarnya.shape
print(f"Tinggi dari citra input pada gambar tersebut adalah {baris} dan "
      f"Lebar dari citra input tersebut adalah {kolom}")

#Mengambil nilai setiap pixel pada titik (x,y)
x = int(input("masukkan Koordinat x : "))
y = int(input("Masukkan Koordinat y : "))

if x< kolom :
    if y<baris:
       # nilaiKeabuan = gmbar[y,x]
        #print(f"Nilai Keabuan pada titik koorninat ({y},{x} ) adalah {nilaiKeabuan} ")
        HitungP8N(Gambarnya,x,y)
    else:
        print("koordinat yang diinputkan melebihi ukuran tinggi gambar")
else:
    print("Koordinat yang diinputkan melebihi lebar gambar")

    #menampilkan citra
cv2.imshow('citra P8N',Gambarnya)
cv2.waitKey(0)
cv2.destroyAllWindows()
