import os

def obtener_ruta_imagen():
    ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
    extension = os.path.splitext(ruta_imagen)[1].upper()

    while extension not in [".JPEG", ".PNG", ".JPG"]:
        print("Por favor, ingresa una imagen con extensión .JPEG, .PNG o .JPG.")
        ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
        extension = os.path.splitext(ruta_imagen)[1].upper()

    return ruta_imagen

def obtener_numero_clave():
    while True:
        try:
            numero = int(input("Por favor, ingresa un número (clave): "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero.")

    return numero

def cifrar_imagen(ruta_imagen, numero):
    with open(ruta_imagen, "rb") as file:
        image = bytearray(file.read())

    for i, j in enumerate(image):
        image[i] = j ^ numero

    with open("imagen_cifrada.jpg", "wb") as file:
        file.write(image)

if __name__ == "__main__":
    ruta_imagen = obtener_ruta_imagen()
    numero_clave = obtener_numero_clave()

    cifrar_imagen(ruta_imagen, numero_clave)
