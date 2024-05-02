
from utils.MasterPiece import MasterPiece
from utils.JSONUtils import JSONUtils
from utils.iTimer import iTimer

debug = True


def print_debug(message):
    new_message = "[DownloaderSecuencial.py]: " + message
    if debug:
        print(new_message)


class DownloaderSecuencial:
    def descargar(canales):
        video_urls = []
        registers = []

        print_debug("Obteniendo ultimos videos.")
        temporizador = iTimer()
        for canal in canales:
            temp_urls = MasterPiece.get_ultimos_videos(canal)

            for url in temp_urls:
                video_urls.append(url)
        temporizador.end()
        print_debug("Ya obtuve los videos.\n\n")

        print_debug(
            "Hay {} video/s a descargar, son:\n\n{}".format(str(len(video_urls)), str(video_urls)))

        print_debug("Iniciando descarga de cola de videos.\n")
        for url in video_urls:
            file_info = MasterPiece.descargar_y_convertir(url)

            register = {
                "titulo_original": file_info['titulo_original'],
                'url': file_info['url'],
                'fecha_publicacion': file_info['fecha_publicacion'],
                'fecha_descarga': file_info['fecha_descarga'],
            }

            registers.append(register)

        print_debug("Agregando descargas al registro.\n")
        original_register = JSONUtils.read_downloads_register()
        new_register = original_register

        for register in register:
            new_register.append(register)

        JSONUtils.write_downloads_register(new_register)
