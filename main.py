import time
from utils.MasterPiece import MasterPiece

debug = True


def print_debug(message):
    new_message = "[main.py]: " + message
    if debug:
        print(new_message)


class iTimer():
    def __init__(self):
        self.start_time = time.time()
        self.end_time = None
        print_debug("iTimer (Class): instance started!")

    def end(self):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print_debug(
            "iTimer (Class): instance end after {:.2f} seconds!".format(total_time))


if __name__ == '__main__':

    video_urls = []
    registers = []

    canales = ["@NoCopyrightSounds",
               "@TongoOficial",
               "@WOSDS3",
               "@TruenoOficial",
               "@DubstepuNk",
               ]

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

    print_debug("Registros: \n{}".format(str(registers)))
