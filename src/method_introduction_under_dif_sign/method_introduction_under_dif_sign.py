from method_introduction_under_dif_sign.generate_func_for_introduction_under_dif_sign import *
from method_introduction_under_dif_sign.arrays_for_introduction_under_dif_sign import *
from method_introduction_under_dif_sign.generate_coef_for_introduction_under_dif_sign import *
from method_introduction_under_dif_sign.calculate_func_for_introduction_under_dif_sing import *
from method_introduction_under_dif_sign.cleaning_machine_for_introd_under_dif_sign import *
from method_introduction_under_dif_sign.arrays_for_introduction_under_dif_sign import *

from random import *

# Интеграл вида P(x)*Q(x), где Q(X) - это производная P(x)
# Фактически P(x)*Q(x), если у нас P(x) - триг функция, то под такой метод может подойти либо полином, либо тригонометрия
# если P(x) - экспонента, логарфим или показательная функция - то с ними могут быть только полиномы
def metohd_introduction_under_dif_sign():
    exist_triganometrix = randint(0, 1)
    exist_exp = randint(0, 1)
    exist_logarifm = randint(0, 1)
    exist_pow = randint(0, 1)

    while (exist_triganometrix == 0 and exist_pow == 0 and exist_exp == 0 and exist_logarifm == 0):
        exist_triganometrix = randint(0, 1)
        exist_exp = randint(0, 1)
        exist_logarifm = randint(0, 1)
        exist_pow = randint(0, 1)

    exist_constant = randint(0, 1)
    exist_variable = randint(0, 1)
    exist_polynom = randint(0, 1)

    while (exist_variable == 0 and exist_polynom == 0):
        exist_variable = randint(0, 1)
        exist_polynom = randint(0, 1)
    
    if (exist_triganometrix): # существование триг-функции, фактически выбор P(x)
        variant_generate_polynom_or_triganometrix = randint(0, 1)

        if (variant_generate_polynom_or_triganometrix):  # то Q(x) - это триганометрия
            res = randint(1, 2)
            coefficient_variable = generate_constant()
            generate_coef_for_polynom()
            generate_degree_for_func()
            res_polynom_for_argument = generate_polynom(
                exist_polynom, exist_variable, exist_constant, 0)

            res = generate_trig_func_introduction_under_dif_sign(
                coefficient_variable, array_degree_for_trig[0], res_polynom_for_argument, res)
            generate_trig_func_introduction_under_dif_sign(
                coefficient_variable, 1, res_polynom_for_argument, res)
            
            generate_result_line()

            return result_all_func(111, res)
        else:  # то Q(x) - это полином
            res = randint(1, 2)
            amount_variable = randint(2, 4)
            coefficient_variable = generate_constant()

            for _ in range(amount_variable):
                generate_coef_for_polynom()
                generate_degree_for_variable_func_polynom()
                
            degree_for_trig_func = randint(-6, 6)
            degree_for_argument = randint(1, 10)

            while (degree_for_trig_func == 0):
                degree_for_trig_func = randint(-6, 6)

            if (exist_polynom == 0):
                if (exist_constant == 1):
                    result_polynom_for_argument_with_degree = generate_polynom(exist_polynom, exist_variable, exist_constant, 1)
                    result_polynom_for_argument_with_degree_2 = result_polynom_for_argument_with_degree ** (degree_for_argument + 1)
                    result_polynom_for_argument_with_degree **= degree_for_argument

                    res = generate_trig_func_introduction_under_dif_sign(coefficient_variable, degree_for_trig_func, result_polynom_for_argument_with_degree_2, res)
                else:
                    result_polynom_for_argument_with_degree_2 = array_coef_for_polynom[0] * x ** (degree_for_argument + 1)
                    result_polynom_for_argument_with_degree = x ** degree_for_argument
                    result_polynom_for_argument_with_degree *= array_coef_for_polynom[0]

                    res = generate_trig_func_introduction_under_dif_sign(coefficient_variable, degree_for_trig_func, result_polynom_for_argument_with_degree_2, res)
            else:
                    result_polynom_for_argument_with_degree = generate_polynom(exist_polynom, exist_variable, exist_constant, 1)
                    result_polynom_for_argument_with_degree_2 = result_polynom_for_argument_with_degree ** (degree_for_argument + 1)
                    result_polynom_for_argument_with_degree **= degree_for_argument

                    res = generate_trig_func_introduction_under_dif_sign(coefficient_variable, degree_for_trig_func, result_polynom_for_argument_with_degree_2, res)
            generate_result_line()
            return result_all_func(1101, result_polynom_for_argument_with_degree)
    elif (exist_exp): # существование экспоненты P(x)
        amount_variable = randint(2, 4)

        for _ in range(amount_variable):
            generate_coef_for_polynom()
            generate_degree_for_variable_func_polynom()
            
        generate_coef_for_exp_introduction_under_dif_sign()
        degree_for_argument = randint(1, 10)
        
        if (exist_polynom == 0):
            if (exist_constant == 1):
                res_polynom_for_argument_exp = generate_polynom(exist_polynom, exist_variable, exist_constant, 1)
                res_polynom_for_argument_exp_2 = res_polynom_for_argument_exp ** degree_for_argument
                res_polynom_for_argument_exp **= (degree_for_argument + 1)

                generate_exp_func_introduction_under_dif_sign(array_coef_for_exp[0], res_polynom_for_argument_exp)
                generate_result_line()
            else:
                res_polynom_for_argument_exp_2 = array_coef_for_polynom[0] * x ** (degree_for_argument + 1)
                res_polynom_for_argument_exp = x ** degree_for_argument
                res_polynom_for_argument_exp *= array_coef_for_polynom[0]

                generate_exp_func_introduction_under_dif_sign(array_coef_for_exp[0], res_polynom_for_argument_exp_2)
                generate_result_line()
                
                return result_all_func(11, res_polynom_for_argument_exp)
        else:
            res_polynom_for_argument_exp = generate_polynom(exist_polynom, exist_variable, exist_constant, 1)
            res_polynom_for_argument_exp_2 = res_polynom_for_argument_exp ** degree_for_argument
            res_polynom_for_argument_exp **= (degree_for_argument + 1)

            generate_exp_func_introduction_under_dif_sign(array_coef_for_exp[0], res_polynom_for_argument_exp)
            generate_result_line()
        return result_all_func(11, res_polynom_for_argument_exp_2)

    elif (exist_logarifm): # P(x) - логаримфм
        base_log = randint(2, 32)

        amount_variable = randint(2, 4)

        for _ in range(amount_variable):
            generate_coef_for_polynom()
            generate_degree_for_variable_func_polynom()
        
        generate_coef_for_logarifm_introduction_under_dif_sign()
        degree_for_argument = randint(1, 100)
        variant_generate_integral_logarifm = randint(1, 2) # если 1 - то вид P(x)*Q(x), если 2, то Q(x)/P(x)
        if (variant_generate_integral_logarifm == 1):
            if (exist_polynom == 0):
                if (exist_constant):
                    res_polynom_for_argument_logarifm = generate_polynom(exist_polynom, exist_variable, exist_constant, 1)
                    res_polynom_for_argument_logarifm_2 = res_polynom_for_argument_logarifm ** (degree_for_argument + 1)
                    res_polynom_for_argument_logarifm **= degree_for_argument

                    generate_logarim_func_introduction_under_dif_sign(array_coef_for_logarifm[0], res_polynom_for_argument_logarifm_2, base_log)
                else:
                    res_polynom_for_argument_logarifm_2 = array_coef_for_polynom[0] * x ** (degree_for_argument + 1)
                    res_polynom_for_argument_logarifm = x ** degree_for_argument
                    res_polynom_for_argument_logarifm *= array_coef_for_polynom[0]

                    generate_logarim_func_introduction_under_dif_sign(array_coef_for_logarifm[0], res_polynom_for_argument_logarifm_2, base_log)
            else:
                res_polynom_for_argument_logarifm = generate_polynom(exist_polynom, exist_variable, exist_constant, 1)
                res_polynom_for_argument_logarifm_2 = res_polynom_for_argument_logarifm ** (degree_for_argument + 1)
                res_polynom_for_argument_logarifm **= degree_for_argument

                generate_logarim_func_introduction_under_dif_sign(array_coef_for_logarifm[0], res_polynom_for_argument_logarifm_2, base_log)
            generate_result_line()
            return result_all_func(10011, res_polynom_for_argument_logarifm)
        else:
            if (exist_polynom == 0):
                if (exist_constant):
                    res_polynom_for_argument_logarifm = generate_polynom(exist_polynom, exist_variable, exist_constant, 0)

                    generate_logarim_func_introduction_under_dif_sign(array_coef_for_logarifm[0], res_polynom_for_argument_logarifm, base_log)
                else:
                    res_polynom_for_argument_logarifm = array_coef_for_polynom[0] * x

                    generate_logarim_func_introduction_under_dif_sign(array_coef_for_logarifm[0], res_polynom_for_argument_logarifm, base_log)
            else:
                res_polynom_for_argument_logarifm = generate_polynom(exist_polynom, exist_variable, exist_constant, 0)

                generate_logarim_func_introduction_under_dif_sign(array_coef_for_logarifm[0], res_polynom_for_argument_logarifm, base_log)
            generate_result_line()
            return result_all_func(10010, res_polynom_for_argument_logarifm)
    elif (exist_pow): # P(x) - показательная функция
        amount_variable = randint(2, 4)

        for _ in range(amount_variable):    
            generate_coef_for_polynom()
            generate_degree_for_variable_func_polynom()
        
        degree_for_argument = randint(1, 10)
        if (exist_polynom == 0):
            if (exist_constant):
                res_polynom_for_pow = generate_polynom(exist_polynom, exist_variable, exist_constant, 0)
                res_polynom_for_pow_2 = res_polynom_for_pow ** (degree_for_argument + 1)
                res_polynom_for_pow **= degree_for_argument 

                generate_pow_func_introduction_under_dif_sign(generate_constant(), res_polynom_for_pow_2)
            else:
                res_polynom_for_pow_2 = array_coef_for_polynom[0] * x ** (degree_for_argument + 1)
                res_polynom_for_pow = x ** degree_for_argument
                res_polynom_for_pow *= array_coef_for_polynom[0]

                generate_pow_func_introduction_under_dif_sign(generate_constant(), res_polynom_for_pow_2)
        else:
            res_polynom_for_pow = generate_polynom(exist_polynom, exist_variable, exist_constant, 1)
            res_polynom_for_pow_2 = res_polynom_for_pow ** (degree_for_argument + 1)
            res_polynom_for_pow **= degree_for_argument

            generate_pow_func_introduction_under_dif_sign(generate_constant(), res_polynom_for_pow_2)
        generate_result_line()
        return result_all_func(10001, res_polynom_for_pow)


def result_introd_under_dif_sign():
    cleaning_machine_for_introd_under_dif_sign()
    return metohd_introduction_under_dif_sign()