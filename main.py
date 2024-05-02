from utils.MasterPiece import MasterPiece

debug = True


def print_debug(message):
    new_message = "[main.py]: " + message
    if debug:
        print(new_message)


if __name__ == '__main__':

    canal = "@NoCopyrightSounds"
    video_urls = []
    registers = []

    print_debug("Obteniendo ultimos videos.\n")
    temp_urls = MasterPiece.get_ultimos_videos(canal)

    print_debug("Cargando videos en la cola de videos a descargar.\n")
    for url in temp_urls:
        video_urls.append(url)

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
