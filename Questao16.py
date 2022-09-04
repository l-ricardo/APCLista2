# Questão 16
def piscininha(x, y, w, h, a, b):
    if x < a and a < x + w and y < b and b < y + h:
        print('Dando um tchibum')
    elif x > a or a > x + w or y > b or b > y + h:
        print('Tomando um solzin')
    else:
        print('So com os pezin dentro da agua')