from glob import escape


def criar_tabuleiro():                          #Criar tabuleiro
  tabuleiro = ['\033[1;36;~\033[m'] * nLinhas
  for linha in range(nLinhas):
    tabuleiro[linha] = ['\033[1;36;44m~\033[m'] * nColunas
  return tabuleiro

def mostrar_tabuleiro(tabuleiro):               #Mostrar tabuleiro
  for linha in range(nLinhas):
    for coluna in range(nColunas):
      print(f'[{tabuleiro[linha][coluna]}]', end= ' ')
    print()

def barco_no_tabuleiro(inicio, fim, barco):     #Salvar as posições dos barcos no tabuleiro
  for cont in range(inicio, fim):
    global linha
    global coluna

    linha = int(input(f'Insira a linha que irá o {cont}° {barco}: '))
    while 0>linha or linha>=20:
      print('\033[1;31mOpção inválida! O máximo de linhas no tabuleiro são 19!\033[m')
      linha = int(input(f'Insira a linha que irá o {barco}: '))

    coluna = int(input(f'Insira a coluna que irá o {cont}° {barco}: '))
    while 0>coluna or coluna>=20:
      print('\033[1;31mOpção inválida! O máximo de colunas no tabuleiro são 19!\033[m')
      coluna = int(input(f'Insira a coluna que irá o Porta-Aviões: '))
      
    if barco == "Porta-Aviões":
      if coluna<=16:
        tabuleiro[linha][coluna] = '\033[33mP\033[m'
        tabuleiro[linha][coluna + 1] = '\033[33mP\033[m'
        tabuleiro[linha][coluna + 2] = '\033[33mP\033[m'
        tabuleiro[linha][coluna + 3] = '\033[33mP\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna+1), 
                      str(linha)+str(coluna+2), 
                      str(linha)+str(coluna+3)]
        print(f'Posições: {temporaria}')
        posicoes_pa.append(temporaria[:])
        todas_posicoes.append(temporaria[:])
        print()

      elif coluna == 17:
        tabuleiro[linha][coluna] = '\033[33mP\033[m'
        tabuleiro[linha][coluna + 1] = '\033[33mP\033[m'
        tabuleiro[linha][coluna + 2] = '\033[33mP\033[m'
        tabuleiro[linha][coluna - 1] = '\033[33mP\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna+1), 
                      str(linha)+str(coluna+2), 
                      str(linha)+str(coluna-1)]
        print(f'Posições: {temporaria}')
        posicoes_pa.append(temporaria[:])
        todas_posicoes.append(temporaria[:])
        print()

      elif coluna == 18:
        tabuleiro[linha][coluna] = '\033[33mP\033[m'
        tabuleiro[linha][coluna + 1] = '\033[33mP\033[m'
        tabuleiro[linha][coluna - 2] = '\033[33mP\033[m'
        tabuleiro[linha][coluna - 1] = '\033[33mP\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna+1), 
                      str(linha)+str(coluna-2), 
                      str(linha)+str(coluna-1)]
        print(f'Posições: {temporaria}')
        posicoes_pa.append(temporaria[:])
        todas_posicoes.append(temporaria[:])
        print()

      elif coluna == 19:
        tabuleiro[linha][coluna] = '\033[33mP\033[m'
        tabuleiro[linha][coluna - 1] = '\033[33mP\033[m'
        tabuleiro[linha][coluna - 2] = '\033[33mP\033[m'
        tabuleiro[linha][coluna - 3] = '\033[33mP\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna-1), 
                      str(linha)+str(coluna-2), 
                      str(linha)+str(coluna-3)]
        print(f'Posições: {temporaria}')
        posicoes_pa.append(temporaria[:])
        todas_posicoes.append(temporaria[:])
        print()

        

    elif barco == "Cruzador":
      if coluna <= 17:
        tabuleiro[linha][coluna] = '\033[35mC\033[m'
        tabuleiro[linha][coluna + 1] = '\033[35mC\033[m'
        tabuleiro[linha][coluna + 2] = '\033[35mC\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna+1), 
                      str(linha)+str(coluna+2)] 
        print(f'Posições: {temporaria}')
        posicoes_c.append(temporaria[:])
        print()

      elif coluna == 18:
        tabuleiro[linha][coluna] = '\033[35mC\033[m'
        tabuleiro[linha][coluna + 1] = '\033[35mC\033[m'
        tabuleiro[linha][coluna - 1] = '\033[35mC\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna+1), 
                      str(linha)+str(coluna-1)] 
        print(f'Posições: {temporaria}')
        posicoes_c.append(temporaria[:])
        print()

      elif coluna == 19:
        tabuleiro[linha][coluna] = '\033[35mC\033[m'
        tabuleiro[linha][coluna - 1] = '\033[35mC\033[m'
        tabuleiro[linha][coluna - 2] = '\033[35mC\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna-1), 
                      str(linha)+str(coluna-2)] 
        print(f'Posições: {temporaria}')
        posicoes_c.append(temporaria[:])
        print()


    elif barco == "Fragata":
      if coluna <= 18:
        tabuleiro[linha][coluna] = '\033[32mF\033[m'
        tabuleiro[linha][coluna + 1] = '\033[32mF\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna+1)] 
        print(f'Posições: {temporaria}')
        posicoes_f.append(temporaria[:])
        print()

      elif coluna == 19:
        tabuleiro[linha][coluna] = '\033[32mF\033[m'
        tabuleiro[linha][coluna - 1] = '\033[32mF\033[m'
        temporaria = [str(linha)+str(coluna), 
                      str(linha)+str(coluna+1)] 
        print(f'Posições: {temporaria}')
        posicoes_f.append(temporaria[:])
        print()

def errou_ou_acertou(acertou):
  if acertou == True:
    tabuleiro2[escolha_linha][escolha_coluna] = '\033[1;32mX\033[m'
  elif acertou == False:
    tabuleiro2[escolha_linha][escolha_coluna] = '\033[1;33mO\033[m'
  mostrar_tabuleiro(tabuleiro2)

#Programa principal
nLinhas = nColunas = 20           #Matriz
turnos = 50                       #Número de turnos pro jogador 2 tentar acertar
tabuleiro = criar_tabuleiro()     #Tabuleiro do jogador 1
tabuleiro2 = criar_tabuleiro()    #Tabuleiro que vai aparecer para o jogador 2
posicoes_pa = []                  #Lista com as posições dos porta aviões
posicoes_c = []                   #Lista com as posições dos cruzadores
posicoes_f = []                   #Lista com as posições dos fragatas
temporaria = []                   #Lista temporária com as posições (só pra copiar pra lista das posições)
todas_posicoes = []               #?

#FIXME Jogador 1
mostrar_tabuleiro(tabuleiro)                #Mostra o tabuleiro
barco_no_tabuleiro(1,4,"Porta-Aviões")      #Salva as posições dos porta aviões
barco_no_tabuleiro(1,5,"Cruzador")          #Salva as posições dos cruzadores
barco_no_tabuleiro(1,6,"Fragata")           #Salva as posicoes dos fragatas
mostrar_tabuleiro(tabuleiro)                #Mostra o tabuleiro com o barco nas devidas posições

#FIXME Jogador 2
print('----------------- JOGADOR 2')
mostrar_tabuleiro(tabuleiro2)     #Mostra o tabuleiro do segundo jogador (sem os barcos)
while turnos > 0:
  escolha_linha = int(input('Linha que você quer jogar a bomba: '))     #Linha onde vai a bomba
  while 0>escolha_linha or escolha_linha>19:                            #Verificação da linha
    print('A menor linha é a 0 e a maior é a 19!')
    escolha_linha = int(input('Linha que você quer jogar a bomba: '))

  escolha_coluna = int(input('Coluna que você quer jogar a bomba: '))   #Coluna onde vai a bomba
  while 0>escolha_coluna or escolha_coluna>19:                          #Verificação da coluna
    print('A menor coluna é a 0 e a maior é a 19!')
    escolha_coluna = int(input('Coluna que você quer jogar a bomba: '))

  juntos = str(escolha_linha)+str(escolha_coluna)    #Forma uma coordenada em string da posição da bomba
  entrou = False                                     #Flag pro if

  for barco in range(3):                             #Verificar cada barco na lista dos porta aviões
    for parte in range(4):                           #Verificar cada parte de cada barco
       if posicoes_pa[barco][parte] == juntos:       #Substituir com um x no tabuleiro caso tenha acertado
        print('Acertou')
        entrou = True
        acertou = True
        errou_ou_acertou(acertou)
        break

  if entrou == False:                                #Substituir com um O no tabuleiro caso tenha errado
    print('Errou')
    turnos -= 1
    print(f'Você tem {turnos} turnos restantes')
    acertou = False
    errou_ou_acertou(acertou)