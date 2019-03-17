# from const import const
# from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot, make_e_expr, make_ln, make_absv
# from tof import tof
# from riemann import riemann_approx, riemann_approx_with_gt, plot_riemann_error
# from deriv import deriv
# from antideriv import antideriv, antiderivdef
# from defintegralapprox import midpoint_rule, trapezoidal_rule, simpson_rule
from hw09_s19 import display_csv_file, read_csv_file
import unittest
import math

class Assign01UnitTests(unittest.TestCase):

    # def test_01(self):
    #     print("****Unit Test 01********")
    #     display_csv_file('bee_traffic_estimates\\192_168_4_5-2018-07-01_08-00-10.csv')
    #     print("Unit Test 01: pass")

    def test_02(self):
        print("****Unit Test 02********")
        fd = read_csv_file('bee_traffic_estimates\\192_168_4_5-2018-07-01_08-00-10.csv')
        print(fd[5])
        print(fd[28])
        print("Unit Test 02: pass")

    if __name__ == "__main__":
        unittest.main()