from concurrent.futures import ThreadPoolExecutor
from utils.MasterPiece import MasterPiece
from utils.JSONUtils import JSONUtils
from utils.iTimer import iTimer

debug = True


def print_debug(message):
    new_message = "[DownloaderMultithreading.py]: " + message
    if debug:
        print(new_message)


class DownloaderMultithreading:
    def descargar(canales):
        video_urls = []
        registers = []

        print_debug("Obteniendo ultimos videos.")
        temporizador = iTimer()
        
        # Cambia a ThreadPoolExecutor
        with ThreadPoolExecutor() as executor:
            # Aquí se retorna una lista de listas con los URLs
            video_urls = list(executor.map(MasterPiece.get_ultimos_videos, canales))
            # Aplanando la lista de lista
            video_urls = [url for sublist in video_urls for url in sublist]
        
        temporizador.end()
        print_debug("Ya obtuve los videos.\n\n")

        print_debug(
            "Hay {} video/s a descargar, son:\n\n{}".format(str(len(video_urls)), str(video_urls)))

        print_debug("Iniciando descarga de cola de videos.\n")
        temporizador = iTimer()
        
        with ThreadPoolExecutor() as executor:
            registers = list(executor.map(MasterPiece.descargar_y_convertir, video_urls))
        
        print_debug("\n\n")
        print_debug("Todas las descargas han sido finalizadas.\n")
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
