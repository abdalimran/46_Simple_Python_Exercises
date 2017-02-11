def reverse(str):

    reversed=""

    for i in range(len(str),0,-1):
        reversed=reversed+str[i-1]

    return  reversed

def Main():

    str=input()

    print(reverse(str))

if __name__=="__main__":
    Main()
