from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os


def get_key_from_password(password: str) -> bytes:
    salt = b"staly_salt_do_testow"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


# Hasło główne przy starcie
master_pwd = input("Podaj haslo glowne: ")
key = get_key_from_password(master_pwd)
fer = Fernet(key)


def zobacz():
    if not os.path.exists("passwords.txt"):
        print("Brak zapisanych hasel.")
        return

    # Ponowne hasło główne przy próbie odszyfrowania
    pwd_confirm = input("Wpisz haslo glowne, aby zobaczyc hasla: ")
    try:
        key_confirm = get_key_from_password(pwd_confirm)
        fer_confirm = Fernet(key_confirm)

        # Test odszyfrowania pierwszej linii (jeśli plik nie jest pusty)
        with open("passwords.txt", "r") as f:
            first_line = f.readline().strip()
            if first_line:
                user, encrypted = first_line.split("|")
                fer_confirm.decrypt(encrypted.encode())

        # Jeśli hasło poprawne, odszyfrowujemy wszystkie hasła
        with open("passwords.txt", "r") as f:
            for line in f:
                user, encrypted = line.strip().split("|")
                decrypted = fer_confirm.decrypt(encrypted.encode()).decode()
                print(f"Uzytkownik: {user} Haslo: {decrypted}")

    except (InvalidToken, ValueError):
        print("Niepoprawne haslo glowne! Nie mozna pokazac hasel.")


def stworz():
    name = input("Nazwa konta: ").strip()
    pwd = input("Haslo: ").strip()
    encrypted = fer.encrypt(pwd.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{encrypted}\n")


def eksport():
    if not os.path.exists("passwords.txt"):
        print("Brak danych do eksportu.")
        return

    pwd_confirm = input("Wpisz haslo glowne, aby eksportowac: ")
    try:
        key_confirm = get_key_from_password(pwd_confirm)
        fer_confirm = Fernet(key_confirm)

        # Test odszyfrowania pierwszej linii
        with open("passwords.txt", "r") as f:
            first_line = f.readline().strip()
            if first_line:
                user, encrypted = first_line.split("|")
                fer_confirm.decrypt(encrypted.encode())

        # Eksport wszystkich haseł
        with open("passwords.txt", "r") as f, open("decrypted_passwords.txt", "w") as out:
            for line in f:
                user, encrypted = line.strip().split("|")
                decrypted = fer_confirm.decrypt(encrypted.encode()).decode()
                out.write(f"{user} | {decrypted}\n")

        print("Hasla zapisane do decrypted_passwords.txt")

    except (InvalidToken, ValueError):
        print("Niepoprawne haslo glowne! Eksport anulowany.")


while True:
    mode = input("Co chcesz zrobic? (zobacz / stworz / eksport / q): ").lower()

    if mode == "q":
        break
    elif mode == "zobacz":
        zobacz()
    elif mode == "stworz":
        stworz()
    elif mode == "eksport":
        eksport()
    else:
        print("Nieznana komenda.")
