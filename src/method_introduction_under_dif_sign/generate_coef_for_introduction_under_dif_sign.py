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
def generate_line(result, float_or_int_line):
    if result == 0:
        if float_or_int_line:
            res_line = randint(-100, 100)

            while res_line == 0:
                res_line = randint(-100, 100)
        else:
            res_line = uniform(-9.99, 9.99)

            while res_line == 0.0:
                res_line = uniform(-9.99, 9.99)

            res_line = round(res_line, 2)
    else:
        if float_or_int_line:
            res_line = randint(result, result + 100)

            while res_line == 0:
                res_line = randint(result, result + 100)
        else:
            res_line = uniform(result, result + 9.99)

            while res_line == 0.0:
                res_line = uniform(result, result + 9.99)

            res_line = round(res_line, 2)
    return res_line


# генератор пределов интеграла
def generate_result_line():
    variant_line = randint(0, 1)
    float_or_int_line = randint(0, 1)

    if variant_line:
        low_line = generate_line(0, float_or_int_line)
        high_line = generate_line(low_line, float_or_int_line)

    else:
        result_variante = randint(-8, -1)

        while (
            result_variante % 2 == 1
            and result_variante % 3 == 1
            and result_variante != 3
        ):
            result_variante = randint(-8, -1)

        result_variante = pi / result_variante

        low_line = result_variante
        high_line = result_variante * (-1)

    array_line.append(low_line)
    array_line.append(high_line)
