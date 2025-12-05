#!/usr/bin/env python3
"""
Calculatrice en Python

Ce module fournit une calculatrice simple avec des opérations
mathématiques de base et avancées.
"""

import math


def addition(a: float, b: float) -> float:
    """Additionne deux nombres."""
    return a + b


def soustraction(a: float, b: float) -> float:
    """Soustrait b de a."""
    return a - b


def multiplication(a: float, b: float) -> float:
    """Multiplie deux nombres."""
    return a * b


def division(a: float, b: float) -> float:
    """
    Divise a par b.
    
    Raises:
        ValueError: Si b est égal à zéro.
    """
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


def puissance(base: float, exposant: float) -> float:
    """Calcule base élevé à la puissance exposant."""
    return math.pow(base, exposant)


def racine_carree(n: float) -> float:
    """
    Calcule la racine carrée d'un nombre.
    
    Raises:
        ValueError: Si n est négatif.
    """
    if n < 0:
        raise ValueError("Racine carrée d'un nombre négatif impossible")
    return math.sqrt(n)


def factorielle(n: int) -> int:
    """
    Calcule la factorielle d'un nombre entier.
    
    Raises:
        ValueError: Si n est négatif.
    """
    if n < 0:
        raise ValueError("Factorielle d'un nombre négatif impossible")
    return math.factorial(n)


def modulo(a: float, b: float) -> float:
    """
    Calcule le reste de la division de a par b.
    
    Raises:
        ValueError: Si b est égal à zéro.
    """
    if b == 0:
        raise ValueError("Modulo par zéro impossible")
    return a % b


def afficher_menu():
    """Affiche le menu principal de la calculatrice."""
    print("\n" + "=" * 50)
    print("        CALCULATRICE PYTHON")
    print("=" * 50)
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Puissance (^)")
    print("6. Racine carrée (√)")
    print("7. Factorielle (!)")
    print("8. Modulo (%)")
    print("9. Quitter")
    print("=" * 50)


def lire_nombre(prompt: str) -> float:
    """
    Lit un nombre depuis l'entrée utilisateur.
    
    Args:
        prompt: Le message à afficher.
        
    Returns:
        Le nombre entré par l'utilisateur.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")


def lire_entier(prompt: str) -> int:
    """
    Lit un entier depuis l'entrée utilisateur.
    
    Args:
        prompt: Le message à afficher.
        
    Returns:
        L'entier entré par l'utilisateur.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Erreur : Veuillez entrer un entier valide.")


def main():
    """Fonction principale de la calculatrice."""
    print("\nBienvenue dans la calculatrice Python !")
    
    while True:
        afficher_menu()
        
        try:
            choix = input("Votre choix (1-9) : ").strip()
        except EOFError:
            print("\nAu revoir !")
            break
        
        if choix == '9':
            print("\nMerci d'avoir utilisé la calculatrice. Au revoir !")
            break
        
        try:
            if choix == '1':
                a = lire_nombre("Premier nombre : ")
                b = lire_nombre("Deuxième nombre : ")
                resultat = addition(a, b)
                print(f"\n{a} + {b} = {resultat}")
            
            elif choix == '2':
                a = lire_nombre("Premier nombre : ")
                b = lire_nombre("Deuxième nombre : ")
                resultat = soustraction(a, b)
                print(f"\n{a} - {b} = {resultat}")
            
            elif choix == '3':
                a = lire_nombre("Premier nombre : ")
                b = lire_nombre("Deuxième nombre : ")
                resultat = multiplication(a, b)
                print(f"\n{a} × {b} = {resultat}")
            
            elif choix == '4':
                a = lire_nombre("Dividende : ")
                b = lire_nombre("Diviseur : ")
                resultat = division(a, b)
                print(f"\n{a} ÷ {b} = {resultat}")
            
            elif choix == '5':
                base = lire_nombre("Base : ")
                exposant = lire_nombre("Exposant : ")
                resultat = puissance(base, exposant)
                print(f"\n{base} ^ {exposant} = {resultat}")
            
            elif choix == '6':
                n = lire_nombre("Nombre : ")
                resultat = racine_carree(n)
                print(f"\n√{n} = {resultat}")
            
            elif choix == '7':
                n = lire_entier("Nombre entier : ")
                resultat = factorielle(n)
                print(f"\n{n}! = {resultat}")
            
            elif choix == '8':
                a = lire_nombre("Dividende : ")
                b = lire_nombre("Diviseur : ")
                resultat = modulo(a, b)
                print(f"\n{a} % {b} = {resultat}")
            
            else:
                print("\nChoix invalide. Veuillez choisir entre 1 et 9.")
        
        except ValueError as e:
            print(f"\nErreur : {e}")
        except EOFError:
            print("\nAu revoir !")
            break


if __name__ == "__main__":
    main()
