# Questão 18
def pitorestico(a, b, c):
    div2 = bool(a%2 == 0 and b%2 == 0 and c%2 == 0)
    div3 = bool(a%3 == 0 and b%3 == 0 and c%3 == 0)
    div5 = bool(a%5 == 0 and b%5 == 0 and c%5 == 0)
    if div2 and div3 and div5:
        print('Pitorestico!!!')
    else:
        print('Nao foi dessa vez')