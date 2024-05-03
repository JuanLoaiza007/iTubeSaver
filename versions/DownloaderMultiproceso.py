from multiprocessing import Pool, Process, Manager
from utils.MasterPiece import MasterPiece
from utils.JSONUtils import JSONUtils
from utils.iTimer import iTimer

debug = True


def print_debug(message):
    new_message = "[DownloaderSecuencial.py]: " + message
    if debug:
        print(new_message)


class DownloaderMultiproceso:
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
        temporizador = iTimer()
        
        with Pool() as p:
            registers = p.map(MasterPiece.descargar_y_convertir, video_urls)
        
        '''
        for url in video_urls:
            file_info = MasterPiece.descargar_y_convertir(url)

            register = {
                "titulo_original": file_info['titulo_original'],
                'url': file_info['url'],
                'fecha_publicacion': file_info['fecha_publicacion'],
                'fecha_descarga': file_info['fecha_descarga'],
            }

            registers.append(register)
        '''
        print_debug("\n\n")
        print_debug("Todas las descargas han sido finalizadas\n")
        temporizador.end()

        print_debug("Agregando descargas al registro.\n")
        temporizador = iTimer()
        original_registers = JSONUtils.read_downloads_register()
        new_registers = original_registers
        
        for register in registers:
            new_registers.append(register)
            
        JSONUtils.write_downloads_register(new_registers)

        temporizador.end()
        print_debug("El programa ha finalizado correctamente.\n")
