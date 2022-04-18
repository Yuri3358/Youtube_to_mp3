from tkinter import *
from download import baixar #Toda a função de baixar o vídeo em um diretório escolhido está no import
class App():

    def __init__(self):
        cor = '#919191'
        self.root = Tk()
        self.root.geometry("600x250")
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(background=f'{cor}')
        self.root.title('Conversor Youtube para audio')

        label_videocode = Label(text='ID do vídeo', font='Arial 18', background=cor) #ID do vídeo são os códigos que aparecem (Melhor explicações no README.md
        label_videocode.pack()
        
        entrada_id = Entry(self.root, font='Arial 14', width=40)
        entrada_id.pack()

        label_mensagem = Label(self.root, text='', background=cor, font=20)

        #contornei o problema da função em command, usando funções lambda
        submit = Button(text='Baixar', command=lambda: baixar(id=entrada_id, labelmessage=label_mensagem), height=2, width=20, pady=10, font=36, background='#636363')
        submit.pack()

        label_mensagem.pack()

        self.root.mainloop()

        
App()