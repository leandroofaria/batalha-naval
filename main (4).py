from time import sleep

def escreva(txt): #Titulo bonitinhio
  print('\033[1;34m-\033[m' * (len(txt)+4))
  print(f'  \033[1;34m{txt}\033[m')
  print('\033[1;34m-\033[m' * (len(txt)+4))
  print()

def linhas(num=0): #Linhas
  print()
  print('\033[1;33m=\033[m'*num)
  print()

def mostrarTabuleiro(tabuleiro): #Mostrar tabuleiro
  # sleep(3)
  for linha in range(nLinhas):
    for coluna in range(nColunas):
      print(f'[{tabuleiro[linha][coluna]}]', end= ' ')
    print()

txt = '              BEM VINDO AO BATALHA NAVAL              '
escreva(txt) #Bem vindo

#Tutorial
# sleep(2) 
print('''Tutorial:
- -> Ondas (Espaços Ocultos)
O -> Lugar Errado
X -> Acertou uma parte um barco''')
linhas(60)

#Tipos de barcos
# sleep(2)
print('''Tipos de barcos:
> 3x Porta-Aviões (4 partes) - 30 pontos após destruir
> 4x Cruzadores   (3 partes) - 20 pontos após destruir
> 5x Fragatas     (2 partes) - 10 pontos após destruir
''')
linhas(60)

#Regras
# sleep(2)
print('''Regras:
1- Os pontos só são marcados se acertar todas as partes do barco.
2- Os barcos só ficarão posicionados na horizontal.
3- O jogador 1 define as posições do barco e o jogador 2 tenta acertá-lo''')
linhas(60)


#Jogadores
# sleep(2)
# j1 = str(input('Jogador 1, insira seu nome: '))
# j2 = str(input('Jogador 2, insira seu nome: '))
# print()


#Criação do tabuleiro
nLinhas = nColunas = 15
tabuleiro = ['\033[1;36m~\033[m'] * nLinhas
for linha in range(nLinhas):
  tabuleiro[linha] = ['\033[1;36m~\033[m'] * nColunas

#começar
txt = '''                     VAMOS COMEÇAR                     '''
escreva(txt)

#Mostrar o tabuleiro na tela
mostrarTabuleiro(tabuleiro)

#porta aviões
print()
for cont in range(1,4):
  linha = int(input(f'Insira a linha que irá o {cont}° Porta-Aviões: '))
  coluna = int(input(f'Insira a coluna que irá o {cont}° Porta-Aviões: '))
  tabuleiro[linha][coluna] = 'pa'
  tabuleiro[linha][coluna - 1] = 'pa'
  tabuleiro[linha][coluna + 1] = 'pa'
  print()
# cont = 0
# for linha in range(nLinhas):
#   for coluna in range(nColunas):
#     cont += 1
#     if cont > 3:
#       break
#     else:
#       print()
#       tabuleiro[linha][coluna] = input(f'Insira a posição do {cont}° Porta-Aviões (Linha/Coluna): ')

mostrarTabuleiro(tabuleiro)