'''Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.'''


def is_prime(func):
    def wraper (a, b, c):
        x = a + b + c
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                return False
        return True
    return wraper


@is_prime
def sum_three (a, b, c):
    sum = a + b + c
    return sum

print(sum_three(1,1,1))


