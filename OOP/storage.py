import os
class user():
    def __init__(self):
        self.judul = judul

def masukkanJudul():
    user.judul = input("Masukkanjudul : ")
    
    f = open("judulstorage.txt","w")
    f.write(user.judul)
    print("Judul : " + user.judul + ", telah diedit")
    f.close()

def hapusNama():
    if os.path.exists("judulstorage.txt"):
        os.remove("judulstorage.txt")
    else:
        print("The file does not exist")

def cetakNama():
    try:
        f = open("judulstorage.txt", "r")
        print("judul : ")
        for x in f:
            print(x)
    except:
        print("Maaf judul = Kosong")