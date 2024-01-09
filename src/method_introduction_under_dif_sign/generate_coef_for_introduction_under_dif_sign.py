from random import *
from method_introduction_under_dif_sign.arrays_for_introduction_under_dif_sign import *


# генератор константы
def generate_constant():
    constant = randint(-10, 10)

    while constant == 0:
        constant = randint(-10, 10)

    return constant


# генератор коэф-та для переменных полинома
def generate_coef_for_polynom():
    coef_for_polynom = randint(-10, 10)

    while coef_for_polynom == 0:
        coef_for_polynom = randint(-10, 10)

    array_coef_for_polynom.append(coef_for_polynom)


# генератор коэф-та для тригонометрической функции
def generate_coef_for_trig_introduction_under_dif_sign():
    coef_for_trig_under_dif_sign = randint(-10, 10)

    while coef_for_trig_under_dif_sign == 0:
        coef_for_trig_under_dif_sign = randint(-10, 10)

    array_coef_for_trig.append(coef_for_trig_under_dif_sign)


# генератор коэф-та для аргумента тригонометрической функции
def generate_coef_polynom_for_trig_under_argemnt():
    coef_for_argument_trig_under_dif_sign = randint(-4, 4)

    while coef_for_argument_trig_under_dif_sign == 0:
        coef_for_argument_trig_under_dif_sign = randint(-4, 4)

    array_coef_for_argument_trig.append(coef_for_argument_trig_under_dif_sign)


# генератор коэф-та для экспоненты
def generate_coef_for_exp_introduction_under_dif_sign():
    coef_for_exp_under_dif_sign = randint(-10, 10)

    while coef_for_exp_under_dif_sign == 0:
        coef_for_exp_under_dif_sign = randint(-10, 10)

    array_coef_for_exp.append(coef_for_exp_under_dif_sign)


# генератор коэф-та для логорифма
def generate_coef_for_logarifm_introduction_under_dif_sign():
    coef_for_logarifm_under_dif_sign = randint(-10, 10)

    while coef_for_logarifm_under_dif_sign == 0:
        coef_for_logarifm_under_dif_sign = randint(-10, 10)

    array_coef_for_logarifm.append(coef_for_logarifm_under_dif_sign)


# генератор для степени тригонометрической функции
def generate_degree_for_func():
    float_or_int_degree_for_trig = randint(0, 1)
    if float_or_int_degree_for_trig:
        degree_for_trig = randint(-10, 10)

        while degree_for_trig == 0:
            degree_for_trig = randint(-10, 10)
    else:
        degree_for_trig = uniform(-9.9, 9.9)

        while degree_for_trig == 0.0:
            degree_for_trig = uniform(-9.9, 9.9)

        degree_for_trig = round(degree_for_trig, 2)

    array_degree_for_trig.append(degree_for_trig)


# генератор степени для полинома
def generate_degree_for_variable_func_polynom():
    degree_for_variable_polynom = randint(-10, 10)

    while degree_for_variable_polynom == 0:
        degree_for_variable_polynom = randint(-10, 10)

    array_degree_for_variable_polynom.append(degree_for_variable_polynom)


# генератор пределов интеграла
def generate_line(result):
    if (result == 0):
        res_line = randint(1, 6)

        while (res_line == 0):
            res_line = randint(1, 6)
    else:
        res_line = randint(result, 10)

        while (res_line == 0):
            res_line = randint(result, 10)
    return res_line

def generate_result_line():
    low_line = generate_line(0)
    high_line = generate_line(low_line)

    while (low_line == high_line):
        low_line = generate_line(0)
        high_line = generate_line(low_line)

    array_line_variable.append(low_line)
    array_line_variable.append(high_line)
