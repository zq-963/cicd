"""
计算器单元测试
"""

import pytest
from calculator import Calculator


class TestCalculator:
    """计算器测试类"""

    def setup_method(self):
        """每个测试方法前都会执行"""
        self.calc = Calculator()

    def test_add(self):
        """测试加法"""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        """测试减法"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(-1, -1) == 0
        assert self.calc.subtract(10.5, 5.5) == 5.0

    def test_multiply(self):
        """测试乘法"""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(2.5, 2) == 5.0

    def test_divide(self):
        """测试除法"""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(-10, 2) == -5

    def test_divide_by_zero(self):
        """测试除零异常"""
        with pytest.raises(ValueError, match="除数不能为0"):
            self.calc.divide(10, 0)

    def test_power(self):
        """测试幂运算"""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(10, 0) == 1
        assert self.calc.power(2, -1) == 0.5

    def test_square_root(self):
        """测试平方根"""
        assert self.calc.square_root(4) == 2
        assert self.calc.square_root(9) == 3
        assert self.calc.square_root(0) == 0
        assert abs(self.calc.square_root(2) - 1.414) < 0.001

    def test_square_root_negative(self):
        """测试对负数求平方根的异常"""
        with pytest.raises(ValueError, match="不能对负数求平方根"):
            self.calc.square_root(-1)


class TestCalculatorEdgeCases:
    """边界情况测试"""

    def setup_method(self):
        """每个测试方法前都会执行"""
        self.calc = Calculator()

    def test_large_numbers(self):
        """测试大数运算"""
        assert self.calc.add(1e10, 1e10) == 2e10
        assert self.calc.multiply(1e5, 1e5) == 1e10

    def test_small_numbers(self):
        """测试小数运算"""
        result = self.calc.add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10

    def test_negative_numbers(self):
        """测试负数运算"""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.multiply(-2, -3) == 6
        assert self.calc.divide(-10, -2) == 5
