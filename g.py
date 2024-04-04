def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sin_degrees(angle_degrees):
    angle_radians = angle_degrees * (3.14159265358979323846 / 180.0)  # Перевод градусов в радианы
    sin_value = 0
    for n in range(10): 
        sign = (-1) ** n
        term = (angle_radians ** (2 * n + 1)) / factorial(2 * n + 1)

        sin_value += sign * term
    return sin_value

# Пример использования
angle_degrees = 250000
print("Синус {} градусов: {:.6f}".format(angle_degrees, sin_degrees(angle_degrees)))
