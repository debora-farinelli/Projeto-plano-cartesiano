import math

# Solicitação do ponto de origem e quantidade de pontos:
X = int(input('Digite o ponto de origem da coordenada x: '))
Y = int(input('Digite o ponto de origem da coordenada y: '))
quantidade_pontos = int(input('Digite a quantidade de ponto(s): '))

# Atribuição de variáveis:
x1 = X
y1 = Y
maior_ponto = 0
menor_ponto = float('inf')  # Inicialização com valor infinito
quadrante_1 = 0
quadrante_2 = 0
quadrante_3 = 0
quadrante_4 = 0
cont = 1

# Solicitação das coordenadas dos pontos e fórmula da distância:
while cont <= quantidade_pontos:
    x = int(input(f'Digite a coordenada x do ponto {cont}: '))
    y = int(input(f'Digite a coordenada y do ponto {cont}: '))
    formula_distancia = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)

    # Localização das coordenadas nos quadrantes e adição para contagem de
    # quantos pontos tem em cada quadrantes:
    if x == x1 or y == y1:
        print(f'O ponto {x, y} está sobre o eixo de coordenadas')
    elif x > 0 and y > 0:
        print(f'O ponto {x, y} está no 1º quadrante')
        quadrante_1 += 1
    elif x < 0 and y > 0:
        print(f'O ponto {x, y} está no 2º quadrante')
        quadrante_2 += 1
    elif x < 0 and y < 0:
        print(f'O ponto {x, y} está no 3º quadrante')
        quadrante_3 += 1
    elif x > 0 and y < 0:
        print(f'O ponto {x, y} está no 4º quadrante')
        quadrante_4 += 1
    elif x == 0 and y == 0:
        print(f'O ponto {x, y} está na coordenada de origem do plano cartesiano')

    # Maior e menor ponto de distância:
    if formula_distancia >= maior_ponto:
        maior_ponto = formula_distancia
        X_maior_ponto = x
        Y_maior_ponto = y
    if formula_distancia < menor_ponto:
        menor_ponto = formula_distancia
        X_menor_ponto = x
        Y_menor_ponto = y

    cont += 1

print(f'O ponto de menor distância é ({X_menor_ponto},{Y_menor_ponto}), distância: {"%.2f" % menor_ponto}')
print(f'O ponto de maior distância é ({X_maior_ponto},{Y_maior_ponto}), distância: {"%.2f" % maior_ponto}')
print(f'Existem {quadrante_1} ponto(s) no primeiro quadrante, {quadrante_2} no segundo quadrante, {quadrante_3} no terceiro quadrante, e {quadrante_4} no quarto quadrante')

# PARTE B:
# Separação da parte A da parte B:
print('------------------------------------------------------------------')

# Solicitação das coordenadas do robô e do tempo:
pontoX = int(input('Digite as coordenadas de origem x do robô: '))
pontoY = int(input('Digite as coordenadas de origem y do robô: '))
tempo = int(input('Digite o tempo total que o robô irá caminhar em segundos: '))

# Cálculos:
movimentoX = tempo // 3
tempo_sobraX = tempo % 3
movimentoY = tempo // 3
tempo_sobraY = tempo % 3

# Movimento do robô:
movimento_roboX = 2 * movimentoX
movimento_roboY = movimentoY + tempo_sobraY

# Coordenadas finais:
totalX = pontoX + movimento_roboX
totalY = pontoY + movimento_roboY
print(f'Ao final da caminhada o robô estará no ponto {totalX, totalY} do plano cartesiano')
