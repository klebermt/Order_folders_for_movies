# Ordenador de Carpetas
---

Este programa en Python te permite copiar archivos de video desde carpetas de capítulos de una serie a una carpeta de destino.

## Funcionamiento

El programa busca archivos de video (`mp4`, `mkv`, `avi`) dentro de las carpetas de capítulos de una serie y los copia a una carpeta de destino llamada "All_chapters". Utiliza la barra de progreso `tqdm` para mostrar el avance del proceso.

## Requisitos

- Python 3.x
- Biblioteca `tqdm`

Puedes instalar la biblioteca `tqdm` ejecutando el siguiente comando:

```bash
pip install tqdm
```
---
## Uso
1. Ejecuta el programa main.py.
2. Ingresa la ruta de la carpeta principal de la serie cuando se te solicite.
3. El programa copiará los archivos de video a la carpeta "All_chapters" en la misma ubicación.

### Ejemplo:
```
Pega la ruta de la carpeta:
/ruta/de/tu/serie
``````
El programa buscará archivos de video en todas las carpetas de capítulos dentro de la carpeta principal de la serie y los copiará a una carpeta llamada "All_chapters".