"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def length(str):
    count=0
    count=int(count)
    for c in str:
        count+=1
    return count

def mapping(li):
    for i in range(0,len(li)):
        print("{}={}".format(li[i],length(li[i])))

def Main():
    l=input()
    li=l.split()
    mapping(li)

Main()