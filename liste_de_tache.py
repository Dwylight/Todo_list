import tache

class ListeTaches:

    def __init__(self):
        self.liste = []
        self.titre = input("Titre de la collection: ")


    def ajouter_tache(self):
        nouvelle_tache = tache.Tache()
        self.liste.append(nouvelle_tache)

    '''ma methode (ne fonctionne pas, à revoir)
    def supprimer_tache(self):
        tache_a_supprimer = input("Quel est le nom de la tâche à supprimer? ")
        if self.existence_tache(tache_a_supprimer):
                for tache in self.liste:
                    if tache.nom == tache_a_supprimer:
                        self.liste.remove(tache)
                        break
        else:
            reponse = input("Cette tache n'existe pas!, voulez vous entrer une autre?(o/n): ")
            if reponse.lower() == "o":
                self.supprimer_tache()'''
    
    # Méthode proposée par Gemini (à revoir après)

    def supprimer_tache(self):
        nom_a_supprimer = input("Quel est le nom de la tâche à supprimer ? ")
    
        tache_trouvee = False
        for tache in self.liste:
            if tache.nom == nom_a_supprimer:
                self.liste.remove(tache)
                print(f"La tâche '{nom_a_supprimer}' a été supprimée.")
                tache_trouvee = True
                break
        if not tache_trouvee:
            print(f"La tâche '{nom_a_supprimer}' n'a pas été trouvée.")
             

    def existence_tache(self, tache_a_verifier):
        for tache in self.liste:
            if tache.nom == tache_a_verifier:
                return True
            else:
                return False
        
    def afficher_contenu_collection(self):
        print()
        print("Collection", self.titre)
        for tache in self.liste:
            tache.info_tache()

def main():
    ecole = ListeTaches()
    ecole.ajouter_tache()
    ecole.ajouter_tache()
    ecole.ajouter_tache()
    ecole.afficher_contenu_collection()
    ecole.supprimer_tache()
    ecole.afficher_contenu_collection()

if __name__ == "__main__":
    main()


    
            



            

        