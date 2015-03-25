"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def length(str):
    count=0
    count=int(count)
    for c in str:
        count+=1
    return count

def filter_long_words(li,n):
    lws=[]
    for i in li:
        if length(i)>n:
            lws.append(i)
    return lws

def Main():
    l=input()
    li=l.split()
    n=int(input())
    print("The words longer than {} are = {}".format(n,filter_long_words(li,n)))

Main()