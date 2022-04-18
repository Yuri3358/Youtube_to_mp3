from tkinter.filedialog import askdirectory
from pytube import YouTube as Yt

def baixar(id, labelmessage):
            code = id.get()
            dto = askdirectory()
            link = str(code)

            if 'youtube' not in link:
                link = f'https://www.youtube.com/watch?v={code}'
            else:
                link = str(code)
        
            video = Yt(link)
            audio = video.streams.get_audio_only()
            
            try:
                audio.download(output_path=f'{dto}')
            except Exception as e:
                labelmessage['text'] = "Algo está errado, cheque o ID do vídeo" #verificar exceção
                print(e)

            else: 
                labelmessage["text"] = "Verifique o arquivo no diretório combinado"
                id.delete(0, "end")