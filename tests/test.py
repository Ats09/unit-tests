import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        """Сложение"""
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction_success(self):
        """Вычитание"""
        assert self.calc.subtraction(self, 1, 1) == 0

    def test_division_success(self):
        """Деление"""
        assert self.calc.division(self, 2, 2) == 1

    def test_zero_division(self):
        """Деление на 0"""
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply_success(self):
        """Деление"""
        assert self.calc.multiply(self, 2, 2) == 4

    def teardown(self):
        print('Выполнение метода Teardown')
