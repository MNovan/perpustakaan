import os,sys,time


def menu():
    os.system("cls")
    print(" " * 12,"PERPUSTAKAAN ABADI"," " * 12)
    print("Pilih daftar menu untuk mengakses Aplikasi :")
    print("=" * 50)
    print("[1] Lihat Daftar Buku")
    print("[2] Cari Buku")
    print("[3] Tambah Data Buku")
    print("[4] Hapus Data Buku")
    print("[5] Lihat Daftar Peminjam Buku")
    print("[6] Tambah Peminjam Buku")
    print("[7] Hapus Data Peminjam Buku")
    print("[8] Keluar dari Aplikasi")

    kode = int(input("\nMasukkan kode menu yang ingin diakses : "))
    pilihmenu(kode)


def pilihmenu(p):
    if p == 1:
        daftarbuku()
    elif p == 2:
        caridata()
    elif p == 3:
        tambahdata()
    elif p == 4:
        hapusdata()
    elif p == 5:
        daftarpeminjam()
    elif p == 6:
        tambahpeminjam()
    elif p == 7:
        hapuspeminjam()
    elif p == 8:
        os.system("cls")
        print("\n" * 6)
        print(" " * 12,"[+] PERPUSTAKAAN ABADI"," " * 12)
        print(" " * 14,"Anda telah keluar dari program" + "\n"*6)
        time.sleep(5)
        os.system("cls")
        exit()
    else:
        print("(kode yang anda masukkan tidak valid)")
        print("\nTekan [ENTER] untuk kembali ke menu.")
        input()
        menu()



def daftarbuku():
    os.system("cls")
    print(" " * 14, "DAFTAR BUKU YANG TERSEDIA", " " * 16,)
    print("=========================================================")
    print("NO   |   NAMA    |   JUDUL BUKU  |   TGL.PEMINJAM    ")
    print("=========================================================")
    bukudata = open("daftarbuku.txt", "r")
    isi = bukudata.readlines()
    if len(isi) == 0:
        print("\n[Data tidak tersedia]")
    else:
        i = 1
        for data_buku in isi:
            pecah = data_buku.split(",")
            print("\n" + str(i) + ".", end="")
            print("  | "+pecah[0]+" | " + pecah[1]+" | " + pecah[2])
            i += 1
    with open("daftarbuku.txt", 'r') as fp:
        x = len(fp.readlines())
        print("\n"+"="* 57)
        print("PERPUSTAKAAN ABADI")
        print("    Total Buku: ",x)
        print("="* 57)
    print("\nTekan [ENTER] untuk kembali ke menu.")
    bukudata.close()
    input()
    menu()


def caridata():
    os.system("cls")
    print(" " * 14, "PENCARIAN BUKU", " " * 16)
    cari = input("\nMasukan judul buku yang ingin dicari : ")
    bukudata = open("daftarbuku.txt", "r")
    isi = bukudata.readlines()
    with open("daftarbuku.txt") as buku:
        if cari in buku.read():
            print("\n=========================================================")
            print("NO   |   NAMA    |   JUDUL BUKU  |   TGL.PEMINJAM    ")
            print("=========================================================")
            i = 1
            for data_buku in isi:
                pecah = data_buku.split(",")
                if pecah[0] == cari:
                    print(str(i) + ".", end="")
                    print("   | "+pecah[0]+" | " + pecah[1]+" | " + pecah[2])
                    i += 1
        else:
            print("Hasil pencarian tidak di temukan")
        print("\nTekan [ENTER] untuk kembali ke menu.")
        bukudata.close()
        input()
        menu()


def tambahdata():
    os.system("cls")
    print(" " * 14, "TAMBAH BUKU", " " * 16)
    print("\nMasukkan data buku baru")
    judul = input("Judul Buku : ")
    penulis = input("Penulis Buku : ")
    tahun = input("Tahun Terbit : ")
    bukadata = open("daftarbuku.txt", "a")
    bukadata.writelines([judul+","+penulis+","+tahun + "\n"])
    print("\n[Data Buku Berhasil Ditambahkan")
    bukadata.close()
    print("\nIngin menambah buku lagi? (y/t)", end=" ")
    tmbhdata = input(" : ")
    if tmbhdata == "ya" or tmbhdata == "YA" or tmbhdata == "y" or tmbhdata == "Y":
        tambahdata()
    else:
        print("\nTekan [ENTER] untuk kembali ke menu.")
        input()
        menu()



def hapusdata():
    os.system("cls")
    print(" " * 14, "HAPUS DATA BUKU", " " * 16)
    bukadata = open("daftarbuku.txt")
    output = []
    str = input("\nMasukkan juduk buku yang ingin dihapus : ")
    for hps in bukadata:
        if not hps.startswith(str):
            output.append(hps)

    bukadata = open("daftarbuku.txt.", "w")
    bukadata.writelines(output)
    print("\n[Data Buku Telah Terhapus]")
    bukadata.close()
    print("\nIngin menghapus data buku lagi? (y/t)", end=" ")
    hpsdata = input(":")
    if hpsdata == "ya" or hpsdata == "Ya" or hpsdata == "y" or hpsdata == "Y":
        hapusdata()
    else:
        print("\nTekan [ENTER] untuk kembali ke menu.")
        input()
        menu()


def daftarpeminjam():
    os.system("cls")
    print(" " * 14, "DAFTAR PEMINJAM BUKU", " " * 16)
    bukadata = open("daftarpinjaman.txt", "r")
    isi = bukadata.readlines()
    if len(isi) == 0:
        print("\n[Data tidak tersedia]")
    else:
        print("\n=========================================================")
        print("NO   |   NAMA    |   JUDUL BUKU  |   TGL.PEMINJAM    ")
        print("=========================================================\n")
        i = 1
        for data_buku in isi:
            pecah = data_buku.split(",")
            print(str(i) + ".", end="")
            print("   | "+pecah[0]+" | " + pecah[1]+" | " + pecah[2])
            i += 1
        with open("daftarpinjaman.txt", 'r') as fp:
            x = len(fp.readlines())
            print("\n"+"=" * 57)
            print("PERPUSTAKAAN ABADI")
            print("Total Peminjam: ",x)
            print("="* 57)
    print("\nTekan [ENTER] untuk kembali ke menu.")
    bukadata.close()
    input()
    menu()


def tambahpeminjam():
    os.system("cls")
    print(" " * 14, "TAMBAH PEMINJAM BUKU", " " * 16)
    print("\nMasukkan data peminjam buku")
    nama = input("Nama      : ")
    judul = input("Judul Buku       : ")
    tanggal = input("Tanggal Peminjaman : ")
    bukadata = open("daftarpinjaman.txt", "a")
    bukadata.writelines([nama + ","+judul+","+tanggal + "\n"])
    print("\n[Data Buku Berhasil Ditambahkan]")
    bukadata.close()

    print("\nIngin menambahkan data peminjam lagi? (y/t)", end=" ")
    tmbhpeminjam = input(":")
    if tmbhpeminjam == "ya" or tmbhpeminjam == "Ya" or tmbhpeminjam == "y" or tmbhpeminjam == "Y":
        tambahpeminjam()
    else:
        print("\nTekan [ENTER] untuk kembali ke menu.")
        input()
        menu()


def hapuspeminjam():
    os.system("cls")
    print(" " * 14, "HAPUS DATA PEMINJAM BUKU", " " * 16)
    bukadata = open("daftarpinjaman.txt")
    output = []
    str = input("\nMasukkan Nama Peminjam yang Ingin Dihapus :")
    for hps in bukadata:
        if not hps.startswith(str):
            output.append(hps)

    bukadata = open("daftarpinjaman.txt.", "w")
    bukadata.writelines(output)
    print("\n[Data Peminjam Telah Terhapus]")
    bukadata.close()
    print("\nIngin menghapus data peminjam lagi? (y/t)", end="")
    hpspeminjam = input(":")
    if hpspeminjam == "ya" or hpspeminjam == "Ya" or hpspeminjam == "y" or hpspeminjam == "Y":
        hapuspeminjam()
    else:
        print("\nTekan [ENTER] untuk kembali ke menu.")
        input()
        menu()
