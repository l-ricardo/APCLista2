# Questão 12
def jogadas(a, b):
    import math
    if a > b:
        min = (a - b)/10
    else:
        min = (b - a)/10
    print(math.ceil(min))