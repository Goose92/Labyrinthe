# -*-coding:Utf-8 -*

import os

def saisieLigneOK(nb,chaine):
    if len(chaine) == int(nb) :
        if formatLigneOK(chaine) :
            return True
        else :
            print("format de la chaine incorrect")
            return False
    else :
        print("Longueur de la chaine incorrecte")
        return False

def formatLigneOK(chaine) :
    for lettre in chaine:
        if not(lettre =="X" or lettre =="O" or lettre =="." or lettre ==" " or lettre =="U") :
            return False
    return True

def choixValide(direction) :
    if len(direction)==0 :
        return False
    else :
        if direction[0]=="N" or direction[0]=="S" or direction[0]=="E" or direction[0]=="O" :
            nbCoupsDirection=direction[1:]
            if len(direction)==1 :
                nbCoupsDirection=1
            else :
                try :
                    int(nbCoupsDirection)
                except ValueError:
                    print("Lorsque vous souhaitez des coups multiples, il faut saisir une valeur numérique après la direction")
                    return False
            return True
        else :
            return False
    return False

def nbCoupsJoue(direction) :
    if len(direction)==1 :
        return 1
    else :
        return int(direction[1:])

def sensJoue(direction) :
    return(direction[0])

def supprimerFichierCarte(nom) :
    if os.path.exists(nom) == True :
           os.remove(nom)

def saisieNombre(question ) :
    fin=False
    while fin==False :
        nombre=input(question)
        try :
            int(nombre)
            fin=True
            return int(nombre)
        except ValueError:
            print("Il faut saisir une valeur numerique entière")

