# Consultorio medico
def consultorio_medico():
    dia  = input('¿Qué día de la semana es?: ')
    lunes = 'Avena y frutas tropicales'
    martes = 'Yogurt y frutas secas'
    miercoles = 'Café y galletas saladas'
    jueves = 'Barra energética y jugo de naranja.'
    respuesta = 'Para el día de hoy deberá comer'
    
    if dia == 'lunes':
       print('\n',respuesta, lunes,'\n')
    elif dia == 'martes':
       print('\n',respuesta, martes,'\n')
    elif dia == 'miercoles':
       print('\n',respuesta, miercoles,'\n')
    elif dia == 'jueves':
       print('\n',respuesta, jueves,'\n')
    else:
        print('Porfavor haga una seleccion valida')

#Paso al siguente nivel
def paso_al_siguente_nivel():
    print('Para avanzar a la siguente etapa complete las siguientes operaciones')
    #Reto 1
    while True:
        reto_1 = int(input('¿Cuanto es: 2 + 2?: '))
        if reto_1 == 4:
            print('Respuesta correcta')
            break
        else:
            print('Trata de nuevo')
    #Reto 2
    while True:
        reto_2 = int(input('¿Cuanto es 10 + 10?: '))
        if reto_2 == 20:
            print('Respuesta correcta')
            break
        else:
            print('Trata de nuevo')
    #Reto 3
    while True:
        reto_3 = int(input('¿Cuanto es 10 - 9?: '))
        if reto_3 == 1:
            print('Respuesta correcta')
            break
        else:
            print('Trata de nuevo')
    
def automotriz():
    #descuentos
    descuento_motor = 0.15
    descuento_accesorios = 0.10
    descuento_limpieza = 0.05
    descuento_frenos = 0.03
    #Productos 
    bomba_de_agua = 20000
    pino = 1000
    spray = 3500
    frenos_liquido = 10000
    #Menu
    print('Bienvenido a la tienda, tenemos los siguientes articulos para su compra en linea')
    print('A) Bomba de agua: 20,000 \nB) Pino aromatico: 1,000 \nC) Spray limpiador: 3,500 \nD) Liquido de freno: 10,000')
    #input
    items = input('introduzca las letra de los productos que desea compar: ')
    carrito_de_compras = 0
    descuentos = 0
    if 'A' in items:
        carrito_de_compras += bomba_de_agua - (bomba_de_agua * descuento_motor)
        descuentos += 15
    if 'B' in items:
        carrito_de_compras += pino - (pino * descuento_accesorios)
        descuentos += 10
    if 'C' in items: 
        carrito_de_compras += spray - (spray * descuento_limpieza)
        descuentos += 5
    if 'D' in items: 
        carrito_de_compras += frenos_liquido - (frenos_liquido * descuento_frenos)
        descuentos += 3
    
    print('El total de los descuentos es de: ', descuentos,'%') 
    print('El total de su compra es de: ', carrito_de_compras)
    


                 
print('Bienvenido a la semana 4 de progamación básica, tenemos 3 programas preparados')
print('Seleccione "1" para una guia dietetica')
print('Seleccione "2" para un mini-juego')
print('Seleccione "3" para una tienda automiriz')
seleccion = input('Digite su respuesta: ')
if seleccion == '1':
    consultorio_medico()
elif seleccion == '2':
    paso_al_siguente_nivel()
elif seleccion == '3':
    automotriz()
