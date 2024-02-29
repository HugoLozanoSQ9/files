import files

#El manejo de errores en realidad se debe hacer desde el manejo de la función

try:
    files.create_file("sample.txt")
except OSError as error:
    print('No se pudo crear el archivo: ',error)

print("Programa terminado con éxito")
# except FileExistsError as error: # con esto podemos delimitar el tipo de arror
#     # except: #mensaje para otros errores.
#     print(f"No se pudo crear el archivo {error}")
#     raise Exception('El archivo ya existe') from error #siempre que un error sea a causa de otro se puede levantar un error (crear)

# except PermissionError:
#     print("No tienes permiso para crear el archivo")
# except OSError:
#     print("No se pudo crear el archivo hubo un error desconocido")

# Aquí podemos seguir con el programa :D

