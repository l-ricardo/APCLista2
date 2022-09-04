# Questão 09
def classificador(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('triangulo ')
        if a == b and a == c:
            print('isosceles')
            print('equilatero')
        elif a != b and a != c:
            print('escaleno')
        else:
            print('isosceles')
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
            print('retangulo')
    else:
        print('gondim sendo gondim')