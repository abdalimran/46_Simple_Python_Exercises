def is_member(x,a):
    mem=False
    for i in range(0,len(a)):
        if a[i]==x:
            mem=True
        else:
            mem=False

    return mem

def Main():
    a=input()
    x=input()
    al=a.split()

    if(is_member(x,al)):
        print("{} is a member of {}".format(x,al))
    else:
        print("{} is not a member of {}".format(x,al))

if __name__=="__main__":
    Main()
