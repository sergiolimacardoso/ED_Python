print("Sistema de emprestimos")
print("Verifique se o cliente está com o nome Positivo ou Negativado")
print("-----------------------------------------------------------------")

cliente = input("informe o nome do cliente ")
print("Seja bem vindo.", cliente)
carteiraAssinada = int(input("Possui carteira assinada? Digite 0 para não e 1 para sim "))
nomeNegativado = int(input("Possui nome Negativado no mercado? Digite 0 para não e 1 para sim "))
recebeAuxilio = int(input("Você recebe Auxilio do governo? Digite 0 para não e 1 para sim "))
dependentes = int(input("Você possui dependentes? Digite 0 para não e 1 para sim "))


if carteiraAssinada == 0:
    print("Você não tem emprestimos liberados.")
    
elif nomeNegativado == 1:
    print("Você não tem emprestimos liberados.")

elif recebeAuxilio == 0:
    print("Você não tem emprestimos liberados.")

elif dependentes == 1:
    print("Você não tem emprestimos liberados.")

#elif carteiraAssinada == 1 & nomeNegativado == 0 & recebeAuxilio == 1 & dependentes == 0:
#        print("Parabnens!. Você tem um emprestimo liberado")

else:
    print("Parabens. Você possui emprestimos liberado.")