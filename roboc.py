# -*-coding:Utf-8 -*

# Ce fichier contient le code principal du jeu de labythinthe
# Exécutez-le avec Python pour lancer le jeu.
# Pour bien faire, il faudrait sauvegarder les points de vies

import os
from carte import Carte
from partie import Partie
from plateau import Plateau
from gestion import saisieLigneOK,formatLigneOK,choixValide,nbCoupsJoue,sensJoue,saisieNombre

# Création du plateau de jeu
lePlateau=Plateau([],Partie(""))
lePlateau.chargerPlateau()
print("Plateau créé")

# Boucle sur le menu principal
sortieJeu=False
while sortieJeu==False :
    print("Menu du jeu : ")
    print("J - Jouer une partie")
    print("V - Voir les cartes existantes")
    print("E - Editer les cartes")
    print("R - Supprimer la sauvegarde du jeu")
    print("Q - Quitter leu jeu")
    choixMenuPrincipal = input("Entrez votre choix : ")

    if choixMenuPrincipal=="J" or choixMenuPrincipal=="V" or choixMenuPrincipal=="E" or choixMenuPrincipal=="Q" or choixMenuPrincipal=="R" :

        # Choix du menu : J - Jouer
        if choixMenuPrincipal=="J" :
            choixCarte=-1
            # On restaure la dernière sauvegarde ou en l'absence on demande avec quelle carte on souhaite jouer
            if lePlateau.partie.chargerSauvegarde()==False :
                print("Il n'y a pas de sauvegarde en cours")
                lePlateau.listerCartes()
                choixUtilisateurValide=False

                while choixUtilisateurValide==False :
                    choixCarte=saisieNombre("Quel numero de carte souhaitez vous afficher ? ( 0 pour revenir au menu précédent)")

                    if choixCarte >0 and choixCarte<=lePlateau.nombreDeCartes() :
                        print("Vous souhaitez jouer avec la carte " + lePlateau.cartes[choixCarte-1].nom)
                        choixUtilisateurValide=True
                        # On initialise la partie avec la grille correspondante à la carte choisie
                        lePlateau.partie.grille=lePlateau.cartes[int(choixCarte)-1].labyrinthe
                    else :
                        if choixCarte==0 :
                            # On revient au menu précédent
                            choixUtilisateurValide=True
                        else :
                            print("Le numéro ne correspond pas à un numéro de carte existant")
            else :
                print("Récupération de la sauvegarde précédente effectuée")

            # La partie est chargée soit avec la dernière sauvegarde, soit avec une carte. On peut commencer à jouer
            if choixCarte!=0 :
                print("Le jeu peut commencer")

                lePlateau.partie.initialiserPositionRobot()
                lePlateau.partie.initialiserTailleMaxGrille()
                lePlateau.partie.afficherPartie()

                finPartie=False
                while finPartie==False :
                    choix=input("Quelle direction ou Q pour quitter")
                    if choix == "Q" :
                        print("Fin de la partie (sauvegarde effectuée)")
                        lePlateau.sauvegarderPartie()
                        finPartie=True
                    else :
                        retour=choixValide(choix)
                        if retour == True :
                            nbCoups=nbCoupsJoue(choix)
                            sens=sensJoue(choix)
                            # On repete autant de "jouerUnCoup" qu'il y a de coups à jouer (en fonction du choix)
                            for i in range(0,int(nbCoups)) :
                                lePlateau.jouerUnCoup(sens)
                            lePlateau.partie.nbCoups=lePlateau.partie.nbCoups+1
                            lePlateau.partie.afficherPartie()
                            print("Vous avez utilisé " + str(lePlateau.partie.nbCoups) + " coup(s) et vous avez " + str(lePlateau.partie.pointDeVie) + " points de vie")
                            finPartie=lePlateau.partie.gagne
                            lePlateau.sauvegarderPartie()
                        else :
                            print("La direction " + choix + " n'a pas un format valide")
                if lePlateau.partie.gagne :
                    print("Gagné !!!!!!! Il vous reste : " + str(lePlateau.partie.pointDeVie) + " points de vie")
                    # On peut supprimer la sauvegarde si il y en a une
                    lePlateau.supprimerSauvegarde()
                    lePlateau.reinitialiserPartie()

        # Choix du menu : V - Visualiser les cartes disponibles
        if choixMenuPrincipal=="V" :
            finVoir=False
            while finVoir==False :
                lePlateau.listerCartes()
                valeur=saisieNombre("Quel numero de carte souhaitez vous afficher ? ( 0 pour revenir au menu précédent)")

                if int(valeur) >0 and int(valeur)<=lePlateau.nombreDeCartes() :
                    print("Voici la carte : " + str(lePlateau.cartes[int(valeur)-1].nom))
                    lePlateau.cartes[int(valeur)-1].afficherCarte()
                else :
                    if int(valeur) == 0 :
                        finVoir=True
                    else :
                        print("Le numéro ne correspond pas à un numéro de carte existant")

        # Choix du menu : E - Editer les cartes
        if choixMenuPrincipal=="E" :
            lePlateau.chargerPlateau()
            finEditionMenu=False
            while finEditionMenu==False :
                lePlateau.chargerPlateau()
                finMenuEdition=False
                while finMenuEdition==False :
                    print("1 - Création d'une nouvelle carte")
                    print("2 - Edition / modification d'une carte existante")
                    print("0 - Supprimer une carte")
                    print("X - Revenir au menu principal")
                    choixEdition = input("Entrez votre choix : ")
                    if choixEdition=="1" or choixEdition=="2" or choixEdition=="0" or choixEdition=="X" :
                        finMenuEdition=True

                        # Choix creation d'une carte
                        if choixEdition=="1" :
                            finMenuCreation=False
                            nouvelleCarte=""
                            while finMenuCreation==False :
                                nomNouvelleCarte=input("Nom de la carte que vous souhaitez créer ? (vide pour revenir au menu précédent)")
                                if nomNouvelleCarte=="" :
                                    finMenuCreation=True
                                else :
                                    # On regarde si le fichier existe déjà
                                    if lePlateau.nomCarteExiste(nomNouvelleCarte)==True :
                                        print("Cette carte existe déjà")
                                    else :
                                        finMenuCreation=True
                                        largeurNouveau= saisieNombre("Nombre de colonnes : ")
                                        hauteurNouveau= saisieNombre("Nombre de lignes : ")
                                        print("On va créer une nouvelle de carte de " + str(largeurNouveau) + " de large et de " + str(hauteurNouveau) + " de haut")
                                        controleNb=0
                                        while controleNb != int(hauteurNouveau) :
                                            nouvelleLigne=input("Entrez une ligne de la carte (avec X, . et 0 en caractères) d'une longueur de " + str(largeurNouveau) + " caractere(s)")
                                            if saisieLigneOK(largeurNouveau,nouvelleLigne) == True :
                                                controleNb=controleNb+1
                                                nouvelleCarte=nouvelleCarte + nouvelleLigne + "\n"
                                            else :
                                                print("Ligne incorrecte : " + nouvelleLigne)
                                        finEdition=True

                                        # On peut à présent créer la carte
                                        map=nouvelleCarte.split("\n")
                                        lePlateau.creerCarte(nomNouvelleCarte,map)
                            lePlateau.chargerPlateau()

                        # Choix Modification  d'une carte
                        if choixEdition=="2" :
                            finEditionMenu=False
                            while finEditionMenu==False :
                                lePlateau.listerCartes()
                                valeur=saisieNombre("Quel numero de carte souhaitez vous éditer ? (0 pour revenir au menu précédent)")
                                if int(valeur) == 0 :
                                    finEditionMenu=True
                                else :
                                    if int(valeur) >0 and int(valeur)<=lePlateau.nombreDeCartes() :
                                        lePlateau.cartes[int(valeur)-1].editerCarte()
                                        finEditionMenu=True
                                        # On met à jour la liste des cartes
                                        lePlateau.chargerPlateau()
                                    else :
                                        print("Le numéro ne correspond pas à un numéro de carte existant")

                        # Choix suppression d'une carte
                        if choixEdition=="0" :
                            finSuppressionMenu=False
                            while finSuppressionMenu==False :
                                lePlateau.listerCartes()
                                valeur=saisieNombre("Quel numero de carte souhaitez vous supprimer ? (0 pour annuler et revenir au menu précédent)")
                                if int(valeur) == 0 :
                                    finSuppressionMenu=True
                                else :
                                    if int(valeur) >0 and int(valeur)<=lePlateau.nombreDeCartes() :
                                        lePlateau.cartes[int(valeur)-1].supprimerCarte()
                                        finSuppressionMenu=True
                                        # On met à jour la liste des cartes
                                        lePlateau.chargerPlateau()
                                    else :
                                        print("Le numéro ne correspond pas à un numéro de carte existant")

                        if choixEdition=="X" :
                            finEdition=True
                            finMenuEdition=True
                            finEditionMenu=True
                    else :
                        print("Vous n'avez pas fait un choix autorisé")

        # Choix du menu : R - Pour remettre à 0 une sauvegarde (suppression)
        if choixMenuPrincipal=="R" :
            if lePlateau.partie.chargerSauvegarde()==False :
                print("Il n'y a pas de sauvegarde en cours")
            else :
                retour=input("Etes-vous sûr de vouloir supprimer la sauvegarde en cours ? (Répondre OUI pour confirmer)")
                if retour=="OUI" :
                    lePlateau.supprimerSauvegarde()
                else :
                    print("Abandon de la suppression de la sauvegarde")

        # Choix du menu : Q - Quitter le jeu
        if choixMenuPrincipal=="Q" :
            print("Merci, à bientôt")
            sortieJeu=True
    else :
        print("Vous n'avez pas fait un choix autorisé")
