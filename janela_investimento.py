from tkinter import *

janela = Tk()
janela.title("Santander")
janela.geometry("650x650")
janela.config(bg="#d90429")
janela.resizable(False, False)


def calcular():
    try:
        valor = float(entry_valor.get().replace(",", "."))
        juros = float(entry_juros.get().replace(",", "."))
        meses = int(entry_meses.get())

        resultado = valor * ((1 + juros / 100) ** meses)

        texto_resultado.config(
            text=f"Valor final: R$ {resultado:.2f}"
        )

    except:
        texto_resultado.config(
            text="Digite valores válidos"
        )


# TITULO
titulo = Label(
    janela,
    text="Santander               ",
    bg="#d90429",
    fg="white",
    font=("Nunito", 50, "bold")
)
titulo.pack(pady=10)


# FRAME
frame = Frame(
    janela,
    bg="#d90429"
)
frame.pack(fill="both", expand=True)

# VALOR
Label(
    frame,
    text="Valor Inicial",
    bg="#d90429",
    fg="white",
    font=("Segoe UI", 16, "bold"),
    anchor="w"
).pack(fill="x", padx=20)

entry_valor = Entry(
    frame,
    font=("Segoe UI", 16),
    width=25,
    bd=0
)
entry_valor.pack(fill="x", padx=20)


# JUROS
Label(
    frame,
    text="Juros ao mês (%)",
    bg="#d90429",
    fg="white",
    font=("Segoe UI", 16, "bold"),
    anchor="w"
).pack(fill="x", padx=20)

entry_juros = Entry(
    frame,
    font=("Segoe UI", 16),
    width=25,
    bd=0
)
entry_juros.pack(fill="x", padx=20)


# MESES
Label(
    frame,
    text="Quantidade de meses",
    bg="#d90429",
    fg="white",
    font=("Segoe UI", 16, "bold"),
    anchor="w"
).pack(fill="x", padx=20)

entry_meses = Entry(
    frame,
    font=("Segoe UI", 16),
    width=25,
    bd=0
)
entry_meses.pack(fill="x", padx=20)


# BOTAO
Button(
    janela,
    text="CALCULAR",
    command=calcular,
    bg="#d90429",
    fg="#ffffff",
    activebackground="#f2f2f2",
    activeforeground="#d90429",
    font=("Segoe UI", 24, "bold"),
    bd=0,
    relief="flat",
    cursor="hand2",
    padx=40,
    pady=15
).pack(pady=50)


# RESULTADO
texto_resultado = Label(
    janela,
    text="Valor final:",
    bg="#d90429",
    fg="white",
    font=("Segoe UI", 24, "bold"),
    
)
texto_resultado.pack(pady=50)


janela.mainloop()