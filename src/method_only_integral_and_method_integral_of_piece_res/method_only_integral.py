from random import *
from sympy import *

from method_only_integral_and_method_integral_of_piece_res.generate_coefficient import *
from method_only_integral_and_method_integral_of_piece_res.arrays_variable_and_symbols import *
from method_only_integral_and_method_integral_of_piece_res.generate_existense_variable import *
from method_only_integral_and_method_integral_of_piece_res.generate_func import *
from method_only_integral_and_method_integral_of_piece_res.calculate_func import *
from method_only_integral_and_method_integral_of_piece_res.clearing_lists import *


def method_only_integral():
    res_generate_exist_pol = generate_existence_degree_polynomial()
    res_generate_exist_polynomial = generate_existence_polynomial()
    res_generate_exist_triganometrix = generate_existence_triganometrix()
    res_generate_exist_exp = generate_existence_exp()

    while (
        res_generate_exist_polynomial == 0
        and res_generate_exist_triganometrix == 0
        and res_generate_exist_exp == 0
    ):
        res_generate_exist_polynomial = generate_existence_polynomial()
        res_generate_exist_triganometrix = generate_existence_triganometrix()
        res_generate_exist_exp = generate_existence_exp()

    if res_generate_exist_pol:
        amount_targers_polynom = randint(2, amount_targers - 2)
        count_polynom = amount_targers - amount_targers_polynom
        if res_generate_exist_polynomial * count_polynom:
            amount_variable_targers = randint(1, count_polynom)
            count = amount_targers - amount_variable_targers
            if res_generate_exist_triganometrix * count:
                amount_triganomix_variable = randint(1, count)
                count_trig_func = count - amount_triganomix_variable
                if res_generate_exist_exp * count_trig_func:
                    amount_logarifmix_variable = count_trig_func

                    for _ in range(1, amount_variable_targers + 1):
                        random_degree()
                        generate_coef_for_polynomial()

                    for _ in range(1, amount_targers_polynom + 1):
                        generate_coef_for_polyn()
                        generate_degree_for_polynomial()

                    for element_trig in range(0, amount_triganomix_variable):
                        generate_coef_for_func_trig()
                        generate_coef_for_argument_triganometrix()
                        generate_trig_func(element_trig)

                    for element_exp in range(0, amount_logarifmix_variable):
                        generate_coef_for_func_exp()
                        generate_coef_for_argument_exp()
                        generate_exp_func(element_exp)

                    generate_result_line()
                else:
                    for _ in range(1, amount_variable_targers + 1):
                        random_degree()
                        generate_coef_for_polynomial()

                    for _ in range(1, amount_targers_polynom + 1):
                        generate_coef_for_polyn()
                        generate_degree_for_polynomial()

                    for element in range(0, amount_triganomix_variable):
                        generate_coef_for_func_trig()
                        generate_coef_for_argument_triganometrix()
                        generate_trig_func(element)

                    generate_result_line()
            elif res_generate_exist_exp * count:
                for _ in range(1, amount_variable_targers + 1):
                    random_degree()
                    generate_coef_for_polynomial()

                for _ in range(1, amount_targers_polynom + 1):
                    generate_coef_for_polyn()
                    generate_degree_for_polynomial()

                for element_exp in range(0, count):
                    generate_coef_for_func_exp()
                    generate_coef_for_argument_exp()
                    generate_exp_func(element_exp)

                generate_result_line()
            else:
                for _ in range(1, amount_variable_targers + 1):
                    random_degree()
                    generate_coef_for_polynomial()

                for _ in range(1, amount_targers_polynom + 1):
                    generate_coef_for_polyn()
                    generate_degree_for_polynomial()

                generate_result_line()
                return polynomial_calc(
                    res_generate_exist_pol,
                    res_generate_exist_polynomial,
                    degree_for_polyn,
                )
        elif res_generate_exist_triganometrix:
            amount_triganomix_variable = randint(1, amount_targers_polynom)
            count_trig_func = amount_targers_polynom - amount_triganomix_variable
            if res_generate_exist_exp * count_trig_func:
                amount_logarifmix_variable = count_trig_func

                for _ in range(1, amount_targers_polynom + 1):
                    generate_coef_for_polyn()
                    generate_degree_for_polynomial()

                for element_trig in range(0, amount_triganomix_variable):
                    generate_coef_for_func_trig()
                    generate_coef_for_argument_triganometrix()
                    generate_trig_func(element_trig)

                for element_exp in range(0, amount_logarifmix_variable):
                    generate_coef_for_func_exp()
                    generate_coef_for_argument_exp()
                    generate_exp_func(element_exp)

                generate_result_line()
            else:
                for _ in range(1, amount_targers_polynom + 1):
                    generate_coef_for_polyn()
                    generate_degree_for_polynomial()

                for element in range(0, amount_triganomix_variable):
                    generate_coef_for_func_trig()
                    generate_coef_for_argument_triganometrix()
                    generate_trig_func(element)

                generate_result_line()
        elif res_generate_exist_exp:
            for _ in range(1, amount_targers_polynom + 1):
                generate_coef_for_polyn()
                generate_degree_for_polynomial()

            for element_exp in range(0, count_polynom):
                generate_coef_for_func_exp()
                generate_coef_for_argument_exp()
                generate_exp_func(element_exp)

            generate_result_line()
        else:
            for _ in range(1, amount_targers_polynom + 1):
                generate_coef_for_polyn()
                generate_degree_for_polynomial()

            generate_result_line()
    else:
        if res_generate_exist_polynomial:
            amount_variable_targers = randint(1, amount_targers)
            count = amount_targers - amount_variable_targers
            if res_generate_exist_triganometrix * count:
                amount_triganomix_variable = randint(1, count)
                count_trig_func = count - amount_triganomix_variable
                if res_generate_exist_exp * count_trig_func:
                    amount_logarifmix_variable = count_trig_func

                    for _ in range(1, amount_variable_targers + 1):
                        random_degree()
                        generate_coef_for_polynomial()

                    for element_trig in range(0, amount_triganomix_variable):
                        generate_coef_for_func_trig()
                        generate_coef_for_argument_triganometrix()
                        generate_trig_func(element_trig)

                    for element_exp in range(0, amount_logarifmix_variable):
                        generate_coef_for_func_exp()
                        generate_coef_for_argument_exp()
                        generate_exp_func(element_exp)

                    generate_result_line()
                else:
                    for _ in range(1, amount_variable_targers + 1):
                        random_degree()
                        generate_coef_for_polynomial()

                    for element in range(0, amount_triganomix_variable):
                        generate_coef_for_func_trig()
                        generate_coef_for_argument_triganometrix()
                        generate_trig_func(element)

                    generate_result_line()
            elif res_generate_exist_exp * count:
                for _ in range(1, amount_variable_targers + 1):
                    random_degree()
                    generate_coef_for_polynomial()

                for element_exp in range(0, count):
                    generate_coef_for_func_exp()
                    generate_coef_for_argument_exp()
                    generate_exp_func(element_exp)

                generate_result_line()
            else:
                for _ in range(1, amount_variable_targers + 1):
                    random_degree()
                    generate_coef_for_polynomial()

                generate_result_line()
                return polynomial_calc(
                    res_generate_exist_pol, res_generate_exist_polynomial, 0
                )
        elif res_generate_exist_triganometrix:
            amount_triganomix_variable = randint(1, amount_targers)
            count_trig_func = amount_targers - amount_triganomix_variable
            if res_generate_exist_exp * count_trig_func:
                amount_logarifmix_variable = count_trig_func

                for element_trig in range(0, amount_triganomix_variable):
                    generate_coef_for_func_trig()
                    generate_coef_for_argument_triganometrix()
                    generate_trig_func(element_trig)
                    
                for element_exp in range(0, amount_logarifmix_variable):
                    generate_coef_for_func_exp()
                    generate_coef_for_argument_exp()
                    generate_exp_func(element_exp)

                generate_result_line()
            else:
                for element in range(0, amount_triganomix_variable):
                    generate_coef_for_func_trig()
                    generate_coef_for_argument_triganometrix()
                    generate_trig_func(element)

                generate_result_line()
        elif res_generate_exist_exp:
            for element_exp in range(0, amount_targers):
                generate_coef_for_func_exp()
                generate_coef_for_argument_exp()
                generate_exp_func(element_exp)

            generate_result_line()
    return calc(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn)


def result_result():
    clearing_machine()
    return method_only_integral()


# def show_result():
#     print(f"∫ ({method_only_integral()}) dx")

# show_result()
