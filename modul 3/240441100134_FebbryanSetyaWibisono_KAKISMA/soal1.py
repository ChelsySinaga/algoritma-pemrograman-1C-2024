ukuran = int(input("Masukan Ukuran : "))

# untuk angka 1
for a in range(ukuran) :
    print(" " * (ukuran // 2) + "x")
print()
# untuk angka 3
for a in range(ukuran) :
    if a == 0 or a == ukuran -1 or a == ukuran // 2:
        print("x" * ukuran)
    else :
        print(" " * (ukuran - 1) + "x")
print()
# untuk angka 4
for a in range(ukuran):
    if a == ukuran // 2:
        print("x" * ukuran)
    elif a > ukuran // 2:
        print(" " * (ukuran - 1) + "x")
    else:
        print("x" + " " * (ukuran - 2) + "x")