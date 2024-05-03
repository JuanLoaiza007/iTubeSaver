# iTubeSaver

iTubeSaver es una aplicación para descargar el audio de videos de YouTube utilizando yt-dlp y ffmpeg.

## Herramientas utilizadas

iTubeSaver utiliza las siguientes herramientas:

- [yt-dlp](https://pypi.org/project/yt-dlp/): La version módulo de Python para descargar videos de YouTube.
- [ffmpeg-python](https://pypi.org/project/ffmpeg-python/): Un módulo de Python para interactuar con FFmpeg, una herramienta de línea de comandos para manipular archivos multimedia.
- [ffmpeg.exe](https://ffmpeg.org/download.html#build-windows): FFmpeg es una suite de software libre que incluye bibliotecas y herramientas para manejar archivos multimedia. La versión para Windows está disponible en el sitio oficial de [FFmpeg](https://ffmpeg.org/).


## Integrantes

- Juan David Loaiza Santiago - 2177570 - juan.loaiza.santiago@correounivalle.edu.co
- Juan Sebastian Muñoz Rojas - 2177436 - juan.munoz.rojas@correounivalle.edu.co
- Julian David Rendon Cardona - 2177387 - julian.david.rendon@correounivalle.edu.co

## Requisitos
**(Solo en Linux)** Instala ffmpeg usando el gestor apt:
```
sudo apt-get install ffmpeg
```

> [!WARNING]
> Es posible que la aplicacion no funcione correctamente si instaló ffmpeg con otros gestores de paquetes como snap o flatpak

## Uso

Para usar iTubeSaver, sigue estos pasos:

1. Clona el repositorio:
```
git clone https://github.com/JuanLoaiza007/iTubeSaver.git
```

2. Crea y activa un entorno virtual. Para crearlo puedes usar:
```
python -m venv venv
```
Consulta como activarlo según tu sistema operativo.

3. Ejecuta el archivo **main.py** **desde la raiz del proyecto.**
