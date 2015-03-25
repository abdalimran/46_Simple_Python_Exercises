"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def generate_n_chars(n,c):
    s=""
    for i in range(0,n):
        s+=c
    return s


def Main():
    n=int(input())
    c=input()

    print(generate_n_chars(n,c))

Main()