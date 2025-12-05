# Langages informatiques - Python, HTML, C++ et Quantum

Ce projet démontre l'utilisation de plusieurs langages de programmation ainsi que leur intégration. Il présente des exemples autonomes pour chaque langage et montre comment les combiner dans une application web interactive.

## Structure du Projet

```
.
├── README.md                  # Ce fichier de documentation
├── html/                      # Exemples HTML/CSS/JavaScript
│   └── index.html            # Page interactive autonome
├── python/                    # Exemples Python
│   └── calculator.py         # Calculatrice scientifique
├── cpp/                       # Exemples C++
│   └── math_operations.cpp   # Opérations mathématiques et STL
└── integration/               # Application intégrée
    ├── app.py                # Backend Flask
    ├── math_lib.cpp          # Librairie C++ partagée
    └── templates/
        └── index.html        # Interface web
```

## Langages Démontrés

### HTML/CSS/JavaScript (`html/`)

Le dossier `html/` contient une page web interactive démontrant :
- Structure HTML5 sémantique
- Styles CSS modernes (Flexbox, animations)
- JavaScript interactif (manipulation du DOM, événements)

**Utilisation :**
Ouvrir `html/index.html` directement dans un navigateur web.

### Python (`python/`)

Le dossier `python/` contient une calculatrice scientifique avec :
- Programmation orientée objet (classe `Calculator`)
- Opérations mathématiques avancées
- Historique des calculs
- Gestion des erreurs

**Utilisation :**
```bash
cd python
python calculator.py
```

### C++ (`cpp/`)

Le dossier `cpp/` démontre :
- Opérations mathématiques de base
- Utilisation de la Standard Template Library (STL)
- Structures de données (vectors, maps)
- Programmation fonctionnelle avec lambdas

**Compilation et exécution :**
```bash
cd cpp
g++ -std=c++17 -o math_operations math_operations.cpp
./math_operations
```

## Application Intégrée (`integration/`)

Le dossier `integration/` présente l'interopérabilité entre les langages :

- **Backend** : Python avec Flask
- **Calculs haute performance** : Librairie C++ (`libmath`)
- **Interface utilisateur** : HTML/CSS/JavaScript

### Compilation de la Librairie C++

```bash
cd integration
g++ -shared -fPIC -o libmath.so math_lib.cpp
```

### Lancement de l'Application

```bash
cd integration
pip install flask
python app.py
```

Puis ouvrir http://localhost:5000 dans un navigateur.

## Prérequis

- **Python** : Version 3.8+
- **C++** : Compilateur supportant C++17 (g++, clang++)
- **Flask** : Pour l'application intégrée (`pip install flask`)
- **Navigateur web** : Pour les exemples HTML et l'interface intégrée

## Licence

Ce projet est à des fins éducatives et de démonstration.

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour améliorer les exemples ou ajouter de nouveaux langages.
