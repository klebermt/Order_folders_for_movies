from tqdm import tqdm
import time
import os
import shutil

# Ruta de la carpeta principal de la serie
print("Pega la ruta de la carpeta: ")
ruta_serie = input()

# Ruta donde quieres copiar los archivos de video
ruta_destino = os.path.join(ruta_serie, "All_chapters") 

# Verifica si la ruta proporcionada existe y contiene carpetas
if os.path.exists(ruta_serie) and any(os.path.isdir(os.path.join(ruta_serie, carpeta)) for carpeta in os.listdir(ruta_serie)):
    # Obtén la lista de carpetas de capítulos
    carpetas_capitulos = [carpeta for carpeta in os.listdir(ruta_serie) if os.path.isdir(os.path.join(ruta_serie, carpeta))]

    # Crea la barra de carga con tqdm
    with tqdm(total=len(carpetas_capitulos), desc="Copiando archivos", unit="capítulo") as barra_progreso:
        # Itera sobre las carpetas de capítulos
        for carpeta_capitulo in carpetas_capitulos:
            ruta_capitulo = os.path.join(ruta_serie, carpeta_capitulo)

            # Verifica si es una carpeta
            if os.path.isdir(ruta_capitulo):
                # Itera sobre los archivos en la carpeta del capítulo
                for archivo in os.listdir(ruta_capitulo):
                    # Verifica si es un archivo de video (puedes ajustar las extensiones según tus necesidades)
                    if archivo.endswith('.mp4') or archivo.endswith('.mkv') or archivo.endswith('.avi'):
                        # Crea el directorio de destino si no existe
                        os.makedirs(ruta_destino, exist_ok=True)
                        
                        ruta_archivo = os.path.join(ruta_capitulo, archivo)

                        # Copia el archivo de video a la carpeta de destino
                        shutil.copy(ruta_archivo, ruta_destino)

                # Actualiza la barra de carga
                barra_progreso.update(1)
                time.sleep(0.1)  # Simula algo de trabajo en cada iteración

    print("Proceso completado.")
else:
    print("No se encontraron carpetas en la ruta proporcionada.")
