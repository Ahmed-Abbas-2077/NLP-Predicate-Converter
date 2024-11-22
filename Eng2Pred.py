# pip install spacy
import spacy  # dah spacy, el model beta3t el NLP ely 3ayz a3ml beh el conversion

nlp = spacy.load("en_core_web_sm")  # load el model beta3t el english language


def English2Predicate(sentence):
    # hena ba3mel pass lel sentence
    doc = nlp(sentence)

    # dah dictionary 3ashan a3raf el quantifier
    quantifier_map = {
        "all": "∀x", "every": "∀x", "each": "∀x",
        "some": "∃x", "a": "∃x", "an": "∃x",
        "no": "¬∃x", "none": "¬∃x"
    }

    # hena ba3mel initialize lel variables
    quantifier = ""
    subject = ""
    verb = ""
    obj = ""
    adj = ""
    subAdj = ""
    objAdj = ""
    adverb = ""
    connector = ""
    negation = ""
    negVerb = ""
    predicate = ""

    # hena ba3mel loop 3ala el tokens beta3t el sentence w a3raf el part of speech beta3t kol token
    for token in doc:
        if token.dep_ == "nsubj" and not subject:
            subject = token.lemma_
        elif token.dep_ == "pobj" and subject:
            subject = token.lemma_
        elif token.dep_ == "ROOT" and not verb:
            verb = token.lemma_
        elif token.dep_ == "dobj" and not obj:
            obj = token.lemma_
        elif token.dep_ == "acomp" and not adj:
            adj = token.lemma_
        elif (token.dep_ == "amod" or token.dep_ == "compound") and not subAdj:
            subAdj = token.lemma_
        elif token.dep_ == "amod" and not objAdj:
            objAdj = token.lemma_
        elif token.dep_ == "advmod" and not adverb:
            adverb = token.lemma_
        elif token.dep_ == "cc" and not connector:
            connector = token.text
        elif token.dep_ == "neg" and not quantifier:
            negation = "¬"
        elif token.dep_ == "neg" and verb:
            negVerb = "¬"

        # dah check 3ala el quantifier
        if token.text.lower() in quantifier_map and not quantifier:
            quantifier = quantifier_map[token.text.lower()]

    # hena ba3mel check 3ala el object w a3mel el conversion
    if obj:
        print("obj", obj)
        if quantifier == "∀x":
            predicate = f"{negation}{quantifier} ({subAdj}{subject}(x) → {negVerb}{verb}_{objAdj}{obj}(x))"
        else:
            predicate = f"{negation}{quantifier} ({subAdj}{subject}(x) ^ {negVerb}{verb}_{objAdj}{obj}(x))"

    # hena ba3mel check 3ala el adjective w adefo lel predicate
    elif adj:
        print("adj", adj)
        if quantifier == "∀x":
            predicate = f"{negation}{quantifier} ({subAdj}{subject}(x) → {negVerb}{adverb}{adj}(x))"
        else:
            predicate = f"{negation}{quantifier} ({subAdj}{subject}(x) ^ {negVerb}{adverb}{adj}(x))"

    # hena ba3mel check 3ala el verb bas
    elif verb:
        print("verb", verb)
        if quantifier == "∀x":
            predicate = f"{negation}{quantifier} ({subAdj}{subject}(x) → {negVerb}{verb}{adverb}(x))"
        else:
            predicate = f"{negation}{quantifier} ({subAdj}{subject}(x) ^ {negVerb}{verb}{adverb}(x))"

    return predicate


# sentences = [
#     "All dogs are loyal.",
#     "Every cat is cute.",
#     "Each person is unique.",
#     "Some birds can fly.",
#     "Not all congressmen are honest.",
#     "No politicians are trustworthy.",
#     "None of the students are failing.",
#     "Some celebrities are not famous.",
#     "Some smart students are not very successful.",
#     "Each of the athletes runs quickly.",
# ]

# for sentence in sentences:
#     print(f"{sentence} :", English2Predicate(sentence))
#     print("--------------------")


# dah shapah el function beta3t el userPrompt fe Pred2Eng.py
def userPrompt():
    try:
        sentence = input("Enter a sentence to convert to predicate logic: ")
        print(English2Predicate(sentence))
    except:
        print("Error occurred. Please try again.")
        userPrompt()


# example: "All dogs are loyal."
userPrompt()
