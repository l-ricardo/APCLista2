# Questão 15
def maravilhosos(x):
    if x == 1:
        print(x)
    elif x%2 == 0:
        print(x)
        x = int(x/2)
        maravilhosos(x)
    else:
        print(x)
        x = int(3*x + 1)
        maravilhosos(x)
        
num = int(input())
maravilhosos(num)