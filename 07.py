"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def reverse(str):

    reversed=""

    for i in range(len(str),0,-1):
        reversed=reversed+str[i-1]

    return  reversed

def Main():

    str=input()

    print(reverse(str))

Main()