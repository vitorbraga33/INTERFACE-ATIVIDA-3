import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Quem se mexer é Gay!")
def mostrar_mensagem2():
    messagebox.showinfo("Mensagem", "ANYONE WHO MOVES IS GAY!")
# Criar a janela principal
janela = tk.Tk()
janela.title("Interface Gráfica com Tkinter")

imagem = tk.PhotoImage(file="spiderman.png")
janela.geometry("800x800")

# Criar o rótulo
rotulo = tk.Label(janela, text="português ou inglês?")
rotulo.pack(padx=20, pady=20)

# Rótulo para a imagem
rotulo = tk.Label(janela, image=imagem)
rotulo.pack(padx=20, pady=20)

# Criar o botão
botao = tk.Button(janela, text="português ", command=mostrar_mensagem)
botao.pack(padx=20, pady=20)
botao = tk.Button(janela, text="inglês", command=mostrar_mensagem2)
botao.pack(padx=20, pady=20)
# Inicia o loop da janela
janela.mainloop()
