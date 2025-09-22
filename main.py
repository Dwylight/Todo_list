import liste_de_tache

#J'ai utilisé un peu d'IA à ce niveau pour apprendre à faire les menu et à corriger les bug, à revoir également!

def menu():
    collection1 = liste_de_tache.ListeTaches() 
    
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter une tâche")
        print("2. Afficher toutes les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        
        choix = input("Quel est votre choix : ")
        
        if choix == "1":
            collection1.ajouter_tache()
        elif choix == "2":
            collection1.afficher_contenu_collection()
        elif choix == "3":
            collection1.supprimer_tache()
        elif choix == "4":
            break 
        else:
            print("Choix invalide. Veuillez réessayer!")


if __name__ == "__main__":
    menu()