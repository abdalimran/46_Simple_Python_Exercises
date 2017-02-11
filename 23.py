import re

def correct(s):
    #Removing extra spaces
    #cs=' '.join(s.split())
    cs = re.sub(' +',' ',s)
    #Putting extra space after period
    cs = re.sub('\.','. ',cs)

    return cs

def Main():
    #s=input("Enter string:")
    s = "This   is  very funny  and    cool.Indeed!. But      you should.try  this also"
    print(correct(s))

if __name__=="__main__":
    Main()
