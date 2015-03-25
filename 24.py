"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def make_3sg_form(v):
    if v.endswith('y'):
        v+='ies'
    elif v.endswith(('o','ch','s','sh','x','z')):
        v+='es'
    else:
        v+='s'
    return v

def Main():
    s=input("Enter verb:")
    print(make_3sg_form(s))

Main()