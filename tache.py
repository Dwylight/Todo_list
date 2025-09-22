class Tache:
    def __init__(self):
        self.nom = input("Nom de la tâche: ")
        self.description_tache()
        self.etat = input("Etat de la tâche (en cours/terminé/abandonné): ")

    def modifier_titre(self):
        nouveau_titre = input("Entrez le nouveau nom de la tâche: ")
        self.nom = nouveau_titre
        print("Nouveau nom de la tâche: ",self.nom)

    def afficher_etat(self):
        print("Etat actuel de la tâche: ",self.etat)

    def changer_etat(self):
        self.afficher_etat()
        self.etat = input("Nouvel état de la tâche: ")

    def description_tache(self):
        question = input(("Voulez vous ajouter une description de la tâche?(o/n) "))
        if question.lower() == "o":
            self.description = input("Description : ")
        else:
            self.description = None

    def info_tache(self):
        print()
        print("Informations sur la tâche:")
        print("- Nom: ",self.nom)
        if self.description:
            print("- Description: ",self.description)
        print("- Etat: ",self.etat)


def main():
        tache1 = Tache()
        tache1.description_tache()
        tache1.modifier_titre()
        tache1.afficher_etat()
        tache1.changer_etat()
        tache1.info_tache()


if __name__ == "__main__":
        main()

   
        

