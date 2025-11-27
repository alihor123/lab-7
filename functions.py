class Functions:

    # 1.1 Сортировка (быстрая сортировка)
    @staticmethod #Декоратор, который отключает передачу self и позволяет использовать метод без создания объекта
    def partition(arr, start, end):
        pivot = arr[end]
        p_index = start
        for i in range(start, end):
            if arr[i] <= pivot:
                arr[i], arr[p_index] = arr[p_index], arr[i]
                p_index += 1
        arr[p_index], arr[end] = arr[end], arr[p_index]
        return p_index

    @staticmethod
    def QuickSort(arr, start=None, end=None):
        if arr is None:
            return "Ошибка: входной массив не может быть пустым"
        if type(arr) != list:
            return "Ошибка: вход должен быть списком"
        if start is None or end is None:
            start = 0
            end = len(arr) - 1
        if start >= end or len(arr) == 0:
            return arr
        pivot = Functions.partition(arr, start, end)
        Functions.QuickSort(arr, start, pivot - 1)
        Functions.QuickSort(arr, pivot + 1, end)
        return arr

    # 1.2 Палиндром
    @staticmethod
    def Palindrom(s):
        if s is None:
            return "Ошибка: входная строка не может быть пустой"
        if type(s) != str:
            return "Ошибка: входные данные должны быть строкой"
        return s == s[::-1]

    # 1.3 Факториал
    @staticmethod
    def Factorial(n):
        if type(n) != int:
            return "Ошибка: входное значение должно быть целым числом"
        if n < 0:
            return "Ошибка: число должно быть неотрицательным"
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    # 1.4 Число Фибоначчи
    @staticmethod
    def Fibonacci(n):
        if type(n) != int:
            return "Ошибка: входное значение должно быть целым числом"
        if n < 0:
            return "Ошибка: число должно быть неотрицательным"
        a, b = 0, 1
        for _ in range(n):
            temp = a + b
            a = b
            b = temp
        return a

    # 1.5 Поиск подстроки
    @staticmethod
    def SubstringSearch(s, sub):
        if s is None or sub is None:
            return "Ошибка: входные строки не могут быть пустыми"
        if type(s) != str or type(sub) != str:
            return "Ошибка: входные данные должны быть строками"
        n, m = len(s), len(sub)
        if m == 0:
            return 0  
        for i in range(n - m + 1):
           
            found = True
            for j in range(m):
                if s[i + j] != sub[j]:
                    found = False
                    break
            if found:
                return i
        return -1 
    
    # 1.6 Проверка на простое число
    @staticmethod
    def IsPrime(n):
        if type(n) != int:
            return "Ошибка: входное значение должно быть целым числом"
        if n < 2:
            return False

        a = 1
        k = 0
        limit = int(n**0.5)
        while a <= limit:
            if n % a == 0:
                k += 1
                if a != n // a:
                    k += 1
            a += 1
        return k == 2

    # 1.7 Реверс 32-битного числа
    @staticmethod
    def ReverseInt(x):
        if type(x) != int:
            return "Ошибка: входное значение должно быть целым числом"

        if x < 0: sign = -1  
        else: sign = 1
        x_abs = abs(x)
        reversed_x = 0

        while x_abs > 0:
            digit = x_abs % 10
            reversed_x = reversed_x * 10 + digit
            x_abs //= 10

        reversed_x *= sign

        return reversed_x

    # 1.8 Перевод в римские цифры
    @staticmethod
    def IntToRoman(num):
        if type(num) != int:
            return "Ошибка: входное значение должно быть целым числом"
        if num <= 0 or num > 3999:
            return "Ошибка: число должно быть в диапазоне от 1 до 3999"
        val = [
            1000, 900, 500, 400, 100, 90,
            50, 40, 10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD", "C", "XC",
            "L", "XL", "X", "IX", "V", "IV", "I"
        ]
        roman = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman += syms[i]
                num -= val[i]
            i += 1
        return roman
