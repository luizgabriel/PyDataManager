import tkinter as Tkinter
from tkinter import ttk


class MainFrame(Tkinter.Tk):
    def __init__(self, *args, **kwargs):
        Tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Gerenciador")
        container = Tkinter.Frame(self)
        

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Livros, Recibos):
            
            frame = F(container, self)
            #print(F)
            self.frames[F] = frame
            #print(frame)
            #print(self.frames[F])
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)
        #print(self.frames[StartPage])
        #print(self.frames[Livros])

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Tkinter.Frame):

    def __init__(self, parent, controller):
        Tkinter.Frame.__init__(self,parent)
        self.controller = controller
        self.initUserInterface()


    def OnDoubleClick(self, event):
        self.controller.show_frame(globals()[self.tableModel.item(self.tableModel.selection()[0], 'text')])

    
    def initUserInterface(self):
        

        self.button1 = Tkinter.Button(self, text="Carregar Modelo")
        self.button1.pack()

        self.tableModel = ttk.Treeview(self, columns=('Campos', 'Qtd', 'Gerenciar'))
        self.tableModel.heading('#0', text='Modelo')
        self.tableModel.heading('#1', text='Campos')
        self.tableModel.heading('#2', text='Qtd.')
        self.tableModel.heading('#3', text='Gerenciar')
        self.tableModel.column('#0', stretch=Tkinter.YES)
        self.tableModel.column('#1', stretch=Tkinter.YES)
        self.tableModel.column('#2', stretch=Tkinter.YES)
        self.tableModel.column('#3', stretch=Tkinter.YES)
        self.tableModel.bind("<Double-1>", self.OnDoubleClick)
        self.tableModel.pack()

        self.tableModel.insert('', 'end', text="Livros", values=('nome|autor|und', '50', 'Gerenciar'))
        self.tableModel.insert('', 'end', text="Recibos", values=('ref|valor|comprador', '80', 'Gerenciar'))


class Livros(Tkinter.Frame):

    def __init__(self, parent, controller):
        Tkinter.Frame.__init__(self, parent)
        self.initUserInterface()
        self.controller = controller

    def initUserInterface(self):
        self.label1 = Tkinter.Label(self, text="Livros")
        self.label1.pack(side="top")
        
        self.button1 = Tkinter.Button(self, text="Voltar para a tela principal", command=lambda:self.controller.show_frame(StartPage))
        self.button1.pack(side="top")
        self.button2 = Tkinter.Button(self, text="Adicionar livro")
        self.button2.pack(side="top")

        self.tableGeneral = ttk.Treeview(self, columns=('Autor', 'Und'))
        self.tableGeneral.heading('#0', text="Nome")
        self.tableGeneral.heading('#1', text="Autor")
        self.tableGeneral.heading('#2', text="Und")
        self.tableGeneral.column('#0', stretch=Tkinter.YES)
        self.tableGeneral.column('#1', stretch=Tkinter.YES)
        self.tableGeneral.column('#2', stretch=Tkinter.YES)
        self.tableGeneral.pack(side="bottom", fill="both")

        self.tableGeneral.insert('', 'end', text="Python o Livro", values=('Ludibriatus Cerivatus', '23'))

class Recibos(Tkinter.Frame):

    def __init__(self, parent, controller):
        Tkinter.Frame.__init__(self, parent)
        self.initUserInterface()
        self.controller = controller

    def initUserInterface(self):
        self.label1 = Tkinter.Label(self, text="Recibos")
        self.label1.pack(side="top")
        
        self.button1 = Tkinter.Button(self, text="Voltar para a tela principal", command=lambda:self.controller.show_frame(StartPage))
        self.button1.pack(side="top")
        self.button2 = Tkinter.Button(self, text="Adicionar recibo")
        self.button2.pack(side="top")

        self.tableGeneral = ttk.Treeview(self, columns=('Valor', 'Comprador'))
        self.tableGeneral.heading('#0', text="Ref")
        self.tableGeneral.heading('#1', text="Valor")
        self.tableGeneral.heading('#2', text="Comprador")
        self.tableGeneral.column('#0', stretch=Tkinter.YES)
        self.tableGeneral.column('#1', stretch=Tkinter.YES)
        self.tableGeneral.column('#2', stretch=Tkinter.YES)
        self.tableGeneral.pack(side="bottom")

        self.tableGeneral.insert('', 'end', text="23812", values=('R$987,34', 'C'))
        

app = MainFrame()
app.mainloop()
        
        
