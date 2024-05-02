import os
from utils.FFmpegUtils import FFmpegUtils as converter
from utils.YtdplUtils import YtdlpUtils as downloader

debug = True


def print_debug(message):
    new_message = "[MasterPiece.py]: " + message
    if debug:
        print(new_message)


class MasterPiece:

    @staticmethod
    def get_ultimos_videos(channel_name):
        return downloader.get_recent_video_urls(channel_name)

    @staticmethod
    def descargar_y_convertir(video_url):
        print_debug("Iniciando descarga del video: {}".format(str(video_url)))
        file_info = downloader.download_video(video_url)

        print_debug("\n\n")
        print_debug(
            "La informacion del video es: {}\n\n".format(str(file_info)))

        print_debug("Convirtiendo el video con url {}\n".format(str(video_url)))
        converter.mp4_to_mp3(file_info)

        print_debug("Eliminando el archivo .mp4")
        if os.path.exists(file_info['ruta_absoluta']):
            os.remove(file_info['ruta_absoluta'])
            print_debug("El archivo {} ha sido eliminado exitosamente.".format(
                str(file_info['ruta_absoluta'])))
        else:
            print_debug("El archivo {} no existe.".format(
                str(file_info['ruta_absoluta'])))

        return file_info
