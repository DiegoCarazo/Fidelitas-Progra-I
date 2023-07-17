def notas():
    decision = input('Desea ver las notas "1" o a agregar una nueva "2"? \n- ')
    archivo = open("notas.py", "a+")
    archivo_lectura = open("notas.txt", "r")
    leer_archivo = archivo_lectura.read()

    if decision == "1":
        print(leer_archivo)
    elif decision == "2":
        grupo = int(input("Grupo: "))
        nombre = input("Nombre: ")
        nota = int(input("Nota: "))
        dic = {grupo: [nombre, nota]}
        archivo.write(str(dic) + "\n")
    else:
        print("Haga una selección valida.")
        
notas()
