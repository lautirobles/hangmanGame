def mostrar_menu():
    print('MENU DE OPCIONES')
    print('1. Ingresar la palabra')
    print('2. Jugar')
    print('0. Salir')


def ingresar_palabra(men):
    while True:
        palabra = input(men)
        if 3 < len(palabra) < 15:
            return palabra
        print('Error!')


def ingresar_letra(men):
    while True:
        abc = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        letra = input(men)
        if letra in abc:
            return letra.lower()
        print('Error! Ingrese una letra válida...')


def jugar(pal):
    pal = pal.lower()
    lon = ['_'] * len(pal)
    vidas = 6
    letras_acertadas = 0
    while vidas > 0:
        print('*' * 40)
        print()
        print(lon)
        print()
        print('*' * 40)
        print()
        letra = ingresar_letra('Ingrese una letra: ')
        print()
        acierto = False
        for i in range(len(pal)):
            if letra == pal[i]:
                lon[i] = letra
                acierto = True
                letras_acertadas += 1
        if not acierto:
            vidas -= 1
            print()
            print('Letra incorrecta...')
            print(f'Te quedan {vidas} vidas...')
            print()

        if letras_acertadas == len(pal):
            print()
            print(lon)
            print('FELICITACIONES! Ganaste!!...')
            print()
            print()
            return
    print()
    print('PERDISTE :(...')
    print(f'La palabra era "{pal}"')
    print()


def main():
    op = -1
    pal = ''
    while op != 0:
        mostrar_menu()
        op = input('Ingrese la opción que desea ejecutar: ')
        if op == '1':
            pal = ingresar_palabra('Ingrese la palabra (mayor a 3 y menor a 15 caracteres): ')
        elif op == '2':
            if pal == '':
                print('Primero debe ingresar una palabra!')
                continue
            jugar(pal)
        elif op == '0':
            print('Gracias por usar nuestro programa!...')
            return
        else:
            print('Opción incorrecta, por favor seleccione una de las opciones válidas...')


if __name__ == '__main__':
    main()
