import csv
from collections import defaultdict

class eleve:
    def __init__(self, name, skills):
            self.name = name
            self.skills = skills
            name = ""
            skills = defaultdict()

    def fill_skills (self) :
        for i in range (0,1) :
            continue       


lire = csv.DictReader(open(r"C://Users\admin\OneDrive\Documents\Learning_coach\notes_classe_test.csv"))
for ligne in lire :
    print(ligne)    

#1 obtenir une liste des élèves
#2 créer des instances de la classe élève en attribuant les éléments de la liste
#3 obtenir des dictionnaires avec 'en-tête : niveau de maîtrise'
#4 pour chaque paire 'k:v' ajouter '%k%v.png' au livret de travail