from diagramasVenn import *

from metodos import *

def realizar_operacion():
    conjunto_a = set(map(str, entry_a.get().split(',')))
    conjunto_b = set(map(str, entry_b.get().split(',')))
    conjunto_c = set(map(str, entry_c.get().split(',')))

    # Obtener la operación deseada del usuario
    operacion = entry_operacion.get()

    # Obtener el número de conjuntos seleccionados por el usuario
    num_conjuntos = conjunto_var.get()

    # Realizar las operaciones desde cero
    if num_conjuntos == '2':
        if operacion == 'union':
            resultado = union(conjunto_a, conjunto_b)
        elif operacion == 'interseccion':
            resultado = interseccion(conjunto_a, conjunto_b)
        elif operacion == 'diferencia':
            resultado = diferencia(conjunto_a, conjunto_b)
        elif operacion == 'complemento':
            resultado = complemento(union(conjunto_a, conjunto_b), conjunto_a)
        else:
            resultado = []
    elif num_conjuntos == '3':
        if operacion == 'union':
            resultado = union3(conjunto_a, conjunto_b, conjunto_c)
        elif operacion == 'interseccion':
            resultado = interseccion(conjunto_a, conjunto_b)
        elif operacion == 'diferencia':
            resultado = diferencia(conjunto_a, conjunto_b)
        elif operacion == 'complemento':
            resultado = complemento(union(conjunto_a, conjunto_b), conjunto_a)
        else:
            resultado = []



    # Mostrar los resultados en las etiquetas
    label_resultado.config(text=f"{operacion.capitalize()}: {resultado}")

    # Mostrar los resultados en los gráficos de Venn
    if num_conjuntos == '2':
        mostrar_venn2(conjunto_a, conjunto_b, resultado)
    elif num_conjuntos == '3':
        conjunto_c = set(map(str, entry_c.get().split(',')))
        mostrar_venn3(conjunto_a, conjunto_b, conjunto_c, resultado)






# Entradas de texto para los conjuntos
label_a = tk.Label(ventana, text="Conjunto A:")
label_a.grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(ventana)
entry_a.grid(row=0, column=1, padx=10, pady=5)

label_b = tk.Label(ventana, text="Conjunto B:")
label_b.grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(ventana)
entry_b.grid(row=1, column=1, padx=10, pady=5)

# Entrada de texto para el conjunto C (si es necesario)
label_c = tk.Label(ventana, text="Conjunto C:")
label_c.grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(ventana)
entry_c.grid(row=2, column=1, padx=10, pady=5)


label_conjuntos = tk.Label(ventana, text="Número de conjuntos:")
label_conjuntos.grid(row=3, column=0, padx=10, pady=5)

conjunto_var = StringVar()
conjunto_var.set("2")  # Por defecto, seleccionar 2 conjuntos
radio_2 = tk.Radiobutton(ventana, text="2 Conjuntos", variable=conjunto_var, value="2")
radio_2.grid(row=3, column=1, pady=5, sticky="w")

radio_3 = tk.Radiobutton(ventana, text="3 Conjuntos", variable=conjunto_var, value="3")
radio_3.grid(row=3, column=1, pady=5, sticky="e")

# Entrada de texto para la operación
label_operacion = tk.Label(ventana, text="Operación:")
label_operacion.grid(row=4, column=0, padx=10, pady=5)
entry_operacion = tk.Entry(ventana)
entry_operacion.grid(row=4, column=1, padx=10, pady=5)

# Botón para realizar las operaciones
boton_operar = tk.Button(ventana, text="Realizar Operación", command=realizar_operacion)
boton_operar.grid(row=5, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=6, column=0, columnspan=2, pady=5)

# Iniciar el bucle principal
ventana.mainloop()
