"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def is_palindrome(str):
    j = len(str)
    pal=False
    for i in range(len(str)//2):
        if str[i]==str[j-1]:
            pal=True
        else:
            pal=False
            break
        j-=1

    return pal

def Main():

    str=input()

    if is_palindrome(str):
        print("{} is a Plindrome!".format(str))
    else:
        print("{} is not a Plindrome!".format(str))

Main()