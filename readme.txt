Il s'agit d'un jeu de labyrinthe dans le cadre du cours PYTHON Openclassroom

Le programme se décompose en plusieurs fichiers :
- roboc.py : Le programme principal
- plateau.py : Le module python qui contient la classe Plateau
- partie.py : Le module python qui contient la classe Partie
- carte.py : Le module python qui contient la classe Carte
- gestion.py : qui contient quelques fontions complémentaires

le jeu principal est un plateau qui contient un ensemble de carte et une partie
une Partie est composée d'une grille de jeu, d'un nombre de coups joués, de la taille de la grille, de la position du robot, etc.

Le robot est contrôlable grâce à des commandes entrées au clavier. Il existe les commandes suivantes :

Q qui permet de sauvegarder et quitter la partie en cours ;
N qui demande au robot de se déplacer vers le nord (c'est-à-dire le haut de votre écran) ;
E qui demande au robot de se déplacer vers l'est (c'est-à-dire la droite de votre écran) ;
S qui demande au robot de se déplacer vers le sud (c'est-à-dire le bas de votre écran) ;
O qui demande au robot de se déplacer vers l'ouest (c'est-à-dire la gauche de votre écran) ;
Chacune des directions ci-dessus suivies d'un nombre permet d'avancer de plusieurs cases (par exemple E3 pour avancer de trois cases vers l'est).

Les symboles utilisés sont O pour un mur, . pour une porte (sur laquelle le robot peut passer), U pour la sortie et X pour le robot lui-même ;
Dans le code, le robot est représenté par :
- un X quand il est sur un élément vide (case vide)
- un x quand il est sur une porte (case avec un ".")

La partie s'achèvent quand le robot atteint le U. Le symbole $ est alors affiché.

Il est possible de créer des cartes.