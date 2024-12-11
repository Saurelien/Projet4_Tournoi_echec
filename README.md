## Titre du projet

- Développez un programme logiciel en Python

## Utilisation local
### Prérequis

- Interpréteur Python, version 3.7 ou supérieure

### Execution du programme

- Clonez le dépot suivant:
   - git clone https://github.com/Saurelien/Projet4_Tournoi_echec
   - Placez-vous à la racine du projet
   - Assurez-vous d'être dans un environnement virtuel:

   #### Créer l'environnement virtuel

     - `python -m venv venv`
       - `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
       - Activer l'environnement `source venv/bin/activate`
       - Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
       `which python`
       - Confirmer que la version de l'interpréteur Python est la version 3.7 ou supérieure `python --version`
       - Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
       - Pour désactiver l'environnement, `deactivate`
   ### Lancement du programme

- Utilisez la méthode "RUN" de pycharm depuis le fichier main.py
  - Vous devriez avoir un affichage du menu principal:

    - 'l' Pour créer un tournoi: 

    - 'B' Afficher la liste des tournois: 

    - 'Y' Afficher les acteurs par ordre aphabétique: 

    - 'T' Afficher les acteurs par classement: 

    - 'Q' Quitter l'application: 

    - Quel est votre choix ?: 

### Divers

- Un tournoi peut-être interrompu pendant la création, l'ajout de joueur, et durant les matchs
- Une Db "db.json" est generer et geré par tinyDB
- il est possible:
  - De pouvoir afficher la liste des tournois:
    - Et du details complet du tournoi selectionné dans la liste:
      - Par exemple: Matchs/Round/Classement
  - La liste des acteurs de tous les tournois par ordre alphabetique
  - Un affichage du classement par points des acteurs de tous les tournois