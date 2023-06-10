def bisiesto():
    edad = int(input('¿Cuál es su fecha de nacimiento?'))
    # Si la division de edad entre 4 da cero y la division de edad entre 100 no da cero o la division en 400 da cero.
    if edad % 4 == 0 and (edad % 100 != 0 or edad % 400 == 0):
        print('El año', edad, 'es un año bisiesto.')
    else:
        print('El año', edad, 'no es un año bisiesto.')


def numeros_a_palabras():
    # Números escritos 
    unidades = {
        0: ' ',
        1: 'uno',
        2: 'dos',
        3: 'tres',
        4: 'cuatro',
        5: 'cinco',
        6: 'seis',
        7: 'siete',
        8: 'ocho',
        9: 'nueve',
        10: 'diez',
        11: 'once',
        12: 'doce',
        13: 'trece',
        14: 'catorce',
        15: 'quince',
        16: 'dieciséis',
        17: 'diecisiete',
        18: 'dieciocho',
        19: 'diecinueve',
        20: 'veinte',
        21: 'Veintiuno',
        22: 'Veintidós',
        23: 'Veintitrés',
        24: 'Veinticuatro',
        25: 'Veinticinco',
        26: 'Veintiséis',
        27: 'Veintisiete',
        28: 'Veintiocho',
        29: 'Veintinueve'
    }
    decenas = {
        1: 'Diez',
        2: 'veinte',
        3: 'treinta',
        4: 'cuarenta',
        5: 'cincuenta',
        6: 'sesenta',
        7: 'setenta',
        8: 'ochenta',
        9: 'noventa'
    }

    # funcionalidad
    while True:
        entrada = input("Ingresa una cadena de números: ")
        # lista de numeros para uso después de 30
        numeros = []
        # Separar los datos
        partes = entrada.split()

        # Iterar sobre las partes y agregar solo los números a la lista 'numeros'
        for parte in partes:
            for i in parte:
                if i.isdigit():
                    numeros.append(int(i))

        # Delimitación de los resultados
        if int(entrada) > 150:
            print('Selección invalida')

        if 0 == int(entrada):
            print('Cero')
        elif int(entrada) <= 29:
            print(unidades[int(entrada)])
        elif 30 <= int(entrada) < 100:
            if numeros[1] == 0:
                y = " "
            else:
                y = "y"
            print(decenas[numeros[0]], y, unidades[numeros[1]])
        elif 100 == int(entrada):
            print('Cien')
        elif 101 <= int(entrada) <= 150:
            if numeros[2] == 0:
                y = " "
            else:
                y = "y"
            print("Ciento", decenas[numeros[1]], y, unidades[numeros[2]])


def par_o_impar():
    num_poi = int(input('Digite el numero para verificar si es par o impar: '))
    # Si el número no es divisible entre 2 es impar
    if num_poi % 2 == 0:
        print('El numero:', num_poi, 'Es par')
    else:
        print('El numero', num_poi, 'Es impar')


def tipo_de_triangulo():
    print('Ingrese el tamaño de los lados de su triangulo')
    lado_a = float(input('Lado A: '))
    lado_b = float(input('Lado B: '))
    lado_c = float(input('Lado C: '))
    # Equilatero Tres lados iguales.
    if lado_a == lado_b == lado_c:
        print('Su triangulo, según la medida de sus lados es equilatero')
    # Isósceles dos lados iguales.
    elif lado_a == lado_b and lado_b != lado_c or lado_a == lado_c and lado_a != lado_b or lado_b == lado_c and lado_b != lado_a:
        print('Su triangulo, según la medida de sus lados es isósceles')
    # Escaleno tres lados desiguales.
    elif lado_a != lado_b and lado_b != lado_c:
        print('Su triangulo, según la medida de sus lados es escaleno')


# Menu
print('Los programas preparados para esta ocasión: ')
print('Digite "1" para calcular si su año de nacimiento fue o sera bisiesto.')
print('Digite "2" para in intercambio de números a palabras.')
print('Digite "3" para identificar si el numero es par o impar.')
print('Digite "4" para determinar el tipo de triangulo.')
while True:
    select = int(input('Digite el programa elegido: '))
    if select == 1:
        bisiesto()
    elif select == 2:
        numeros_a_palabras()
    elif select == 3:
        par_o_impar()
    elif select == 4:
        tipo_de_triangulo()
