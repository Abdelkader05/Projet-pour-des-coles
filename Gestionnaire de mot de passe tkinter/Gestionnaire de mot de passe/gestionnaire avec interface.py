import webbrowser
from tkinter import *


def menu(x,y):

    window = Tk()
    window.title("gestionnaire de mot de passe")
    window.geometry("1080x620+"+str(x)+"+"+str(y))
    window.minsize(480, 360)
    window.config(background='black')

    def nv_mdp(x,y):

        creation_window = Tk()
        creation_window.title("gestionnaire de mot de passe")
        creation_window.geometry("1080x62+"+str(x)+"+"+str(y))
        creation_window.minsize(480, 360)
        creation_window.config(background='black')

        def destroy_4():
            x = creation_window.winfo_x()
            y = creation_window.winfo_y()
            creation_window.destroy()
            menu(x,y)

        def enregistrement(nom, site, mdp, creation_window):

            file = open('gestionnaire de mot de passe.txt', "r+")
            file.write(str(len(file.readlines()) + 1) + ") nom:_ " + nom + "_ site:_ " + site + "_ mot de passe:_ " + mdp + "_\n")
            file.close()
            enregistrement_txt = Label(creation_window, background="black",
                                       text="MOT DE PASSE ENREGISTRER",
                                       font=("Courrier", 40), foreground="white")
            enregistrement_txt.pack(expand=YES)

            suivant = Button(creation_window, text="Suivant", font=("Courrier", 30), command=destroy_4)
            suivant.pack(expand=YES)

        def verification(nom, site, mdp, creation_window):

            file = open('gestionnaire de mot de passe.txt', "r+")

            liste_gestionnaire = file.readlines()

            if not liste_gestionnaire:
                enregistrement(nom, site, mdp, creation_window)

            else:
                for element in liste_gestionnaire:

                    if ("nom:_" + nom) not in element:
                        enregistrement(nom, site, mdp, creation_window)
                        break

                    if ("nom:_" + nom) in element:
                        verfication_txt = Label(creation_window, background="black",
                                                text="un mot de passe exsiste deja pour se nom",
                                                font=("Courrier", 40), foreground="white")
                        verfication_txt.pack(expand=YES)
                        suivant = Button(creation_window, text="Suivant", font=("Courrier", 30), command=destroy_4)
                        suivant.pack(expand=YES)

        def creation_mdp(nom, site):
            nom = nom
            site = site
            def destroy_3():
                mdp = ""
                mdp = mdp_entry.get()
                if mdp != "" and mdp != " ":
                    title_creation_mdp.destroy()
                    mdp_entry.destroy()
                    suivant.destroy()
                    retour.destroy()
                    verification(nom, site, mdp, creation_window)

            def retour_3():
                title_creation_mdp.destroy()
                mdp_entry.destroy()
                suivant.destroy()
                retour.destroy()
                creation_site(nom)

            title_creation_mdp = Label(frame, background="black",
                                        text="veuiller rentrer le mot de passe", font=("Courrier", 20),
                                        foreground="white")
            title_creation_mdp.pack()

            mdp_entry = Entry(frame, background='gray', font=("Courrier", 40), foreground="white")
            mdp_entry.pack()

            retour = Button(frame_option, text="Retour", font=("Courrier", 30), command=retour_3)
            retour.pack(expand=YES, padx="100", side=LEFT)
            suivant = Button(frame_option, text="Suivant", font=("Courrier", 30), command=destroy_3)
            suivant.pack(expand=YES, padx="100")

            frame.pack(expand=YES)
            frame_option.pack(expand=YES)

        def creation_site(nom):
            nom = nom

            def destroy_2():
                site = ""
                site = site_entry.get()
                title_creation_site.destroy()
                site_entry.destroy()
                suivant.destroy()
                retour.destroy()
                creation_mdp(nom,site)

            def retour_2():
                creation_window.destroy()
                nv_mdp(x,y)

            title_creation_site = Label(frame, background="black",
                                        text="veuiller rentrer le lien du site (facultatif)", font=("Courrier", 20),
                                        foreground="white")
            title_creation_site.pack()

            site_entry = Entry(frame, background='gray', font=("Courrier", 40), foreground="white")
            site_entry.pack()

            retour = Button(frame_option, text="Retour", font=("Courrier", 30), command=retour_2)
            retour.pack(expand=YES, padx="100", side=LEFT)
            suivant = Button(frame_option, text="Suivant", font=("Courrier", 30), command=destroy_2)
            suivant.pack(expand=YES, padx="100")

            frame.pack(expand=YES)
            frame_option.pack(expand=YES)

        def destroy_1():
            nom = nom_entry.get()
            if nom != "" and nom != " ":
                title_creation_mom.destroy()
                nom_entry.destroy()
                suivant.destroy()
                retour.destroy()
                creation_site(nom)

        frame = Frame(creation_window, background="black")
        frame_option = Frame(creation_window, background="black")

        title_creation_mom = Label(frame, background="black",
                                   text="veuiller entrer nom de reference pour le mot de passe",
                                   font=("Courrier", 20), foreground="white")
        title_creation_mom.pack()

        nom_entry = Entry(frame, background='gray', font=("Courrier", 40), foreground="white")
        nom_entry.pack()

        retour = Button(frame_option, text="Retour", font=("Courrier", 30), command=destroy_4)
        retour.pack(expand=YES,padx="100",side=LEFT)
        suivant = Button(frame_option, text="Suivant", font=("Courrier", 30), command=destroy_1)
        suivant.pack(expand=YES,padx="100")

        frame.pack(expand=YES)
        frame_option.pack(expand=YES)
        creation_window.mainloop()

    def liste(x,y):

        window_liste = Tk()
        window_liste.title("gestionnaire de mot de passe")
        window_liste.geometry("1080x620+"+str(x)+"+"+str(y))
        window_liste.minsize(480, 360)
        window_liste.config(background='black')

        file = open('gestionnaire de mot de passe.txt', "r+")
        liste_mdp = file.readlines()
        frame_liste = Frame(window_liste, background="black")


        def retour():
            x = window_liste.winfo_x()
            y = window_liste.winfo_y()
            window_liste.destroy()
            menu(x,y)

        class element_page():
            def __init__(self):
                self.default = 0
                self.element = 0
                self.max = 11

            def plus_element(self):
                self.element += 1

            def moin_element(self):
                self.element -= 1
        element_page = element_page()

        def delete_frame():
            for widget in frame_liste.winfo_children():
                widget.destroy()

        def redirection(label):
            """new_text = str.swapcase(lab["text"])
            lab.config(text=new_text)"""
            label.bind("<Enter>", label.config(fg="red"))
            label.bind("<Leave>", label.config(fg="white"))
            """"texte = liste_mdp[self.indice]
            texte = texte.split('_')
            webbrowser.open(texte[3], new=0, autoraise=True)"""


        def next_page():

            if element_page.element >= len(liste_mdp):
                element_page.element = element_page.default

            if len(liste_mdp) < element_page.max:
                max = len(liste_mdp)
            else:
                max = element_page.element + element_page.max

            delete_frame()
#creer une classe pour pouvoir renvoyer sur le site
            for i in range(element_page.element, max):
                if i < len(liste_mdp):
                    label = Label(frame_liste, text=liste_mdp[i], justify=LEFT, background="black",
                              foreground="white", font=("courriel", 15))
                    label.bind("<Enter>", label.config(fg="red"))
                    label.bind("<Leave>", label.config(fg="white"))
                    label.bind("<Button-1>",redirection(label))
                    label.pack()
                    element_page.plus_element()
                frame_liste.pack(expand=YES, side=LEFT)

        def last_page():

            if len(liste_mdp) < element_page.max or element_page.element <= element_page.max:
                max = element_page.max
                element_page.element = 0
            else:
                if element_page.element % 11 > 0:
                    element_page.element -= (element_page.element % 11) + 11
                else:
                    element_page.element -= element_page.max * 2

                max = element_page.element + element_page.max

            delete_frame()

            for i in range(element_page.element, max):
                if i < len(liste_mdp):
                    texte = liste_mdp[i]
                    label = Label(frame_liste, text=texte, justify=LEFT, background="black",
                                  foreground="white", font=("courriel", 15))
                    label.pack()
                    element_page.plus_element()
                frame_liste.pack(expand=YES, side=LEFT)

        frame_option = Frame(window_liste, background="black")

        retour = Button(frame_option, text="Menu", font=("courriel", 20), command=retour)
        retour.pack(expand=YES, side=LEFT, padx=50)

        last_page = Button(frame_option, text="Retour", font=("courriel", 20), command=last_page)
        last_page.pack(expand=YES,  side=LEFT, padx=50)

        page = Button(frame_option, text="Suivant", font=("courriel", 20),command=next_page)
        page.pack(expand=YES, padx=50)

        frame_option.pack(expand=YES, side=BOTTOM)
        next_page()

    def run_mdp():
        x = window.winfo_x()
        y = window.winfo_y()
        window.destroy()
        nv_mdp(x,y)

    def run_liste():
        x = window.winfo_x()
        y = window.winfo_y()
        window.destroy()
        liste(x,y)

    title = Label(window, background='black', text="Gestionnaire de mot de passe",
                  font=("Courrier", 40), foreground="white")
    title.pack(side=TOP)

    frame = Frame(window,background="black")

    run_mdp = Button(frame, text="Enregistrer un nouveau mot de passe",
                 font=("Courrier", 30), command=run_mdp)
    run_mdp.pack()

    run_liste = Button(frame, text="liste des mot de passe", font=("Courrier", 30),command=run_liste)
    run_liste.pack()
    frame.pack(expand=YES)
    window.mainloop()

menu(0,0)