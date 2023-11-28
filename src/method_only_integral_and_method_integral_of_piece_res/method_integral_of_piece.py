from method_only_integral_and_method_integral_of_piece_res.arrays_variable_and_symbols import *
from method_only_integral_and_method_integral_of_piece_res.generate_coefficient import *
from method_only_integral_and_method_integral_of_piece_res.generate_existense_variable import *
from method_only_integral_and_method_integral_of_piece_res.generate_func import *
from method_only_integral_and_method_integral_of_piece_res.calculate_func import *
from method_only_integral_and_method_integral_of_piece_res.clearing_lists import *

def method_integral_of_piece():
    res_generate_exist_pol = generate_existence_degree_polynomial()
    res_generate_exist_polynomial = generate_existence_polynomial()
    res_generate_exist_triganometrix = generate_existence_triganometrix()
    res_generate_exist_triganometrix_up = generate_existence_triganometrix_up()
    res_generate_exist_exp = generate_existence_exp()
    res_generate_exist_logarifm = generate_existence_logarifm()
    res_generate_exist_power = generate_existence_power()

    
    while (res_generate_exist_triganometrix == 0 and res_generate_exist_exp == 0 and
        res_generate_exist_triganometrix_up == 0 and res_generate_exist_logarifm == 0 and res_generate_exist_power == 0 and res_generate_exist_pol == 0):
        res_generate_exist_pol = generate_existence_degree_polynomial()
        res_generate_exist_triganometrix = generate_existence_triganometrix()
        res_generate_exist_triganometrix_up = generate_existence_triganometrix_up()
        res_generate_exist_exp = generate_existence_exp()
        res_generate_exist_logarifm = generate_existence_logarifm()
        res_generate_exist_power = generate_existence_power()
    
    if (res_generate_exist_pol == 0):
        res_generate_exist_polynomial = 1
        random_degree_integral_of_piece()
        generate_coef_for_polynomial()
        while (res_generate_exist_triganometrix == 0 and res_generate_exist_exp == 0 and
            res_generate_exist_triganometrix_up == 0 and res_generate_exist_logarifm == 0 and res_generate_exist_power == 0):
            res_generate_exist_triganometrix = generate_existence_triganometrix()
            res_generate_exist_triganometrix_up = generate_existence_triganometrix_up()
            res_generate_exist_exp = generate_existence_exp()
            res_generate_exist_logarifm = generate_existence_logarifm()
            res_generate_exist_power = generate_existence_power()
        if (res_generate_exist_triganometrix):
            generate_coef_for_func_trig()
            generate_coef_for_argument_triganometrix()
            generate_degree_for_func_trig_integral_of_piece()
            generate_trig_func_with_degree(0)
            generate_result_line()
        elif (res_generate_exist_triganometrix_up):
            generate_coef_for_func_trig_up()
            generate_coef_for_argument_triganometrix_up()
            generate_degree_for_func_trig_integral_of_piece()
            generate_trig_up_func_with_degree(0)
            generate_result_line()
        elif (res_generate_exist_exp):
            generate_coef_for_func_exp();
            generate_coef_for_argument_exp_integral_of_piece()
            generate_exp_func(0)
            generate_result_line()
        elif (res_generate_exist_logarifm):
            generate_coef_for_func_logarifm()
            generate_coef_for_argument_logarifm_integral_of_piece()
            generate_logarifm_func(0)
            generate_result_line()
        elif (res_generate_exist_power):
            generate_coef_for_power()
            generate_coef_for_argument_power_integral_of_piece()
            generate_power_func(0)
            generate_result_line()
    else:
        degree_for_poly_method_integral_of_piece = randint(1, 2)
        amount_tageres_for_integral_of_piece = randint(2, 4)
        for _ in range(1, amount_tageres_for_integral_of_piece + 1):
            generate_coef_for_polyn()
            generate_degree_for_polynomial_integral_of_piece(degree_for_poly_method_integral_of_piece)
        while (res_generate_exist_triganometrix == 0 and res_generate_exist_exp == 0 and res_generate_exist_triganometrix_up == 0 and res_generate_exist_logarifm == 0 and res_generate_exist_power == 0):
            res_generate_exist_triganometrix = generate_existence_triganometrix()
            res_generate_exist_triganometrix_up = generate_existence_triganometrix_up()
            res_generate_exist_exp = generate_existence_exp()
            res_generate_exist_logarifm = generate_existence_logarifm()
            res_generate_exist_power = generate_existence_power()
        res_generate_exist_polynomial = 0
        if (res_generate_exist_triganometrix):
            generate_coef_for_func_trig()
            generate_coef_for_argument_triganometrix()
            generate_degree_for_func_trig_integral_of_piece()
            generate_trig_func_with_degree(0)
            generate_result_line()
        elif (res_generate_exist_triganometrix_up):
            generate_coef_for_func_trig_up()
            generate_coef_for_argument_triganometrix_up()
            generate_degree_for_func_trig_integral_of_piece()
            generate_trig_up_func_with_degree(0)
            generate_result_line()
        elif (res_generate_exist_exp):
            generate_coef_for_func_exp();
            generate_coef_for_argument_exp_integral_of_piece()
            generate_exp_func(0)
            generate_result_line()
        elif (res_generate_exist_logarifm):
            generate_coef_for_func_logarifm()
            generate_coef_for_argument_logarifm_integral_of_piece()
            generate_logarifm_func(0)
            generate_result_line()
        elif (res_generate_exist_power):
            generate_coef_for_power()
            generate_coef_for_argument_power_integral_of_piece()
            generate_power_func(0)
            generate_result_line()
        return calc_of_piece(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_poly_method_integral_of_piece)
    return calc_of_piece(res_generate_exist_pol, res_generate_exist_polynomial, 0)

def result_method_integral_of_piece():
    clearing_machine()
    return method_integral_of_piece()

# def show_result():
#     print(f"∫ ({method_integral_of_piece()}) dx")

# show_result()