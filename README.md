# Projet Python 1 - Mathis et Arnaud - Groupe BDX

## Partie 1

Dans cette partie, nous avons développé les fonctions TF-IDF : 

- Fonction occurrenceOfWords -> Paramètres : `text` -> **string** et `word` -> **str**. Retourne _counter_ (**int**) le nombre d'occurrence du mot '`word`' dans le texte '`text`'. Cette fonction est principalement utilisé dans la fonction TFCalculator.

- Fonction TFCalculator -> Paramètres : `text` -> **string**. Retourne _TF_ (**dictionnaire**) le score TF de chaque mot présent dans le texte `text`.

- Fonction IDFCalculator -> Paramètres : `folderAddr` -> **string**. Retourne _IDF_ (**dictionnaire**) le score IDF de chaque mot présent dans le répertoire `folderAddr`.

- Fonction TFIDFList -> Paramètres : `folderAddr` -> **string**. Retourne _TFIDF_ (**liste 2D**) et _list(IDF.keys())_  (**liste**), TFIDF étant le score _TFIDF_ de chaque mot présent dans le répertoire `folderAddr` et _list(IDF.keys())_ tous les mots présent dans le dictionnaire IDF (utilisé plus tard dans les finctions utilisant TF-IDF).

- Fonction printTab2D -> Paramètres : `listOfTFIDF` -> **liste**. Affiche la liste 2D `listOfTFIDF`.
