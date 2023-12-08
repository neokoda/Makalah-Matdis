# Nama : Muhammad Neo Cicero Koda
# NIM : 13522108

# Fungsi pembantu
def komposisi_relasi(a, b):
    c = [[0 for i in range(len(a))] for j in range(len(a))]
    for i in range(len(c)):
        for j in range(len(c)):
            for k in range(len(c)):
                if a[i][k] * b[k][j] == 1:
                    c[i][j] = 1
                    break
    return c

def union_relasi(a, b):
    for i in range(len(a)):
        for j in range(len(a)):
            if b[i][j] == 1:
                a[i][j] = 1
    return a

# Merapihkan penampilan matriks
def print_matriks(a):
    for i in range(len(a)):
        print(a[i])

# Algoritma pembentuk klosur relasi
def klosur_refleksif(relasi):
    for i in range(len(relasi)):
        relasi[i][i] = 1
    return relasi

def klosur_setangkup(relasi):
    for i in range(len(relasi)):
        for j in range(len(relasi)):
            if relasi[i][j] == 1 and i != j:
                relasi[j][i] = 1
    return relasi

def klosur_transitif(relasi):
    n = len(relasi)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        mr = relasi
        for j in range(i):
            mr = komposisi_relasi(mr, relasi)
        result = union_relasi(mr, result)
    return result

# Program utama
def main():
    # Data uji
    a = [[0, 1, 1],
         [0, 1, 0],
         [1, 0, 0]]
    
    b = [[1, 0, 1, 0],
         [0, 0, 0, 1],
         [0, 1, 0, 1],
         [0, 0, 1, 1]]
    
    c = [[0, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 0, 0, 1],
         [0, 0, 0, 1]]
    
    # Output hasil
    print("Hasil klosur refleksif matriks a: ")
    print_matriks(klosur_refleksif(a))
    print()
    print("Hasil klosur setangkup matriks b: ")
    print_matriks(klosur_setangkup(b))
    print()
    print("Hasil klosur menghantar matriks c: ")
    print_matriks(klosur_transitif(c))
    print()


if __name__ == "__main__":
    main()