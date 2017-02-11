def histogram(li):
    hist=""
    for i in range(len(li)):
        for j in range(0,li[i]):
            hist+="*"
        hist+="\n"

    return hist

def Main():
    l=input()
    ls=l.split()
    li=[int(i) for i in ls]

    print(histogram(li))

if __name__=="__main__":
    Main()
