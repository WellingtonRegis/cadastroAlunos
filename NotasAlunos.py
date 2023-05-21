from tkinter import *
from tkinter import messagebox

root = Tk()

class Funcs():
    def calcularMedia(self, nota1_entry=None, nota2_entry=None, nota3_entry=None, nota4_entry=None):
        try:
            nota1 = float(nota1_entry.get())
            nota2 = float(nota2_entry.get())
            nota3 = float(nota3_entry.get())
            nota4 = float(nota4_entry.get())

            media = (nota1 + nota2 + nota3 + nota4) / 4

            messagebox.showinfo('Media', f'A media do aluno eh: {media:.2f}')
        except ValueError:
            messagebox.showerror('Erro', 'Por favor digite apenas numeros nas notas')

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.framesTela()
        self.botoes()
        self.calcularMedia()
        root.mainloop()


    def tela(self):
        self.root.title('Media dos Alunos')
        self.root.configure(background='#C0C0C0')
        self.root.geometry('500x400')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

    def framesTela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#D3D3D3', highlightbackground='#D3D3D3', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)


    def botoes(self):
        self.bt_calcular = Button(self.frame_1, text='Calcular Media', bd=4, command=self.calcularMedia)
        self.bt_calcular.place(relx=0.1, rely=0.05, relwidth=0.1, relheight=0.13)

        self.lb_nota1 = Label(self.frame_1, text='Nota 1', background='#D3D3D3')
        self.lb_nota1.place(relx=0.15, rely=0.12)
        self.nota1_entry = Entry(self.frame_1)
        self.nota1_entry.place(relx=0.35, rely=0.12, relwidth=0.30)
        ###Label e entrada do telefone
        self.lb_nota2 = Label(self.frame_1, text='Nota 2', background='#D3D3D3')
        self.lb_nota2.place(relx=0.15, rely=0.29)
        self.nota2_entry = Entry(self.frame_1)
        self.nota2_entry.place(relx=0.35, rely=0.29, relwidth=0.30)
        ###Label e entrada da cidade
        self.lb_nota3 = Label(self.frame_1, text='Nota 3', background='#D3D3D3')
        self.lb_nota3.place(relx=0.15, rely=0.46)
        self.nota3_entry = Entry(self.frame_1)
        self.nota3_entry.place(relx=0.35, rely=0.46, relwidth=0.30)
        ###Label e entrada do endereco
        self.lb_nota4 = Label(self.frame_1, text='Nota 4', background='#D3D3D3')
        self.lb_nota4.place(relx=0.15, rely=0.63)
        self.nota4_entry = Entry(self.frame_1)
        self.nota4_entry.place(relx=0.35, rely=0.63, relwidth=0.30)




Application()