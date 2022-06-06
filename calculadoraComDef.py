from funcsCalc import *


linha()
print('calculadora python'.center(35))
linha()

while True:
    print('Qual opção você deseja realizar ?')
    print('1 - SOMAR')
    print('2 - SUBTRAIR')
    print('3 - MULTIPLICAR')
    print('4 - DIVIDIR')
    print('5 - SAIR')
    opc = int(input('Escolha a opção que deseja '))

    if opc == 5:
        print('BYE - BYE')
        break

    n1 = int(input('Primeiro numero'))
    n2 = int(input('Segundo numero'))

    if opc == 1:
        soma(n1,n2)

    elif opc == 2:
        sub(n1,n2)

    elif opc == 3:
        mult(n1,n2)

    elif opc == 4:
        div(n1,n2)

