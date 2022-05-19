# Ley de la suma

def f(n):
    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) simplificado crece en O(n) (Crecimiento lineal)  


def f(n):
    for i in range(n):
        print(i)
    
    for i in range(n * n):
        print(i)

# O(n) + O(n * n) = O(n + n**2) simplificado crece en O(n**2) (Crecimiento cuadratico)

#Ley de multiplicación

def f(n):
    for i in range(n): 
        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n * n) = O(n**2) (Crecimiento cuadratico)

#Recursividad Multiple

def fibonacci(n):

    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n-2)

# O(2**n) es 1**n por cada funsion recursiva (Crecimiento exponencial)

