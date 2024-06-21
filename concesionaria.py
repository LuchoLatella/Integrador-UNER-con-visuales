import tkinter as tk
from tkinter import ttk, messagebox
from vehiculos import cargar_vehiculos, guardar_vehiculos, agregar_vehiculo, editar_vehiculo, eliminar_vehiculo
from clientes import cargar_clientes, guardar_clientes, agregar_cliente, editar_cliente, eliminar_cliente
from transacciones import cargar_transacciones, guardar_transacciones, agregar_transaccion

def main():
    root = tk.Tk()
    root.title("Concesionaria")
    
    menu = tk.Menu(root)
    root.config(menu=menu)
    
    vehiculos_menu = tk.Menu(menu)
    menu.add_cascade(label="Vehículos", menu=vehiculos_menu)
    vehiculos_menu.add_command(label="Gestionar Vehículos", command=gestionar_vehiculos)
    
    clientes_menu = tk.Menu(menu)
    menu.add_cascade(label="Clientes", menu=clientes_menu)
    clientes_menu.add_command(label="Gestionar Clientes", command=gestionar_clientes)
    
    transacciones_menu = tk.Menu(menu)
    menu.add_cascade(label="Transacciones", menu=transacciones_menu)
    transacciones_menu.add_command(label="Registrar Transacciones", command=gestionar_transacciones)
    
    salir_menu = tk.Menu(menu)
    menu.add_cascade(label="Salir", menu=salir_menu)
    salir_menu.add_command(label="Salir", command=root.quit)
    
    root.mainloop()

def gestionar_vehiculos():
    vehiculos = cargar_vehiculos()
    ventana_vehiculos = tk.Toplevel()
    ventana_vehiculos.title("Gestionar Vehículos")
    
    etiqueta = tk.Label(ventana_vehiculos, text="Vehículos", font=("Arial", 14))
    etiqueta.pack()

    ttk.Button(ventana_vehiculos, text="Crear Vehículo", command=lambda: crear_vehiculo(ventana_vehiculos, vehiculos)).pack()
    ttk.Button(ventana_vehiculos, text="Editar Vehículo", command=lambda: editar_vehiculo_ventana(ventana_vehiculos, vehiculos)).pack()
    ttk.Button(ventana_vehiculos, text="Eliminar Vehículo", command=lambda: eliminar_vehiculo_ventana(ventana_vehiculos, vehiculos)).pack()
    ttk.Button(ventana_vehiculos, text="Buscar Vehículos", command=lambda: buscar_vehiculos(vehiculos)).pack()

def crear_vehiculo(parent, vehiculos):
    def guardar():
        agregar_vehiculo(vehiculos, 
                         patente_entry.get(), 
                         marca_entry.get(), 
                         modelo_entry.get(), 
                         tipo_entry.get(), 
                         año_entry.get(), 
                         kilometraje_entry.get(), 
                         precio_compra_entry.get(), 
                         precio_venta_entry.get(), 
                         estado_entry.get())
        ventana_crear.destroy()
        messagebox.showinfo("Éxito", "Vehículo creado con éxito")
    
    ventana_crear = tk.Toplevel(parent)
    ventana_crear.title("Crear Vehículo")
    
    campos = ["Patente", "Marca", "Modelo", "Tipo", "Año", "Kilometraje", "Precio de Compra", "Precio de Venta", "Estado"]
    entries = {}
    
    for campo in campos:
        tk.Label(ventana_crear, text=campo).pack()
        entries[campo] = tk.Entry(ventana_crear)
        entries[campo].pack()
    
    patente_entry = entries["Patente"]
    marca_entry = entries["Marca"]
    modelo_entry = entries["Modelo"]
    tipo_entry = entries["Tipo"]
    año_entry = entries["Año"]
    kilometraje_entry = entries["Kilometraje"]
    precio_compra_entry = entries["Precio de Compra"]
    precio_venta_entry = entries["Precio de Venta"]
    estado_entry = entries["Estado"]

    ttk.Button(ventana_crear, text="Guardar", command=guardar).pack()

def editar_vehiculo_ventana(parent, vehiculos):
    # Implementación de la funcionalidad de editar un vehículo
    pass

def eliminar_vehiculo_ventana(parent, vehiculos):
    # Implementación de la funcionalidad de eliminar un vehículo
    pass

def buscar_vehiculos(vehiculos):
    # Implementación de la funcionalidad de buscar vehículos
    pass

def gestionar_clientes():
    clientes = cargar_clientes()
    ventana_clientes = tk.Toplevel()
    ventana_clientes.title("Gestionar Clientes")
    
    etiqueta = tk.Label(ventana_clientes, text="Clientes", font=("Arial", 14))
    etiqueta.pack()

    ttk.Button(ventana_clientes, text="Crear Cliente", command=lambda: crear_cliente(ventana_clientes, clientes)).pack()
    ttk.Button(ventana_clientes, text="Editar Cliente", command=lambda: editar_cliente_ventana(ventana_clientes, clientes)).pack()
    ttk.Button(ventana_clientes, text="Eliminar Cliente", command=lambda: eliminar_cliente_ventana(ventana_clientes, clientes)).pack()
    ttk.Button(ventana_clientes, text="Buscar Clientes", command=lambda: buscar_clientes(clientes)).pack()

def crear_cliente(parent, clientes):
    # Implementación de la funcionalidad de crear un cliente
    pass

def editar_cliente_ventana(parent, clientes):
    # Implementación de la funcionalidad de editar un cliente
    pass

def eliminar_cliente_ventana(parent, clientes):
    # Implementación de la funcionalidad de eliminar un cliente
    pass

def buscar_clientes(clientes):
    # Implementación de la funcionalidad de buscar clientes
    pass

def gestionar_transacciones():
    transacciones = cargar_transacciones()
    vehiculos = cargar_vehiculos()
    clientes = cargar_clientes()
    ventana_transacciones = tk.Toplevel()
    ventana_transacciones.title("Registrar Transacciones")
    
    etiqueta = tk.Label(ventana_transacciones, text="Transacciones", font=("Arial", 14))
    etiqueta.pack()

    ttk.Button(ventana_transacciones, text="Registrar Compra", command=lambda: registrar_compra(ventana_transacciones, transacciones, vehiculos, clientes)).pack()
    ttk.Button(ventana_transacciones, text="Registrar Venta", command=lambda: registrar_venta(ventana_transacciones, transacciones, vehiculos, clientes)).pack()
    ttk.Button(ventana_transacciones, text="Listar Compras", command=lambda: listar_compras(transacciones)).pack()
    ttk.Button(ventana_transacciones, text="Listar Ventas", command=lambda: listar_ventas(transacciones)).pack()

def registrar_compra(parent, transacciones, vehiculos, clientes):
    # Implementación de la funcionalidad de registrar una compra
    pass

def registrar_venta(parent, transacciones, vehiculos, clientes):
    # Implementación de la funcionalidad de registrar una venta
    pass

def listar_compras(transacciones):
    # Implementación de la funcionalidad de listar las compras
    pass

def listar_ventas(transacciones):
    # Implementación de la funcionalidad de listar las ventas
    pass

if __name__ == "__main__":
    main()