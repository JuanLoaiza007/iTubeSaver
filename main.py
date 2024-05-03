from versions.DownloaderSecuencial import DownloaderSecuencial as Secuencial
from versions.DownloaderMultiproceso import DownloaderMultiproceso as Multiproceso

if __name__ == '__main__':

    canales = [
        "@duki",
        "@MiliMilanss",
        "@TongoOficial",
        "@WOSDS3",
        "@TruenoOficial",
    ]

    # Secuencial.descargar(canales)
    Multiproceso.descargar(canales)
    
