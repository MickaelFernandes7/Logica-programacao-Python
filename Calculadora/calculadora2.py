def calculadora() :
    operacao = (int(input('Qual operação matemática deseja realizar? | 1 - Soma, 2 - Subtração, 3-Divisão, 4 - Multiplicação, 5 - Raiz, 6 - Potência ')))
    numeros = []

    for n in range(0,2) :
        numeros.append(int(input('Digite os números que deseja calcular : ')))


    if operacao == 1 :
        print('Soma : ', numeros[0] + numeros[1])    
    elif operacao == 2 :
        print('Subtração : ', numeros[0] - numeros[1])
    elif operacao == 3 :
        print('Divisão : ', numeros[0] / numeros[1]) 
    elif operacao == 4 :
        print('Multiplicação : ', numeros[0] * numeros[1])
    elif operacao == 5 :
        print('Raiz : ', numeros[0] ** 0.5)
    else :
        print('Potência : ', numeros[0] ** numeros[1])
    
calculadora()