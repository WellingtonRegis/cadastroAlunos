from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs():
    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_telas()
        self.botoes()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Alunos')
        self.root.configure(background='#4682B4')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    def frames_telas(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#D3D3D3', highlightbackground='#D3D3D3', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd=4, bg='#D3D3D3', highlightbackground='#D3D3D3', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def botoes(self):
        ###Criando Botoes
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=4, bg='black', fg='red', font=('verdana', 8, 'bold'), command=self.limpar_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=4, bg='red', fg='black', font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_novo = Button(self.frame_1, text='Novo', bd=4, bg='red', fg='black', font=('verdana', 8, 'bold'))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=4, bg='red', fg='black', font=('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=4, bg='black', fg='red', font=('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ###Criando Label e Entradas
        self.lb_codigo = Label(self.frame_1, text='Codigo')
        self.lb_codigo.place(relx=0.05, rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome = Label(self.frame_1, text='Nome')
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.45)

        self.lb_telefone = Label(self.frame_1, text='Telefone')
        self.lb_telefone.place(relx=0.05, rely=0.7)
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.8, relwidth=0.4)

        self.lb_cidade = Label(self.frame_1, text='Cidade')
        self.lb_cidade.place(relx=0.5, rely=0.7)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.8, relwidth=0.4)

    def lista_frame2(self):
        self.lista_Aluno = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.lista_Aluno.heading('#0', text='')
        self.lista_Aluno.heading('#1', text='Codigo')
        self.lista_Aluno.heading('#2', text='Nome')
        self.lista_Aluno.heading('#3', text='Telefone')
        self.lista_Aluno.heading('#4', text='Cidade')

        self.lista_Aluno.column('#0', width=1)
        self.lista_Aluno.column('#1', width=50)
        self.lista_Aluno.column('#2', width=200)
        self.lista_Aluno.column('#3', width=125)
        self.lista_Aluno.column('#4', width=125)

        self.lista_Aluno.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_Aluno.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)


Application()