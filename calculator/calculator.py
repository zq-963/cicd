"""
计算器类实现
提供基本的数学运算功能
"""


class Calculator:
    """简单计算器类，提供基本数学运算"""

    def add(self, a: float, b: float) -> float:
        """
        加法运算

        Args:
            a: 第一个数
            b: 第二个数

        Returns:
            两数之和
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        减法运算

        Args:
            a: 被减数
            b: 减数

        Returns:
            差值
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        乘法运算

        Args:
            a: 第一个因数
            b: 第二个因数

        Returns:
            乘积
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        除法运算

        Args:
            a: 被除数
            b: 除数

        Returns:
            商

        Raises:
            ValueError: 当除数为0时
        """
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """
        幂运算

        Args:
            base: 底数
            exponent: 指数

        Returns:
            幂运算结果
        """
        return base**exponent

    def square_root(self, n: float) -> float:
        """
        平方根运算

        Args:
            n: 待求平方根的数

        Returns:
            平方根

        Raises:
            ValueError: 当输入为负数时
        """
        if n < 0:
            raise ValueError("不能对负数求平方根")
        return n**0.5


# 测试tag
