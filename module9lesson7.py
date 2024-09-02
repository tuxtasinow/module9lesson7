def is_prime(func):
    def wrapper(*args):
        total = func(*args)
        if total <= 1:
            return f'Сумма: {total} - Не является ни простым, ни составным'
        for i in range(2, total):
            if total % i == 0:
                return f'Сумма: {total} - Составное'
        return f'Сумма: {total} - Простое'
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)