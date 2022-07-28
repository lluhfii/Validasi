from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def cekUsername():
    valid = False
    while not valid:
        try:
            username = input("\t[?] Masukkan Username : ")
            if (username[0].isupper() == True and len(username) > 10 and " " not in username) == True:
                print("\t[✓] Username berhasil di validasi")
                valid = True
                return username
            else:
                print("\t[✕] Username tidak valid")
        except ValueError:
            print("\t[✕] Username tidak valid")

def cekEmail():
    valid = True
    while valid:
        try:
            email = input("\t[?] Masukkan Email : ")
            if ("@" and "." in email) == True:
                print("\t[✓] Email berhasil di validasi")
                valid = True
                return email
            else:
                print("\t[✕] Email tidak valid")
        except ValueError:
            print("\t[✕] Email tidak valid")

def cekNomor():
    valid = True
    while valid:
        try:
            nomor = input("\t[?] Masukkan Nomor : ")
            if nomor.isdigit():
                print("\t[✓] Nomor berhasil di validasi")
                valid = True
                return nomor
            else:
                print("\t[✕] Nomor tidak valid")
        except ValueError:
            print("\t[✕] Nomor tidak valid")

def main():

    clear()

    username = cekUsername()
    email = cekEmail()
    nomor = cekNomor()

    print("\n\t[✓] Username : ", username)
    print("\t[✓] Email    : ", email)
    print("\t[✓] Nomor    : ", nomor, "\n")

main()