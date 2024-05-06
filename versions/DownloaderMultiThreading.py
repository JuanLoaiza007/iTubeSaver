import threading
from utils.MasterPiece import MasterPiece
from utils.JSONUtils import JSONUtils
from utils.iTimer import iTimer

debug = True


def print_debug(message):
    new_message = "[DownloaderMultithreading.py]: " + message
    if debug:
        print(new_message)


class DownloaderMultithreading:
    def descargar(canales, num_hilos=16):
        video_urls = []
        registers = []

        print_debug("Obteniendo ultimos videos.")
        temporizador = iTimer()
        
        # Lista para guardar los resultados de los hilos
        results = []

        def fetch_videos(canal):
            # Obtener los últimos videos del canal
            videos = MasterPiece.get_ultimos_videos(canal)
            results.append(videos)
        
        # Crear y iniciar hilos para obtener videos
        threads = []
        for canal in canales:
            thread = threading.Thread(target=fetch_videos, args=(canal,))
            threads.append(thread)
            thread.start()
        
        # Esperar a que todos los hilos terminen
        for thread in threads:
            thread.join()
        
        # Aplanar la lista de listas de resultados
        video_urls = [url for sublist in results for url in sublist]
        
        temporizador.end()
        print_debug("Ya obtuve los videos.\n\n")

        print_debug(
            "Hay {} video/s a descargar, son:\n\n{}".format(str(len(video_urls)), str(video_urls)))

        print_debug("Iniciando descarga de cola de videos.\n")
        temporizador = iTimer()
        
        # Lista para guardar los registros de los hilos
        download_results = []

        def download_and_convert(url):
            # Descargar y convertir el video, luego guardarlo en la lista de resultados
            result = MasterPiece.descargar_y_convertir(url)
            download_results.append(result)

        # Crear y iniciar hilos para descargar y convertir videos
        threads = []
        for url in video_urls:
            if len(threads) < num_hilos:
                thread = threading.Thread(target=download_and_convert, args=(url,))
                threads.append(thread)
                thread.start()
            else:
                # Esperar a que uno de los hilos termine antes de crear otro
                for thread in threads:
                    thread.join()
                # Limpiar la lista de hilos terminados
                threads = [thread for thread in threads if thread.is_alive()]
                # Crear y empezar el siguiente hilo
                thread = threading.Thread(target=download_and_convert, args=(url,))
                threads.append(thread)
                thread.start()
        
        # Esperar a que todos los hilos terminen
        for thread in threads:
            thread.join()

        registers = download_results
        
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
