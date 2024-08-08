
from pytube import YouTube

url = "ENLACE DE VIDEO DE YOUTUBE"

try:

   video = YouTube(url)
   stream = video.streams.filter(only_audio=True).first()
   stream.download(filename=f"{video.title}.mp3")
   print("El archivo fue descargado correctamente")
  
except KeyError:
   print("Ha ocurrido un error al descargar el archivo")


# En caso de obtener el error "pytube.exceptions.RegexMatchError"
# Reemplazar las líneas 273 y 274 del archivo cipher por:
# r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
# r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',