def overlapping(l1,l2):
    ovrl=False
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if l1[i]==l2[j]:
                ovrl=True
            else:
                ovrl=False

    return ovrl

def Main():
    a=input()
    l1=a.split()
    b=input()
    l2=b.split()

    if overlapping(l1,l2):
        print("The list has overlapping member!")
    else:
        print("The list has no overlapping member!")

if __name__=="__main__":
    Main()
