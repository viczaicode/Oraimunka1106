import random

def lista_letrehozasa():
    szamok = []
    # generálj 100 véletlen egész számot -50 és 150 között
    for i in range(0,100,1):
        veletlenszam = int(random.random()*(151+50)-50)
        szamok.append(veletlenszam)
        #print(szamok)
    return szamok

def szoveggealakit(szamok):
    szoveg:str = ""
    for i in range(0, len(szamok),1):
        if (i<len(szamok)-1):
            szoveg+=f"{szamok[i]}; "
        else:
            szoveg+=f"{szamok[i]}; "
    return szoveg


def fajlba_mentes(szoveg):
    fajlom = open("adatok.txt", "w", encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()


def fajlbol_olvas():
    fajlom = open("adatok.txt", "r", encoding='utf-8')
    szoveg_fajlbol:str = fajlom.read()
    szoveg_lista=szoveg_fajlbol.split(";")
    lista=[]
    for i in range(0,len(szoveg_lista),1):
        szam:int=int(szoveg_lista[i].strip())
        lista.append(szam)
    print(szoveg_fajlbol)
    print(lista)
    fajlom.close
    return lista

def hany_negativ(lista):
    szamlalo = 0
    for i in range(0,len(lista),1):
        if lista[i] < 0:
            szamlalo+1
    print(szamlalo)

def legnagyobb_szam(lista):
    max_index = 0
    for i in range(0,len(lista)):
        for i in range(0,len(lista),1):
            if lista[i] > lista[max_index]:
                max_index = i
    print(max_index)

def paros_szamok(lista):
    parosok_lista = []
    for i in range(0, len(lista),1):
        if lista[i] % 2 == 0:
            parosok_lista.append(lista[i])

def ottel_oszthatok(lista):
    ottelosztottosszeg = 0
    for i in range(0,len(lista),1):
        if lista[i] % 5 == 0:
            ottelosztottosszeg += lista[i]

def legkisebbSzam(lista):
    sorszam = 0
    for i in range(0,len(lista)):
        for i in range(0,len(lista),1):
            if lista[i] < lista[sorszam]:
                sorszam = i


