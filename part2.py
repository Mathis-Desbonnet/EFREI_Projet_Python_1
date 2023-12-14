import os


def tokenQuestion(question: str):
    question = (
        question.replace("?", "")
        .replace(".", "")
        .replace(";", "")
        .replace(",", "")
        .replace(":", "")
        .replace("!", "")
        .replace("/", "")
        .replace("-", " ")
        .replace("'", " ")
        .replace('"', " ")
    )
    question = question.lower()
    return list(set(question.split()))


def searchInteristingTerms(question: list, folderAddr: str):
    files = os.listdir(folderAddr)
    allWords = []
    for _ in files:
        text = open(folderAddr + _, "r").read()
        allWords += text.split()
        allWords = list(set(allWords))

    interistingWord = []
    for word in question:
        if word in allWords:
            interistingWord.append(word)
    return interistingWord


print(
    tokenQuestion(
        "Quelle est la capitale de la France ? , et vous; . êtes-vous vous mêê ?./:!"
    )
)

print(
    searchInteristingTerms(
        tokenQuestion(
            "Quelle est la capitale de la France ? , et vous; . êtes-vous vous mêê ?./:!"
        ),
        "./cleaned/",
    )
)
