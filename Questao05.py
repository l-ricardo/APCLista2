# Questão 5
def dinheiros(n, a, b):
    if a > b/2:
        conta = (n//2)*b + (n%2)*a
    else:
        conta = n*a
    print(conta)