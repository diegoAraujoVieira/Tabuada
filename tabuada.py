def multiplicacao():
    numero = int(input('Digite um número => ')) 

    print('---------------------------------------------------------------------------')
    print('------------- TABUADA DE ' + str(numero), '(MULTIPLICAÇÃO) ----------------------')
    print('---------------------------------------------------------------------------')

    multiplicador = 1

    while multiplicador <= 10:

        calculo = numero * multiplicador

        resposta = (str(numero) + ' x ' + str(multiplicador) + ' = ' + str(calculo))
        print(resposta)

        multiplicador += 1
    
def divisao():
    numero = int(input('Digite um número => '))

    print('---------------------------------------------------------------------------')
    print('------------- TABUADA DE ' + str(numero), '(DIVISÃO) ----------------------')
    print('---------------------------------------------------------------------------')
    dividendo = numero
    contador = 1
    while contador <= 10:
        
        calculo = dividendo / numero

        resposta = (str(dividendo) + ' / ' + str(numero) + ' = ' + str(calculo))
        print(resposta)

        dividendo += numero
        contador += 1

def adicao():
    numero = int(input('Digite um número => ')) 

    print('---------------------------------------------------------------------------')
    print('------------- TABUADA DE ' + str(numero), '(ADIÇÃO) ----------------------')
    print('---------------------------------------------------------------------------')

    somador = 1

    while somador <= 10:

        calculo = numero + somador

        resposta = (str(numero) + ' + ' + str(somador) + ' = ' + str(calculo))
        print(resposta)

        somador += 1

def subtracao():
    numero = int(input('Digite um número => ')) 

    print('---------------------------------------------------------------------------')
    print('------------- TABUADA DE ' + str(numero), '(SUBTRAÇÃO) ----------------------')
    print('---------------------------------------------------------------------------')

    subtrai = numero
    contador = 1

    while contador <= 10:
        numero += 1

        calculo = numero - subtrai

        resposta = (str(numero) + ' - ' + str(subtrai) + ' = ' + str(calculo))
        print(resposta)

        contador += 1

        
def menu():

    while True:
        try:
            print('-------------------------------------------------')
            print('------------- BEM VINDO A TABUADA! --------------')
            print('-------------------------------------------------')
            print('1 - Multiplicação')
            print('2 - Divisão')
            print('3 - Adição')
            print('4 - Subtração')
            print('5 - Fechar')
            print('-------------------------------------------------')
            opcao = int(input('Digite a opção desejada => '))
            print('-------------------------------------------------')
            if opcao == 1:
                multiplicacao()
            elif opcao == 2:
                divisao()
            elif opcao == 3:
                adicao()
            elif opcao == 4:
                subtracao()    
            elif opcao == 5:
                print('--------------------')
                print('Fechando programa...')
                print('--------------------')
                break  
            else:
                print('-------------------------------------')
                print('Ops! Opção inválida. Tente Novamente!')
                print('-------------------------------------')
        except ValueError:
            print('-----------------------------------------------------------------------')
            print('vish! Parece que você digitou uma letra. Apenas números são permitidos!')       
            print('-----------------------------------------------------------------------')
menu()
    

