print('***************************************')
print('****** Adivinhe qual é o número  ******')
print('***************************************')



numero_secreto = 83 
tentativa = input('Tente acertar o número: ')
print('Você digitou: ', tentativa)


tentativa_int = int(tentativa)

rodada=1
total_de_tentativa = 3

while (rodada <= total_de_tentativa):
    tentativa = input('tente acertar o numero:')
    print(f'voce digitou : {tentativa}')
    print(f'\ntentativa {rodada:02d} de {total_de_tentativa:02d}')
    rodada +=1
    try:
        total_de_tentativa = int(tentativa)
    except ValueError:
        print('valor invalido, escreva numeros inteiros. por favor')
        exit()
    except Exception as e:
        print(f'erro {e}')
        exit()
    else:
        pass
    finally:
        pass




    # if (numero_secreto == tentativa_int):
    #     print("Boa tentativa. ACERTOU!")
    # else:
    #     print('Não foi dessa vez. ERROU!')
    
    #     if (tentativa_int > numero_secreto):
    #         print('Sua tentativa foi MAIOR que o número secreto.')
    #     else:
    #         print('Sua tentativa foi MENOR que o número secreto.')
        
    #         print('GAME OVER!')
    # print('Obrigado por participar!')





    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto


    if acerto:
        print('Boa tentativa. ACERTOU!!!!')
        break
    else:
        print('Não foi dessa vez. ERROU!!!!')
        if ehmaior:
            print('Sua tentativa foi MAIOR que o número secreto.')
        if ehmenor:
            print('Sua tentativa foi MENOR que o número secreto.')
        print('GAME OVER!')
    print('Obrigado por participar')