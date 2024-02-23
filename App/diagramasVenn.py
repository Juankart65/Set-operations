from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import StringVar
from matplotlib_venn import venn2, venn3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from metodos import *


def mostrar_venn2(conjunto_a, conjunto_b, resultado):
    plt.clf()  # Limpiar el gráfico anterior

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(5, 3))
    fig.suptitle('Operaciones de Conjuntos (2 Conjuntos)')

    # Mostrar el gráfico de Venn
    if len(resultado) > 0:
        venn_diagram = venn2([conjunto_a, conjunto_b], set_labels=('A', 'B'), ax=axes)
        axes.set_title(f'Resultado: {resultado}')

        # Obtener los objetos de las áreas
        area_100 = venn_diagram.get_patch_by_id('100')
        area_010 = venn_diagram.get_patch_by_id('010')
        area_110 = venn_diagram.get_patch_by_id('110')

        # Etiquetar las áreas con los elementos
        area_100.set_label(', '.join(diferencia(conjunto_a, conjunto_b)))
        area_010.set_label(', '.join(diferencia(conjunto_b, conjunto_a)))
        area_110.set_label(', '.join(interseccion(conjunto_a, conjunto_b)))

        # Agregar leyenda
        plt.legend(loc="lower left", bbox_to_anchor=(1.5, 0), title="Valores")
    else:
        axes.set_title('Operación no válida')

    # Ajustes para evitar superposiciones
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=8, column=0, columnspan=2, pady=10)

    ventana.update_idletasks()  # Actualizar la ventana después de mostrar el gráfico

def mostrar_venn3(conjunto_a, conjunto_b, conjunto_c, resultado):
    plt.clf()  # Limpiar el gráfico anterior

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(5, 3))
    fig.suptitle('Operaciones de Conjuntos (3 Conjuntos)')

    # Mostrar el gráfico de Venn
    if len(resultado) > 0:
        venn_diagram = venn3([conjunto_a, conjunto_b, conjunto_c], set_labels=('A', 'B', 'C'), ax=axes)
        axes.set_title(f'Resultado: {resultado}')

        # Obtener los objetos de las áreas
        area_100 = venn_diagram.get_patch_by_id('100')
        area_010 = venn_diagram.get_patch_by_id('010')
        area_001 = venn_diagram.get_patch_by_id('001')
        area_110 = venn_diagram.get_patch_by_id('110')
        area_101 = venn_diagram.get_patch_by_id('101')
        area_011 = venn_diagram.get_patch_by_id('011')
        area_111 = venn_diagram.get_patch_by_id('111')

        # Etiquetar las áreas con los elementos
        if area_100 is not None:
            area_100.set_label(', '.join(diferencia3(conjunto_a, conjunto_b, conjunto_c)))
        if area_010 is not None:
            area_010.set_label(', '.join(diferencia3(conjunto_a, conjunto_b, conjunto_c)))
        if area_001 is not None:
            area_001.set_label(', '.join(diferencia3(conjunto_a, conjunto_b, conjunto_c)))
        if area_110 is not None:
            area_110.set_label(', '.join(interseccion3(conjunto_a, conjunto_b, conjunto_c)))
        if area_101 is not None:
            area_101.set_label(', '.join(interseccion3(conjunto_a, conjunto_b, conjunto_c)))
        if area_011 is not None:
            area_011.set_label(', '.join(interseccion3(conjunto_a, conjunto_b, conjunto_c)))
        if area_111 is not None:
            area_111.set_label(', '.join(union3(conjunto_a, conjunto_b, conjunto_c)))


        # Agregar leyenda
        plt.legend(loc="lower left", bbox_to_anchor=(1.5, 0), title="Valores")
    else:
        axes.set_title('Operación no válida')

    # Ajustes para evitar superposiciones
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=8, column=0, columnspan=2, pady=10)

    ventana.update_idletasks()  # Actualizar la ventana después de mostrar el gráfico
  

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Operaciones de Conjuntos")