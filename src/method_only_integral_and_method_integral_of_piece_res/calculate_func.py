from math import *
from method_only_integral_and_method_integral_of_piece_res.arrays_variable_and_symbols import *
from method_only_integral_and_method_integral_of_piece_res.generate_existense_variable import *
from method_only_integral_and_method_integral_of_piece_res.help_arrays_for_image import *

def polynomial_calc(trust, trust_degree_polynom, degree_for_polyn):
    element_polynomial = 0
    if (len(array_coefficients_polynomial) or len(array_coefficients_polynom)):
        if (trust and trust_degree_polynom):
            element = array_coefficients_polynom[element_polynomial] * x ** array_degree_for_variable_polyn[element_polynomial]
            for element_polynomial_1 in range(1, len(array_degree_for_variable_polyn)):
                element += array_coefficients_polynom[element_polynomial_1] * x ** array_degree_for_variable_polyn[element_polynomial_1]
            res_elem_with_degree = element ** degree_for_polyn
            if (len(array_coefficients_polynomial)):
                for element_polynomial in range(1, len(array_coefficients_polynomial)):
                    res_elem_with_degree += array_coefficients_polynomial[element_polynomial] * x ** array_degree_polynomial[element_polynomial]
                return res_elem_with_degree
            return res_elem_with_degree
        elif (trust):
            element = array_coefficients_polynom[element_polynomial] * x ** array_degree_for_variable_polyn[element_polynomial]
            for element_polynomial_2 in range(1, len(array_degree_for_variable_polyn)):
                element += array_coefficients_polynom[element_polynomial_2] * x ** array_degree_for_variable_polyn[element_polynomial_2]
            res_elem_with_degree = element ** degree_for_polyn  
            return res_elem_with_degree
        elif (trust_degree_polynom):
            res_elem_without_degree = array_coefficients_polynomial[element_polynomial] * x ** array_degree_polynomial[element_polynomial]
            for element_polynomial in range(1, len(array_coefficients_polynomial)):
                    res_elem_without_degree += array_coefficients_polynomial[element_polynomial] * x ** array_degree_polynomial[element_polynomial]
            return res_elem_without_degree
        
def polynomial_calc1(trust, trust_degree_polynom, degree_for_polyn):
    element_polynomial = 0
    if (len(array_coefficients_polynomial) or len(array_coefficients_polynom)):
        if (trust and trust_degree_polynom):
            element = Symbol(f'{array_coefficients_polynom[element_polynomial]}x^{{{array_degree_for_variable_polyn[element_polynomial]}}}')
            for element_polynomial_1 in range(1, len(array_degree_for_variable_polyn)):
                element += Symbol(f'{array_coefficients_polynom[element_polynomial_1]}x^{{{array_degree_for_variable_polyn[element_polynomial_1]}}}')
            if (len(array_coefficients_polynomial)):
                res_elem_with_degree = Symbol('')
                for element_polynomial in range(1, len(array_coefficients_polynomial)):
                    res_elem_with_degree += Symbol(f'{array_coefficients_polynomial[element_polynomial]}x^{{{array_degree_polynomial[element_polynomial]}}}')
                return res_elem_with_degree
            return element
        elif (trust):
            element = Symbol(f'{array_coefficients_polynom[element_polynomial]}x^{{{array_degree_for_variable_polyn[element_polynomial]}}}')
            for element_polynomial_2 in range(1, len(array_degree_for_variable_polyn)):
                element += Symbol(f'{array_coefficients_polynom[element_polynomial_2]}x^{{{array_degree_for_variable_polyn[element_polynomial_2]}}}')
            return element
        elif (trust_degree_polynom):
            res_elem_without_degree = Symbol(f'{array_coefficients_polynomial[element_polynomial]}x^{{{array_degree_polynomial[element_polynomial]}}}')
            for element_polynomial in range(1, len(array_coefficients_polynomial)):
                    res_elem_without_degree += Symbol(f'{array_coefficients_polynomial[element_polynomial]}x^{{{array_degree_polynomial[element_polynomial]}}}')
            return res_elem_without_degree


def trig_calc():
    global element_trig_result
    if (len(array_coefficients_for_argument_triganometrix) != 0):
        for element_coef_trig, trig_func in zip(array_coefficients_trig, array_trig):
            array_trig_result.append(element_coef_trig * trig_func)
        element_trig_result = array_trig_result[0]
        for element_trig in range(1, len(array_trig_result)):
            element_trig_result += array_trig_result[element_trig]
        return element_trig_result

def trig_calc1():
    global element_trig_result
    if (len(array_coefficients_for_argument_triganometrix) != 0):
        for element_coef_trig, trig_func in zip(array_coefficients_trig, array_trig1):
            array_trig_result1.append(Symbol(f'{2 * element_coef_trig}{trig_func}'))
        element_trig_result = array_trig_result1[0]
        for element_trig in range(1, len(array_trig_result1)):
            element_trig_result += array_trig_result1[element_trig]
        return element_trig_result

def exp_calc():
    global element_exp_result
    if (len(array_coefficients_for_argument_exp) != 0):
        for element_coef_exp, exp_func in zip(array_coefficients_exp, array_exp):
            array_exp_result.append(element_coef_exp * exp_func)
        element_exp_result = array_exp_result[0]
        for element_exp in range(1, len(array_exp_result)):
            element_exp_result += array_exp_result[element_exp]
        return element_exp_result
    
def exp_calc1():
    global element_exp_result
    if (len(array_coefficients_for_argument_exp) != 0):
        for element_coef_exp, exp_func in zip(array_coefficients_exp, array_exp1):
            array_exp_result1.append(Symbol(f'{2 * element_coef_exp}{exp_func}'))
        element_exp_result = array_exp_result1[0]
        for element_exp in range(1, len(array_exp_result1)):
            element_exp_result += array_exp_result1[element_exp]
        return element_exp_result

def log_calc():
    global element_log_result
    if (len(array_coefficients_for_argument_logarifm) != 0):
        for element_coef_log, log_func in zip(array_coefficients_logarifm, array_logarifm):
            array_logarifm_result.append(element_coef_log * log_func)
        element_log_result = array_logarifm_result[0]
        for element_log in range(1, len(array_logarifm_result)):
            element_log_result += array_logarifm_result[element_log]
        return element_log_result
    
def log_calc1():
    global element_log_result
    if (len(array_coefficients_for_argument_logarifm) != 0):
        for element_coef_log, log_func in zip(array_coefficients_logarifm, array_logarifm1):
            array_logarifm_result1.append(Symbol(f'{2 * element_coef_log}{log_func}'))
        element_log_result = array_logarifm_result1[0]
        for element_log in range(1, len(array_logarifm_result)):
            element_log_result += array_logarifm_result1[element_log]
        return element_log_result

def trig_calc_up():
    global element_trig_result_up
    if (len(array_coefficients_for_argument_triganometrix_up) != 0):
        for element_coef_trig, trig_func in zip(array_coefficients_trig_up, array_trig):
            array_trig_result.append(element_coef_trig * trig_func)
        element_trig_result_up = array_trig_result[0]
        for element_trig in range(1, len(array_trig_result)):
            element_trig_result_up += array_trig_result[element_trig]
        return element_trig_result_up

def trig_calc_up1():
    global element_trig_result_up
    if (len(array_coefficients_for_argument_triganometrix_up) != 0):
        for element_coef_trig, trig_func in zip(array_coefficients_trig_up, array_trig1):
            array_trig_result1.append(Symbol(f'{2 * element_coef_trig}{trig_func}'))
        element_trig_result_up = array_trig_result1[0]
        for element_trig in range(1, len(array_trig_result1)):
            element_trig_result_up += array_trig_result1[element_trig]
        return element_trig_result_up
    
def trig_calc_with_degree():
    global element_trig_result_with_degree
    if (len(array_coefficients_for_argument_triganometrix) != 0):
        for element_coef_trig, trig_func in zip(array_coefficients_trig, array_trig):
            array_trig_result.append(element_coef_trig * trig_func)
        element_trig_result_with_degree = array_trig_result[0]
        for element_trig in range(1, len(array_trig_result)):
            element_trig_result_with_degree += array_trig_result[element_trig]
        return element_trig_result_with_degree
    
def trig_calc_with_degree1():
    global element_trig_result_with_degree
    if (len(array_coefficients_for_argument_triganometrix) != 0):
        for element_coef_trig, trig_func in zip(array_coefficients_trig, array_trig1):
            array_trig_result1.append(Symbol(f'{2 * element_coef_trig}{trig_func}'))
        element_trig_result_with_degree = array_trig_result1[0]
        for element_trig in range(1, len(array_trig_result1)):
            element_trig_result_with_degree += array_trig_result1[element_trig]
        return element_trig_result_with_degree
    
def power_calc():
    global element_power_result
    if (len(array_coefficients_for_argument_power) != 0):
        element_power_result = array_power[0]
        for element_power in range(1, len(array_power)):
            element_power_result += array_power[element_power]
        return element_power_result
    
def power_calc1():
    global element_power_result
    if (len(array_coefficients_for_argument_power) != 0):
        element_power_result = array_power1[0]
        for element_power in range(1, len(array_power1)):
            element_power_result += array_power1[element_power]
        return element_power_result

def calc(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn):
    a = exp_calc()
    b = trig_calc()
    c = polynomial_calc(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn)
    if (a != None and b != None and c != None):
        return b + c + a
    elif (a == None and b != None and c != None):
        return c + b
    elif (a != None and b != None and c == None):
        return a + b
    elif (a != None and b == None and c != None):
        return c + a
    elif (a == None and b == None and c != None):
        return c
    elif (a == None and b != None and c == None):
        return b
    elif (a != None and b == None and c == None):
        return a
    
def calc1(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn):
    a = exp_calc()
    b = trig_calc()
    c = polynomial_calc1(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn)
    if (a != None and b != None and c != None):
        return b + c + a
    elif (a == None and b != None and c != None):
        return c + b
    elif (a != None and b != None and c == None):
        return a + b
    elif (a != None and b == None and c != None):
        return c + a
    elif (a == None and b == None and c != None):
        return c
    elif (a == None and b != None and c == None):
        return b
    elif (a != None and b == None and c == None):
        return a
    
def calc_of_piece(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn):
    existence_polynomial = polynomial_calc(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn)
    existence_trig = trig_calc()
    existence_trig_with_degree = trig_calc_with_degree()
    existence_trig_up = trig_calc_up()
    existence_exp = exp_calc()
    existence_logarifm = log_calc()
    existence_power = power_calc()
    if (existence_polynomial != None and existence_trig != None):
        return existence_polynomial * existence_trig_with_degree
    elif (existence_polynomial != None and existence_trig_up != None):
        return existence_polynomial * existence_trig_up
    elif (existence_polynomial != None and existence_exp != None):
        return existence_polynomial * existence_exp
    elif (existence_polynomial != None and existence_logarifm != None):
        return existence_polynomial * existence_logarifm
    elif (existence_polynomial != None and existence_power != None):
        return existence_polynomial * existence_power
    
def calc_of_piece1(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn):
    existence_polynomial = polynomial_calc1(res_generate_exist_pol, res_generate_exist_polynomial, degree_for_polyn)
    existence_trig = trig_calc1()
    existence_trig_with_degree = trig_calc_with_degree1()
    existence_trig_up = trig_calc_up1()
    existence_exp = exp_calc1()
    existence_logarifm = log_calc1()
    existence_power = power_calc1()
    if (existence_polynomial != None and existence_trig != None):
        return existence_polynomial * existence_trig_with_degree
    elif (existence_polynomial != None and existence_trig_up != None):
        return existence_polynomial * existence_trig_up
    elif (existence_polynomial != None and existence_exp != None):
        return existence_polynomial * existence_exp
    elif (existence_polynomial != None and existence_logarifm != None):
        return existence_polynomial * existence_logarifm
    elif (existence_polynomial != None and existence_power != None):
        return existence_polynomial * existence_power
