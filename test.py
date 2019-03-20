# from const import const
# from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot, make_e_expr, make_ln, make_absv
# from tof import tof
# from riemann import riemann_approx, riemann_approx_with_gt, plot_riemann_error
# from deriv import deriv
# from antideriv import antideriv, antiderivdef
# from defintegralapprox import midpoint_rule, trapezoidal_rule, simpson_rule
from hw09_s19 import display_csv_file, read_csv_file, plot_bee_traffic, sr_approx, test
import unittest
import numpy as np
import math

class Assign01UnitTests(unittest.TestCase):

    # def test_01(self):
    #     print("****Unit Test 01********")
    #     display_csv_file('bee_traffic_estimates\\192_168_4_5-2018-07-01_08-00-10.csv')
    #     print("Unit Test 01: pass")
    #
    # def test_02(self):
    #     print("****Unit Test 02********")
    #     fd = read_csv_file('bee_traffic_estimates\\192_168_4_5-2018-07-01_08-00-10.csv')
    #     print(fd[5])
    #     print(fd[28])
    #     plot_bee_traffic('bee_traffic_estimates\\192_168_4_5-2018-07-01_08-00-10.csv')
    #     print("Unit Test 02: pass")

    def test_03(self):
        print("****Unit Test 03********")
        print( sr_approx(lambda x: x**2, 0, 2, 10))
        # print(sr_approx(lambda x: x**3, 1, 5, 100))

    # def test_04(self):
    #     print("****Unit Test 04********")
    #     test('bee_traffic_estimates\\192_168_4_5-2018-07-01_08-00-10.csv')
    #     print("*****")
    #     test('bee_traffic_estimates\\192_168_4_5-2018-07-01_08-30-10.csv')
    #     print("*****")
    #     test('bee_traffic_estimates\\192_168_4_5-2018-07-01_16-30-10.csv')

    if __name__ == "__main__":
        unittest.main()