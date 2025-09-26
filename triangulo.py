# Receber um tipo de triângulo e definir pontos para sua existência
print('| FORMAÇÃO DE PONTOS |\n| Equilátero - 1 | Isósceles - 2 | Escaleno - 3 |')
# Input principal pra definir a escolha do usuário
escolha = int(input('Que tipo de triângulo você quer analisar? '))
# EQUILÁTERO
if escolha == 1:
    print('Você escolheu um triângulo equilátero!\n3 possíveis conjuntos de pontos são:\nA(0,0) B(1,0) C(0.5,0.866)\nA(-1,0) B(1,0) C(0,1.732)\nA(2,3) B(3,4.732) C(4,3)')
elif escolha == 2:
    print('Você escolheu um triângulo isósceles!\n3 possíveis conjuntos de pontos são:\nA(3,2) B(1,4) C(2,3)\n A(0,0) B(4,0) C(2,3)\nA(-3,-2) B(3,-2) C(0,4)')
elif escolha == 3:
    print('Você escolheu um triângulo escaleno!\n3 possíveis conjuntos de pontos são:\nA((0,0) B(4,3) C(9,6)\nA(4,5) B(6,2) C(4,3)\nA(6,4) B(3,2) C(4,6)')
else:
    print('Entrada inválida')