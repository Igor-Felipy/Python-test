# função que consome recursos desnecessários
"""def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(1, 101):
    for n in range(1, 101):
        print(n, ":", fibonacci(n))
"""

#função otimizada com cache
"""fibonacci_cache = {}

def fibonacci(n):
    #Se tivermos o valor em cache, entao o retornamos
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Calcule o termo de n
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    #cachear o valor e retorna-lo
    fibonacci_cache[n] = value
    return value

num = int(input('Até qual numero da sequencia queres calcular? '))
for n in range(1, num + 1):
    print(n, ":", fibonacci(n))

"""


#Função que consome muito usando LRU_cache para acelerar recursivas
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(1, 500):
    print(n, ":", fibonacci(n))