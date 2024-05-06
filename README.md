# iTubeSaver

iTubeSaver es una aplicación para descargar el audio de los ultimos 5 videos de YouTube de algunos canales utilizando yt-dlp y ffmpeg.

## Herramientas utilizadas

iTubeSaver utiliza las siguientes herramientas:

- [yt-dlp](https://pypi.org/project/yt-dlp/): Un módulo de Python para descargar videos de YouTube.
- [FFmpeg](https://ffmpeg.org/): FFmpeg es una suite de software libre que incluye bibliotecas y herramientas para manejar archivos multimedia. La versión para Windows está disponible en el sitio oficial de [FFmpeg](https://ffmpeg.org/download.html#build-windows), en este repositorio se aloja un ejecutable en la raiz del proyecto para usuarios de Windows.
- [ffmpeg-python](https://pypi.org/project/ffmpeg-python/): Un módulo de Python para interactuar con FFmpeg, una herramienta de línea de comandos para manipular archivos multimedia.

## Integrantes

- Juan David Loaiza Santiago - 2177570 - juan.loaiza.santiago@correounivalle.edu.co
- Juan Sebastian Muñoz Rojas - 2177436 - juan.munoz.rojas@correounivalle.edu.co
- Julian David Rendon Cardona - 2177387 - julian.david.rendon@correounivalle.edu.co

## Requisitos

**(Solo en Linux)** Instala ffmpeg usando el gestor apt:

```
sudo apt install ffmpeg
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

3. Agrega los **nombres** de los canales en el **main.py**. La forma correcta es **@NombreCanal**

> [!WARNING] > **\*No debe agregar las direcciones url**, solo el **nombre de usuario** del canal como se muestra en la imagen:
> <img src="https://github.com/JuanLoaiza007/iTubeSaver/assets/116226390/0b132711-eb59-40a0-9d32-cf58ec84da99" width="1000"/>

4. Ejecuta el archivo **main.py** **desde la raiz del proyecto.**

5. **(Opcional)** Crea un archivo .env en la raiz del proyecto para recibir notificaciones por correo cuando la aplicacion finalice las descargas.

```
REMITENTE=correo@gmail.com
DESTINATARIO=otrocorreo@gmail.com
ASUNTO=Descarga de audio exitosa! | iTubeSaver
MENSAJE=Mensaje default
CLAVE_CORREO=clave de gmail desde myaccount.google.com/apppasswords
```
