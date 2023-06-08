# Operaciones
def Calculadora():
    primer_numero = int(input('Primer numero: '))
    segundo_numero = int(input('Segundo numero: '))
    denominador = input('Introduzca el denominador deseado, por ejemplo: use +, -, *, /')
    if denominador == '+':
        print('El resultado es: ', primer_numero + segundo_numero)
    elif denominador == '-':
        print('El resultado es: ', primer_numero - segundo_numero)
    elif denominador == '*':
        print('El resultado es: ', primer_numero * segundo_numero)
    elif denominador == '/':
        print('El resultado es: ', primer_numero / segundo_numero)
    else:
        print('Seleccione una respuesta valida: +, -, /, *')
    print('\nDe regreso al estudio\n')
        
def Rectangulo():
    print('Seguiremos con el calculo del area y permitro de un rectangulo')
    print(nombre, 'introduce la el: ')
    base = int(input('introduce el base: '))
    altura = int(input('introduce el altura: '))
    area = base * altura
    perimetro = (base * 2) + (altura * 2)
    print('El area del rectangulo es de: ', area, 'y su perimetro es de: ', perimetro)
    print('\nDe regreso al estudio\n')

def Intercambio():
    print ('Bienvenido a una maquina fantastica que intercambia las edades de las personas')
    print ('Nuestros dos participantes "Pedro y Pablo" estan listos.')
    pedro = int(input('¿Qué edad parece tener Pedro? '))
    pablo = int(input('¿Qué edad parece tener Pablo? '))
    print ('Pedro y pablo entrar en la maquina la cual hace un estruendoso sonido \n')
    if pedro > pablo:
        print('Un renovado Pedro de ', pablo, 'años sale da la maquina mientras que Pablo yace envejecido con sus ', pedro, 'años \n')
    elif pedro < pablo:
        print('Un renovado Pablo de ', pedro, 'años sale da la maquina mientras que Pedro yace envejecido con sus ', pablo, 'años \n')
    elif pedro == pablo:
        print ('Como ambos tenian la misma edad ninguno sufre un cambio')
    print('\nDe regreso al estudio\n')

def Potencia():
    n_elevado = int(input('Digite el numero que desea elevar a una potencia: '))
    elevacion = int(input('Digite a la potencia que desea elevarlo: '))
    print('Su resultado es: ', n_elevado ** elevacion)
    print('\nDe regreso al estudio\n')


#interfaz
print ('Bienvenido a la clase 3')
nombre = input('¿Cuál es su numbre?: ')
while True:
    print ('Ahora bien,',nombre, 'Tenemos varias opciones, dijite: \n"1" para una calculadora \n"2" para el calculo del area y perimetro de un rectangulo \n"3" para ua maquina estaordinaria que intercambia las edades \n"4" para elevar un numero a una potencia \nCualquier otra tecla para terminar el programa')
    seleccion = input('Digite su respuesta: ')
    if seleccion == '1':
        Calculadora()
    elif seleccion == '2':
        Rectangulo()
    elif seleccion == '3':
        Intercambio()
    elif seleccion == '4':
        Potencia()
    else:
        break
