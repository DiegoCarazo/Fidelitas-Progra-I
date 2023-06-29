# compañía de seguros
def plan_seguros():
    resultado = 0
    # Selección del plan
    while True:
        selection_plan = input('La compañía ofrece "Alfa" el cual inicia desde los 1200$ y "Beta" que inicia desde los 950'
                               '\nUtilice "A" para el plan "Alfa" y "B" para el plan "Beta": ')
        if selection_plan == "A":
            resultado += 1200
            break
        elif selection_plan == "B":
            resultado += 950
            break
        else:
            print('Selección invalida intente de nuevo')

    # cargos extra
    alcohol_datos = input('Consume alcohol frecuentemente?(digite "si" o "no"): ')
    if alcohol_datos == 'si' or alcohol_datos == 'Si':
        resultado += resultado * 0.10

    lentes_datos = input('Necesita lente para ver bien?(digite "si" o "no"): ')
    if lentes_datos == 'si' or lentes_datos == 'Si':
        resultado += resultado * 0.05

    enfermedad_datos = input('Existe alguna enfermedad pre-existente?(digite "si" o "no"): ')
    if enfermedad_datos == "si" or enfermedad_datos == 'Si':
        resultado += resultado * 0.05

    edad_datos = int(input('Digite su edad: '))
    if edad_datos > 40:
        resultado += resultado * 0.20
    else:
        resultado += resultado * 0.10

    print('La cuota de su seguros es de: ', resultado)

plan_seguros()


# Bono salarial
def bonos():
    # variables para los valores
    bono_antiguedad = 0
    bono_mensual = 0

    # entrada de datos
    antiguedad_empleado = int(input('Cuanto lleva trabajando en la empresa en años?: '))
    salario_empleado = float(input('Cual es el salario del trabajador?: '))

    # Bono de antiguedad
    if 2 < antiguedad_empleado < 5:
        bono_antiguedad += salario_empleado * 0.20
    else:
        bono_antiguedad += salario_empleado * 0.30

    # bono mensual
    if salario_empleado < 1000:
        bono_mensual += salario_empleado * 0.25
    elif 1000 <= salario_empleado < 3500:
        bono_mensual += salario_empleado * 0.15
    else:
        bono_mensual += salario_empleado * 0.10

    if bono_antiguedad > bono_mensual:
        print('El bono total es de: ', bono_antiguedad)
        print('Salario sin bono: ', salario_empleado)
        print('Salario con el bono de antiguedad: ', salario_empleado + bono_antiguedad)
    else:
        print('El bono total es de: ', bono_mensual)
        print('Salario sin bono: ', salario_empleado)
        print('Salario con el bono mensual: ', salario_empleado + bono_mensual)


bonos()

# parte II
def parte_ii():
    # definidas con el operador incorrecto, falta de paréntesis, se agraga la "i" para guardar el valor
    punto_c = int(input("Ingrese c: "))
    punto_p = float(input('Ingrese p: '))
    dolares = 0
    # definidas con el operador incorrecto, "p" no existe se cambia por "y"
    c_por_p= punto_c * punto_p

    # indentanción incorrecta, se puede simplificar la entrada la segunda entrada
    if c_por_p >= 1 and punto_c <= 8:
        dolares += punto_c * 0.125
    elif 6 <= punto_c <= 8:
        dolares += c_por_p * 0.20
    else:
        dolares += c_por_p * 0.315

    Nuevo_valor = c_por_p * dolares

    # multiples print, indentacion, print cerrados correctamente
    print(f'En resumen la multiplicación  de "C" por "P" da como resultado {c_por_p}.'
          f'\nEs decir el monto total en dolares es de: {dolares}.'
          f'\nAjustado a su valor real es de {Nuevo_valor}')
    # no tengo ni idea de que calcula el codigo haha

parte_ii()
