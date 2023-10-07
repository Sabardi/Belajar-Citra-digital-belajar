x =int(input("masukkan nilai x :"))
y = int(input("masukan nilai y :"))

print("pilih oprator")
print("1 = penjumlahan")
print("2 = pengurangan")
print("3 = perkalian ")
print("4 = pembagian ")

oprator = input("masukan oprator nya : ")
if oprator =="1":
    hasil = x + y
    print("hasil nya : ", hasil)

elif oprator == "2":
    hasil = x - y
    print("hasil nya : ", hasil)

elif oprator == "3":
    hasil = x * y
    print("hasil nya : ", hasil)

elif oprator == "4":
    hasil = x / y
    print("hasil nya : ", hasil)
else:
    print("masukan dengan benar")