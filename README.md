# TransL - A transliteration and text composition tool for polyglots
This is an old project, so you can compare my code (I haven't touched it since 2011). Also it shows my usage of the GUI Tkinter, unicode features and text manipulation, etc.

[Version Française en bas]

# Background
In 2011, I was passionate about language learning and I had started to learn Russian and Esperanto. For my learning, I wanted to have penpals who were native speakers of the languages I was learning, via the internet. To write them in the target language, especially in Russian, I needed to write in different alphabets. I did not yet have a Russian keyboard (the project "Keyboard-layout-script" then replaces this one). This program had therefore the aime to do transliteration while I typed on the keyboard. A bit like Lexilogos (https://www.lexilogos.com/keyboard/russian.htm) - indeed this was my source of inspiration, but I wanted to make my own version, and for it to work offline (I then lived in a remote area with poor internet connection).

# Usage
The Tkinter library is needed to run this program

In a Linux console, enter:

  $ python3 main.py

The program will initialise the GUI mode, but the console remains with output in the background - which can be used for debugging. 

It also works under Windows with Python 3

# Features
The main text area to enter text. The target language can be chosen above. Special letters can be chosen below. To the right there is a dictionary feature. You can enter a word in any language (of those supported) and it will be translated into the target language. The dictionary, however, is limited (see below).

# Limitations and Bugs

1. The dictionaries are very limited, so there are several words which are not found. Also, it only accepts head words ("have" is accepted, but not "has", "had").
2. There are bugs with uncaught exceptions in the console if we click on "Open" or "Save" and then cancel the process.
3. The code is ugly. I programmed it in 2011 and I have not touched it since. This makes it more difficult to understand and maintain (if ever I want to come back to it).
4. The GUI is oldfashioned - it is Tkinter. But my aime was not to make it beautiful, but useful.
5. It never passed version Alpha - with the console which gives all sorts of debugging messages. And these have no meaning for people who don't know the code.
6. All the files (images, dictionaries) are a little disorganised in the main folder. 


############################################################################################

# Version Française

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
