import tkinter as Tkinter
from tkinter import ttk


class MainFrame(Tkinter.Frame):
    
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initUserInterface()
        
        
    def OnDoubleClick(self, event):
            item = self.tableModel.selection()[0]
            print("you clicked on", self.tableModel.item(item,"text"))
            
            
    def initUserInterface(self):

        self.parent.title("Gerenciador de Dados")
    
        '''
            Inicializando labels e botões
        '''

        self.load_button = Tkinter.Button(self.parent, text="Carregar Modelo")
        self.load_button.grid(row = 0, column = 0, sticky = Tkinter.W)


        '''
            Inicializando a tabela e nomeando suas colunas
        '''
        self.tableModel = ttk.Treeview(self.parent, columns=('Campos', 'Qtd', 'Gerenciar'))
        self.tableModel.heading('#0', text='Modelo')
        self.tableModel.heading('#1', text='Campos')
        self.tableModel.heading('#2', text='Qtd.')
        self.tableModel.heading('#3', text='Gerenciar')
        self.tableModel.column('#0', stretch=Tkinter.YES)
        self.tableModel.column('#1', stretch=Tkinter.YES)
        self.tableModel.column('#2', stretch=Tkinter.YES)
        self.tableModel.column('#3', stretch=Tkinter.YES)
        self.tableModel.bind("<Double-1>", self.OnDoubleClick)
        self.tableModel.grid(row=1, columnspan=1)

        '''
            Populando a tabela
        '''
        
        self.tableModel.insert('', 'end', text="Livros", values=('nome|autor|und', '50', 'Gerenciar'))
        self.tableModel.insert('', 'end', text="Recibos", values=('ref|valor|comprador', '80', 'Gerenciar'))


    
        
        
win = Tkinter.Tk()
d = MainFrame(win)


        

        



