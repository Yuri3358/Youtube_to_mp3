
from tkinter import *
from download import baixar #Toda a função de baixar o vídeo em um diretório escolhido está no import

class App():

    def __init__(self):
        cor = '#1295db'
        self.root = Tk()
        self.root.geometry("600x270")
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(background=f'{cor}')
        self.root.title('Conversor Youtube para Áudio')

        label_videocode = Label(text='ID do vídeo', font='Arial 18', background=cor) #ID do vídeo são os códigos que aparecem (Melhor explicações no README.md
        label_videocode.pack()
        
        entrada_id = Entry(self.root, font='Arial 14', width=40, background='#fdff96')
        entrada_id.pack(pady=20)
        
        label_videotitle = Label(text='Tìtulo do arquivo', font='Arial 18', background=cor)
        label_videotitle.pack()
        
        entrada_titulo = Entry(self.root, font='Arial 14', width=40, background='#fdff96')
        entrada_titulo.pack(pady=10)

        label_mensagem = Label(self.root, text='', background=cor, font=20)

        download = lambda: baixar(id=entrada_id, labelmessage=label_mensagem, title=entrada_titulo)

        #contornei o problema da função em command, usando funções lambda
        submit = Button(text='Download', command=download, height=1, width=18, pady=10, font=30, background='#fffb00')
        submit.pack()
    
        label_mensagem.pack()

        self.root.mainloop()

        
App()