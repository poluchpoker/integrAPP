import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from method_only_integral_and_method_integral_of_piece_res.method_only_integral import *
from method_only_integral_and_method_integral_of_piece_res.method_integral_of_piece import *
from method_introduction_under_dif_sign.method_introduction_under_dif_sign import *

LARGEFONT = ("Helvetica", 35)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True, ipadx=200, ipady=200, anchor="center", padx=0, pady=80)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Menu, Definite_Integral, Indefinite_Integral):
            frame = F(container, self)
            
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Страница меню
class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Выберите раздел интегралов", font=LARGEFONT, foreground='red')
        label.grid(row=0, column=0, padx=400, pady=100, columnspan=2)

        button_definite_integral = ttk.Button(self, text="Определенные интегралы",
                            command=lambda: controller.show_frame(Definite_Integral))
        button_definite_integral.grid(row=1, column=0, padx=50, pady=50, columnspan=1, ipadx=60, ipady=60)

        button_indefinite_integral = ttk.Button(self, text="Неопределенные интегралы",
                            command=lambda: controller.show_frame(Indefinite_Integral))
        button_indefinite_integral.grid(row=1, column=1, padx=10, pady=50, columnspan=1, ipadx=60, ipady=60)


# Страница определенных интегралов
class Definite_Integral(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Определенные интегралы", font=LARGEFONT, foreground='red')
        label.grid(row=0, column=2, padx=5, pady=10)

        button_indefinite_integral = ttk.Button(self, text="Неопределенные интегралы",
                            command=lambda: controller.show_frame(Indefinite_Integral))
        button_indefinite_integral.grid(row=2, column=2, padx=10, pady=55, columnspan=1, ipadx=40, ipady=40)

        button_method_only_integral = ttk.Button(self, text="Метод непосредственного интегрирования",
                            command=method_only_integral_definite_integral)
        button_method_only_integral.grid(row=1, column=1, padx=40, pady=50, columnspan=1, ipadx=40, ipady=40)

        button_integral_of_piece = ttk.Button(self, text="Интегрирование по частям",
                            command=method_integral_of_piece_definite_integral)
        button_integral_of_piece.grid(row=1, column=3, padx=40, pady=60, columnspan=1, ipadx=40, ipady=40)

        button_introduction_under_dif_sign = ttk.Button(self, text="Внесение под знак дифферинциала",
                                                        command=method_introduction_under_dif_sign)
        button_introduction_under_dif_sign.grid(row=1, column=2, padx=40, pady=60, columnspan=1, ipadx=40, ipady=40)


# Страница неопределенных интегралов
class Indefinite_Integral(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Неопределенные интегралы", font=LARGEFONT, foreground='red')
        label.grid(row=0, column=2, padx=5, pady=10)

        button_definite_integral = ttk.Button(self, text="Определенные интегралы",
                            command=lambda: controller.show_frame(Definite_Integral))
        button_definite_integral.grid(row=2, column=2, padx=10, pady=10, ipadx=40, ipady=40)

        button_method_only_integral = ttk.Button(self, text="Метод непосредственного интегрирования",
                            command=method_only_integral)
        button_method_only_integral.grid(row=1, column=1, padx=40, pady=50, columnspan=1, ipadx=40, ipady=40)

        button_integral_of_piece = ttk.Button(self, text="Интегрирование по частям",
                            command=method_integral_of_piece)
        button_integral_of_piece.grid(row=1, column=3, padx=40, pady=60, columnspan=1, ipadx=40, ipady=40)

        button_introduction_under_dif_sign = ttk.Button(self, text="Внесение под знак дифферинциала",
                                                        command=method_introduction_under_dis_sign)
        button_introduction_under_dif_sign.grid(row=1, column=2, padx=40, pady=60, columnspan=1, ipadx=40, ipady=40)


def method_only_integral():
    messagebox.showinfo('Метод непосредственного интегрирования', f'∫ ({result_result()}) dx')

def method_integral_of_piece():
    messagebox.showinfo('Метод интегрирования по частям', f'∫ ({result_method_integral_of_piece()}) dx')

def method_introduction_under_dis_sign():
    messagebox.showinfo('Метод интегрирования путем внесения под дифферинциал', f'∫ ({result_introd_under_dif_sign()}) dx')

def method_only_integral_definite_integral():
    messagebox.showinfo('Метод непосредственного интегрирования для определенного интеграла', f'∫ ({result_result()}) dx   найти интеграл от {array_line_variable[0]} до {array_line_variable[1]}')

def method_integral_of_piece_definite_integral():
    messagebox.showinfo('Метод интегрирования по частям для определенного интеграла', f'∫ ({result_method_integral_of_piece()}) dx   найти интеграл от {array_line_variable[0]} до {array_line_variable[1]}')

def method_introduction_under_dif_sign():
    messagebox.showinfo('Метод интегрирования путем внесения под дифферинциал', f'∫ ({result_introd_under_dif_sign()}) dx    найти интеграл от {array_line[0]} до {array_line[1]}')

# Driver Code
app = tkinterApp()
app.title("integrApp")
app.geometry("1920x1080")
app.option_add('*Helvetica', 25)


app.mainloop()
