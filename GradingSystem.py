import tkinter as tk
from tkinter import messagebox


def calcularMedia():
    try:
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
        nota3 = float(entry_nota3.get())
        nota4 = float(entry_nota4.get())

        media = (nota1 + nota2 + nota3 + nota4) / 4

        messagebox.showinfo('Media', f'A media do aluno eh: {media:.2f}')
    except ValueError:
        messagebox.showerror('Erro', 'Por favor digite apenas numeros nas notas')


janela = tk.Tk()
janela.title('Calcular media do aluno')
janela. configure(background='#2F4F4F')
janela.geometry('400x200')
janela.resizable(True, True)
janela.maxsize(width=800, height=700)
janela.minsize(width=400, height=300)

label_nota1 = tk.Label(janela, text='Nota 1: ')
label_nota1.pack()
entry_nota1 = tk.Entry(janela)
entry_nota1.pack()

label_nota2 = tk.Label(janela, text='Nota 2: ')
label_nota2.pack()
entry_nota2 = tk.Entry(janela)
entry_nota2.pack()

label_nota3 = tk.Label(janela, text='Nota 3: ')
label_nota3.pack()
entry_nota3 = tk.Entry(janela)
entry_nota3.pack()

label_nota4 = tk.Label(janela, text='Nota 4: ')
label_nota4.pack()
entry_nota4 = tk.Entry(janela)
entry_nota4.pack()

botao_calcular = tk.Button(janela, text='Calcular Media', command=calcularMedia)
botao_calcular.pack()

janela.mainloop()