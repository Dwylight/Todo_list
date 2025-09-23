class Tache:

    def __init__(self, titre, description, statut, date):
        self.titre = titre
        self.description = description
        self.statut = statut
        self.date = date 

    def __str__(self):
        return (
            f"Tâche : {self.titre}\n"
            f"Date de création: {self.date}\n"
            f"Description : {self.description}\n"
            f"Statut : {self.statut}"
        )

    def tache_achevee(self):
        return self.statut.lower() == "achevé" 
    
    def changer_statut(self, nouveau_statut):
        self.statut = nouveau_statut
    
    def modifier_description(self, nouvelle_description):
        self.description = nouvelle_description

    def modifier_titre(self, nouveau_titre):
        self.titre = nouveau_titre


def ajouter_tache(liste_tache):
    print()
    titre = input("Enrez le titre de la tâche: ")
    date = input("Date de création: ")
    question = input(("Voulez vous ajouter une description de la tâche?(o/n) "))
    if question.lower() == "o":
        description = input("Description : ")
    else:
        description = "Aucune"
    statut = input("Statut de la tâche (Achevé/En cours): ")
    tache_cree = Tache(titre, description, statut, date)
    liste_tache.append(tache_cree)

def afficher_taches(liste_tache):
    for tache in liste_tache:
        print(tache)
        print()

def afficher_nom_taches(liste_tache):
    for tache in liste_tache:
        print("-", tache.titre)

def taches_achevees(liste_tache):
    liste_achevee = []
    for tache in liste_tache:
        if tache.tache_achevee():
            liste_achevee.append(tache)
       
    if not liste_achevee:
        print("Aucune tâche n'est achevée!")
    else:
        print("Liste des taches achevées: ")
        afficher_nom_taches(liste_achevee)


def taches_en_cours(liste_tache):
    liste_en_cours = []
    for tache in liste_tache:
        if not tache.tache_achevee():
            liste_en_cours.append(tache)
       
    if not liste_en_cours:
        print("Aucune tâche n'est en cours!")
    else:
        print("Liste des taches en cours: ")
        afficher_nom_taches(liste_en_cours)

def existence_tache(liste_tache, tache_a_verifier):
        for tache in liste_tache:
            if tache.titre == tache_a_verifier:
                return tache
            return False

def modifier_tache(liste_tache):
    while True:
        titre_a_modifier = input("Entrez le titre de la tâche à modifier: ")
        tache_a_modifier = existence_tache(liste_tache, titre_a_modifier)
        if tache_a_modifier:
            while True:
                print()
                print("--- MENU MODIFICATION---")
                print("1- Modifier le titre")
                print("2- Modifier la description")
                print("3- Modifier le statut ")
                print("4- Quitter")
                print("__________________________")
                choix = input("Quel est votre choix?: ")
                if choix == "1":
                    nouveau_titre = input("Entrez le nouveau titre: ")
                    tache_a_modifier.modifier_titre(nouveau_titre)
                elif choix == "2":
                    nouvelle_description = input("Entrez une nouvelle description: ")
                    tache_a_modifier.modifier_description(nouvelle_description)
                elif choix == "3":
                    nouveau_statut = input("Entrez le nouveau statut (En cours/Achevé): ")
                    tache_a_modifier.changer_statut(nouveau_statut)
                elif choix == "4":
                    break
                else:
                    print("Choix invalide. Veuillez réessayer!")
        else:
            recommencer = input("Cette tâche n'existe pas! Voulez vous réessayer?(o/n): ")
            if recommencer.lower() != "o":
                break

def supprimer_tache(liste_tache):
    while True:
        titre_a_supprimer = input("Entrez le titre de la tâche à supprimer: ")
        tache_a_supprimer = existence_tache(liste_tache, titre_a_supprimer)
        if tache_a_supprimer:
            liste_tache.remove(tache_a_supprimer)
            print("Tache supprimée avec succès!")
        else:
            recommencer = input("Cette tâche n'existe pas! Voulez vous réessayer?(o/n): ")
            if recommencer.lower() != "o":
                break













           
        


        

    


        
    




   
        

