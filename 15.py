"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def length(str):
    count=0
    count=int(count)
    for c in str:
        count+=1
    return count

def find_longest_word(li):
    lwl=-1
    lw=""
    for i in range(0,len(li)):
        if length(li[i])>lwl:
            lwl=length(li[i])
            lw=li[i]
    print("The length of the longest word '{}' is {}".format(lw,lwl))

def Main():
    l=input()
    li=l.split()
    find_longest_word(li)

Main()