"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def char_freq(s):
    l=str(set(s))
    freq={}
    for ch in s:
        c=s.count(ch)
        freq[ch]=c
    for i in freq:
        print("{}={}".format(i,freq[i]))

def Main():
    s=input("Input a string:")
    char_freq(s)
Main()