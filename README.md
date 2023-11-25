# Projet Python 1 - Mathis et Arnaud - Groupe BDX

## Partie 5

Dans cette partie, nous avons `merge` toutes nos branches pour arriver à la version finale.

Vous trouverez donc dans notre branche main notre version **FINALE !**

### Installation des modules :

Pour installer les modules nécessaires au fonctionnement du menu, merci de saisir la commande suivante dans un terminal (attention à bien ajouter `python` et `pip` au `path`) : 

```
pip install -r requirements.txt
```

### Fonctionnement du menu : 

1) Renseigner le chemin d'accès (en relatif) du dossier comprenant les textes **CLEANED**.
2) Choisir la fonction à exécuter.
   a) Fonction irrelevantWords -> Donne les mots ayant un TF-IDF de 0 dans tous les fichiers.
   b) Fonction importantWords -> Donne les mots ayant le score TF-IDF le plus élevé.
   c) Fonction mostUsedWords -> Donne les mots le(s) plus répété(s) par le président choisi dans _Enter the arguments_.
   d) Fonction whoTalkAbout -> Indique le(s) président(s) qui a/ont dit le mot choisi dans _Enter the arguments_ ainsi que celui qui l'a le plus dit.
   f) Fonction firstToSay -> Indique le président qui a dit le mot choisi dans _Enter the arguments_ en premier. 
   g) Fonction universalWords -> Indique le(s) mot(s) que tous les présidents ont dit (sans les mots ayant un TF-IDF de 0).
3) Saisir le mot dans _Enter the arguments_ (si nécessaire)
4) Appuyer sur GO

Le lien de notre github : [https://github.com/Mathis-Desbonnet/pychatbot-mathis-arnaud-bdx/](https://github.com/Mathis-Desbonnet/pychatbot-mathis-arnaud-bdx/)
