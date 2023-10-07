import cv2

def hitungN4p(img,x,y):
    f1 = img[(y-1),x]
    f2 = img[(y+1),x]
    f3 = img[y,(x+1)]
    f4 = img[y,(x-1)]
    print(f" Himpunan Nilai intensitas N4P adalah ({f1,f2,f3,f4} ")

gambar = cv2.imread('th.jpg',cv2.IMREAD_GRAYSCALE)
# Mengambil ukuran gambar citra
baris, kolom = gambar.shape
print(f"Tinggi dari citra input pada gambar tersebut adalah {baris} dan "
      f"Lebar dari citra input tersebut adalah {kolom}")
#Mengambil nilai setiap pixel pada titik (x,y)
x = int(input("masukkan Koordinat x : "))
y = int(input("Masukkan Koordinat y : "))
if x< kolom :
    if y<baris:
       # nilaiKeabuan = gmbar[y,x]
        #print(f"Nilai Keabuan pada titik koorninat ({y},{x} ) adalah {nilaiKeabuan} ")
        hitungN4p(gambar,x,y)
    else:
        print("koordinat yang diinputkan melebihi ukuran tinggi gambar")
else:
    print("Koordinat yang diinputkan melebihi lebar gambar")

# Menampilkan citra
cv2.imshow('Citra RGB', gambar)
cv2.waitKey(0)
cv2.destroyAllWindows()