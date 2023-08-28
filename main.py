arq = open("arquivo.txt")
arquivo = arq.readlines()
linha = arquivo.split("\n")

estadoInicial = ""

estadoInicial = linha[0]
alfabeto = linha[1].split(" ")
estados = linha[2].split(" ")
estadosFinais = linha[3].split(" ")
nodos = linha[4:]

# print("Estado Inicial:", estadoInicial)
# print("Alfabeto:", alfabeto)
# print("Estados:", estados)
# print("Estados Finais:", estadosFinais)
# print("Nodos:", nodos)

palavra = input("Informe a palavra: ")

atual = estadoInicial


def procuraEstados(estado, letra):
  for nodo in nodos:
    n = nodo.split(" ")
    if n[0] == estado and letra == n[2]:
      return n[1]
  return None


print("estado atual " + atual)

i = -1
for letra in palavra:
  i += 1
  atual = procuraEstados(atual, letra)
  if atual is None:
    print("Palavra invalida \n ")
    break
  else:
    print(atual + ", " + letra)
    if i != len(palavra) - 1:
      print("Para")
    else:
      if atual in estadosFinais:
        print("\n Aceita ")
      else:
        print("\n Rejeita")
