# [FFmpegUtils.py]

import os
import ffmpeg


class FFmpegUtils:

    @staticmethod
    def mp4_to_mp3(file_info):

        if 'ruta_absoluta' not in file_info:
            raise ValueError(
                "El diccionario file_info no contiene la clave 'ruta_absoluta'")

        input_file = file_info['ruta_absoluta']

        if not os.path.isfile(input_file):
            raise FileNotFoundError(
                f"El archivo de video '{input_file}' no existe")
        else:
            print("Archivo encontrado!!!")

        output_file = "{}.mp3".format(os.path.splitext(input_file)[0])

        ffmpeg.input(input_file).output(output_file).run()
