from random import *
from sympy import *

array_constants = []
array_coefficients_polynomial = []
array_coefficients_polynom = []
array_coefficients_trig = []
array_coefficients_exp = []
array_coefficients_trig_up = []
array_coefficients_logarifm = []
array_coefficients_power = []
array_coefficients_for_argument_triganometrix = []
array_coefficients_for_argument_exp = []
array_coefficients_for_argument_triganometrix_up = []
array_coefficients_for_argument_logarifm = []
array_coefficients_for_argument_power = []
array_trig = []
array_trig_result = []
array_exp = []
array_exp_result = []
array_logarifm = []
array_logarifm_result = []
array_power = []
array_power_result = []
array_degree_for_polyn = []
array_degree_for_variable_polyn = []
array_degree_polynomial = []
array_degree_trig = []
array_expression = []
array_line_variable = []

x = symbols("x")
amount_targers = randint(4, 10)
float_or_int_degree_for_polyn = 1
degree_for_polyn = 10
if (float_or_int_degree_for_polyn):
    degree_for_polyn = randint(-100, 100)
    while (degree_for_polyn == 0):
        degree_for_polyn = randint(-100, 100)
else: 
    degree_for_polyn = uniform(-100.09, 100.09)
    while(degree_for_polyn == 0):
        degree_for_polyn = uniform(-100.09, 100.09)
    degree_for_polyn = round(degree_for_polyn, 1)
amount_targers_for_method_integral_of_piece = 2
integral_base = randint(2, 64)