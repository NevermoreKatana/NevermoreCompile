def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sin(x, n_terms=50):
    """
    Вычисляет значение синуса угла 'x' в радианах с использованием 'n_terms' членов ряда Тейлора.
    """
    sine = 0
    for i in range(n_terms):
        coefficient = (-1) ** i
        exponent = 2 * i + 1
        term = coefficient * (x ** exponent) / factorial(exponent)
        sine += term
    return sine

# Пример использования:
angle_in_radians = 1.2
sin_value = sin(angle_in_radians)
print("Синус угла", angle_in_radians, "равен", sin_value)






