"""
Calculatrice Python - Module de démonstration.

Ce module contient des fonctions mathématiques de base
démontrant les capacités du langage Python.
"""

import math
from typing import Union

Number = Union[int, float]


def addition(a: Number, b: Number) -> Number:
    """
    Additionne deux nombres.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        Somme des deux nombres
    """
    return a + b


def soustraction(a: Number, b: Number) -> Number:
    """
    Soustrait deux nombres.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        Différence des deux nombres
    """
    return a - b


def multiplication(a: Number, b: Number) -> Number:
    """
    Multiplie deux nombres.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        Produit des deux nombres
    """
    return a * b


def division(a: Number, b: Number) -> float:
    """
    Divise deux nombres.

    Args:
        a: Numérateur
        b: Dénominateur

    Returns:
        Quotient de la division

    Raises:
        ValueError: Si b est égal à 0
    """
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


def puissance(base: Number, exposant: int) -> Number:
    """
    Calcule la puissance d'un nombre.

    Args:
        base: Base
        exposant: Exposant

    Returns:
        base^exposant
    """
    return base ** exposant


def racine_carree(n: Number) -> float:
    """
    Calcule la racine carrée d'un nombre.

    Args:
        n: Nombre positif

    Returns:
        Racine carrée de n

    Raises:
        ValueError: Si n est négatif
    """
    if n < 0:
        raise ValueError("La racine carrée n'est pas définie pour les nombres négatifs")
    return math.sqrt(n)


def factorielle(n: int) -> int:
    """
    Calcule la factorielle d'un nombre.

    Args:
        n: Nombre entier positif

    Returns:
        Factorielle de n

    Raises:
        ValueError: Si n est négatif
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs")
    return math.factorial(n)


def est_premier(n: int) -> bool:
    """
    Vérifie si un nombre est premier.

    Args:
        n: Nombre à vérifier

    Returns:
        True si le nombre est premier, False sinon
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def moyenne(nombres: list[Number]) -> float:
    """
    Calcule la moyenne d'une liste de nombres.

    Args:
        nombres: Liste de nombres

    Returns:
        Moyenne des nombres

    Raises:
        ValueError: Si la liste est vide
    """
    if not nombres:
        raise ValueError("La liste ne peut pas être vide")
    return sum(nombres) / len(nombres)


def pgcd(a: int, b: int) -> int:
    """
    Calcule le Plus Grand Commun Diviseur (PGCD) de deux nombres.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        PGCD de a et b
    """
    return math.gcd(a, b)


def ppcm(a: int, b: int) -> int:
    """
    Calcule le Plus Petit Commun Multiple (PPCM) de deux nombres.

    Args:
        a: Premier nombre
        b: Deuxième nombre

    Returns:
        PPCM de a et b
    """
    return abs(a * b) // math.gcd(a, b)


def main():
    """Fonction principale - démonstration des opérations."""
    print("=== Démonstration de la Calculatrice Python ===\n")

    a, b = 10, 3

    print(f"Avec a = {a} et b = {b}:")
    print(f"Addition: {a} + {b} = {addition(a, b)}")
    print(f"Soustraction: {a} - {b} = {soustraction(a, b)}")
    print(f"Multiplication: {a} * {b} = {multiplication(a, b)}")
    print(f"Division: {a} / {b} = {division(a, b):.2f}")
    print()

    n = 5
    print(f"Factorielle de {n} = {factorielle(n)}")
    print()

    print("Nombres premiers de 1 à 20:", end=" ")
    premiers = [i for i in range(1, 21) if est_premier(i)]
    print(" ".join(map(str, premiers)))
    print()

    print(f"Puissance: 2^8 = {puissance(2, 8)}")
    print(f"Racine carrée de 16 = {racine_carree(16)}")
    print()

    nombres = [1, 2, 3, 4, 5]
    print(f"Moyenne de {nombres} = {moyenne(nombres)}")
    print(f"PGCD de 12 et 18 = {pgcd(12, 18)}")
    print(f"PPCM de 12 et 18 = {ppcm(12, 18)}")


if __name__ == "__main__":
    main()
