from method_introduction_under_dif_sign.arrays_for_introduction_under_dif_sign import *
from method_introduction_under_dif_sign.generate_coef_for_introduction_under_dif_sign import *

from sympy import *
from random import *


# генератор полинома (trust_polynom - наличие полинома, trust_variable - наличие переменной(в случае отсутствия полинома),
# trust_constant - наличие константыm, exist_degree - наличие степени у переменных)
def generate_polynom(trust_polynom, trust_variable, trust_constant, exist_degree):
    constant_for_res = generate_constant()
    if trust_polynom == 1 and trust_constant == 1 and exist_degree == 0:
        element = array_coef_for_polynom[0] * x + constant_for_res
        for number_element in range(1, len(array_coef_for_polynom)):
            element += array_coef_for_polynom[number_element] * x

        return element
    elif trust_polynom == 1 and trust_constant == 1 and exist_degree == 1:
        element = (
            array_coef_for_polynom[0] * x ** array_degree_for_variable_polynom[0]
            + constant_for_res
        )
        for number_element in range(1, len(array_coef_for_polynom)):
            element += (
                array_coef_for_polynom[number_element]
                * x ** array_degree_for_variable_polynom[number_element]
            )

        return element
    elif trust_polynom == 1 and trust_constant == 0 and exist_degree == 1:
        element = array_coef_for_polynom[0] * x ** array_degree_for_variable_polynom[0]
        for number_element in range(1, len(array_coef_for_polynom)):
            element += (
                array_coef_for_polynom[number_element]
                * x ** array_degree_for_variable_polynom[number_element]
            )

        return element
    elif trust_polynom == 1 and trust_constant == 0 and exist_degree == 0:
        element = array_coef_for_polynom[0] * x
        for number_element in range(1, len(array_coef_for_polynom)):
            element += array_coef_for_polynom[number_element] * x

        return element
    elif trust_variable == 1 and trust_constant == 1 and exist_degree == 0:
        element = array_coef_for_polynom[0] * x + constant_for_res

        return element
    elif trust_variable == 1 and trust_constant == 1 and exist_degree == 1:
        degree = randint(1, 4)
        element = array_coef_for_polynom[0] * x**degree + constant_for_res

        return element
    elif trust_variable == 1 and trust_constant == 0 and exist_degree == 0:
        element = array_coef_for_polynom[0] * x

        return element
    elif trust_variable == 1 and trust_constant == 0 and exist_degree == 1:
        degree = randint(1, 4)
        element = array_coef_for_polynom[0] * x**degree

        return element
    else:
        return constant_for_res


# генератор триг функции коэф-нт, степень, аргумент функции, результат для НЕ повторения функции
def generate_trig_func_introduction_under_dif_sign(coef_trig, degree, variable, res):
    variant_triganometrix_variable = randint(1, 2)

    if (
        variant_triganometrix_variable == 1
        and res == 2
        or variant_triganometrix_variable == 2
        and res == 2
    ):
        sinus = lambda x, coef_trig, degree: coef_trig * sin(x) ** degree
        array_trig.append(sinus(variable, coef_trig, degree))

        return 1
    elif (
        variant_triganometrix_variable == 2
        and res == 1
        or variant_triganometrix_variable == 1
        and res == 1
    ):
        cosinus = lambda x, coef_trig, degree: coef_trig * cos(x) ** degree
        array_trig.append(cosinus(variable, coef_trig, degree))

        return 2


# генератор экспоненты коэф-нт, аргумент экспоненты
def generate_exp_func_introduction_under_dif_sign(coef_exp, variable):
    expanenta = lambda x, coef_exp: coef_exp * exp(x)
    array_exp.append(expanenta(variable, coef_exp))


# генератор логарифма коэф-нт, аргумент интеграла, основание
def generate_logarim_func_introduction_under_dif_sign(coef_logarifm, variable, base):
    logarifm = lambda x, coef_logarifm, base: coef_logarifm * log(x, base)
    array_log.append(logarifm(variable, coef_logarifm, base))


# генератор показательной функции основание степени, показатель степени
def generate_pow_func_introduction_under_dif_sign(const, variable):
    pow_func = lambda x, const: const**x
    array_pow.append(pow_func(variable, const))
