import tkinter
import tkinter.ttk
import tkinter.filedialog
import tkinter.messagebox
import os
import Fonctions.Learning_coach as Learning_coach


filename =""
fenetre = tkinter.Tk()  
fenetre.configure(bg='#9896E1')
fenetre.geometry("1920x1080")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

IMG_TempsLibre = tkinter.PhotoImage(file = "Images/temps-libre.png")
IMG_Dossier = tkinter.PhotoImage(file="Images/Dossier.png")
IMG_Sortie = tkinter.PhotoImage(file ="Images/sortie.png")
IMG_Choix= tkinter.PhotoImage(file="Images/choose.png")
IMG_Fond = tkinter.PhotoImage(file="Images/Fond2.png")

label1 = tkinter.Label(fenetre, image = IMG_Fond)
label1.place(x = -70, y = -10, relheight=1, relwidth=1)

X_Bienvenue = 300
Y_Bienvenue = 100

Bienvenue = tkinter.Label(fenetre, text="Bienvenue sur Learning Coach", bg='#E0D496',font=('Broadway', 32))
Bienvenue.place(x = X_Bienvenue, y = Y_Bienvenue)

def Choix():
    global filename
    filename = tkinter.filedialog.askopenfilename(title="Ouvrir votre document", filetypes=[('csv files','.csv'),('all files','.*')])

Choisir = tkinter.Button(fenetre, image=IMG_Choix, bg='#E0D496', command=Choix, width=100, height=100)
Choisir.place(x = X_Bienvenue + 700, y = Y_Bienvenue + 200)

Tuto_Choisir = tkinter.Label(fenetre, text="1. Entrez vos données : \n insérez le tableau CSV avec les résultats de l'évaluation fournie codés de 1 à 4", font=('Helvetica', 18))
Tuto_Choisir.place(x = X_Bienvenue - 190, y = Y_Bienvenue + 225)

Valider = tkinter.Button(fenetre, image=IMG_TempsLibre, bg='#E0D496', width=100, height=100, command = lambda :[Learning_coach.Learning_coach(filename), tkinter.messagebox.showinfo("Fin de l'écriture", "Écriture terminée !")] , font=('Helvetica', 12))
Valider.place(x = X_Bienvenue + 330, y = Y_Bienvenue + 350)

Tuto_Valider = tkinter.Label(fenetre, text="2. Cliquez ici pour \n générer les plans de travail ►", font=('Helvetica', 18))
Tuto_Valider.place(x = X_Bienvenue - 110, y = Y_Bienvenue + 375)

Afficher = tkinter.Button(fenetre, image=IMG_Dossier, bg='#E0D496', command = lambda :[os.chdir(os.path.dirname(os.path.abspath(__file__))), os.startfile("Plans_de_travail")], width=100, height=100)
Afficher.place(x = X_Bienvenue + 1000, y = Y_Bienvenue + 350)

Tuto_Afficher = tkinter.Label(fenetre, text="3. Cliquez ici pour \n afficher les plans de travail ►", font=('Helvetica', 18))
Tuto_Afficher.place(x = X_Bienvenue + 550 , y = Y_Bienvenue + 375)

Credits_Photo = tkinter.Label(fenetre, bg='#9896E1', text="Crédits images : maswan, kalashnyk, chattapat.k, goodware \n https://www.flaticon.com \nDéveloppement : Guillaume PAYAN, Python 3.11", font=('Helvetica', 18))
Credits_Photo.place(x = X_Bienvenue - 100, y = Y_Bienvenue + 600)

Fermer = tkinter.Button(fenetre, image=IMG_Sortie, bg='#E0D496', width=100, height=100, command=fenetre.quit, font=('Helvetica', 12))
Fermer.place(x = X_Bienvenue + 700, y = Y_Bienvenue + 500)

fenetre.mainloop()

##Affichage_fichier = tkinter.Label(fenetre, text="Vous avez choisi le fichier %s " %filename)
##Affichage_fichier.place(x = 500, y = 500)##