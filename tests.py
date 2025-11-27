import unittest
from functions import Functions

class TestFunctions(unittest.TestCase):
    def test_QuickSort(self):
        self.assertEqual(Functions.QuickSort([3,1,4,1,5]), [1,1,3,4,5])
        self.assertEqual(Functions.QuickSort([]), [])
        self.assertEqual(Functions.QuickSort(None), "Ошибка: входной массив не может быть пустым")
        self.assertEqual(Functions.QuickSort("list"), "Ошибка: вход должен быть списком")

    def test_Palindrom(self):
        self.assertTrue(Functions.Palindrom("racecar"))
        self.assertFalse(Functions.Palindrom("hello"))
        self.assertTrue(Functions.Palindrom(""))
        self.assertEqual(Functions.Palindrom(None), "Ошибка: входная строка не может быть пустой")

    def test_Factorial(self):
        self.assertEqual(Functions.Factorial(5), 120)
        self.assertEqual(Functions.Factorial(0), 1)
        self.assertEqual(Functions.Factorial(-1), "Ошибка: число должно быть неотрицательным")
        self.assertEqual(Functions.Factorial(3.5), "Ошибка: входное значение должно быть целым числом")

    def test_Fibonacci(self):
        self.assertEqual(Functions.Fibonacci(7), 13)
        self.assertEqual(Functions.Fibonacci(0), 0)
        self.assertEqual(Functions.Fibonacci(-2), "Ошибка: число должно быть неотрицательным")
        self.assertEqual(Functions.Fibonacci("10"), "Ошибка: входное значение должно быть целым числом")

    def test_SubstringSearch(self):
        self.assertEqual(Functions.SubstringSearch("hello world", "world"), 6)
        self.assertEqual(Functions.SubstringSearch("hello world", "bye"), -1)
        self.assertEqual(Functions.SubstringSearch("hello", ""), 0)
        self.assertEqual(Functions.SubstringSearch(None, "test"), "Ошибка: входные строки не могут быть пустыми")

    def test_IsPrime(self):
        self.assertTrue(Functions.IsPrime(17))
        self.assertFalse(Functions.IsPrime(1))
        self.assertFalse(Functions.IsPrime(0))
        self.assertEqual(Functions.IsPrime("11"), "Ошибка: входное значение должно быть целым числом")

    def test_ReverseInt(self):
        self.assertEqual(Functions.ReverseInt(123), 321)
        self.assertEqual(Functions.ReverseInt(-456), -654)
        self.assertEqual(Functions.ReverseInt(0), 0)
        self.assertEqual(Functions.ReverseInt(12.5), "Ошибка: входное значение должно быть целым числом")

    def test_IntToRoman(self):
        self.assertEqual(Functions.IntToRoman(1994), "MCMXCIV")
        self.assertEqual(Functions.IntToRoman(44), "XLIV")
        self.assertEqual(Functions.IntToRoman(0), "Ошибка: число должно быть в диапазоне от 1 до 3999")
        self.assertEqual(Functions.IntToRoman("100"), "Ошибка: входное значение должно быть целым числом")
unittest.main()