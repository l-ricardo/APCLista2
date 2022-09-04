# Questão 08
def formamisteriosa(a, b, c):
    if a == b:
        print('pode ser quadrado')
    else:
        print('pode ser retangulo')
    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c:
            print('pode ser triangulo equilatero')
        elif a != b and a != c:
            print('pode ser triangulo escaleno')
        else:
            print('pode ser triangulo isosceles')