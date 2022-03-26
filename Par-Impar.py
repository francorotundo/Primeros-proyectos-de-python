try:
    numero = int(input("¿En que numero del 1 al 1000 estas pensando?\n"))
    if numero>=1 and numero<=1000:
        if numero%2==0:
            print(f'{numero} es un numero par')
        else:
            print(f'{numero} es un numero impar')
    else:
        print(f'El numero que pensaste esta fuera de rango. \nIntentalo de nuevo...')
except ValueError:
    print(f'Te equivocaste solo puedes ingresar numeros')