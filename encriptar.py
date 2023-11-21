from cryptography.fernet import Fernet
from PIL import Image

def es_imagen(arch):
    try:
        Image.open(arch)
        return True
    except:
        return False

def genera_clave(tamano):
    clave = Fernet.generate_key()
    # Añadir el tamaño deseado al final de la clave
    clave = clave + str(tamano).encode()
    with open("clave.key", "wb") as key:
        key.write(clave)

def cargar_clave():
    return open("clave.key", "rb").read()

def encript(arch, clave, tamano):
    f = Fernet(clave)
    # Añadir el tamaño al final de los datos antes de encriptar
    with open(arch, "rb") as file:
        info = file.read() + str(tamano).encode()
    encrypted_data = f.encrypt(info)
    with open(arch, "wb") as file:
        file.write(encrypted_data)

def desencript(arch, clave):
    f = Fernet(clave)
    with open(arch, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    tamano = int(decrypted_data[-1:])
    decrypted_data = decrypted_data[:-1]
    with open(arch, "wb") as file:
        file.write(decrypted_data)
    print(f"Tamaño personalizado: {tamano}")

tamano_personalizado = int(input("Ingrese el tamaño deseado para la encriptación: "))

genera_clave(tamano_personalizado)

clave = cargar_clave()

arch = input("Ingrese la ruta del archivo: ")

if es_imagen(arch):
    checker = input("Encriptar o desencriptar? (E/D)")
    if checker.lower() == "e":
        encript(arch, clave, tamano_personalizado)
    elif checker.lower() == "d":
        desencript(arch, clave)
    else:
        print("Opción no válida. Intentelo de nuevo.")
else:
    print("El archivo no es una imagen.")
