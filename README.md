# Langages Informatiques : Python, HTML, C++ et Quantum

Ce dépôt rassemble des exemples de code dans différents langages de programmation (Python, HTML, C++) ainsi qu'une application d'intégration qui combine ces trois langages.

## Structure du Projet

```
├── README.md                      # Documentation du projet
├── cpp/
│   └── math_operations.cpp        # Bibliothèque mathématique en C++
├── html/
│   └── index.html                 # Page HTML interactive
├── python/
│   └── calculator.py              # Calculatrice en Python
└── integration/
    ├── app.py                     # Application Flask (Python)
    ├── math_lib.cpp               # Bibliothèque C++ pour l'intégration
    └── templates/
        └── index.html             # Template HTML pour Flask
```

## Exemples de Code

### 1. Python - Calculatrice (`python/calculator.py`)

Une calculatrice simple en Python démontrant les opérations mathématiques de base :
- Addition, soustraction, multiplication, division
- Puissance et racine carrée
- Interface en ligne de commande

**Exécution :**
```bash
python python/calculator.py
```

### 2. C++ - Opérations Mathématiques (`cpp/math_operations.cpp`)

Une bibliothèque C++ pour les opérations mathématiques :
- Factorielle
- Fibonacci
- Vérification de nombres premiers
- Calcul du PGCD et PPCM

**Compilation et exécution :**
```bash
g++ -o math_ops cpp/math_operations.cpp
./math_ops
```

### 3. HTML - Page Interactive (`html/index.html`)

Une page HTML interactive avec :
- Formulaire de saisie
- Affichage dynamique avec JavaScript
- Styles CSS intégrés

**Visualisation :**
Ouvrir `html/index.html` dans un navigateur web.

## Application d'Intégration

Le dossier `integration/` contient une application Flask qui démontre l'intégration des trois langages :

- **Python (Flask)** : Backend web
- **C++ (ctypes)** : Calculs mathématiques performants
- **HTML (Jinja2)** : Interface utilisateur

### Installation

```bash
# Installer les dépendances Python
pip install flask

# Compiler la bibliothèque C++
cd integration
g++ -shared -fPIC -o libmath.so math_lib.cpp
```

### Exécution

```bash
cd integration
python app.py
```

Puis ouvrir http://localhost:5000 dans un navigateur.

## Prérequis

- Python 3.x
- Flask (`pip install flask`)
- GCC/G++ (pour compiler le code C++)
- Un navigateur web moderne

## Licence

Ce projet est destiné à des fins éducatives.

## Auteur

Fondation Yann LEHAU et ADO
