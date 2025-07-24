#lemnbre-se de sempre verificar o valor testado se é int ou string

#print("Verifica Lâmpada")

#lampada = int(input("Escolha os valores  0 para desligada e 1 para Ligada "))

#aqui usamos int e roda normal
#if lampada == 0:
#    print("lâmpada desligada. ", lampada)
#elif lampada == 1:
#    print("lâmpada ligada. ", lampada)
#else:
#    print("impossivel verificar a lâmpada. ", lampada)
    
print("Verifica Lâmpada")

lampada = input("Escolha os valores  0 para desligada e 1 para Ligada ")
#aqui usamos string e roda normal
if lampada == "0":
    print("lâmpada desligada. ", lampada)
elif lampada == "1":
    print("lâmpada ligada. ", lampada)
else:
    print("impossivel verificar a lâmpada. ", lampada)
