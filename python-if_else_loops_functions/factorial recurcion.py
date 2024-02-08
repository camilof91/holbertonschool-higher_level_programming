def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('ingrese el numero: '))
if n < 0:
        n = int(input('ingrese el numero mayor a 0: '))
print(f'El factorial de {n} es: {factorial(n)}')
