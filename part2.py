def tokenQuestion(question: str):
    question = (
        question.replace("?", "")
        .replace(".", "")
        .replace(";", "")
        .replace(",", "")
        .replace(":", "")
        .replace("!", "")
        .replace("-", " ")
        .replace("'", " ")
        .replace('"', " ")
    )
    question = question.lower()
    return list(set(question.split()))


print(
    tokenQuestion(
        "Quelle est la capitale de la France ? , et vous; . êtes-vous vous mêê ?./:!"
    )
)
