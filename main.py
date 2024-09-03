import math
import tkinter as tk
from tkinter import messagebox

class ConvertidorAngulo:
    def __init__(self, valor):
        self.valor = valor

    def grados_a_radianes(self):
        """Convierte el valor de grados a radianes."""
        return self.valor * (math.pi / 180)

    def radianes_a_grados(self):
        """Convierte el valor de radianes a grados."""
        return self.valor * (180 / math.pi)

class InterfazConvertidor:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor de Ángulos")

        # Etiqueta para la opción
        self.label_opcion = tk.Label(root, text="Selecciona la conversión:")
        self.label_opcion.pack(pady=10)

        # Botones de conversión
        self.btn_grados_a_radianes = tk.Button(root, text="Grados a Radianes", command=self.convertir_grados_a_radianes)
        self.btn_grados_a_radianes.pack(pady=5)

        self.btn_radianes_a_grados = tk.Button(root, text="Radianes a Grados", command=self.convertir_radianes_a_grados)
        self.btn_radianes_a_grados.pack(pady=5)

        # Entrada de valor
        self.label_valor = tk.Label(root, text="Ingrese el valor:")
        self.label_valor.pack(pady=10)
        self.entry_valor = tk.Entry(root)
        self.entry_valor.pack(pady=5)

    def convertir_grados_a_radianes(self):
        try:
            valor = float(self.entry_valor.get())
            convertidor = ConvertidorAngulo(valor)
            radianes = convertidor.grados_a_radianes()
            messagebox.showinfo("Resultado", f"{valor} grados son {radianes:.4f} radianes.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

    def convertir_radianes_a_grados(self):
        try:
            valor = float(self.entry_valor.get())
            convertidor = ConvertidorAngulo(valor)
            grados = convertidor.radianes_a_grados()
            messagebox.showinfo("Resultado", f"{valor} radianes son {grados:.4f} grados.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazConvertidor(root)
    root.mainloop()
