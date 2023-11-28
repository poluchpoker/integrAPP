from random import *
from method_only_integral_and_method_integral_of_piece_res.arrays_variable_and_symbols import *

def generate_constants():
    constant = randint(-100, 100)
    while (constant == 0):
        constant = randint(-100, 100)
    array_constants.append(constant)

def generate_coef_for_polyn():  
    coefficient_polynom = randint(-100, 100)
    while (coefficient_polynom == 0):
        coefficient_polynom = randint(-100, 100)
    res_coef_polynom = coefficient_polynom
    array_coefficients_polynom.append(res_coef_polynom)

def generate_coef_for_polynomial():
    float_or_int_coefficient = randint(0, 1)
    if (float_or_int_coefficient):
        coefficient = randint(-100, 100)
        while (coefficient == 0):
            coefficient = randint(-100, 100)
        res_coef_polynomial = coefficient
    else:
        coefficient = uniform(-100.09, 100.09)
        while (coefficient == 0):
            coefficient = uniform(-100.09, 100.09)
        res_coef_polynomial = round(coefficient, 2)
    array_coefficients_polynomial.append(res_coef_polynomial)

def generate_degree_for_polynomial_integral_of_piece(degree_for_polynom_integral_of_piece):
    degree_integral_of_piece = randint(1, 4 / degree_for_polynom_integral_of_piece)
    while (degree_integral_of_piece == 0):
        degree_integral_of_piece = randint(1, 4 / degree_for_polynom_integral_of_piece)
    array_degree_for_variable_polyn.append(degree_integral_of_piece)

def generate_coef_for_func_trig():
    float_or_int_coefficient_trig = randint(0, 1)
    if (float_or_int_coefficient_trig):
        coefficient_trig = randint(-100, 100)
        while (coefficient_trig == 0):
            coefficient_trig = randint(-100, 100)
        res_coef_trig = coefficient_trig
    else:
        coefficient_trig = uniform(-100.09, 100.09)
        while (coefficient_trig == 0):
            coefficient_trig = uniform(-100.09, 100.09)
        res_coef_trig = round(coefficient_trig, 2)
    array_coefficients_trig.append(res_coef_trig)

def generate_coef_for_argument_triganometrix():
    coefficient_for_argument_triganometrix = randint(-4, 4)
    while (coefficient_for_argument_triganometrix == 0):
        coefficient_for_argument_triganometrix = randint(-4, 4)
    res_coef_trig = coefficient_for_argument_triganometrix
    array_coefficients_for_argument_triganometrix.append(res_coef_trig)

def generate_coef_for_func_exp():
    float_or_int_coefficient_exp = randint(0, 1)
    if (float_or_int_coefficient_exp):
        coefficient_exp = randint(-100, 100)
        while (coefficient_exp == 0):
            coefficient_exp = randint(-100, 100)
        res_coef_exp = coefficient_exp
    else:
        coefficient_exp = uniform(-100.09, 100.09)
        while (coefficient_exp == 0):
            coefficient_exp = uniform(-100.09, 100.09)
        res_coef_exp = round(coefficient_exp, 2)
    array_coefficients_exp.append(res_coef_exp)

def generate_coef_for_argument_exp():
    coefficient_for_argument_exp = randint(-4, 4)
    while (coefficient_for_argument_exp == 0):
        coefficient_for_argument_exp = randint(-4, 4)
    res_coef_exp = coefficient_for_argument_exp
    array_coefficients_for_argument_exp.append(res_coef_exp)

def generate_coef_for_argument_exp_integral_of_piece():
    coefficient_for_argument_exp_integral_of_piece = randint(1, 3)
    while (coefficient_for_argument_exp_integral_of_piece == 0):
        coefficient_for_argument_exp_integral_of_piece = randint(1, 3)
    array_coefficients_for_argument_exp.append(coefficient_for_argument_exp_integral_of_piece)

def generate_coef_for_func_logarifm():
    float_or_int_coefficient_logarifm = randint(0, 1)
    if (float_or_int_coefficient_logarifm):
        coefficient_logarifm = randint(-100, 100)
        while (coefficient_logarifm == 0):
            coefficient_logarifm = randint(-100, 100)
        res_coef_logarifm = coefficient_logarifm
    else:
        coefficient_logarifm = uniform(-100.09, 100.09)
        while (coefficient_logarifm == 0):
            coefficient_logarifm = uniform(-100.09, 100.09)
        res_coef_logarifm = round(coefficient_logarifm, 2)
    array_coefficients_logarifm.append(res_coef_logarifm)

def generate_coef_for_argument_logarifm():
    coefficient_for_argument_logarifm = randint(-4, 4)
    while (coefficient_for_argument_logarifm == 0):
        coefficient_for_argument_logarifm = randint(-4, 4)
    res_coef_logarifm = coefficient_for_argument_logarifm
    array_coefficients_for_argument_logarifm.append(res_coef_logarifm)

def generate_coef_for_argument_logarifm_integral_of_piece():
    coefficient_for_argument_logarifm_integral_of_piece = randint(1, 3)
    while (coefficient_for_argument_logarifm_integral_of_piece == 0):
        coefficient_for_argument_logarifm_integral_of_piece = randint(1, 3)
    array_coefficients_for_argument_logarifm.append(coefficient_for_argument_logarifm_integral_of_piece)

def generate_coef_for_func_trig_up():
    float_or_int_coefficient_trig_up = randint(0, 1)
    if (float_or_int_coefficient_trig_up):
        coefficient_trig_up = randint(-100, 100)
        while (coefficient_trig_up == 0):
            coefficient_trig_up = randint(-100, 100)
        res_coef_trig_up = coefficient_trig_up
    else:
        coefficient_trig_up = uniform(-100.09, 100.09)
        while (coefficient_trig_up == 0):
            coefficient_trig_up = uniform(-100.09, 100.09)
        res_coef_trig_up = round(coefficient_trig_up, 2)
    array_coefficients_trig_up.append(res_coef_trig_up)

def generate_coef_for_argument_triganometrix_up():
    coefficient_for_argument_triganometrix_up = randint(-4, 4)
    while (coefficient_for_argument_triganometrix_up == 0):
        coefficient_for_argument_triganometrix_up = randint(-4, 4)
    res_coef_trig_up = coefficient_for_argument_triganometrix_up
    array_coefficients_for_argument_triganometrix_up.append(res_coef_trig_up)

def generate_coef_for_argument_triganometrix_up_integral_of_piece():
    coefficient_for_argument_triganometrix_up_integral_of_piece = randint(1, 3)
    while (coefficient_for_argument_triganometrix_up_integral_of_piece == 0):
        coefficient_for_argument_triganometrix_up_integral_of_piece = randint(1, 3)
    array_coefficients_for_argument_triganometrix_up.append(coefficient_for_argument_triganometrix_up_integral_of_piece)

def generate_coef_for_power():
    float_or_int_coefficient_power = randint(0, 1)
    if (float_or_int_coefficient_power):
        coefficient_power = randint(-100, 100)
        while (coefficient_power == 0):
            coefficient_power = randint(-100, 100)
        res_coef_power = coefficient_power
    else:
        coefficient_power = uniform(-100.09, 100.09)
        while (coefficient_power == 0):
            coefficient_power = uniform(-100.09, 100.09)
        res_coef_power = round(coefficient_power, 2)
    array_coefficients_power.append(res_coef_power)

def generate_coef_for_argument_power():
    coefficient_for_argument_power = randint(-4, 4)
    while (coefficient_for_argument_power == 0):
        coefficient_for_argument_power = randint(-4, 4)
    array_coefficients_for_argument_power.append(coefficient_for_argument_power)

def generate_coef_for_argument_power_integral_of_piece():
    coefficient_for_argument_power_integral_of_piece = randint(1, 3)
    while (coefficient_for_argument_power_integral_of_piece == 0):
        coefficient_for_argument_power_integral_of_piece = randint(1, 3)
    array_coefficients_for_argument_power.append(coefficient_for_argument_power_integral_of_piece)

def random_degree():
    float_or_int_degree = randint(0, 1)
    if (float_or_int_degree):
        degree = randint(-100, 100)
        while (degree == 0): 
            degree = randint(-100, 100)
        res_degree = degree
    else:
        degree = uniform(-100.09, 100.09)
        while (degree == 0):
            degree = uniform(-100.09, 100.09)
        res_degree = round(degree)
    array_degree_polynomial.append(res_degree)

def random_degree_integral_of_piece():
    degree_integral_of_piece = randint(1, 3)
    while (degree_integral_of_piece == 0): 
        degree_integral_of_piece = randint(1, 3)
    array_degree_polynomial.append(degree_integral_of_piece)

def generate_degree_for_polynomial():
    float_or_int_degree_polyn = randint(0, 1)
    if (float_or_int_degree_polyn):
        degree_polynom = randint(-100, 100)
        while (degree_polynom == 0):
            degree_polynom = randint(-100, 100)
        res_degree_polynom = degree_polynom
    else:
        degree_polynom = uniform(-100.09, 100.09)
        while(degree_polynom == 0):
            degree_polynom = uniform(-100.09, 100.09)
        res_degree_polynom = round(degree_polynom, 2)
    array_degree_for_variable_polyn.append(res_degree_polynom)

def generate_degree_for_func_trig():
    float_or_int_degree_trig = randint(0, 1)
    if (float_or_int_degree_trig):
        degree_trig = randint(-100, 100)
        while (degree_trig == 0):
            degree_trig = randint(-100, 100)
        res_degree_trig = degree_trig
    else:
        degree_trig = uniform(-100.09, 100.09)
        while (degree_trig == 0):
            degree_trig = uniform(-100.09, 100.09)
        res_degree_trig = round(degree_trig, 2)
    array_degree_trig.append(res_degree_trig)

def generate_degree_for_func_trig_integral_of_piece():
    degree_trig_integral_of_piece = randint(1, 3)
    while (degree_trig_integral_of_piece == 0):
        degree_trig_integral_of_piece = randint(1, 3)
    array_degree_trig.append(degree_trig_integral_of_piece)

def generate_line(result, float_or_int_line):
    if (result == 0):
        if (float_or_int_line):
            res_line = randint(-100, 100)

            while (res_line == 0):
                res_line = randint(-100, 100)
        else:
            res_line = uniform(-9.99, 9.99)

            while (res_line == 0.0):
                res_line = uniform(-9.99, 9.99)

            res_line = round(res_line, 2)
    else:
        if (float_or_int_line):
            res_line = randint(result, result + 100)

            while (res_line == 0):
                res_line = randint(result, result + 100)
        else:
            res_line = uniform(result, result + 9.99)

            while (res_line == 0.0):
                res_line = uniform(result, result + 9.99)

            res_line = round(res_line, 2)
    return res_line

def generate_result_line():
    variant_line = randint(0, 1)
    float_or_int_line = randint(0, 1)

    if (variant_line):
        low_line = generate_line(0, float_or_int_line)
        high_line = generate_line(low_line, float_or_int_line)

    else:
        result_variante = randint(-8, -1)
        
        while (result_variante % 2 == 1 and result_variante % 3 == 1 and result_variante != 3):
            result_variante = randint(-8, -1)
        
        result_variante = pi / result_variante

        low_line = result_variante
        high_line = result_variante * (-1)

    array_line_variable.append(low_line)
    array_line_variable.append(high_line)