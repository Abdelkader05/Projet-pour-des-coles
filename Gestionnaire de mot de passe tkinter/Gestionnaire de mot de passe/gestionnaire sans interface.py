
def creation_mdp() :
    nom = ""
    site = ""
    mdp = ""
    nom = input(str("veuiller entrer nom de reference pour le mot de passe"))
    if nom != "" :
        site = input(str("veuiller rentrer le lien du site/page (facultatif)"))
        mdp = input(str("veuiller rentrer le mot de passe"))
        if mdp != "" :
            verification(mdp, nom, site)
        else :
            print("ecrivez le mot de passe")
            creation_mdp()
    else:
        print("ecrivez un nom")
        creation_mdp()


def verification(mdp, nom, site):
    file = open('gestionnaire de mot de passe.txt', "r+")

    liste = file.readlines()

    if liste == []:
        enregistrement(mdp, nom, site)

    else:
        for element in liste :
            if ("nom:_" + nom) not in element :
                enregistrement(mdp, nom, site)

            else :
                print("un mot de passe exsiste deja pour se nom")
                creation_mdp()

def enregistrement(mdp, nom, site):
    file = open('gestionnaire de mot de passe.txt', "r+")
    file.write(str(len(file.readlines())+1) + ") Le nom de reference est : " + nom + "  le site est: " + site + "  et le mot de passe est: " + mdp + "\n")
    file.close()
    print("MOT DE PASSE ENREGISTRER")
    creation_mdp()

creation_mdp()