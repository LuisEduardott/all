import tkinter as tk

root = tk.Tk()
root.title(".exe")# nome da janela
root.geometry("600x600")# resolucao
root.configure(bg="#E31D2B")# cor do fundo
root.resizable(width=False, height=False)#

titulo = tk.Label(
    root,
    text="Santander", # texto do titulo
    font=("Nunito", 50, "bold"),#fonte do text
    bg="#E31D2B", #fundo do titulo
    fg="#fff" #cor do titulo
)
titulo.pack(anchor="center",pady=(20, 4))

# Valor Inicial
valor_inicial = tk.Label(root,
text= "Valor Inicial: ",
font= ("Arial", 15, "bold"),
bg="#E31D2B",
fg="#fff"        
)
valor_inicial.pack(anchor="center",pady=(10,5))

# Entrada de texto
entrada_texto = tk.Entry(root, font=("Arial, 15"))
entrada_texto.pack(side="left", padx=5)
entrada_texto.configure(bg="#fff", fg="#000")


root.mainloop()






























root.mainloop()