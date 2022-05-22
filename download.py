from tkinter.filedialog import askdirectory
from pytube import YouTube as Yt
from moviepy.editor import *
import os

def baixar(id, title, labelmessage, cb):
            cbtt = cb.get()
            code = id.get()
            filetitle = str(title.get())
            dto = askdirectory()
            link = str(code)

            if 'youtube' not in link:
                link = f'https://www.youtube.com/watch?v={code}'
            else:
                link = str(code)
        
            video_mp4 = Yt(link)
            audio_video = video_mp4.streams.get_audio_only()
            
            try:
                midea_dir = dto +  f"/{filetitle}"
                if cbtt:
                    baixar = audio_video.download(output_path=f'{dto}', filename=f'{filetitle}.mp4')
                else:
                    baixar
                    video = AudioFileClip(midea_dir + '.mp4')
                    video.write_audiofile(midea_dir +'.mp3')
                    os.remove(midea_dir + '.mp4')
                    os.system("cls")

            except Exception as e:
                labelmessage['text'] = "Algo está errado, cheque o ID/link do vídeo"
                print(e)

            else: 
                labelmessage["text"] = "Verifique o arquivo no diretório combinado"
                id.delete(0, "end")
                title.delete(0, "end")