def Predicate2English(predicate):

    # Hena 3ayz a3ml check 3ala el quantifier w a3ml return lel sentence el motabka
    quantifiers = {
        '∀x': 'Everyone',
        '∃x': 'Someone',
        '¬∀x': 'Not everyone',
        '¬∃x': 'No one'}

    text = ""
    predicate = predicate.strip()

    # Ba3mel append lel sentence
    quantifier = predicate.split()[0]
    if quantifier in quantifiers:
        text += quantifiers[quantifier] + ' '

    text += "who "

    # Ba3mel append lel subject we ba check 3ala el negation
    if '¬' in predicate.split()[1]:
        text += predicate.split()[1].split('(')[1].lower().replace('_',
                                                                   ' ').replace('is', 'is not a').replace('¬', '') + ' '
    else:
        text += predicate.split()[1].split(
            '(')[1].lower().replace('_', ' ').replace('is', 'is a') + ' '

    # Ba3mel append lel verb we ba check 3ala el negation
    if '¬' in predicate.split()[3]:
        text += (predicate.split()[3].split('(')[0]
                 ).lower().replace('_', ' ').replace('is', 'is not'). replace('¬', '')
    else:
        text += (predicate.split()[3].split('(')[0]
                 ).lower().replace('_', ' ')

    return text


# sentences = [
#     "∀x (is_human(x) → is_mortal(x))",
#     "∃x (is_human(x) ∧ is_mortal(x))",
#     "¬∀x (is_human(x) → is_mortal(x))",
#     "¬∃x (is_human(x) ∧ is_mortal(x))",
#     "∃x (is_animal(x) ∧ is_endangered(x))",
#     "∀x (is_animal(x) → is_endangered(x))",
#     "¬∀x (is_animal(x) → is_endangered(x))",
#     "¬∃x (is_animal(x) ∧ is_endangered(x))",
#     "∃x (is_politician(x) ∧ is_corrupt(x))",
#     "∀x (is_politician(x) → is_corrupt(x))",
#     "¬∀x (is_politician(x) → ¬is_corrupt(x))",
#     "¬∃x (¬is_politician(x) ∧ is_corrupt(x))",
# ]

# for sentence in sentences:
#     print(Predicate2English(sentence))
#     print("----------------------------------")


# Hena bas2al el user 3ala el predicate w a3ml call lel function
def userPrompt():
    try:
        predicate = input("Enter a predicate: ")
        print(Predicate2English(predicate))
    except:
        print("Invalid input. Please try again.")
        userPrompt()


# Predicate2English("∀x (is_human(x) → is_mortal(x))")
userPrompt()
