"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def sum(arr):
    r=0
    r=int(r)

    for i in arr:
        r=r+int(i)

    return r

def multiply(arr):
    r=1
    r=int(r)

    for i in arr:
        r=r*int(i)

    return r



def Main():

    ar=input()

    arr=ar.split()

    #You can convert arr into a int list by the following methods
    #arri = map(int, arr)
    #arri = [int(i) for i in arr]

    print("Sum of {} is = {} \nAnd Multiplication of {} is = {}".format(arr,sum(arr),arr,multiply(arr)))


Main()