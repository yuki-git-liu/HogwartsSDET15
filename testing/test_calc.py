# coding = utf-8

import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print('开始计算')
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [-1, -1, -2], [0, -1, -1], [33333333, 1232244353, 1265577686]])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.1, 0.2, 0.3], [1.1, 2.4, 3.5], [-123.3, -234.5, -357.8]])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a, b, expect', [[4, 2, 2], [0.1, 0.1, 1], [2.3, 2, 1.15], [-123.3, 4, -30.83]])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a, b', [[2.3, 0], [-123.3, 0], [5, 0]])
    def test_div_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)
