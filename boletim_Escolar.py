
print("A média de Frequência é maior ou igual a 6.0")
print("A Média para passar de ano é maior ou igual a 6.0")
print("----------------------------------------------------")
nota1 = float(input("Informe a nota do bimestre 1 (1-10): "))
nota2 = float(input("Informe a nota do bimestre 2 (1-10): "))
freq = float(input("Informe a Frequência 3 (0-10): "))


media = (nota1 + nota2) / 2


if nota1 > 10:
    print("Informe um número entre 1 e 10")

elif nota2 > 10:
    print("Informe um número entre 1 e 10")

elif freq < 6 :
    print("Aluno reprovado por faltas ", freq, "e Média ", media)
    
elif freq > 10:
    print("Numero inválido ", freq)
    
elif media >= 6:
    print("alunos aprovado com Média ", media , "e Frequência", freq)
    
elif media > 10:
    print("Numero inválido ", media)

else:
    print("não foi possivel calcular a nota")

#falta o else que poderia ser uma mensagem informando que não foi possível calcular     