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

    linha = int(input(f'\nInsira a \033[1;33mlinha\033[m que irá o \033[1;33m{cont}° {barco}\033[m: '))
    while 0>linha or linha>=20:
      print('\033[1;31mOpção inválida! O máximo de linhas no tabuleiro são 19!\033[m')
      linha = int(input(f'Insira a \033[1;33mlinha\033[m que irá o {barco}: '))

    coluna = int(input(f'Insira a \033[1;33mcoluna\033[m que irá o \033[1;33m{cont}° {barco}\033[m: '))
    while 0>coluna or coluna>=20:
      print('\033[1;31mOpção inválida! O máximo de colunas no tabuleiro são 19!\033[m')
      coluna = int(input(f'Insira a \033[1;33mcoluna\033[m que irá o {cont}° {barco}: '))
      
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

def acertou_barco(linha, coluna):               #Completa a função de cima, contando as pontuações
  global cont_cruzadores, cont_fragatas, cont_portavioes, pontos, cruzadores_destruidos, portavioes_destruidos, fragatas_destruidos
  
  if tabuleiro[linha][coluna] == '\033[1;36;~\033[m':
    print('Errou')
    tabuleiro2[linha][coluna] = '\033[1;35mO\033[m'
    return False
  else:
    print('Acertou')
    tabuleiro2[linha][coluna] = '\033[1;32mX\033[m'
    if tabuleiro[linha][coluna] == '\033[35mC\033[m':
      cont_cruzadores += 1
      if (cont_cruzadores % 3) == 0:
        print('\033[1;32m\n-> Você marcou 20 pontos!\033[m')
        cruzadores_destruidos += 1
        pontos += 20
    
    elif tabuleiro[linha][coluna] == '\033[33mP\033[m':
      cont_portavioes += 1
      if (cont_portavioes % 4) == 0:
        print('\033[1;32m\n-> Você marcou 30 pontos!\033[m')
        portavioes_destruidos += 1
        pontos += 30

    elif tabuleiro[linha][coluna] == '\033[32mF\033[m':
      cont_fragatas += 1
      if (cont_fragatas % 2 ) == 0:
        print('\033[1;32m\n-> Você marcou 10 pontos!\033[m')
        fragatas_destruidos += 1
        pontos += 10

    return True

def estatisticas():                             #Mostra as estatísticas do jogo
  global cont_cruzadores, cont_fragatas, cont_portavioes, pontos, cruzadores_destruidos, portavioes_destruidos, fragatas_destruidos
  print(f'''\033[1;33mEstatísticas: \033[m
  -> \033[1;32mVocê marcou {pontos} pontos no total, parabéns!
  -> Você destruiu {portavioes_destruidos} Porta-Aviões!
  -> Você destruiu {cruzadores_destruidos} Cruzadores!
  -> Você destriu {fragatas_destruidos} Fragatas!\033[m''')

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
cont_cruzadores = cont_portavioes = cont_fragatas = pontos = cruzadores_destruidos = portavioes_destruidos = fragatas_destruidos = 0         #variaveis


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
  escolha_linha = int(input('\033[1;33mLinha que você quer jogar a bomba: \033[m'))     #Linha onde vai a bomba
  while 0>escolha_linha or escolha_linha>19:                            #Verificação da linha
    print('\033[1;31mA menor linha é a 0 e a maior é a 19!\033[m')
    escolha_linha = int(input('Linha que você quer jogar a bomba: '))

  escolha_coluna = int(input('\033[1;33mColuna que você quer jogar a bomba: \033[m'))   #Coluna onde vai a bomba
  while 0>escolha_coluna or escolha_coluna>19:                          #Verificação da coluna
    print('\033[1;31mA menor coluna é a 0 e a maior é a 19!\033[m')
    escolha_coluna = int(input('Coluna que você quer jogar a bomba: '))

  juntos = str(escolha_linha)+str(escolha_coluna)    #Forma uma coordenada em string da posição da bomba
  entrou = False                                     #Flag pro if
   
  acertou_barco(escolha_linha,escolha_coluna)
  mostrar_tabuleiro(tabuleiro2)

  desistir = str(input('\033[1;31m\n-> Você deseja desistir? (s/n)\033[m')).strip().lower()[0]
  if desistir in 's':
    turnos = 0

  if turnos == 0:
    print('\033[1;31m\n -> Seus turnos acabaram\033[m')
    estatisticas()