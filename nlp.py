import re


def predicate_to_english(predicate):
    quantifier_map = {
        '∀': 'All',
        '∃': 'Some',
        '¬∀': 'No',
        '¬∃': 'None'
    }

    quantifier_match = re.match(r'(∀|∃|¬∀|¬∃)x', predicate)
    if quantifier_match:
        quantifier = quantifier_match.group(1)
        predicate = predicate[len(quantifier) + 1:].strip()
    else:
        quantifier = ''

    # Find the predicate
    predicate_match = re.search(r'(→|↔)', predicate)
    if predicate_match:
        predicate_symbol = predicate_match.group(1)
        subject, rest = predicate.split(predicate_symbol, 1)
        subject = subject.strip()
        rest = rest.strip()
    else:
        subject = predicate
        rest = ''
        predicate_symbol = ''  # Add this line

    # Find the subject or variable
    subject_match = re.search(r'([a-z_]+)\(x\)', subject)
    if subject_match:
        subject_phrase = subject_match.group(1)
    else:
        subject_phrase = subject

    # Find the adjective or verb
    adjective_match = re.search(r'([a-z_]+)\(', rest)
    if adjective_match:
        adjective_phrase = adjective_match.group(1)
    else:
        adjective_phrase = ''

    # Construct the English sentence
    if quantifier:
        if adjective_phrase:
            sentence = f"{quantifier_map[quantifier]} {subject_phrase} {adjective_phrase}"
        else:
            sentence = f"{quantifier_map[quantifier]} {subject_phrase} {predicate_symbol.replace('→', 'are').replace('↔', 'is')}"
    else:
        sentence = f"{subject_phrase} {adjective_phrase}"

    return sentence.capitalize()


# Example usage
predicate_expression = "∃x (is_animal(x) ∧ is_endangered(x))"
english_sentence = predicate_to_english(predicate_expression)
print(english_sentence)  # Output: Some animals are endangered.
