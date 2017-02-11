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

if __name__=="__main__":
    Main()
