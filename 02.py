"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def max_of_three(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z


def Main():
    x,y,z=input().split()
    x=input(x)
    y=input(y)
    z=input(z)

    print(max_of_three(x,y,z))

Main()