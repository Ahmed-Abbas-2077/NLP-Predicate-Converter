# NLP-Predicate Converter

## Overview
The **NLP-Predicate Converter** is a Python-based tool designed to bridge natural language and predicate logic. It allows users to seamlessly convert English sentences into predicate logic expressions and vice versa, enabling applications in computational linguistics, formal logic education, and AI systems requiring reasoning capabilities.

This project was developed as part of the **Knowledge Representation and Reasoning (DSAI 104)** course.

---

## Features
- **English to Predicate Logic Conversion**:
  - Parses sentences using SpaCy's NLP model.
  - Identifies quantifiers, subjects, verbs, adjectives, and objects to generate formal predicate logic expressions.
- **Predicate Logic to English Conversion**:
  - Translates predicate logic expressions back into natural English.
  - Handles universal $\forall$ and existential $\exists$ quantifiers, negations $\neg$, and logical operators $\wedge$, $\vee$, $\rightarrow$.
- **Interactive Command-line Interface**:
  - Allows users to input English sentences or predicate logic expressions for real-time conversion.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ahmed-Abbas-2077/NLP-Predicate-Converter.git
   cd NLP-Predicate-Converter
   ```

2. **Download SpaCy Model**:
   Download the SpaCy English language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

---

## Usage

### Run the Converter
1. **English to Predicate Logic**:
   ```bash
   python Eng2Pred.py
   ```
   - Enter sentences like:
     - `All dogs are loyal.`
     - `Some politicians are corrupt.`

2. **Predicate Logic to English**:
   ```bash
   python Pred2Eng.py
   ```
   - Enter predicate expressions like:
     - `∀x (is_human(x) → is_mortal(x))`
     - `∃x (is_animal(x) ∧ is_endangered(x))`

---

## Examples

### Input (English to Predicate Logic)
```
All dogs are loyal.
```

### Output
```
∀x (is_dog(x) → is_loyal(x))
```

### Input (Predicate Logic to English)
```
∃x (is_animal(x) ∧ is_endangered(x))
```

### Output
```
Some animals are endangered.
```

---

## File Structure

- `nlp.py`: Shared utilities for handling predicates and conversions.
- `Eng2Pred.py`: Converts English sentences into predicate logic.
- `Pred2Eng.py`: Converts predicate logic into English sentences.
