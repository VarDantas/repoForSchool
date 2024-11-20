N = 1000000000
nums = list(range(N + 1))
k = 2

while k < int(N**0.5) + 1:
    if nums[k] != 'x':
        i = k**2
        while i <= N:
            nums[i] = 'x'
            i += k
    k += 1

primes = [p for p in range(2, N + 1) if nums[p] != 'x']

result_p = []

for p in primes:
    if p < 1000000000:
        if (5 * p + 1) <= N and nums[5 * p + 1] != 'x':
            result_p.append(p)

print(result_p)

result_pairs = []

primes_set = set(primes) 

for p in primes:
    if p + 17 in primes_set:
        result_pairs.append((p, p + 17))

print(result_pairs)
