import Joueur
import random

def traiter(contenu):
    """ traiter u une information récupérer à partie du fichier les_joueur
    elle renvoie le nom,le mot de passe et le score du joueur enregistrer
    """
    position_sep = []
    for i in range(len(contenu)):
        #récupération de la position du séparateur
        if contenu[i]==" " or contenu[i]=="\n":
            position_sep.append(i)
        
        #récupération dans l'ordre le nom, le mot de passe et le dernier score du joueur
    nom = contenu[:position_sep[0]]
    mot_de_passe = contenu[position_sep[0]+1:position_sep[1]]
    old_score = contenu[position_sep[1]+1: position_sep[2]]
    return nom,mot_de_passe,old_score
    
# fonction pour rechercher un joueur
def recherche_joueur(nom):
    """recherche d'un joueur dans la liste des joueurs  """
    with open("C:/Users/hp/Desktop/Quizz/les_joueurs","r") as file:
        for line in file:
            personne = traiter(line)
            nom_personne,password_personne,score_personne = personne
            if nom == nom_personne:
                valider = True
                break
            else:
                valider = False
        file.close()
    if valider == True:
        return personne
    else: 
        return False

#Recherche d'un chiffre dans un mot
def verification(mot):
    trouver = False
    for i in mot:
        if i.isdigit() or i == "" or i== " " or ((ord(i)<65 or ord(i)>90) and (ord(i)<97 and ord(i)>122)) :
            trouver = True
            break
    return trouver

#gestionnaire de mot de passe 
def generateur(mot):
    chiffre = random.randint(1, 501)
    password = mot[:2].upper()+str(chiffre).zfill(3)
    return password

#fonction pour saisir un nom
def saisir_nom():
    while True:
        nom = input("Veillez entrer votre nom: ").capitalize()
        valider = verification(nom)
        if valider == False:
            return nom
            break
            
    
#recuperation du score
def recuperateur_score(mot):
    """Récupération du score d'un joueur existant  """
    personne = recherche_joueur(mot)
    if personne == False:
        print(f"{mot} n'est pas un joueur. ")
        
#Enregistrement d'un nouveau joueur
def enregistrement_joueur():
    print("lolo")
    