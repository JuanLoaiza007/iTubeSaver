from versions.DownloaderSecuencial import DownloaderSecuencial as Secuencial
from versions.DownloaderMultiThreading import DownloaderMultithreading as Multithreading

if __name__ == '__main__':

    canales = [
        "@duki",
        "@MiliMilanss",
        "@TongoOficial",
        "@WOSDS3",
        "@TruenoOficial",
    ]
    #Secuencial.descargar(canales)
    Multithreading.descargar(canales)
