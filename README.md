
### Maillage

Maillage Project
Polytech Paris-UPMC

Year 2016-2017

### Author: Lancelot Satge, Suzanne Sleiman, Geng Ren
Professor: Chiara Nardoni

This project proposes two kinds of deformation: Most Least Square (MLS) and Barycentric

### Usage

Before using a deformation, be sure to have Python 2 AND Python 3 (versions that we used : Python 2.7.6 and Python 3.4.3) and to install Pygame for Python2 and Numpy for Python3.

/!\ If you use a mac, change the line 149 of the file Execution_Barycentre.py and the line 161 of the file Execution_MLS.py by os.system("./medit ../mesh/mesh_2D/"+nom_fichier+".mesh &")

### MLS deformation
To use the MLS deformation, go in the directory code/Programmes/, launch the file MLS_python2.py with python2, then write the noun of the file .mesh which you want to modify, which is in the directory code/mesh/mesh_2D without the extension (example: man for man.mesh). A pygame's window will open, then select points of the drawing with the left clic after that select the new position of the point with the right clic. Repeat this process as much as you want.
When you have done, press enter, and follow the instructions on the terminal.

If you choose medit, a medit window will apear, to see your deformation, you need to right clic, then go to Data and clic on Toggle displacement

### Barycentric deformation
To use the Barycentric deformation, go in the directory code/Programmes/, launch the file Barycentrique_python2.py with python2, then write the noun of the file .mesh which you want to modify, which is in the directory code/mesh/mesh_2D without the extension (example: man for man.mesh). A pygame's window will open, then select points of the drawing with the left clic after that select the new position of the point with the right clic. Repeat this process as much as you want.
When you have done, press enter, and follow the instructions on the terminal.

If you choose medit, a medit window will apear, to see your deformation, you need to right clic, then go to Data and clic on Toggle displacement
