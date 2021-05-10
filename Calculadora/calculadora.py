operacao = (int(input('Qual operação matemática deseja realizar? | 1 - Soma, 2 - Subtração, 3-Divisão, 4 - Multiplicação, 5 - Raiz, 6 - Potência ')))

if operacao == 1 :
    n1 = (int(input('Digite um número para ser calculado : '  )))
    n2 = (int(input('Digite outro número para ser calculado : '  )))
    print('Soma : ', n1 + n2)    
elif operacao == 2 :
    n1 = (int(input('Digite um número para ser calculado : '  )))
    n2 = (int(input('Digite outro número para ser calculado : '  )))
    print('Subtração : ', n1 - n2)
elif operacao == 3 :
    n1 = (int(input('Digite um número para ser calculado : '  )))
    n2 = (int(input('Digite outro número para ser calculado : '  )))
    print('Divisão : ', n1 / n2) 
elif operacao == 4 :
    n1 = (int(input('Digite um número para ser calculado : '  )))
    n2 = (int(input('Digite outro número para ser calculado : '  )))
    print('Multiplicação : ', n1 * n2)
elif operacao == 5 :
    n1 = (int(input('Digite um número para ser calculado : '  )))
    print('Raiz : ', n1 ** 0.5)
else :
    n1 = (int(input('Digite um número para ser calculado : '  )))
    n2 = (int(input('Digite outro número para ser calculado : '  )))
    print('Potência : ', n1 ** n2)

