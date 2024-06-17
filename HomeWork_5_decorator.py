'''�������� 2 �������:
�������, ������� ���������� 3 ����� (sum_three)
������� ��������� (is_prime), ������� ������������� "�������", ���� ��������� 1�� ������� ����� ������� ������ � "���������" � ��������� ������.'''


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


