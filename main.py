import os
from utils.FFmpegUtils import FFmpegUtils as converter
from utils.YtdplUtils import YtdlpUtils as downloader

url_posible = "https://www.youtube.com/watch?v=K4DyBUG242c"
url_falsa = "https://www.youtube.com/watch?v=python"

video_url = url_posible

file_info = downloader.download_video(video_url)
converter.mp4_to_mp3(file_info)

if os.path.exists(file_info['ruta_absoluta']):
    os.remove(file_info['ruta_absoluta'])
    print(
        f"El archivo {file_info['ruta_absoluta']} ha sido eliminado exitosamente.")
else:
    print(f"El archivo {file_info['ruta_absoluta']} no existe.")
