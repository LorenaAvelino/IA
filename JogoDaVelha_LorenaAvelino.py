from time import sleep
import sys
import math

def jogador(tabuleiro):
    total_jogadas = 0
    for i in range(0, len(tabuleiro)):
        for j in range(0, len(tabuleiro[i])):
            if tabuleiro[i][j] != 0: total_jogadas+=1

    if total_jogadas % 2 == 0: return True
    else: return False

#Retorna todas as jogadas disponíveis
def acoes(tabuleiro):
    jogadas_disp = [] #jogadas disponiveis
    for i in range(0, len(tabuleiro)):
        for j in range(0, len(tabuleiro[i])):
            if tabuleiro[i][j] == 0: jogadas_disp.append([i, j])
    return jogadas_disp

#Retorna o tabuleiro que resulta ao fazer a jogada i, j
def resultado(tabuleiro, acao):
    novo_tabuleiro = [[], [], []]
    for i in range(0, len(tabuleiro)):
        for j in range(0, len(tabuleiro[i])):
            novo_tabuleiro[i].append(tabuleiro[i][j]) 
    if jogador(tabuleiro): novo_tabuleiro[acao[0]][acao[1]] = 1
    else: novo_tabuleiro[acao[0]][acao[1]] = -1

    return novo_tabuleiro

#Retorna verdadeiro se o jogo acabou, Falso o contrário
def final(tabuleiro):
    if math.fabs(custo(tabuleiro)) == 1 or len(acoes(tabuleiro)) == 0 : return True
    else: return False

#Retorna 1 se X ganhou, -1 se O ganhou, 0 caso contrário.
def custo(tabuleiro):
    for i in range(0, len(tabuleiro)):
            #Linhas e Colunas
        sum_linha = tabuleiro[i][0] + tabuleiro[i][1] + tabuleiro[i][2]
        sum_coluna = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]
        if abs(sum_linha) == 3: return sum_linha / 3
        if abs(sum_coluna) == 3: return sum_coluna / 3
        #Diagonais 
        sum_diagonal = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
        if abs(sum_diagonal) == 3: return sum_diagonal / 3
            
        sum_diagonal = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
        if abs(sum_diagonal) == 3: return sum_diagonal / 3
            
    return 0

#Retorna a jogada ótima oara o jogador atual
def minimax(tabuleiro):
    if jogador(tabuleiro): return maxValor(tabuleiro)[1]
    else: return minValor(tabuleiro)[1]

#Valor máximo
def maxValor(tabuleiro):
    valorMax = float('-inf')
    for acao in acoes(tabuleiro):
        novo_tabuleiro = resultado(tabuleiro, acao)
        if final(novo_tabuleiro):
            valor = custo(novo_tabuleiro)
        else: valor = minValor(novo_tabuleiro)[0]
        if valor > valorMax:
            valorMax = valor
            jogadaMax = acao

    return [valorMax, jogadaMax]

#Valor mínimo
def minValor(tabuleiro):
    valorMin = float('inf')
    for acao in acoes(tabuleiro):
        novo_tabuleiro = resultado(tabuleiro, acao)
        if final(novo_tabuleiro):
            valor = custo(novo_tabuleiro)
        else: valor = maxValor(novo_tabuleiro)[0]
        if valor < valorMin:
            valorMin = valor
            jogadaMin = acao

    return [valorMin, jogadaMin]

def minhaJogada(tabuleiro):
    jogada = int(input("\nDigite um número inteiro de 1 a 9! "))
    if jogada < 0 or jogada > 10:
        linha = 0
        coluna = 0
    else:
        linha = int((jogada-1)/3)
        coluna = (jogada-1) - linha*3
    while jogada <= 0 or jogada >= 10 or tabuleiro[linha][coluna] != 0:
        if jogada <= 0 or jogada >= 10:
            jogada = int(input("\nJogada invalida! Digite um número inteiro de 1 a 9! "))
        linha = int((jogada-1)/3)
        coluna = (jogada-1) - linha*3 
        if tabuleiro[linha][coluna] != 0:
            jogada = int(input("\nPosição ja oculpada! Escolha outra! "))
        
    return resultado(tabuleiro, [linha, coluna])

def mostrarTabuleiro(tabuleiro, j , adv, primeiro):
    if primeiro == 'EU':
        simbol1 = j
        simbol2 = adv
    else:
        simbol1 = adv
        simbol2 = j
    tabela = [[], [], []]
    for i in range(0 , len(tabuleiro)):
        for j in range(0, len(tabuleiro[i])):
            if tabuleiro[i][j] == 1:
                tabela[i].append(simbol1)
            elif tabuleiro[i][j] == -1:
                tabela[i].append(simbol2)
            elif  tabuleiro[i][j] == 0:
                tabela[i].append(' ')
    str = ''''''
    for i in range(0, len(tabela)):
        str = str+'''     |     |   
  {}  |  {}  |  {}
'''.format(tabela[i][0], tabela[i][1], tabela[i][2])
        if i != 2:
            str = str+'''_____|_____|_____
'''
        else:
            str = str+'''     |     |     
'''
    print(str)

pc = 0
usuario = 0
def verificarGanhador(tabuleiro, primeiro):
    global pc
    global usuario
    ganhador = custo(tabuleiro)
    if ganhador == 0:
        print('NÓS EMPATAMOS!\n')
    elif custo(tabuleiro) == 1:
        if primeiro == "EU": 
            print('VOCÊ GANHOU!\n')
            usuario+=1
        else:
            print('EU GANHEI!\n')
            pc+=1
    elif custo(tabuleiro) == -1:
        if primeiro == "EU": 
            print('EU GANHEI!\n')
            pc+=1
        else:
            print('VOCÊ GANHOU!\n')
            usuario+=1
    print("(Usuário: " + str(usuario) + ", PC: " + str(pc) + ")")

def game():
    tabuleiro_inicial = '''
--- COMO JOGAR ---
Quando for sua vez, digite o número correspondente à posição no tabuleiro para fazer sua jogada nela.
Por exemplo, digamos que você queira jogar no centro, então você digita 5.
     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
    '''
    print(tabuleiro_inicial)
    primeiro = ''
    j = ''
    print('Você quer ser o X (xis) ou a O (bola)?', end=' ')

    while j != 'O' and j != 'X':
        j = str(input('Digite X ou O e pressione Enter para escolher: ')).strip().upper()
        if j != 'O' and j != 'X':
            print('\nEscolha inválida!\n')

    if j == 'O':
        adv = 'X'
    elif j == 'X':
        adv = 'O'
    print('\nEntão eu fico com {}.'.format(adv))

    print('\nQuem joga primeiro?', end=' ')

    while primeiro != 'EU' and primeiro != 'PC':
        instr = 'Digite EU e pressione Enter para você começar, ou digite PC e pressione Enter para eu começar: '
        primeiro = str(input(instr)).strip().upper()
        if primeiro != 'EU' and primeiro != 'PC':
            print('\nEscolha inválida!\n')

    if primeiro == 'EU':
        print('\nEntão você joga primeiro.\n')
    elif primeiro == 'PC':
        print('\nEntão eu jogo primeiro.\n')

    tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while not final(tabuleiro):
        if primeiro == 'EU':
            tabuleiro = minhaJogada(tabuleiro) 
            mostrarTabuleiro(tabuleiro, j , adv, primeiro)
            if final(tabuleiro): break
            print('Deixe-me pensar...')
            sleep(1.0)
            tabuleiro = resultado(tabuleiro, minimax(tabuleiro))   
        else:
            print('Deixe-me pensar...')
            sleep(1.0)
            tabuleiro = resultado(tabuleiro, minimax(tabuleiro))
            mostrarTabuleiro(tabuleiro, j , adv, primeiro) 
            if final(tabuleiro): break
            tabuleiro = minhaJogada(tabuleiro) 
        mostrarTabuleiro(tabuleiro, j , adv, primeiro)

    verificarGanhador(tabuleiro, primeiro)
game()
while True:  
    reiniciar = input('\nQuer jogar de novo? Digite S para sim ou N para não: ').lower()
    if reiniciar == 's': game()
    elif reiniciar == 'n': break