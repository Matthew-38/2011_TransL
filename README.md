# TransL
Ancien projet pour comparer (je n'ai pas touché le code depuis 2011). Aussi ça démontre l'usage de GUI Tkinter, des fichiers en unicode,  etc.

# Contexte
En 2011, j'étais bien passioné par l'apprentissage des langues et j'avais commencé à apprendre le russe et l'esperanto. Pour mon apprentissage, je voulais tenir des correspondances dans la langue cible avec des personnes de ces pays. Pour ce faire, surtout pour le russe, il me fallait écrire dans un alphabet différent. Je n'avais pas encore une clavier russe en ce moment là (le projet Keyboard-Layout-Script remplace ce projet). Cette programme avait donc but de faire du transliteration, lorsqu'on tappe à la clavier. Un peu comme Lexilogos (https://www.lexilogos.com/keyboard/russian.htm) - en effet, j'ai été bien inspiré par ce site, mais je voulais faire ma propre version et hors ligne.

# Usage

Dans une console Linux, saissez :

  $ python3 main.py
  
La programme initialize dans le mode graphique, mais la console reste avec des informations de debugging. 
Ça marche aussi sous Windows avec Python 3

# Fonctionalités

Fênetre principale pour saisir des textes. Langue cible peut être choisie en haut. Lettres spéciales peuvent être choisis en bas. À droit se trouve une dictionnaire. Vous pouvez saisir un mot dans n'importe laquelle des langues du logiciel et ça le traduit dans la langue cible. 

# Limitations et Bugs
1. Les dictionnaires sont très limités, donc il y a bien des mots qui sont pas trouvés.

2. Il existe des bugs (des Exceptions Pythons dans la console) lorsqu'on clique sur «open» ou «save» et ensuite annule. 

3. Le code est moche - je l'ai programmé en 2011 et je ne l'ai pas touché depuis.

4. L'interface est surannée - c'est du Tkinter. Mon but n'était pas de le rendre jolie, mais fonctionelle.

5. C'est en mode Alpha - avec la console qui donne toute sorte de message de debugging. Ça n'aurait pas de sens pour ceux qui ne connaissent pas le code

6. Tous les fichiers (dictionnaires, images) sont un peu malorganisés. 
