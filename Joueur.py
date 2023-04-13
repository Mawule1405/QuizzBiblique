import fonctions
class Joueur:
    
    """Classe de gestion des joueurs """
    def __init__(self,nom,password,scores):
        """ création d'un joueur"""
        self.nom = nom
        self.password = password
        self.scores = scores
        self.position = 0
    
    def initialisation_password(self,name,newpassword,score):
        """ Cette méthode permet d'initialiser le mot de passe  """
        if name == self.nom and score == self.scores :
            
            self.password = newpassword
        else :
            print(" Le nom ou le score est ncorrecte. Vous ne pouvez pas changer le mot de passe.")
    
    def Inscription(self):
        """ Cette méthode permet au joueur de s"rnregistrer dans un fichier """
        fonctions.enregistrement_Njoueur()
    
    def enregistrerAncien(self, nom, password, scores):
        """Cette méthode permet d'enregistrer le scores d'un ancien joueur dans le fichier"""
        
        
    def jouer(self):
        """ Cette méthode permet au joueur de participer au jeu """
        print(f"Bienvenu dans le jeu de Quizz")
        print(f"""      Super QUizz
                Nom du joueur:      {self.nom}
                Ancien score:       {self.scores}
              """)
    
    def afficher_score(self,new_score):
        print(f"Nouveau score: {new_score}")  

