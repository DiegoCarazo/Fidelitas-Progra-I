from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('800x600')
root.config(background='white')


def gestionar_info():
    # Formato del diccionario = {Tipo: [Nombre, Correo, Dirección, Teléfono]}
    # Funcionalidad para la subida de datos al diccionario
    def subir_datos(clase):
        nombre_datos = nombre.get()
        correo_datos = correo.get()
        direccion_datos = direccion.get()
        telefono_datos = telefono.get()
        lista_datos = [nombre_datos, correo_datos, direccion_datos, telefono_datos]
        dicionario_usuario = {clase: lista_datos}
        return dicionario_usuario

    # Labels de la sección
    Label(text="Sistema de gestion de usuarios", background="white", font=("Arial", 12)).grid(row="1", column="2")
    Label(text="ingrese los datos y suba la información seleccionando el tipo de usuario", background="white", font=("Arial", 10)).grid(row="2", column="1", columnspan="4", sticky="W")
    Label(text="Tipo de usuario: ", background="white", font=("Arial", 12)).grid(row="1", column="1")
    Label(text="Nombre: ", background="white", font=("Arial", 12)).grid(row="3", column="1")
    Label(text="Correo: ", background="white", font=("Arial", 12)).grid(row="4", column="1")
    Label(text="Dirección: ", background="white", font=("Arial", 12)).grid(row="5", column="1")
    Label(text="Telefono: ", background="white", font=("Arial", 12)).grid(row="6", column="1")

    # Botones para los usuarios
    personal = ttk.Button(root, text="Personal", command=lambda: subir_datos("Personal"))
    cliente = ttk.Button(root, text="Cliente", command=lambda: subir_datos("Cliente"))
    proveedor = ttk.Button(root, text="Proveedor", command=lambda: subir_datos("Personal"))
    usuarios = ttk.Button(root, text="Usuarios ya registrados")  # Crear función que devuelva los usuarios en pantalla

    # Introducción de información
    nombre = ttk.Entry(root)
    correo = ttk.Entry(root)
    direccion = ttk.Entry(root)
    telefono = ttk.Entry(root)

    # Parte visual de las Entry
    nombre.grid(row="3", column="2")
    correo.grid(row="4", column="2")
    direccion.grid(row="5", column="2")
    telefono.grid(row="6", column="2")

    # Parte Visual Botones
    personal.grid(row="7", column="1")
    cliente.grid(row="7", column="2")
    proveedor.grid(row="7", column="3")
    usuarios.grid(row="7", column="4")


def catalogo_de_productos():
    # articulo : [Precio, proveedor, IVA, Descripción]
    def subir_datos(producto_datos, precios_datos,proveedores_datos, iva_datos, descripción_datos):
        producto_datos = producto.get()
        precio_datos = precio.get()
        proveedor_datos = proveedor.get()
        iva_datos = iva.get()
        descripción_datos = descripción.get()
        lista_datos = [precio_datos, proveedor_datos, iva_datos, descripción_datos]
        dicionario_productos = {producto_datos: lista_datos}
        return dicionario_productos

    # Labels de la sección
    Label(text="Catalogo de productos", background="white", font=("Arial", 12)).grid(row="1", column="2")
    Label(text="Ingrese el producto y la cantidad a agregar", background="white", font=("Arial", 10)).grid(row="2", column="1", columnspan="4", sticky="W")
    Label(text="Producto: ", background="white", font=("Arial", 12)).grid(row="3", column="1", sticky="W")
    Label(text="Precio: ", background="white", font=("Arial", 12)).grid(row="4", column="1", sticky="W")
    Label(text="Proveedor: ", background="white", font=("Arial", 12)).grid(row="5", column="1", sticky="W")
    Label(text="IVA: ", background="white", font=("Arial", 12)).grid(row="6", column="1", sticky="W")
    Label(text="Descripción: ", background="white", font=("Arial", 12)).grid(row="7", column="1", sticky="W")

    # Botón de subir
    btn = ttk.Button(root, text="Subir", command=lambda: subir_datos(producto, precio,proveedor, iva, descripción))
    btn.grid(row="8", column=3)

    # Introducción de información
    producto = ttk.Entry(root)
    precio = ttk.Entry(root)
    proveedor = ttk.Entry(root)
    iva = ttk.Entry(root)
    descripción = ttk.Entry(root)

    # Parte visual de las Entry
    producto.grid(row="3", column="2")
    precio.grid(row="4", column="2")
    proveedor.grid(row="5", column="2")
    iva.grid(row="6", column="2")
    descripción.grid(row="7", column="2")


def sistema_pagos():
    def tarjeta_pago():
        # Labels de la sección
        Label(root, text="Ingrese los datos de la tarjeta", background="white", font=("Arial", 12)).grid(row="2", column="3", stick="W", columnspan="2")
        Label(root, text="Nombre del titular: ", background="white").grid(row="3", column="3", stick="W")
        Label(root, text="Numero de tarjeta: ", background="white").grid(row="4", column="3", stick="W")
        Label(root, text="Expiración(Mes): ", background="white").grid(row="5", column="3", stick="W")
        Label(root, text="Expiración(Año): ", background="white").grid(row="6", column="3", stick="W")
        Label(root, text="Código de seguridad: ", background="white").grid(row="7", column="3", stick="W")

        # Entry de la sección
        nombre = ttk.Entry(root)
        numero = ttk.Entry(root)
        fecha_mes = ttk.Entry(root)
        fecha_año = ttk.Entry(root)
        codigo = ttk.Entry(root)

        # Entry visuales
        nombre.grid(row="3", column="4", stick="W")
        numero.grid(row="4", column="4", stick="W")
        fecha_mes.grid(row="5", column="4", stick="W")
        fecha_año.grid(row="6", column="4", stick="W")
        codigo.grid(row="7", column="4", stick="W")






    # Labels de la sección
    Label(root, text="Seleccione un metodo de pago", background="white", font=("Arial", 12)).grid(row="1", column="2")

    # Botones para los usuarios
    tarjeta = Button(root, text="Tarjeta de crédito", font=("Arial", 12), height=1, width=18, command=tarjeta_pago)
    transferencia = Button(root, text="Transferencia bancaria", font=("Arial", 12), height=1, width=18)
    efectivo = Button(root, text="Efectivo", font=("Arial", 12), height=1, width=18)
    paypal = Button(root, text="PayPal", font=("Arial", 12), height=1, width=18)

    # Botones visuales
    tarjeta.grid(row="2", column="2", sticky="W")
    transferencia.grid(row="3", column="2", sticky="W")
    efectivo.grid(row="4", column="2", sticky="W")
    paypal.grid(row="5", column="2", sticky="W")


def calculo_iva():
    print(inventario)
    articulo = input('Escriba el nombre: ')
    iva = inventario[articulo][2]
    precio = inventario[articulo][0]
    calculo = precio + precio * iva
    print('El precio final con el iva del', iva * 100, 'es de: ', calculo)


def generar_informe_ventas():
    # imprimir encabezado del informe de ventas
    print("Informe de Ventas")
    # buscar la venta en la lista de ventas
    for venta in ventas:
        # obtener los valores de cada venta
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]
        monto_total = cantidad * precio

    # imprimir el informe
    # print("Producto:", producto)
    # print("Cantidad vendida:", cantidad)
    # print("Monto total:", monto_total)


# ----- Sistema de Pagos -----
pagos = []



# interfaz grafica

Label(root, text="Bienvenido al centro de servicio", background='white', font=("Arial", 15)).grid(row="0", columnspan="4", sticky="W")
Button(root, text="Gestion de usuarios", command=gestionar_info, font=("Arial", 12), height=1, width=20).grid(row="1", column="0", sticky="W")
Button(root, text="Catalogo de productos", command=catalogo_de_productos, font=("Arial", 12), height=1, width=20).grid(row="2", column="0", sticky="W")
Button(root, text="Informe de ventas", command=generar_informe_ventas, font=("Arial", 12), height=1, width=20).grid(row="4", column="0", sticky="W")
Button(root, text="Sistema pagos", command=sistema_pagos, font=("Arial", 12), height=1, width=20).grid(row="3", column="0", sticky="W")

root.mainloop()
