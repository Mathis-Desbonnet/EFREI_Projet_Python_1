# Projet Python 1 - Mathis et Arnaud - Groupe BDX

## Partie 2

Dans cette partie, nous avons développé les fonctions qui utilise les résultats TF-IDF : 

- Fonction irrelevantWords -> Paramètres : `matrice` -> **liste** et `wordsList` -> **liste**. Retourne _irrelevants_ (**liste**) la liste des mots ayant un TF-IDF de 0 dans la liste `matrice` (donc dans tous les fichiers).

- Fonction importantWords -> Paramètres : `matrice` -> **liste** et `wordsList` -> **liste**. Retourne _betterWords_ (**liste**) la liste de(s) mot(s) ayant le TF-IDF le plus élevé de la liste `matrice`.

- Fonction listOfWords -> Paramètres : `president` -> **string**, `irrelevants` -> **liste** et `folderAddr` -> **string**. Retourne _relevantUsedWords_ (**liste**) la liste des mots utilisé par un président (sauf les mots ayant un TF-IDF de 0. Voir _irrelevantWords_).

- Fonction mostUsedWords -> Paramètres : `president` -> **string**, `irrelevants` -> **liste** et `folderAddr` -> **string**. Retourne _mostUsedWords_ (**liste**) la liste des mots les plus utilisés par un président.

- Fonction whoTalkAbout -> Paramètres : `word` -> **string**, `irrelevants` -> **liste** et `folderAddr` -> **string**. Retourne _hasTalkAbout_ le(s) nom(s) du/des président(s) qui a/ont parlé(s) du mot `word` ainsi que le nom du président qui l'a dit le plus.

- Fonction firstToSay -> Paramètres : `words` -> **list**, `irrelevants` -> **liste** et `folderAddr` -> **string**. Retourne _president_ le(s) nom(s) du/des président(s) qui a/ont parlé(s) en premier du/des mots `words`. Sinon, il renvoie "Nobody talked about this word or maybe it's an irrelevant one...".

- Fonction universalWords -> Paramètres : `wordsList` -> **list**, `irrelevants` -> **liste** et `folderAddr` -> **string**. Retourne _universals_ le(s) mot(s) utilisé(s) par tous les présidents. Sinon il renvoie "No important word has been used by all the presidents.".
