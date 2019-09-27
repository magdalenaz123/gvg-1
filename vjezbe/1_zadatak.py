
#ZADATCI(riješite, dokumentirajte I zatim pročitajte docstring): 
#Kreirajte funkciju koja računa zbroj svih znamenaka nekog cijelog broja
def zbroj_znamenki(a):
    '''funkcija koja računa broj znamenaka cijelog broja'''
    L=list(str(a))
    b=0
    for i in L:
        b+=int(i)
    return b
x=int(input('Upiši cijeli broj:'))
print(zbroj_znamenki(x))