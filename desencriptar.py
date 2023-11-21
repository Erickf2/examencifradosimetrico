def obtener_numero_clave():
    while True:
        try:
            numero = int(input("Por favor, ingresa el número (clave): "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero.")
    return numero

def leer_imagen(nombre_archivo):
    with open(nombre_archivo, "rb") as file:
        image = bytearray(file.read())
    return image

def aplicar_xor_a_imagen(image, numero):
    for i, j in enumerate(image):
        image[i] = j ^ numero
    return image

def guardar_imagen(image, nombre_archivo):
    with open(nombre_archivo, "wb") as file:
        file.write(image)

if __name__ == "__main__":
    numero_clave = obtener_numero_clave()
    nombre_archivo_entrada = "tester.jpg"
    nombre_archivo_salida = "decrypted.jpg"

    image = leer_imagen(nombre_archivo_entrada)
    image_cifrada = aplicar_xor_a_imagen(image, numero_clave)
    guardar_imagen(image_cifrada, nombre_archivo_salida)
