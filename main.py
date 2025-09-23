import tache

def main():
    todo_list = []
    print("************")
    print("TO-DO LIST")
    print("************")
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter une tâche")
        print("2. Afficher toutes les tâches")
        print("3. Modifier une tâche")
        print("4. Afficher les tâches en cours")
        print("5. Afficher les tâches achevées")
        print("6. Supprimer une tâche")
        print("7. Quitter")
        print()
        choix = input("Quel est votre choix : ")
        if choix == "1":
            tache.ajouter_tache(todo_list)
        elif choix == "2":
            tache.afficher_taches(todo_list)
        elif choix == "3":
            tache.modifier_tache(todo_list)
        elif choix == "4":
            tache.taches_en_cours(todo_list)
        elif choix == "5":
            tache.taches_achevees(todo_list)
        elif choix == "6":
            tache.supprimer_tache(todo_list)
        elif choix == "7":
            break 
        else:
            print("Choix invalide. Veuillez réessayer!")

if __name__ == "__main__":
    main()




