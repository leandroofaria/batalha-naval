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

def criarTabuleiro(): #Criar tabuleiro
  tabuleiro = ['\033[1;36;~\033[m'] * nLinhas
  for linha in range(nLinhas):
    tabuleiro[linha] = ['\033[1;36;44m~\033[m'] * nColunas
  return tabuleiro

def mostrarTabuleiro(tabuleiro): #Mostrar tabuleiro
  # sleep(3)

  for linha in range(nLinhas):
    for coluna in range(nColunas):
      print(f'[{tabuleiro[linha][coluna]}]', end= ' ')
    print()

def barcoTabuleiro(inicio,fim,barco): #Escolher as posiçoes no tabuleiro
  print()
  for cont in range(inicio,fim):
    global linha
    global coluna

    linha = int(input(f'Insira a linha que irá o {cont}° {barco}: '))
    verificarLinha(barco)

    coluna = int(input(f'Insira a coluna que irá o {cont}° {barco}: '))
    verificarColuna(barco)

    salvarPosicoes(barco)

    if barco == "Porta-Aviões":
      tabuleiro[linha][coluna] = '\033[33mP\033[m'
      tabuleiro[linha][coluna - 1] = '\033[33mP\033[m'
      tabuleiro[linha][coluna + 1] = '\033[33mP\033[m'
      tabuleiro[linha][coluna + 2] = '\033[33mP\033[m'

    elif barco == "Cruzador":
      tabuleiro[linha][coluna] = '\033[35mC\033[m'
      tabuleiro[linha][coluna - 1] = '\033[35mC\033[m'
      tabuleiro[linha][coluna + 1] = '\033[35mC\033[m'

    elif barco == "Fragata":
      tabuleiro[linha][coluna] = '\033[32mF\033[m'
      #tabuleiro[linha][coluna - 1] = '\033[32;40mC\033[m'
      tabuleiro[linha][coluna + 1] = '\033[32mF\033[m'

  mostrarTabuleiro(tabuleiro)

def verificarLinha(barco): #Ver se o input foi correto
  global linha
  while 0>linha or linha>15:
    print('\033[1;31mOpção inválida! O máximo de linhas no tabuleiro são 15!\033[m')
    linha = int(input(f'Insira a linha que irá o {barco}: '))

def verificarColuna(barco): #Ver se o input foi correto
  global coluna
  while 0>coluna or coluna>15:
    print('\033[1;31mOpção inválida! O máximo de colunas no tabuleiro são 15!\033[m')
    coluna = int(input(f'Insira a coluna que irá o Porta-Aviões: '))

def salvarPosicoes(barco): #Salvar as posições
  if barco == "Porta-Aviões":
    temporaria = [[linha, coluna],[linha, coluna-1],[linha, coluna+1],[linha, coluna+2]]
    print(f'Posições: {temporaria}')
    posicoes_pa.append(temporaria)
    print()
  elif barco == "Cruzador":
    temporaria = [[linha, coluna],[linha, coluna-1],[linha, coluna+1]]
    print(f'Posições: {temporaria}')
    posicoes_c.append(temporaria)
    print()
  elif barco == "Fragata":
    temporaria = [[linha, coluna],[linha, coluna+1]]
    print(f'Posições: {temporaria}')
    posicoes_f.append(temporaria)
    print()

#variaveis
posicoes_pa = []
posicoes_c = []
posicoes_f = []
temporaria = []

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
tabuleiro = criarTabuleiro()
tabuleiro2 = criarTabuleiro()

#j1
txt = '''                       JOGADOR 1                       '''
escreva(txt)

#Mostrar o tabuleiro na tela
mostrarTabuleiro(tabuleiro)

#porta aviões
print()
barcoTabuleiro(1,4,"Porta-Aviões")

#Cruzadores:
print()
barcoTabuleiro(1,5,"Cruzador")

#Fragatas
print()
barcoTabuleiro(1,6,"Fragata")

print(f'''\n Essas são suas posições:
Porta-Aviões: {posicoes_pa} 
Cruzadores:   {posicoes_c}
Fragatas:     {posicoes_f}''')

#sleep(5) #adcionar um for para contaagem regressiva

txt = '''                       JOGADOR 2                       '''
escreva(txt)

mostrarTabuleiro(tabuleiro2)

escolhaLinha = int(input('Linha que você quer jogar a bomba: '))
escolhaColuna = int(input('Coluna que você quer jogar a bomba: '))
