import random

# Jogo de Atualização

print("=== Adivinhe o número! ===")
numero_secreto = random.randint(1, 100)
tentativas = 0
palpites = 0

while palpites != numero_secreto:
    palpites = int(input("\nDigite um número entre (1/100):"))
    tentativas += 1

    if palpites < numero_secreto:
        print("Muito baixo!")
    elif palpites > numero_secreto:
        print("Muito alto!")
    else:
        clear = lambda: print("\n" * 100)  # Função para limpar a tela
        clear()
        print("Parabéns! O numero era {}.".format(numero_secreto))
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.") 
    