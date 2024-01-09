from method_introduction_under_dif_sign.arrays_for_introduction_under_dif_sign import *
from method_introduction_under_dif_sign.generate_func_for_introduction_under_dif_sign import *


# функция для подсчета интеграла с тригонометричискими функциями
def trig_calc():
    if len(array_trig):
        res_element = array_trig[0]

        for element_tring in range(1, len(array_trig)):
            res_element *= array_trig[element_tring]

        return res_element
    
def trig_calc1():
    if len(array_trig1):
        res_element = Symbol(f'{array_trig1[0]}')

        for element_tring in range(1, len(array_trig1)):
            res_element *= Symbol(f'{array_trig1[element_tring]}')

        return res_element


def result_all_func(
    number_code, result_polynom_for_argument_with_degree
):  # по кодовому номеру выполняем создание интеграла
    if number_code == 111:
        return trig_calc()
    elif number_code == 1101:
        return trig_calc() * result_polynom_for_argument_with_degree
    elif number_code == 11:
        return array_exp[0] * result_polynom_for_argument_with_degree
    elif number_code == 10011:
        return array_log[0] * result_polynom_for_argument_with_degree
    elif number_code == 10010:
        return array_log[0] / result_polynom_for_argument_with_degree
    elif number_code == 10001:
        return array_pow[0] * result_polynom_for_argument_with_degree
    
def result_all_func1(
    number_code, result_polynom_for_argument_with_degree
):  # по кодовому номеру выполняем создание интеграла
    if number_code == 111:
        return trig_calc1()
    elif number_code == 1101:
        return trig_calc1() * result_polynom_for_argument_with_degree
    elif number_code == 11:
        return array_exp1[0] * result_polynom_for_argument_with_degree
    elif number_code == 10011:
        return array_log1[0] * result_polynom_for_argument_with_degree
    elif number_code == 10010:
        return array_log1[0] / result_polynom_for_argument_with_degree
    elif number_code == 10001:
        return array_pow1[0] * result_polynom_for_argument_with_degree
