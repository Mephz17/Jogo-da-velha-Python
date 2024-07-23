import random
# Definindo uma matriz 3x3
def definindo_matriz():
    global matriz_jogo
    matriz_jogo = [[i for i in range(1, 4)] for j in range(3)]
    i = 1 
    coluna = 0
    variante = 1
    contador = 0 
    while True:
        matriz_jogo[i][coluna] = matriz_jogo[0][2] + variante
        variante += 1 
        coluna += 1 
        contador += 1 
        if contador % 3 == 0:
            i += 1 
            coluna = 0
        if variante > 6:
            break

# Definindo o display do jogo
def display_jogo():
    print('+-------+-------+-------+')
    coluna = 0 
    linha = 0 
    while True:
        print(f'|   {matriz_jogo[linha][coluna]}   |   {matriz_jogo[linha][coluna + 1]}   |   {matriz_jogo[linha][coluna + 2]}   |')
        linha += 1 
        if linha > 2:
            break
    print('+-------+-------+-------+')
# Definindo as regras da jogada e incrementando a jogada do usuário no indice da matriz correspondente 
def jogada_usuario():
    jogada = int(input('Digite seu movimento: '))
    linha = 0
    for i in matriz_jogo:
        if jogada in i:
            coluna = i.index(jogada)
            break
        linha += 1 
    if linha > 2:
        linha = 2 
    matriz_jogo[linha][coluna] = 'O'
# Avaliando a jogada do computador. Mesmo processo
def jogada_computador():
    jogada = random.randint(1, 9)
    linha = 0
    coluna = 0
    for i in matriz_jogo:
        if jogada in i:
            coluna = i.index(jogada)
            break
        linha += 1 
    if linha > 2:
        linha = 2  
    if coluna == 0:
        return jogada_computador()
    else:
       matriz_jogo[linha][coluna] = 'X'
       return display_jogo()
# Avaliando possibilidades de vitoria do computador
def vitoria_computador():
    if matriz_jogo[0][0] == 'X' and matriz_jogo[0][1] == 'X' and matriz_jogo[0][2] == 'X':
        return True
    elif matriz_jogo[0][0] == 'X' and matriz_jogo[1][0] == 'X' and matriz_jogo[2][0] == 'X':
        return True
    elif matriz_jogo[0][1] == 'X' and matriz_jogo[1][1] == 'X' and matriz_jogo[2][1] == 'X':
        return True
    elif matriz_jogo[0][2] == 'X' and matriz_jogo[1][2] == 'X' and matriz_jogo[2][2] == 'X':
        return True
    elif matriz_jogo[1][0] == 'X' and matriz_jogo[1][1] == 'X' and matriz_jogo[1][2] == 'X':
        return True
    elif matriz_jogo[2][0] == 'X' and matriz_jogo[2][1] == 'X' and matriz_jogo[2][2] == 'X':
        return True
    elif matriz_jogo[0][0] == 'X' and matriz_jogo[1][1] == 'X' and matriz_jogo[2][2] == 'X':
        return True
    elif matriz_jogo[0][2] == 'X' and matriz_jogo[1][1] == 'X' and matriz_jogo[2][0] == 'X':
        return True
    else:
        return False
# Avaliando possibilidades de vitória do usuario
def vitoria_usuario():
    if matriz_jogo[0][0] == 'O' and matriz_jogo[0][1] == 'O' and matriz_jogo[0][2] == 'O':
        return True
    elif matriz_jogo[0][0] == 'O' and matriz_jogo[1][0] == 'O' and matriz_jogo[2][0] == 'O':
        return True
    elif matriz_jogo[0][1] == 'O' and matriz_jogo[1][1] == 'O' and matriz_jogo[2][1] == 'O':
        return True
    elif matriz_jogo[0][2] == 'O' and matriz_jogo[1][2] == 'O' and matriz_jogo[2][2] == 'O':
        return True
    elif matriz_jogo[1][0] == 'O' and matriz_jogo[1][1] == 'O' and matriz_jogo[1][2] == 'O':
        return True
    elif matriz_jogo[2][0] == 'O' and matriz_jogo[2][1] == 'O' and matriz_jogo[2][2] == 'O':
        return True
    elif matriz_jogo[0][0] == 'O' and matriz_jogo[1][1] == 'O' and matriz_jogo[2][2] == 'O':
        return True
    elif matriz_jogo[0][2] == 'O' and matriz_jogo[1][1] == 'O' and matriz_jogo[2][0] == 'O':
        return True
    else:
        return False
# Código em si.
definindo_matriz()
display_jogo()
cont = 0
while True:
    jogada_usuario()
    verificando_usuario = vitoria_usuario()
    if verificando_usuario == True:
        display_jogo()
        print('Parabéns. Você venceu!!')
        termino = input(' ')
        break
    if cont > 4:
        print('Empate')
        break
    jogada_computador()
    verificando_computador = vitoria_computador() 
    if verificando_computador == True:
        print('Infelizmente você perdeu')
        termino = input(' ')
        break
    cont += 1 


