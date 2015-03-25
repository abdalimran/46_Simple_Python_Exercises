"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def max_in_list(li):
    max=-99999999
    max=int(max)
    for i in range(0,len(li)):
        if li[i]>max:
            max=li[i]
        else:
            max=max
    return max

def Main():
    l=input()
    ls=l.split()
    li=[int(i) for i in ls]

    print(max_in_list(li))

Main()