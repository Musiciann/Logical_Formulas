from unittest import TestCase
from Source import Logical_Formulas


class Test(TestCase):
    def test_binary_to_decimal_direct_code(self):
        binary_num, decimal_num = Logical_Formulas.binary_to_decimal_direct_code('00000010')
        assert binary_num == '00000010'
        assert decimal_num == 2

    def test_parse_expression(self):
        variables, operations = Logical_Formulas.parse_expression('a&b')
        assert variables == ['a', 'b']
        assert operations == ['&']

    def test_evaluate_formula(self):
        result = Logical_Formulas.evaluate_formula('a&b', {'a':1, 'b':0})
        assert result == 0

    def test_truth_table(self):
        variables, expr_result, combinations = Logical_Formulas.truth_table('a&b')
        assert variables == ['a', 'b']
        assert expr_result == [({'a': 0, 'b': 0}, 0), ({'a': 0, 'b': 1}, 0), ({'a': 1, 'b': 0}, 0), ({'a': 1, 'b': 1}, 1)]
        assert combinations == [(0, 0), (0, 1), (1, 0), (1, 1)]

    def test_generate_sdnf(self):
        variables = ['a', 'b']
        expr_result = [({'a': 0, 'b': 0}, 0), ({'a': 0, 'b': 1}, 0), ({'a': 1, 'b': 0}, 0), ({'a': 1, 'b': 1}, 1)]
        sdnf = Logical_Formulas.generate_sdnf(variables, expr_result)
        assert sdnf == '(a & b)'

    def test_generate_sknf(self):
        variables = ['a', 'b']
        expr_result = [({'a': 0, 'b': 0}, 0), ({'a': 0, 'b': 1}, 0), ({'a': 1, 'b': 0}, 0), ({'a': 1, 'b': 1}, 1)]
        sknf = Logical_Formulas.generate_sknf(variables, expr_result)
        assert sknf == '(a | b) & (a | ~b) & (~a | b)'

    def test_generate_sdnf_numeric(self):
        expr_result = [({'a': 0, 'b': 0}, 0), ({'a': 0, 'b': 1}, 0), ({'a': 1, 'b': 0}, 0), ({'a': 1, 'b': 1}, 1)]
        combinations = [(0, 0), (0, 1), (1, 0), (1, 1)]
        sdnf_numeric = Logical_Formulas.generate_sdnf_numeric(expr_result, combinations)
        assert sdnf_numeric == [3]

    def test_generate_sknf_numeric(self):
        expr_result = [({'a': 0, 'b': 0}, 0), ({'a': 0, 'b': 1}, 0), ({'a': 1, 'b': 0}, 0), ({'a': 1, 'b': 1}, 1)]
        combinations = [(0, 0), (0, 1), (1, 0), (1, 1)]
        sknf_numeric = Logical_Formulas.generate_sknf_numeric(expr_result, combinations)
        assert sknf_numeric == [0, 1, 2]

    def test_binary_result_decimal(self):
        decimal_result = Logical_Formulas.binary_result_decimal((0, 0, 0, 1))
        assert decimal_result == 1