def ciclista():
    kilometros_dia = []
    dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    total = 0
    for dia in range(7):
        cantidad_dia = float(input(f"Cantidad de kilometros recorridos el {dias_semana[dia]}: "))
        kilometros_dia.append(cantidad_dia)
        total += cantidad_dia

    lista_obj = zip(dias_semana, kilometros_dia)
    lista_read = list(lista_obj)
    print(lista_read)
    print('El total de kilometros de la semana fue: ', total)


def teatro():
    persona = []
    butaca = [1,2,3,4,5,6,7,8,9,10]
    for asiento in range(2):
        nombre = input(f'Nombre de la persona del asiento {asiento}: ')
        persona.append(nombre)
    
    lista = zip(butaca, persona)
    lista_correjida = list(lista)
    print(lista_correjida)

def palabra_revez(palabra):
     for i in range(len(palabra) - 1, -1, -1):
        print(palabra[i])
    
# palabra_revez(input('Palabra: '))

def uber():
    dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    monto_ganado = []
    total = 0 
    peor_dia = 999999999
    for dia in range(len(dias_semana)):
        monto = float(input(f'Monto del dia {dias_semana[dia]}: '))
        monto_ganado.append(monto)
        total += monto
        if monto < peor_dia:
            peor_dia = monto

    print(f'El monto total ganado es de {total}$')
    print(f'El peor dia se genero {peor_dia}$')

uber()
