class Livre:    #class livre
    def __init__(self, Titre, Auteur, Nb_Pages):    #constructeur de class Livre
        self.Titre = Titre      #Attributs Titre | Auteur 
        self.Auteur = Auteur
        try:
            self.Nb_Pages = int(Nb_Pages)
            if Nb_Pages > 0:
                print("nombre des pages accepté")
            else:
                raise ValueError("le nombre des pages doit etre POSITIVE") 
        except Exception as e:  #-----except an error 
            print(f"Erreur de type : {e}")
        finally:    #----Finally
            print(f"le titre de livre {self.Titre}, l' auteur {self.Auteur},
                    et le Nombre des pages {self.Nb_Pages}")


class Bibliotheque:     #class Bibliothéque
    
    def __init__(self, Livres=None):     #constructeur de Bibliothéque
        if self.Livres is None:
            Livres = [] 
        self.Livres = Livres    #Attribut de l'instance


    def AjouterLivre(self):     #fonction de l' Ajoute de Livre
        try:
            livre_A = input("Entrer un livre : ")
            if isinstance(livre_A, Livre):   
                self.Livres.append(livre_A)
            else:
                raise TypeError(f"la class livre pas contient de : {livre_A} !")
        except Exception as e:  #----except an error
            print(f"Erreur de type : {e}")
        finally:
            print("Le livre etait ajouté avec succes. ")
        

    def SupprimerLivre(self):   #fonction de supprission 
        try:    
            Titre_S = input("entrer le titre pour le supprimer : ")
            for Livre in self.Livres:
                if Titre_S in self.Livres:
                    self.Livres.remove(Livre) 
                else:
                    raise Exception("Ce titre n'est exist pas !")
        except Exception as e:  #----except an error 
            print(f"Erreur de type : {e}")
        finally:
            print("Le titre etait supprimé avec succes")