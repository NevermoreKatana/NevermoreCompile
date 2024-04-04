from functools import lru_cache
import time
import datetime

# @lru_cache
# def fibonachi(x):
#     if x in (1, 2):
#         return 1
#     return fibonachi(x-1) + fibonachi(x-2)

# print(fibonachi(40))



def square_root_recursive(number, guess=1.0, tolerance=0.0001):
    if abs(guess**2 - number) < tolerance:
        return guess
    else:
        new_guess = (guess + number / guess) / 2
        return square_root_recursive(number, new_guess, tolerance)

# Пример использования
number = 120
start_time = time.time()
print("Квадратный корень числа", number, ":", square_root_recursive(number))
print(datetime.timedelta(seconds=(time.time() - start_time)))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(40))
    
    

# def sin(x, n_terms=50):
#     """
#     Вычисляет значение синуса угла 'x' в радианах с использованием 'n_terms' членов ряда Тейлора.
#     """
#     sine = 0
#     for i in range(n_terms):
#         coefficient = (-1) ** i
#         exponent = 2 * i + 1
#         term = coefficient * (x ** exponent) / factorial(exponent)
#         sine += term
#     return sine

# # Пример использования:
# angle_in_radians = 1.2
# sin_value = sin(angle_in_radians)
# print("Синус угла", angle_in_radians, "равен", sin_value)






