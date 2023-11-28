import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkButton, CTkLabel, CTkFrame
from method_only_integral_and_method_integral_of_piece_res.method_only_integral import *
from method_only_integral_and_method_integral_of_piece_res.method_integral_of_piece import *
from method_introduction_under_dif_sign.method_introduction_under_dif_sign import *

LARGEFONT = ("Helvetica", 35)


class tkinterApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs) 
        container = CTkFrame(self)
        
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
class Menu(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        label = CTkLabel(self, text="Выберите раздел интегралов", font=LARGEFONT)
        label.grid(row=0, column=0, padx=400, pady=100, columnspan=2, sticky='nsew')

        button_definite_integral = CTkButton(self, text="Определенные интегралы",
                                            command=lambda: controller.show_frame(Definite_Integral))
        button_definite_integral.grid(row=1, column=0, padx=50, pady=50, columnspan=1, ipadx=60, ipady=60, sticky='nsew')

        button_indefinite_integral = CTkButton(self, text="Неопределенные интегралы",
                                                command=lambda: controller.show_frame(Indefinite_Integral))
        button_indefinite_integral.grid(row=1, column=1, padx=10, pady=50, columnspan=1, ipadx=60, ipady=60, sticky='nsew')


# Страница определенных интегралов
class Definite_Integral(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        label = CTkLabel(self, text="Определенные интегралы", font=LARGEFONT)
        label.grid(row=0, column=2, padx=5, pady=10, sticky='nsew')

        button_indefinite_integral = CTkButton(self, text="Неопределенные интегралы",
                                                command=lambda: controller.show_frame(Indefinite_Integral))
        button_indefinite_integral.grid(row=2, column=2, padx=10, pady=55, columnspan=1, ipadx=40, ipady=40, sticky='nsew')

        button_method_only_integral = CTkButton(self, text="Метод непосредственного интегрирования",
                                                command=method_only_integral_definite_integral)
        button_method_only_integral.grid(row=1, column=1, padx=40, pady=50, columnspan=1, ipadx=40, ipady=40, sticky='nsew')

        button_integral_of_piece = CTkButton(self, text="Интегрирование по частям",
                                            command=method_integral_of_piece_definite_integral)
        button_integral_of_piece.grid(row=1, column=3, padx=40, pady=60, columnspan=1, ipadx=40, ipady=40, sticky='nsew')

        button_introduction_under_dif_sign = CTkButton(self, text="Внесение под знак дифферинциала",
                                                        command=method_introduction_under_dif_sign)
        button_introduction_under_dif_sign.grid(row=1, column=2, padx=40, pady=60, columnspan=1, ipadx=40, ipady=40, sticky='nsew')


# Страница неопределенных интегралов
class Indefinite_Integral(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)

        label = CTkLabel(self, text="Неопределенные интегралы", font=LARGEFONT)
        label.grid(row=0, column=2, padx=5, pady=10, sticky='nsew')

        button_definite_integral = CTkButton(self, text="Определенные интегралы",
                                            command=lambda: controller.show_frame(Definite_Integral))
        button_definite_integral.grid(row=2, column=2, padx=10, pady=55, columnspan=1, ipadx=40, ipady=40, sticky='nsew')

        button_method_only_integral = CTkButton(self, text="Метод непосредственного интегрирования",
                                                command=method_only_integral)
        button_method_only_integral.grid(row=1, column=1, padx=40, pady=50, columnspan=1, ipadx=40, ipady=40, sticky='nsew')

        button_integral_of_piece = CTkButton(self, text="Интегрирование по частям",
                                            command=method_integral_of_piece)
        button_integral_of_piece.grid(row=1, column=3, padx=40, pady=60, columnspan=1, ipadx=40, ipady=40, sticky='nsew')

        button_introduction_under_dif_sign = CTkButton(self, text="Внесение под знак дифферинциала",
                                                        command=method_introduction_under_dif_sign)
        button_introduction_under_dif_sign.grid(row=1, column=2, padx=40, pady=60, columnspan=1, ipadx=40, ipady=40, sticky='nsew')


def method_only_integral():
    CTkMessagebox(title='Метод непосредственного интегрирования', message=f'∫ ({result_result()}) dx', width=500, height=250)

def method_integral_of_piece():
    CTkMessagebox(title='Метод интегрирования по частям', message=f'∫ ({result_method_integral_of_piece()}) dx', width=500, height=250)

def method_introduction_under_dis_sign():
    CTkMessagebox(title='Метод интегрирования путем внесения под дифферинциал', message=f'∫ ({result_introd_under_dif_sign()}) dx')

def method_only_integral_definite_integral():
    CTkMessagebox(title='Метод непосредственного интегрирования для определенного интеграла', message=f'∫ ({result_result()}) dx   найти интеграл от {array_line_variable[0]} до {array_line_variable[1]}')

def method_integral_of_piece_definite_integral():
    CTkMessagebox(title='Метод интегрирования по частям для определенного интеграла', message=f'∫ ({result_method_integral_of_piece()}) dx   найти интеграл от {array_line_variable[0]} до {array_line_variable[1]}')

def method_introduction_under_dif_sign():
    CTkMessagebox(title='Метод интегрирования путем внесения под дифферинциал', message=f'∫ ({result_introd_under_dif_sign()}) dx    найти интеграл от {array_line[0]} до {array_line[1]}')


# Driver Code
app = tkinterApp()
app.title("integrApp")
app.geometry("1280x720")
# app.resizable(True, True)
app.option_add('*Helvetica', 25)
# app.set_default_color_theme("dark-blue")

app.mainloop()

