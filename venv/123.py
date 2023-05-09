'''
Задание 1.
Базовые математические операции, приоритеты выполнения, условные операторы, циклы.
'''

from typing import Tuple



# Реализовать функции сложения, вычитания и умножения двух чисел.
def add_mul(first: float, second: float) -> Tuple[float, float, float]:
    return first + second, first - second, first * second,

res = add_mul(4.5, 4.5)
print(res)


# Реализовать функции деления, деления нацело и нахождения остатка от деления.
def div_int_rem(first: float, second: float) -> Tuple[float, float, float]:
    return first / second, first // second, first % second

res = div_int_rem(10.5, 10.8)
print(res)


# Обменять два целочисленных значение с помощью битового xor не используя промежуточноые переменные.
def xor_swap(first: int, second: int) -> int:
    return first ^ second

res = xor_swap(5, 4)
print(res)


# Вернуть наименьшее число, используя условный оператор.
def min_conditional(first: float, second: float) -> float:
    if first > second:
        print(second)
    else:
        print(first)
    return res


res = min_conditional(15.5, 6.3)


# Реализовать функции умножения на 2, 8 и 32 с помощью битовых операций сдвига.
def mul_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value << 1, value << 3, value << 5

r = mul_shift_2_8_32(10)
print(r)


# Реализовать функции деления на 2, 8 и 32 с помощью битовых операций сдвига.
def div_shift_2_8_32(value: int) -> Tuple[int, int, int]:
    return value >> 1, value >> 3, value >> 5
r = div_shift_2_8_32(320)
print(r)


# Реализовать операцию возведения в степень остатка от деления.
def exponentiation(divident: float, divider: float, power: float) -> float:
    return (divident % divider) ** power
r = exponentiation(16,7,2)
print(r)


# Определить знак 32-битного числа с помощью операции &.
def sign(value: int) -> int:
    if value > -2147483648 & value < 2147483647 and value > 0:
        print('положительное')
    else:
        print('отрицательное')
    return value

r = sign(int(input()))

# Умножить целочисленное значение на -1 с помощью битовых операций и сложения.
def change_sign(value: int) -> int:
    x = value << 1
    z = ~x + 1
    print(z)
    return z
r = change_sign(int(input()))

# Возвратить True, если хотя бы один четный бит 32-х битного числа установлен в 1.
def check_32_even_bit_set(value: int) -> bool:
    return ...


# Посчитать количество бит в 32-х битном числе, установленных в ноль.
def calculate_32_zero_bits(value: int) -> int:
    return ...


# Упаковать два целочисленных значения в 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def pack_4_4(first: int, second: int) -> int:
    return ...


# Распоковать два целочисленных значения из 8 бит.
# Первое число должно располагаться в 4 младших битах, второе число в - 4 старших.
def unpack_4_4(value: int) -> Tuple[int, int]:
    return ...


# Ограничить число заданным интервалом. Нижняя граница заданного интервала меньше либо равна верхней.
import numpy as np

def clamp(value: float, low: float, high: float) -> float:
    
    if low <= high and value >= low:
        for i in np.arange(low, high, value):
            print(i)
        return i
    elif value < low:
        print('Число меньше границы заданного интервала')        
    else:
        print('Нижняя граница заданного интервала меньше либо равна верхней')        
         
r = clamp(float(input()), float(input()), float(input())) 


# Ограничить число заданным интервалом. Нижняя граница может быть как меньше, так и больше верхней.
def clamp_any(value: float, low: float, high: float) -> float:
    
    if value >= low:
        for i in np.arange(low, high, value):
            print(i)
        return i
    else:
        print('Число меньше границы заданного интервала')
        
r = clamp_any(float(input()), float(input()), float(input()))


# Вернуть True, если число нечетно и входит в интервал от -10 до 10.
def event_and_match_interval_m10_10(value: int) -> bool:
    if value % 2 != 0 and value >= -10 and value <= 10:
        print(True)
    else:
        print('Четное или не входит')
        
    return True

r = event_and_match_interval_m10_10(int(input()))

# Определить порядок выолнения операций и расстваить скобки таким образом, чтобы он стал обратным.
def reverse_operations(value: float):
    return value ** (4 * (0.5 + 0.25))

r = reverse_operations(float(input()))
print(r)


# Установить n-ый бит числа в единицу.
def set_nth_bit(value: int, n: int) -> int:
    return value | (1<<n)

r= set_nth_bit(int(input()), int(input()))
print(r)

# Переключить n-ый бит числа.
def switch_nth_bit(value: int, n: int) -> int:
     return value ^ (1<<n)
 
r = switch_nth_bit(int(input()), int(input()))
print(r)

# Расставить скобки таким образом, чтобы выражение в задаче было возведено в степень 3.
def change_priorities(x: float) -> float:
    return (x + 3) ** 3
r = change_priorities(3)
print(r)


'''
Задачи повышенной сложности.
'''


# Ковертировать целое число в формат float32.
# Для того, чтобы разобраться с форматом, можно использовать следующие источники:
# https://goo.su/ipKzbY
# https://learn.microsoft.com/ru-ru/cpp/build/ieee-floating-point-representation?view=msvc-170
# https://habr.com/ru/post/337260/
# Для решения этой задачи нужно также выяснить, как конвертировать байты в целые и дробные числа.
def int_to_float(value: int) -> float:
    return ...


# Вернуть наименьшее целое число без использования условных операторов и встроенных функций.
def min_raw(first: int, last: int) -> int:
    
    m = (first > last) * last + (last > first) * first
    print(m)
    return m
r = min_raw(int(input()), int(input()))
