from tkinter import ttk
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
        if operacion == 'u':
            resultado = union(conjunto_a, conjunto_b)
        elif operacion == '&':
            resultado = interseccion(conjunto_a, conjunto_b)
        elif operacion == '-':
            resultado = diferencia(conjunto_a, conjunto_b)
        elif operacion == '^':
            resultado = complemento(union(conjunto_a, conjunto_b), conjunto_a)
        else:
            resultado = []
    elif num_conjuntos == '3':
        if operacion == 'u':
            resultado = union3(conjunto_a, conjunto_b, conjunto_c)
        elif operacion == '&':
            resultado = interseccion3(conjunto_a, conjunto_b, conjunto_c)
        elif operacion == '-':
            resultado = diferencia3(conjunto_a, conjunto_b, conjunto_c)
        elif operacion == '^':
            resultado = complemento3(union3(conjunto_a, conjunto_b, conjunto_c), conjunto_a)
        else:
            resultado = []



    # Mostrar los resultados en las etiquetas
    label_resultado.config(text=f"{operacion.capitalize()}: {resultado}")

    # Mostrar los resultados en los gráficos de Venn
    if num_conjuntos == '2':
        mostrar_venn2(conjunto_a, conjunto_b, resultado)
    elif num_conjuntos == '3':
        mostrar_venn3(conjunto_a, conjunto_b, conjunto_c, resultado)


# Frames para organizar la interfaz
frame_entradas = ttk.Frame(ventana, padding="10")
frame_entradas.grid(row=0, column=0, columnspan=2, pady=10)

frame_radios = ttk.Frame(ventana)
frame_radios.grid(row=1, column=0, columnspan=2, pady=5)

frame_resultado = ttk.Frame(ventana, padding="10")
frame_resultado.grid(row=2, column=0, columnspan=2, pady=5)

# Entradas de texto para los conjuntos
label_a = ttk.Label(frame_entradas, text="Conjunto A:")
label_a.grid(row=0, column=0, padx=10, pady=5)
entry_a = ttk.Entry(frame_entradas)
entry_a.grid(row=0, column=1, padx=10, pady=5)

label_b = ttk.Label(frame_entradas, text="Conjunto B:")
label_b.grid(row=1, column=0, padx=10, pady=5)
entry_b = ttk.Entry(frame_entradas)
entry_b.grid(row=1, column=1, padx=10, pady=5)

# Entrada de texto para el conjunto C (si es necesario)
label_c = ttk.Label(frame_entradas, text="Conjunto C:")
label_c.grid(row=2, column=0, padx=10, pady=5)
entry_c = ttk.Entry(frame_entradas)
entry_c.grid(row=2, column=1, padx=10, pady=5)

# Número de conjuntos
label_conjuntos = ttk.Label(frame_radios, text="Número de conjuntos:")
label_conjuntos.grid(row=0, column=0, pady=5, sticky="e")

conjunto_var = StringVar()
conjunto_var.set("2")  # Por defecto, seleccionar 2 conjuntos
radio_2 = ttk.Radiobutton(frame_radios, text="2 Conjuntos", variable=conjunto_var, value="2")
radio_2.grid(row=0, column=1, pady=5, padx=(0, 10))

radio_3 = ttk.Radiobutton(frame_radios, text="3 Conjuntos", variable=conjunto_var, value="3")
radio_3.grid(row=0, column=2, pady=5)

# Entrada de texto para la operación
label_operacion = ttk.Label(frame_entradas, text="Operación:")
label_operacion.grid(row=3, column=0, padx=10, pady=5)
entry_operacion = ttk.Entry(frame_entradas)
entry_operacion.grid(row=3, column=1, padx=10, pady=5)

# Botón para realizar las operaciones
boton_operar = ttk.Button(ventana, text="Realizar Operación", command=realizar_operacion)
boton_operar.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = ttk.Label(frame_resultado, text="")
label_resultado.grid(row=0, column=0, pady=5)

def actualizar_habilitacion_conjunto_c():
    if conjunto_var.get() == '3':
        entry_c.config(state=tk.NORMAL)
    else:
        entry_c.config(state=tk.DISABLED)

# Asociar la función de actualización a los RadioButtons
radio_2.config(command=actualizar_habilitacion_conjunto_c)
radio_3.config(command=actualizar_habilitacion_conjunto_c)

# Llamar a la función al inicio para configurar el estado inicial
actualizar_habilitacion_conjunto_c()

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x_pos = (ancho_pantalla - ventana.winfo_reqwidth()) // 2
y_pos = (alto_pantalla - ventana.winfo_reqheight()) // 2

# Establecer las coordenadas de la ventana
ventana.geometry(f"+{x_pos-80}+{y_pos-100}")

# Iniciar el bucle principal
ventana.mainloop()
