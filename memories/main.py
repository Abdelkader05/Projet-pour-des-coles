import tkinter
import os
import  random
from PIL import ImageTk

window = tkinter.Tk()
window.configure()

jeu = tkinter.Frame(window, background="cyan")

score_total = 0
score_manche = 0
ancienne_image = ""
liste_case = []

score_label  = tkinter.Label(window, text="Tu as " + str(score_manche) + " point", font=("broadway", 40))
score_label.pack()

image_gris = ImageTk.PhotoImage(file="image/gris.png")
image_verifier = tkinter.PhotoImage(file="image/valide.png")

liste_image = os.listdir("image/teste")
for i in range(len(liste_image)):
    image = ImageTk.PhotoImage(file=f"image/teste/{liste_image[i]}")
    couple = (liste_image[i], image )
    liste_image[i] = couple
class case():
    def __init__(self,couple):
        self.couple = couple
        self.nom = couple[0]
        self.image = couple[1]
        self.widjet = None

    def entrer_coordonner(self, ligne, colonne):
        self.ligne, self.colonne = ligne,colonne

    def entry_widjet(self, widjet):
        self.widjet = widjet
        return self.widjet

    def monter(self):
        self.widjet.configure(image = self.image)

    def commande(self):
        global score_manche, score_total, ancienne_image
        if ancienne_image == "":
            ancienne_image = [self]
            self.monter()
        elif len(ancienne_image) >= 2:
            for i in ancienne_image:
                i.widjet.configure(image = image_gris)
            ancienne_image = [self]
            self.monter()
        else:
            self.monter()
            if ancienne_image[0].image == self.image and ancienne_image[0] != self:
                ancienne_image.append(self)
                valider_case(ancienne_image)
                score_manche = score_manche + 1
                score_total += 1
                score_label.configure(text="Tu as " + str(score_total) + " point")
                ancienne_image = ""
                if score_manche == len(liste_image):
                    verif_win()
            else :
                ancienne_image.append(self)


def affiche(taille = 4):
    try:
        assert taille >= 3
        assert taille < 10
        cpt = 0
        copy = list(liste_image)
        copy = copy + copy
        random.shuffle(copy)
        colonne = 0
        ligne = 0
        while copy != []:
            if cpt > taille - 2:
                cpt = 0
                classe = case(copy[0])
                label = tkinter.Button(jeu, image=image_gris, command=classe.commande)
                label.grid(column=colonne, row=ligne)
                classe.entry_widjet(label)
                classe.entrer_coordonner(ligne, colonne)
                liste_case.append(classe)
                copy.remove(copy[0])
                ligne += 1
                colonne = 0
            else:
                classe = case(copy[0])
                label = tkinter.Button(jeu, image=image_gris, command=classe.commande)
                label.grid(column=colonne, row=ligne)
                classe.entry_widjet(label)
                classe.entrer_coordonner(ligne, colonne)
                liste_case.append(classe)
                del copy[0]
                cpt += 1
                colonne += 1
    except:
        erreur = tkinter.Label(jeu,text="choisir une taille plus grande", font=("broadway", 50), background="black", foreground="white" )
        erreur.pack()


def valider_case(liste: list):
    for element in liste:
        element.widjet.destroy()
        label = tkinter.Button(jeu, image=image_verifier)
        label.grid(column=element.colonne, row=element.ligne)
def verif_win():
    global score_manche
    for i in jeu.winfo_children():
        i.destroy()
        score_manche = 0
    for instance in liste_case:
        liste_case.remove(instance)
        del instance
    affiche(4)

affiche(4)
jeu.pack()

window.mainloop()


