def caesar(text, posun):
    abece = "abcdefghijklmnopqrstuvwxyz"
    vysledok = ""
    

    for znak in text:

        if znak in abece:
            index=abece.index(znak)
            novy_index=(index+posun) % 26
            vysledok += abece[novy_index]
        else:
            vysledok+=znak
    return vysledok
print(caesar("abc",7))
#Na dekódovanie použijeme tú istú funkciu len zmenime hodnotu posunu: print(caesar("khoor",-3)
