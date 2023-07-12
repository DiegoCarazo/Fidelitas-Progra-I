def nota_final():
    # 5 estudiantes | 4 actividades
    lista_notas = [
        [89,95,56,87,100],
        [100,76,92,48,80],
        [95,76,74,89,82],
        [100,82,75,79,68,]
    ]
    estudiantes = ['Juan','Jose','Carlos', 'Mateo', 'Federico']
    total_notas = []
    for notas in range(len(lista_notas)):
        notas_total = lista_notas[notas]
        x = sum(notas_total)
        y = x / 5
        total_notas.append(y)
        

    lista_union = zip(estudiantes, total_notas)
    lista = list(lista_union)
    print(lista)


def microbus():
    bus = [0] * 20

    while True:
        print("Espacios disponibles: ", bus.count(0))
        if bus.count(0) == 0:
            print("Lo siento, no hay espacios disponibles.")
            break

        pos = int(input("Ingrese la posición que desea reservar (1-20): "))
        if bus[pos - 1] == 1:
            print("Lo siento, ese espacio ya está reservado.")
        else:
            bus[pos - 1] = 1
            print(f"Ha reservado el espacio {pos}.")

        continuar = input("¿Desea continuar? (s/n): ")
        if continuar.lower() == "n":
            break

microbus()
