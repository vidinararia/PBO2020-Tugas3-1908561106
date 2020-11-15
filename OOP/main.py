from storage import masukkanjudul, hapusjudul, cetakjudul

def main ():
    print("Selamat datang")
    print("Menu :\n 1. masukkanjudul\n 2. hapusjudul\n 3. cetakjudul\n")
    pil = (int(input("pil :")))

    if pil == 1:
        masukkanjudul()
    elif pil == 2:
        hapusjudul()
    elif pil == 3:
        cetakjudul()
    elif pil == 4:
        exit()
    else :
        print("Maaf, pilihan anda tidak tersedia, silahkan coba memasukan kembali")

    input("Tekan enter untuk melanjutkan")
if __name__ == "__main__":

    while(True):
        main()
