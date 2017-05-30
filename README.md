### Maillage

Projet Maillage
Polytech Paris-UPMC

Année 2016-2017

### Auteur: Lancelot Satge, Suzanne Sleiman, Ren Geng
Encadrant: Chiara Nardoni

Ce projet propose 2 sortes de déformation: MLS et barycentrique

### Usage

Avant d'utiliser une déformation, assurez-vous d'avoir une version 2 et 3 de Python (les versions qu'on a utilisé sont Python 2.7.6 et Python 3.4.3) et d'avoir installé le module pygame. De plus assurez vous que l'éxecutable medit-linux(si vous utilisez linux) ou medit(si vous utilisez un mac) et dans votre variable d'environnement PATH.
/!\ Si vous utiliez un mac, changez la ligne 148 du fichier Execution_Barycentre.py et la ligne 161 du fichier par os.system("medit ../mesh/mesh_2D/"+nom_fichier+".mesh &")

Pour utiliser la déformation MLS, allez dans le dossier code/Programmes/, lancez le fichier MLS.py avec python2, ensuite tapez le nom d'un des fichier mesh se trouvant dans le dossier code/mesh/mesh_2D sans l'extension (par exemple juste man pour le fichier man.mesh).
Un fenêtre pygame s'ouvre, puis sélectionnez un point du dessin	avec le clique gauche et l'endroit où vous voulez que le point arrive.
Répétez ce procédée autant de fois que vous voulez.
Lorsque vous avez fini, appuyer sur entrée, et suivez les instructions sur le terminal.
Si vous avez choisi l'option medit-linux
