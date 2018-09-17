import random

palavras = []
cont = 0
rodar = "s"
palavra = 0
while rodar == "s":
    rodar = str.lower(input("Quer gerar outra wordlist? (S/N) "))
    if rodar != "s":
        break
    print("Para parar de entrar com palavras, digite -101")
    while palavra != "-101":
        cont +=1
        palavra = input("Entre com a palavra: ")
        if palavra == "-101":
            break
        else:
            palavras.append(palavra)
    senhas = int(input("Quantas senhas você quer? "))
    digitos = int(input("Quantos dígitos? "))
    wordlist = []
    lista1 = []
    lista2 = []
    lista1 = palavras
    lista2 = palavras
    palavras.sort
    lista1.sort(reverse=True)
    lista2.reverse()
    for i in range(senhas):
        word = random.choice(palavras)+random.choice(lista1)
        while len(word) < digitos:
            word += random.choice(lista2)
        wordlist.append(word)
    arq = open("wordlist.txt", "w")
    for x in wordlist:
        arq.write(x)
        arq.write("\n")
        arq.close
