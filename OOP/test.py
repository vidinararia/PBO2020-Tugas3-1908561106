# Variabel global untuk menyimpan data judul
judul = []


# fungsi untuk menampilkan semua data
def show_data():
    if len(judul) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(judul)):
            print ("[%d] %s" % (indeks, judul[indeks]))


# fungsi untuk menambah data
def insert_data():
    judul_baru = input("Judul judul: ")
    judul.append(judul_baru)

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = input("Inputkan ID judul: ")
    if(indeks > len(judul)):
        print ("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# fungsi untuk menhapus data
def delete_data():
    show_data()
    indeks = input("Inputkan ID judul: ")
    if(indeks > len(judul)):
        print ("ID salah")
    else:
        judul.remove(judul[indeks])


# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    
    menu = input("PILIH MENU> ")
    print ("\n")

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print ("Salah pilih!")


if __name__ == "__main__":

    while(True):
        show_menu()
