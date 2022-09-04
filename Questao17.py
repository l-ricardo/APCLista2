# Questão 17
def quantosJantam(n, g, f, c):
    NumGF = min(g, f)
    MaxQueJantam = NumGF + c
    if MaxQueJantam < n:
        print(MaxQueJantam)
    else:
        print(n)