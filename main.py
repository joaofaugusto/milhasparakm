import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# função de converter

def converter():
    entrada_milha = entry_int.get()
    km_saida = entrada_milha * 1.61
    output_string.set(km_saida)


# janela
janela = ttk.Window(themename= 'litera')
janela.title('Demo')
janela.geometry('300x150')

# titulo
title_label = ttk.Label(master = janela, text = 'Milhas para quilômetros', font = 'Calibri 24 bold')
title_label.pack()

# campo de entrada
input_frame = ttk.Frame(master = janela)
entry_int = tk.IntVar()
entry = ttk.Entry(
    master = input_frame, 
    textvariable = entry_int)
button = ttk.Button(
    master = input_frame, 
    text = 'Converter', 
    command= converter)
entry.pack(side = 'left', padx= 10)
button.pack(side = 'left')
input_frame.pack(pady= 10)

# saída
output_string = tk.StringVar()
output_label = ttk.Label(
    master = janela, 
    text = 'Saída', 
    font = 'Calibri 24', 
    textvariable = output_string)
output_label.pack()
# executar 
janela.mainloop()