import les_joueurs 
import random #package des fonctions de gestions aléatoires
import donnees


#cette fonction permet de traiter les mauvaises réponses du fichier MReponses
def traiterDonnees(compteur):
    """Elle prend des phrases comportants < et renvois trois mot ou expressions  """
    #les trois mauvaises réponses reçu à partir de la phrase
    Question = donnees.Questions
    Breponse = donnees.Breponses
    Mrep1 = donnees.Mreponse1 
    Mrep2 = donnees.Mreponse2
    Mrep3 = donnees.Mreponse3
    return Question[str(compteur)],Breponse[str(compteur)], Mrep1[str(compteur)], Mrep2[str(compteur)], Mrep3[str(compteur)]
#Cette foncion permettra de traiter le nom des joueurs

def name_traitment(nom):
    """Elle permet de valider un nom: Vérifier que le nom est uniquement composer de lettre et renvoie True
    Si oui et False si non"""
    valider = True
    try:
        for i in nom: #Parcours du nom
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122): #Condition de vérification
                validation = True
            else:
                validation = False
                break
        return validation
    except UnboundLocalError: #gestion de l'exception pour le cas où le nom est vide
        return False


#Cette fonction permet générer du mot de passe du joueur: composer de 2 lettres capital
#ET 3chiffre

def password_generator(nom):
    nombre = random.randint(1, 500)
    if len(nom)>=2:
        password = nom[:2].upper()+str(nombre).zfill(3)
        return password
    else:
        print("Nous ne pouvons pas vous générer un mot de passe") 

#cette fonction permettra de rechercher un joueur dans le dictionnaire des joueurs
def recherche_joueurs(name,password):
    """Recherche dans le disctionnaire des joueurs si un joueur appartient ou pas. 
    Si oui il renvoie son identifiant (la cle) et sa valeur
    si non il renvoie none"""
    try:
        joueurs = les_joueurs.les_joueurs #récuperation du dictionnaire des joueurs
        for key,joueur in joueurs.items():#parcours du dictionnaire avec stockage de la cle et la valeur
            if joueur[0] == name and joueur[1] == password:#Comparaison des données
                trouver = True
                break
            else: 
               trouver = False
        
        if trouver == True :
            return key,joueur # resultat si le joueur est trouvé
        else:
            return None #resutat si le joueur n'est pas trouver              
    except:
        print("Désolé! Nous avons un petit problème")


#cette fonction permet d'enregistrer des données nouveau joueur
def enregistrer_Njoueur(nom,motPasse):
    try:
        appartenance = recherche_joueurs(nom, motPasse) #vérifier s'il un joueur du meme nom
        if appartenance == None: # Si non
            print("Merci pour votre inscription au jeu QuizzBiblique! Bonne chance")
            joueurs = les_joueurs.les_joueurs #récuperation du dictionnaire des joueurs
            nombre = len(joueurs) #nombre d'ancien joueur.
            joueurs[str(nombre+1)]=(nom,motPasse,0,1) #Enrédistrement du nouveau joueur dictionnaire
            #Enregistrement du dictionnaire modifier
            with open("./les_joueurs.py","w") as file:
                file.write(f"les_joueurs = {joueurs}")
                file.close()
    except: #En cas d'exception
        print("Problème de connexion")


#cette fonction permet de mettre ajout les score d'un ancien joueur 
def miseAjourScore(nom, motPass, newscore,numeroQ):
    """Elle prend trois paramètre et ne renvoie rien. Elle se contente d'enregistrer le nouveau score du joueur """
    appartenance = recherche_joueurs(nom, motPass) #Recherche du jour
    if appartenance != None: #si il a été trouver
        key,joueur = appartenance #récupération de la clé et des informations du joueur
        score = joueur[2] #Récuperation du score du jour
        score +=newscore #mise à jour du score du jour
        joueurs =  les_joueurs.les_joueurs 
        joueurs[key]=(nom,motPass,score,numeroQ)#Remplacement du score du joueur
        #Sauvegarde des informations dans le dictionnaire
        with open("./les_joueurs.py","w") as file:
            file.write(f"les_joueurs = {joueurs}")
            file.close()


#Cette fonction permet au joueur de joueur au jeu
def PlayTheGame():
    """Elle permet de lancer une parti de jeu """
    #Demande d'avis du au jours
    Avis = input("Etes vous déjà inscrit pour joueur au jeu de QUIZZBIBLIQUE?(O/N)  ").upper()
    if Avis == "O":#Si déjà inscrit, il va faire saisir son mot de passe et son nom d'utilisateur
        nom_joueur = input("Veillez entrer votre nom:  ").capitalize()
        password_joueur = input("Veillez entrer votre mot de passe:  ")
        confirmation = recherche_joueurs(nom_joueur, password_joueur)#Confirmation d'inscription
        if confirmation == None: #Si non
            print("Désolé! Vous n'êtes pas inscrit")
        else: #Si oui
            key,joueur = confirmation #la cle et les informations du joueur
            score = joueur[2]#Ancien score
            numero = joueur[3]
            newscore = 0 #initialisation du nombre de point à gagner aucours de la partir
            
            
            #Le début du jeu avec l'ancien score
            while numero<=len(donnees.Questions):
                #lecture ses élééments de fichier question, Breponse, et Mreponses
                question,BReponse,MReponse1,MReponse2,MReponse3 = traiterDonnees(numero)
               
                #Déroulement du jeu
                
                #Questions,Breponse,MReponse1,MReponse2,MReponse3 = traiterDonnees(line)   
                print(f"Nom: {nom_joueur}           Score: {score}")
                print("")
                print(f"Question: {question}")
                reponses = [BReponse, MReponse1,MReponse2,MReponse3]
                random.shuffle(reponses)
                answer = input(f"""Choisis la bonne réponse en saisissant la lettre correspondantes:
                                a:  {reponses[0]} b:  {reponses[1]} 
                                c:  {reponses[2]} d:  {reponses[3]}
                                :  """).lower()
                if answer == "a":
                    answer = reponses[0]
                elif answer == "b":
                        answer = reponses[1]
                elif answer == "c":
                       answer = reponses[2]
                elif answer == "d":
                        answer = reponses[3]
                else:
                        penalite = -2
                        newscore +=penalite
                        print(f"Valeur invalide! Pénalité: {penalite}")
                if answer == BReponse:
                        print(f"Bonne réponse. Tu as gagné 10 points")
                        newscore +=10
                else:
                        print(f"""Mauvaise réponse!
                              {question} {Breponse}.
                          Vous avez perdu 5 points""")
                        newscore -=5
                numero +=1
                miseAjourScore(nom_joueur,password_joueur, newscore,numero)   
                     
                
                while True:
                    continuer = input("Souhaitez vous continuer (O/N)").upper()
                    if continuer == "O" or continuer == "N":
                        break 
                if continuer == "N":
                    print(f"Merci d'avoir participer au jeu. Votre dernier score est de: {score}")
                    break     
                                  
    elif Avis == "N":
        while True:
            nomN = input("Veillez entrer votre nom: ")
            validation = name_traitment(nomN)
            if validation:
                break
            else:
                print("Nom invalide!")
        motPasse = password_generator(nomN)
        enregistrer_Njoueur(nomN, motPasse)
        print(f"""Enregistrement réussie. 
                    Votre nom d'utilisateur est {nomN}
                    Votre mot de passe est {motPasse}""")
    else:
        print("Saisir invalide !!!!")       

PlayTheGame()