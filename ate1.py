print('')
print('Adivinhe qual e o numero'.center(100, ' '))
print('')

NUMERO_SECRETO=10
tentativa=input('tente acertar o numero')
print('voce digitou: ', tentativa)

tentativa_int = int(tentativa)

if (NUMERO_SECRETO == tentativa_int):
    print(f'boa tentativa.acertou! o numero e {tentativa}')

else:
    print(f'voce errou, o numero nao e {tentativa}')