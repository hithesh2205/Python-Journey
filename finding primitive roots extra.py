def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_primitive_root(g, n, phi_n):
    powers = set()
    for k in range(1, phi_n + 1):
        powers.add(pow(g, k, n))
    return len(powers) == phi_n

def find_primitive_roots(n):
    phi_n = euler_totient(n)
    primitive_roots = []
    for g in range(1, n):
        if gcd(g, n) == 1 and is_primitive_root(g, n, phi_n):
            primitive_roots.append(g)
    return primitive_roots

# Example: Find primitive roots of 7
n = 13
print(find_primitive_roots(n))
