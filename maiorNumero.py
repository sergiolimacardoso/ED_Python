valor1 = input("digite o numero ")
valor2 = input("digite o numero ")
valor3 = input("digite o numero ")
valor4 = input("digite o numero ")
valor5 = input("digite o numero ")

if valor1 == 0 and valor2 == 0 and valor3 == 0 and valor4 == 0 and valor5 == 0:
    
    maior_numero = max(valor1, valor2, valor3, valor4, valor5)
    
    print("o maior numero digitado é: ", maior_numero)
    
else:
    print("Insira números maior que 0. Refaça a operação")  