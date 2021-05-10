operacao = (int(input('Qual operação matemática deseja realizar? | 1 - Soma, 2 - Subtração, 3-Divisão, 4 - Multiplicação, 5 - Raiz, 6 - Potência ')))

numeros = []
for n in range(0,2) :
    numeros.append(int(input('Digite os números que deseja calcular : ')))

def soma(numeros) :
    print('Soma : ' , numeros[0] + numeros[1])
    

def subtracao(numeros) :
    print('Subtração : ', numeros[0] - numeros[1])

def divisao(numeros) :
    print('Divisão : ', numeros[0] / numeros[1]) 

def multiplicacao(numeros) :
    print('Multiplicação : ', numeros[0] * numeros[1])

def raiz(numeros) :
    print('Raiz : ', numeros[0] ** 0.5 , ' 1° Número Digitado : ' , numeros[0], )
    print('Raiz : ', numeros[1] ** 0.5 , ' 2° Número Digitado : ' , numeros[1], )

def potencia(numeros) :
    print('Potência : ', numeros[0] ** numeros[1])

if operacao == 1 :
    soma(numeros)    
elif operacao == 2 :
    subtracao(numeros)
elif operacao == 3 :
    divisao(numeros) 
elif operacao == 4 :
    multiplicacao(numeros)
elif operacao == 5 :
    raiz(numeros)
else :
   potencia(numeros)