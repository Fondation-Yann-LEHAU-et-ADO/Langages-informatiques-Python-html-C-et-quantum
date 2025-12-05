# Langages Informatiques: Python, HTML, C++ et Quantum

Ce projet démontre l'interopérabilité entre différents langages de programmation: **Python**, **HTML**, et **C++**.

## Structure du Projet

```
├── README.md                   # Documentation du projet
├── cpp/                        # Exemples C++
│   └── math_operations.cpp     # Opérations mathématiques en C++
├── html/                       # Exemples HTML
│   └── index.html              # Page HTML simple
├── python/                     # Exemples Python
│   └── calculator.py           # Calculatrice en Python
└── integration/                # Intégration des langages
    ├── app.py                  # Application Flask
    ├── math_lib.cpp            # Bibliothèque C++ pour l'intégration
    └── templates/
        └── index.html          # Template HTML pour Flask
```

## Exemples par Langage

### C++ (`cpp/math_operations.cpp`)

Un exemple d'opérations mathématiques de base en C++ incluant:
- Addition, soustraction, multiplication, division
- Factorielle
- Vérification de nombre premier

### HTML (`html/index.html`)

Une page HTML simple démontrant:
- Structure HTML5
- Styles CSS inline
- Calculatrice basique en JavaScript

### Python (`python/calculator.py`)

Un module de calculatrice Python avec:
- Opérations arithmétiques
- Calculs de puissance et racine carrée
- Fonctions utilitaires

## Application d'Intégration

Le dossier `integration/` contient une application Flask qui démontre l'interopérabilité entre:
- **Python** (Flask backend)
- **HTML** (Templates Jinja2)
- **C++** (Bibliothèque mathématique compilée avec ctypes)

### Lancer l'Application Flask

```bash
cd integration
pip install flask
python app.py
```

L'application sera accessible à `http://localhost:5000`

### Compiler la Bibliothèque C++

```bash
cd integration
g++ -shared -fPIC -o math_lib.so math_lib.cpp
```

## Prérequis

- Python 3.x
- Flask (`pip install flask`)
- Compilateur C++ (g++ ou clang++)
- Navigateur web moderne

## Auteur

Fondation Yann LEHAU et ADO

## Licence

Ce projet est sous licence MIT.
