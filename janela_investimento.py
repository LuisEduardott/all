import tkinter as tk

root = tk.Tk()
root.title("Simulador de Investimentos - Sicredi")# nome da janela
root.geometry("600x600")# resolucao
root.configure(bg="#333")# cor do fundo
root.resizable(width=False, height=False)#

# Título
titulo = tk.Label(
    root,
    text="Simulador de Investimentos", # texto do titulo
    font=("Arial", 25, "bold italic"),#fonte do text
    bg="#333", #fundo do titulo
    fg="#fff" #cor do titulo
)
titulo.pack(anchor="center",pady=(20, 4))

# Valor Inicial
valor_inicial = tk.Label(root,
text= "Valor Inicial: ",
font= ("Arial", 15, "bold"),
bg="#333",
fg="#fff"
         
)
valor_inicial.pack(anchor="center",pady=(10,5))

root.mainloop()






























root.mainloop()