def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_consecutive_numbers(start):
    numbers = list(range(start, start + 10))  # Генерация 10 последовательных чисел
    primes = [n for n in numbers if is_prime(n)]  # Находим простые числа среди них
    return numbers, primes
#a
start = 1
while True:
    numbers, primes = find_consecutive_numbers(start)
    if len(primes) == 0:
        print("10 последовательных чисел без простых:", numbers)
        break
    start += 1
#b
start = 1
while True:
    numbers, primes = find_consecutive_numbers(start)
    if len(primes) == 1:
        print("10 последовательных чисел с одним простым числом:", numbers)
        break
    start += 1
#c
start = 1
while True:
    numbers, primes = find_consecutive_numbers(start)
    if len(primes) == 2:
        print("10 последовательных чисел с двумя простыми числами:", numbers)
        break
    start += 1
#d
start = 1
while True:
    numbers, primes = find_consecutive_numbers(start)
    if len(primes) == 3:
        print("10 последовательных чисел с тремя простыми числами:", numbers)
        break
    start += 1
#e
start = 1
while True:
    numbers, primes = find_consecutive_numbers(start)
    if len(primes) == 4:
        print("10 последовательных чисел с четырьмя простыми числами:", numbers)
        break
    start += 1
#f
start = 1
while start != 1000:
    numbers, primes = find_consecutive_numbers(start)
    count_primes = len(primes)
    if count_primes <= 10:
        print(f"Количество простых чисел среди {numbers}: {count_primes}")
    start += 1

