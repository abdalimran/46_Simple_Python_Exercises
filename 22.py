"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def encoder(s):
    encoded=""

    for ch in s:
        if ch in key:
            encoded+=key[ch]
        else:
            encoded+=ch
    return encoded

def decoder(s):
    decoded=""

    for ch in s:
        if ch in key:
            decoded+=key[ch]
        else:
            decoded+=ch
    return decoded

def Main():
    n=int(input("What do you want to do?? Enter 1 for encoding, 2 for decoding:"))
    s=input("Enter string for Encoding/Decoding:")
    if n==1:
        print("The Encoded message is = {}".format(encoder(s)))
    elif n==2:
        print("The Dencoded message is = {}".format(decoder(s)))

Main()