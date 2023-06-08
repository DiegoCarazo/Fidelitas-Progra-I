# Suma los salarios de 10 colaboradores menos las cargas sociales.
def calcular_salario_total(salarios):
    total = 0
    for salario in salarios:
        deduccion = salario * 0.09
        salario_neto = salario - deduccion
        total += salario_neto
    return total
    salarios = input(['Hello'])
    salario_total = calcular_salario_total(salarios)

    print("El total pagado por la empresa por concepto de salarios es:", salario_total)





print('Bienvenido a las clase 5, para está oportunidad tenemos 3 programas')
print('Seleccione "1" para un calculo de salarios')
seleccion = int(input('Seleccione una de las opciones disponibles'))
if seleccion == 1:
    calcular_salario_total()
