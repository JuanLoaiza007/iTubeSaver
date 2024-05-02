import os
import re
import yt_dlp


class YtdlpUtils:
    def limpiar_titulo(titulo):
        # Paso 1: Cambiar letras con acento por letras sin acento
        titulo = titulo.replace('á', 'a').replace('é', 'e').replace(
            'í', 'i').replace('ó', 'o').replace('ú', 'u')
        titulo = titulo.replace('Á', 'A').replace('É', 'E').replace(
            'Í', 'I').replace('Ó', 'O').replace('Ú', 'U')

        # Paso 2: Cambiar espacios y guiones medios por guiones bajos
        titulo = titulo.replace(' ', '_').replace('-', '_')

        # Paso 3: Eliminar todos los símbolos que no sean guiones bajos o letras
        titulo = re.sub(r'[^a-zA-Z0-9_]', '', titulo)

        # Paso 4: Eliminar guiones bajos repetidos
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
    def download_video(video_url):

        file_info = None  # Se establece que no se ha generado ningun archivo

        carpeta_destino = "downloads"
        titulo = YtdlpUtils.limpiar_titulo(
            YtdlpUtils.obtener_titulo(video_url))

        try:
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            ruta_salida = os.path.join(carpeta_destino, titulo)

            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                'outtmpl': ruta_salida,
            }

            ydl = yt_dlp.YoutubeDL(ydl_opts)

            with ydl:
                ydl.extract_info(video_url, download=True)

                file_info = {
                    'ruta_absoluta': os.path.abspath(ruta_salida) + ".mp4",
                    'titulo': titulo
                }

            return file_info

        except Exception as e:
            print("Error inesperado durante la descarga:", e)


if __name__ == '__main__':

    url_posible = "https://www.youtube.com/watch?v=K4DyBUG242c"
    url_falsa = "https://www.youtube.com/watch?v=python"

    print("\n\n{}".format(str(YtdlpUtils.download_video(url_posible))))
