# Questão 14
def  qtdcopos(n):
    x = n%4
    if x == 0 and n != 0:
        print('Pode levar pros calourinhos, deivis!')
    else:
        print(f'Pode voltar pro ceubinho, deivis! Falta(m) {4 - x} copo(s)!')