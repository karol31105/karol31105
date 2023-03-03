
lista=[]

#from this import d
#from unittest import TextTestResult
from array import array
from turtle import back
#class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#lista

#funkcje
def tab():
    print ( bcolors.WARNING + '+' + '-'*80  +'+' +  bcolors.ENDC )


def wypisz():
 
    tab()
    print ( bcolors.WARNING  + '|'+  bcolors.OKBLUE +  ' '*10 + 'lista zadan' + ' '*(80-10-11) + bcolors.WARNING +'|' +  bcolors.ENDC )
    tab()
    index = 0
    for value in lista:

        n = " nr:" +  str(index +1)  +  "  -> " + str(value)

        print ( bcolors.WARNING  + '|'+  bcolors.OKGREEN +  str(n )   + ' '* (80- len(n)) + bcolors.WARNING +'|' +  bcolors.ENDC )
        tab()
        index += 1
    
 

def dodaj(z):
    lista.append(input("podaj nazwe zadania " + str(z) +": "))
    if z == "karol" :
        u=str(len(lista))
        lista.pop(u-1)
        lista.append("karol Giga kox")
        
    #wypisz()


def usun():
    u = int(input("podaj numer zadania do usuniecia: [1 - " + str(len(lista)) + "] : " )  )
    lista.pop(u-1)
    
     
    
#liczba
liczba= int(input("podaj liczbę zadan: ") )

i=1 

#zadania
while i <= liczba :
    dodaj(i)
    i=i+1
wypisz()

#zmiena (usuwania/dodawania/wypisania)
o=""

while o!= "z"  :
    o = input("napisz : D aby dodac, U aby usnąc, Z aby zakonczyc, W aby wypisac: ")


    if o=="d":
        dodaj( len(lista) + 1 )
        
    if o=="u":
        usun()

    if o=="w":
        wypisz()
#koniec


print ("Bye")
 
