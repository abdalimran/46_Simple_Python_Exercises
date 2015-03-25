"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def translate(s):
    dic={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

    trns=""
    for i in s:
        trns+=dic[i]+' '
    return  trns

def Main():

    s=input()
    ss=s.split()

    print(translate(ss))

Main()