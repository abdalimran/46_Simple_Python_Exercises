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

if __name__=="__main__":
    Main()
