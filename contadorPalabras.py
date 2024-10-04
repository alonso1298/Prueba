def contar_palabras(archivo):
    try:
        # Abrir el archivo en modo de lectura
        with open(archivo, 'r') as f: # Se crea un alias al archivo
            contenido = f.read()  # Leer el contenido del archivo
            palabras = contenido.split()  # Dividir el contenido en palabras usando split()
            return len(palabras)  # Contar la cantidad de palabras
    except FileNotFoundError: # Si se genera el error FileNotFoundError ejecuta el script
        print(f'El archivo {archivo} no fue encontrado.')
        return 0 #Al no encontrar el archivo retorna 0

# Solicitar el nombre del archivo al usuario
archivo = input('Ingresa el nombre del archivo de texto: ')
numero_palabras = contar_palabras(archivo)
print(f'El archivo {archivo} tiene {numero_palabras} palabras.')