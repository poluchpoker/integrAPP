from random import *
from sympy import *

from method_only_integral_and_method_integral_of_piece_res.arrays_variable_and_symbols import *

def generate_trig_func(element):
    triganomterix_variable = randint(1, 4)
    if (triganomterix_variable == 1):
        # sin = symbols(f'sin({array_coefficients_for_argument_triganometrix[element] * x})')
        sinus = lambda element, x: sin(array_coefficients_for_argument_triganometrix[element] * x)
        array_trig.append(sinus(element, x))
    elif (triganomterix_variable == 2):
        # cos = symbols(f'cos({array_coefficients_for_argument_triganometrix[element] * x})')
        cosinus = lambda element, x: cos(array_coefficients_for_argument_triganometrix[element] * x)
        array_trig.append(cosinus(element, x))
    elif (triganomterix_variable == 3):
        # tan = symbols(f'tan({array_coefficients_for_argument_triganometrix[element] * x})')
        tangens = lambda element, x: tan(array_coefficients_for_argument_triganometrix[element] * x)
        array_trig.append(tangens(element, x))
    else:
        # ctg = symbols(f'ctg({array_coefficients_for_argument_triganometrix[element] * x})')
        cotan = lambda element, x: cot(array_coefficients_for_argument_triganometrix[element] * x)
        array_trig.append(cotan(element, x))

def generate_trig_func_with_degree(element):
    triganomterix_variable = randint(1, 4)
    if (triganomterix_variable == 1):
        # sin = symbols(f'sin({array_coefficients_for_argument_triganometrix[element] * x})^({array_degree_trig[element]})')
        sinus = lambda element, x: sin(array_coefficients_for_argument_triganometrix[element] * x) ** (array_degree_trig[element])
        array_trig.append(sinus(element, x))
    elif (triganomterix_variable == 2):
        # cos = symbols(f'cos({array_coefficients_for_argument_triganometrix[element] * x})^({array_degree_trig[element]})')
        cosinus = lambda element, x: cos(array_coefficients_for_argument_triganometrix[element] * x) ** (array_degree_trig[element])
        array_trig.append(cosinus(element, x))
    elif (triganomterix_variable == 3):
        # tan = symbols(f'tan({array_coefficients_for_argument_triganometrix[element] * x})^({array_degree_trig[element]})')
        tangens = lambda element, x: tan(array_coefficients_for_argument_triganometrix[element] * x) ** (array_degree_trig[element])
        array_trig.append(tangens(element, x))
    else:
        # ctg = symbols(f'ctg({array_coefficients_for_argument_triganometrix[element] * x})^({array_degree_trig[element]})')
        cotangens = lambda element, x: cot(array_coefficients_for_argument_triganometrix[element] * x) ** (array_degree_trig[element])
        array_trig.append(cotangens(element, x))

def generate_trig_up_func_with_degree(element):
    triganomterix_up_variable = randint(1, 4)
    if (triganomterix_up_variable == 1):
        # arcsin = symbols(f'arcsin({array_coefficients_for_argument_triganometrix_up[element] * x})^({array_degree_trig[element]})')
        arcsin = lambda element, x: asin(array_coefficients_for_argument_triganometrix_up[element] * x) ** (array_degree_trig[element])
        array_trig.append(arcsin(element, x))
    elif (triganomterix_up_variable == 2):
        # arccos = symbols(f'arccos({array_coefficients_for_argument_triganometrix_up[element] * x})^({array_degree_trig[element]})')
        arccos = lambda element, x: acos(array_coefficients_for_argument_triganometrix_up[element] * x) ** (array_degree_trig[element])
        array_trig.append(arccos)
    elif (triganomterix_up_variable == 3):
        # arctan = symbols(f'arctan({array_coefficients_for_argument_triganometrix_up[element] * x})^({array_degree_trig[element]})')
        arctan = lambda element, x: atan(array_coefficients_for_argument_triganometrix_up[element] * x) ** (array_degree_trig[element])
        array_trig.append(arctan(element, x))
    else:
        arcctg = lambda element, x: 1 / atan(array_coefficients_for_argument_triganometrix_up[element] * x) ** (array_degree_trig[element])
        array_trig.append(arcctg(element, x))

def generate_exp_func(element):
    # exp = symbols(f'exp({array_coefficients_for_argument_exp[element] * x})')
    expanents = lambda element, x: exp(array_coefficients_for_argument_exp[element] * x)
    array_exp.append(expanents(element, x))

def generate_logarifm_func(element):
    # log = symbols(f'log{integral_base}({array_coefficients_logarifm[element] * x})')
    logarifm = lambda element, x: log(integral_base, array_coefficients_logarifm[element] * x)
    array_logarifm.append(logarifm(element, x))

def generate_trig_up_func(element):
    triganometrix_up_variable = randint(1, 4)
    if (triganometrix_up_variable == 1):
        # arcsin = symbols(f'arcsin({array_coefficients_for_argument_triganometrix_up[element] * x})')
        arcsinus = lambda element, x: asin(array_coefficients_for_argument_triganometrix_up[element] * x)
        array_trig.append(arcsinus(element, x))
    elif (triganometrix_up_variable == 2):
        # arccos = symbols(f'arccos({array_coefficients_for_argument_triganometrix_up[element] * x})')
        arccosinus = lambda element, x: acos(array_coefficients_for_argument_triganometrix_up[element] * x)
        array_trig.append(arccosinus(element, x))
    elif (triganometrix_up_variable == 3):
        # arctg = symbols(f'arctg({array_coefficients_for_argument_triganometrix_up[element] * x})')
        arctangens = lambda element, x: atan(array_coefficients_for_argument_triganometrix_up[element] * x)
        array_trig.append(arctangens(element, x))
    elif (triganometrix_up_variable == 4):
        # arcctg = symbols(f'arcctg({array_coefficients_for_argument_triganometrix_up[element] * x})')
        arcctangens = lambda element, x: 1 / atan(array_coefficients_for_argument_triganometrix_up[element] * x)
        array_trig.append(arcctangens(element, x))
    
def generate_power_func(element):
    # power = symbols(f'{array_coefficients_power[element]}^({array_coefficients_for_argument_power[element] * x})')
    power = lambda element, x: array_coefficients_power[element] ** (array_coefficients_for_argument_power[element] * x)
    array_power.append((power(element, x)))

