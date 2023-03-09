##Desafio: Dada a sequência de Fibonacci, verificar se um valor aleatório informado pelo usuário está na sequência

##Sequência de fibonacci
a = 0
y = 1
lista = []

def fibonacci ():
    contador = int(input("Insira quantos números da sequência serão calculados: "))
    lista.append(a)
    lista.append(y)
    for cont in range(1, contador - 1):
        x = lista[cont] + lista[cont-1]
        lista.append(x)
fibonacci()

##Entrada do usuário e busca na lista
valor = int(input("Informe um número: "))
for cont2 in lista:
    if (valor == cont2):
        print("O valor está na sequência informada")
        break
if (valor != cont2):
    print("O valor não está na sequência informada")




