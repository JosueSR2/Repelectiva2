import os
import random

def eliminar_archivos_aleatorios(directorio, num_archivos_a_eliminar):
    # Listar todos los archivos en el directorio
    try:
        archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    except FileNotFoundError:
        print("El directorio no existe.")
        return
    except PermissionError:
        print("No tienes permisos para acceder al directorio.")
        return

    # Si no hay archivos en el directorio
    if not archivos:
        print("No se encontraron archivos en el directorio.")
        return

    # Asegurar que no se pidan eliminar más archivos de los que existen
    if num_archivos_a_eliminar > len(archivos):
        print(f"Solo hay {len(archivos)} archivos disponibles para eliminar.")
        num_archivos_a_eliminar = len(archivos)

    # Seleccionar archivos aleatorios para eliminar
    archivos_a_eliminar = random.sample(archivos, num_archivos_a_eliminar)

    # Eliminar los archivos seleccionados
    for archivo in archivos_a_eliminar:
        try:
            os.remove(os.path.join(directorio, archivo))
            print(f"Archivo eliminado: {archivo}")
        except Exception as e:
            print(f"No se pudo eliminar el archivo {archivo}. Error: {e}")
