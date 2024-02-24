from cryptography.fernet import Fernet




def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode
fer = Fernet(key)


def view():
    with open('password.txt', "r") as r:
        for line in r.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:", str(fer.encrypt(passw.encode())))

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('password.txt', "a") as f: # open() fonksiyonu dosyaları açmak için kullanılır. 3 modu bulunur "w" modu dosyaları mevcutsa üzerine yazar değilse sıfırdan oluşturur. "r" modu sadece dosyayı okur ama yazamaz. "a" modu hem yazar hem de okur ama dosyanın üzerine yazmaz.
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add) press q to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue