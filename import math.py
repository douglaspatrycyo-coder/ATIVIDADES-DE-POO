import math
# Entrada do usuário, se deseja analisar 3 ou 4 pontos 
print('| ANÁLISE DE PONTOS |')
escolha = int(input('Deseja analisar 3 ou 4 pontos? '))
# Se o usuário escolher analisar 3 pontos 
if escolha == 3:
    # Entrada de pontos (X,Y)
    x1 = float(input('Digite o valor de X da primeira coordenada: '))
    y1 = float(input('Digite o valor de Y da primeira coordenada: '))
    x2 = float(input('Digite o valor de X da segunda coordenada: '))
    y2 = float(input('Digite o valor de X da segunda coordenada: '))
    x3 = float(input('Digite o valor de X da terceira coordenada: '))
    y3 = float(input('Digite o valor de X da terceira coordenada: '))
    # Cálculo da distância entre pontos
    lAB = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    lAC = math.sqrt((x3-x1)**2 + (y3-y1)**2)
    lBC = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    # Análise se esse triângulo existe ou não, se existir, que tipo de triângulo é 
    if lAB + lAC > lBC or lAB + lBC > lAC or lBC + lAC > lAB:
        if math.isclose(lAB,lAC, rel_tol=1e-9) and math.isclose(lAB,lBC, rel_tol=1e-9):
            tipo = 'Equilátero'
        elif (math.isclose(lAB, lAC, rel_tol=1e-9) or math.isclose(lAB, lBC, rel_tol=1e-9) or math.isclose(lAC, lBC, rel_tol=1e-9)):
            tipo = 'Isósceles'
        else:
            tipo = 'Escaleno'
        print(f'Esse triângulo existe e ele é {tipo}')
    else:
        print('Esse triângulo não existe')
# Se o usuário escolher analisar 4 pontos 
elif escolha == 4:
    # Entrada de pontos (X,Y)
    print('Coloque os pontos de forma ordenada, respeitando a proximidade dos mesmos')
    x1 = float(input('Digite o valor de X da primeira coordenada: '))
    y1 = float(input('Digite o valor de Y da primeira coordenada: '))
    x2 = float(input('Digite o valor de X da segunda coordenada: '))
    y2 = float(input('Digite o valor de Y da segunda coordenada: '))
    x3 = float(input('Digite o valor de X da terceira coordenada: '))
    y3 = float(input('Digite o valor de Y da terceira coordenada: '))
    x4 = float(input('Digite o valor de X da quarta coordenada: '))
    y4 = float(input('Digite o valor de Y da quarta coordenada: '))
     # Cálculo da distância entre pontos 
     #LADOS
    lAB = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    lCD = math.sqrt((x4-x3)**2 + (y4-y3)**2)
    lBC = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    lAD = math.sqrt((x4-x1)**2 + (y4-y1)**2)
    #DIAGONAIS
    dAC = math.sqrt((x3-x1))**2 + (y3-y1)**2
    dBD = math.sqrt((x4-x2))**2 +  (y4-y2)**2
    if math.isclose(lAB, lBC) and math.isclose(lBC, lCD) and math.isclose(lCD, lAD) and math.isclose(dAC, dBD):
        print("Os pontos formam um Quadrado.")
    elif math.isclose(lAB, lCD) and math.isclose(lBC, lAD) and math.isclose(dAC, dBD):
        print("Os pontos formam um Retângulo.")
    else:
        print("Os pontos formam um Quadrilátero qualquer.")