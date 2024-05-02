import os
import re
import yt_dlp
import json
from datetime import datetime


class YtdlpUtils:
    def limpiar_titulo(titulo):
        titulo = titulo.replace('á', 'a').replace('é', 'e').replace(
            'í', 'i').replace('ó', 'o').replace('ú', 'u')
        titulo = titulo.replace('Á', 'A').replace('É', 'E').replace(
            'Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        titulo = titulo.replace(' ', '_').replace('-', '_')

        titulo = re.sub(r'[^a-zA-Z0-9_]', '', titulo)
        titulo = re.sub(r'[_]+', '_', titulo)

        return titulo

    @staticmethod
    def obtener_titulo(video_url):
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(video_url, download=False)
                if 'title' in result:
                    return result['title']
                else:
                    return None
        except Exception as e:
            print("Error al obtener el título:", e)
            return None

    @staticmethod
    def get_video_info(video_url):
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(video_url, download=False)
                video_info = {
                    'titulo': result['title'],
                    'url': video_url,
                    'fecha_publicacion': result.get('upload_date'),
                    'fecha_descarga': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                }
            return video_info
        except Exception as e:
            print("Error al obtener información del video:", e)
            return None

    @staticmethod
    def download_video(video_url):

        file_info = None  # Se establece que no se ha generado ningun archivo

        try:

            video_info = YtdlpUtils.get_video_info(video_url)

            if video_info:

                carpeta_destino = "downloads"
                titulo = YtdlpUtils.limpiar_titulo(video_info['titulo'])

                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)

                ruta_salida = os.path.join(carpeta_destino, titulo)

                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                    'outtmpl': ruta_salida,
                }

                ydl = yt_dlp.YoutubeDL(ydl_opts)

                with ydl:
                    result = ydl.extract_info(video_url, download=True)

                    file_info = {
                        'ruta_absoluta': os.path.abspath(ruta_salida) + ".mp4",
                        'titulo_descarga': titulo+".mp4",
                        'titulo_original': result['title'],
                        'url': video_info['url'],
                        'fecha_publicacion': video_info['fecha_publicacion'],
                        'fecha_descarga': video_info['fecha_descarga'],
                    }
            return file_info

        except Exception as e:
            print("Error inesperado durante la descarga:", e)
            return None

    @staticmethod
    def download_recent_videos(channel_url, num_videos=5):
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'playlist_items': '1-{}'.format(num_videos),
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                'outtmpl': '%(title)s.mp4',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([channel_url])
            print("Descarga completada correctamente.")
        except Exception as e:
            print("Error durante la descarga:", e)

    @staticmethod
    def get_recent_video_urls(channel_name, num_videos=5):

        channel_url = "https://www.youtube.com/{}/videos".format(
            str(channel_name))
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'playlist_items': '1-{}'.format(num_videos),
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(channel_url, download=False)
                video_urls = [entry['webpage_url']
                              for entry in result['entries']]
            return video_urls
        except Exception as e:
            print("Error al obtener las URL de los videos:", e)
            return None


if __name__ == '__main__':
    import time

    start_time = time.time()  # Tiempo de inicio

    videos_recientes = YtdlpUtils.get_recent_video_urls("@NoCopyrightSounds")

    end_time = time.time()  # Tiempo de finalización

    tiempo_total = end_time - start_time

    print("Tiempo total de ejecución: {:.2f} segundos".format(tiempo_total))
    print("\n\n{}".format(str(videos_recientes)))
