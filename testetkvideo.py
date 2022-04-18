from cProfile import label
from cgitb import text
from tkinter import *
from pytube import YouTube as Yt
class App():
    def __init__(self):
        cor = '#919191'
        self.root = Tk()
        self.root.geometry("600x300")
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(background=f'{cor}')
        self.root.title('Conversor Youtube para mp3')

        def baixar():
            code = entrada_codigo.get()
            link = str(code)

            if 'youtube' not in link:
                link = f'https://www.youtube.com/watch?v={code}'
            else:
                link = str(code)

            video = Yt(link)
            dto = diretorio.get()
            audio = video.streams.get_audio_only()
            audio.download(output_path=f'{dto}')


        label_videocode = Label(text='Código do vídeo', font='Arial 18', background=cor)
        label_videocode.pack()
        
        entrada_codigo = Entry(self.root, font='Arial 14', width=40)
        entrada_codigo.pack()

        Label_diretorio = Label(self.root, text='Diretório do áudio', font='Arial 18', background=cor)
        Label_diretorio.pack()

        diretorio = Entry(self.root, font='Arial 18', width=35)
        diretorio.pack()


        submit = Button(text='Baixar', command=baixar, height=2, width=20, pady=10, font=36, background='#636363')
        submit.pack()

        label_mensagem = Label(self.root, text='', background=cor)
        label_mensagem.pack()

        self.root.mainloop()

App()