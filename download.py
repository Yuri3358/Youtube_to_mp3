
from tkinter.filedialog import askdirectory
from pytube import YouTube as Yt
from moviepy.editor import *
import os

def baixar(id, labelmessage):
            code = id.get()
            dto = askdirectory()
            link = str(code)

            if 'youtube' not in link:
                link = f'https://www.youtube.com/watch?v={code}'
            else:
                link = str(code)
        
            video_mp4 = Yt(link)
            audio_video = video_mp4.streams.get_audio_only()
            
            try:
                midea_dir = dto + f'/{video_mp4.title}'
                audio_video.download(output_path=f'{dto}')
                video = AudioFileClip(midea_dir + '.mp4')
                video.write_audiofile(midea_dir +'.mp3')
                os.remove(midea_dir + '.mp4')
                os.system("cls")

            except Exception as e:
                labelmessage['text'] = "Algo está errado, cheque o ID/link do vídeo" #verificar exceção
                print(e)

            else: 
                labelmessage["text"] = "Verifique o arquivo no diretório combinado"
                id.delete(0, "end")

