#!/usr/bin/env python3
"""
Calculatrice Scientifique en Python

Ce module démontre la programmation orientée objet en Python
avec une calculatrice scientifique complète.
"""

import math
from typing import List, Tuple, Optional, Union
from datetime import datetime


class Calculator:
    """
    Une calculatrice scientifique avec historique des opérations.
    
    Attributs:
        memory (float): Valeur stockée en mémoire
        history (List[Tuple]): Historique des calculs
        precision (int): Nombre de décimales pour l'affichage
    """
    
    def __init__(self, precision: int = 10):
        """
        Initialise la calculatrice.
        
        Args:
            precision: Nombre de décimales pour les résultats (défaut: 10)
        """
        self.memory: float = 0.0
        self.history: List[Tuple[str, float, datetime]] = []
        self.precision: int = precision
    
    def _add_to_history(self, operation: str, result: float) -> None:
        """Ajoute une opération à l'historique."""
        self.history.append((operation, result, datetime.now()))
    
    def _format_result(self, value: float) -> float:
        """Formate le résultat selon la précision définie."""
        return round(value, self.precision)
    
    # ==================== Opérations de base ====================
    
    def add(self, a: float, b: float) -> float:
        """Addition de deux nombres."""
        result = self._format_result(a + b)
        self._add_to_history(f"{a} + {b}", result)
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Soustraction de deux nombres."""
        result = self._format_result(a - b)
        self._add_to_history(f"{a} - {b}", result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiplication de deux nombres."""
        result = self._format_result(a * b)
        self._add_to_history(f"{a} × {b}", result)
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        Division de deux nombres.
        
        Raises:
            ValueError: Si le diviseur est zéro
        """
        if b == 0:
            raise ValueError("Division par zéro impossible")
        result = self._format_result(a / b)
        self._add_to_history(f"{a} ÷ {b}", result)
        return result
    
    def modulo(self, a: float, b: float) -> float:
        """Reste de la division (modulo)."""
        if b == 0:
            raise ValueError("Modulo par zéro impossible")
        result = self._format_result(a % b)
        self._add_to_history(f"{a} mod {b}", result)
        return result
    
    # ==================== Puissances et racines ====================
    
    def power(self, base: float, exponent: float) -> float:
        """Élève un nombre à une puissance."""
        result = self._format_result(base ** exponent)
        self._add_to_history(f"{base}^{exponent}", result)
        return result
    
    def square(self, x: float) -> float:
        """Calcule le carré d'un nombre."""
        return self.power(x, 2)
    
    def cube(self, x: float) -> float:
        """Calcule le cube d'un nombre."""
        return self.power(x, 3)
    
    def sqrt(self, x: float) -> float:
        """
        Calcule la racine carrée.
        
        Raises:
            ValueError: Si le nombre est négatif
        """
        if x < 0:
            raise ValueError("Racine carrée d'un nombre négatif impossible")
        result = self._format_result(math.sqrt(x))
        self._add_to_history(f"√{x}", result)
        return result
    
    def nth_root(self, x: float, n: float) -> float:
        """Calcule la racine n-ième d'un nombre."""
        if x < 0 and n % 2 == 0:
            raise ValueError("Racine paire d'un nombre négatif impossible")
        result = self._format_result(x ** (1/n))
        self._add_to_history(f"{n}√{x}", result)
        return result
    
    # ==================== Fonctions trigonométriques ====================
    
    def sin(self, x: float, degrees: bool = False) -> float:
        """Calcule le sinus."""
        angle = math.radians(x) if degrees else x
        result = self._format_result(math.sin(angle))
        unit = "°" if degrees else " rad"
        self._add_to_history(f"sin({x}{unit})", result)
        return result
    
    def cos(self, x: float, degrees: bool = False) -> float:
        """Calcule le cosinus."""
        angle = math.radians(x) if degrees else x
        result = self._format_result(math.cos(angle))
        unit = "°" if degrees else " rad"
        self._add_to_history(f"cos({x}{unit})", result)
        return result
    
    def tan(self, x: float, degrees: bool = False) -> float:
        """Calcule la tangente."""
        angle = math.radians(x) if degrees else x
        result = self._format_result(math.tan(angle))
        unit = "°" if degrees else " rad"
        self._add_to_history(f"tan({x}{unit})", result)
        return result
    
    def asin(self, x: float, degrees: bool = False) -> float:
        """Calcule l'arc sinus."""
        if x < -1 or x > 1:
            raise ValueError("Arc sinus défini uniquement sur [-1, 1]")
        result = math.asin(x)
        if degrees:
            result = math.degrees(result)
        result = self._format_result(result)
        self._add_to_history(f"asin({x})", result)
        return result
    
    def acos(self, x: float, degrees: bool = False) -> float:
        """Calcule l'arc cosinus."""
        if x < -1 or x > 1:
            raise ValueError("Arc cosinus défini uniquement sur [-1, 1]")
        result = math.acos(x)
        if degrees:
            result = math.degrees(result)
        result = self._format_result(result)
        self._add_to_history(f"acos({x})", result)
        return result
    
    def atan(self, x: float, degrees: bool = False) -> float:
        """Calcule l'arc tangente."""
        result = math.atan(x)
        if degrees:
            result = math.degrees(result)
        result = self._format_result(result)
        self._add_to_history(f"atan({x})", result)
        return result
    
    # ==================== Logarithmes et exponentielles ====================
    
    def log(self, x: float, base: float = 10) -> float:
        """Calcule le logarithme."""
        if x <= 0:
            raise ValueError("Logarithme défini uniquement pour x > 0")
        if base <= 0 or base == 1:
            raise ValueError("Base du logarithme invalide")
        result = self._format_result(math.log(x, base))
        self._add_to_history(f"log_{base}({x})", result)
        return result
    
    def ln(self, x: float) -> float:
        """Calcule le logarithme naturel."""
        if x <= 0:
            raise ValueError("Logarithme naturel défini uniquement pour x > 0")
        result = self._format_result(math.log(x))
        self._add_to_history(f"ln({x})", result)
        return result
    
    def exp(self, x: float) -> float:
        """Calcule l'exponentielle."""
        result = self._format_result(math.exp(x))
        self._add_to_history(f"e^{x}", result)
        return result
    
    # ==================== Fonctions statistiques ====================
    
    def factorial(self, n: int) -> int:
        """Calcule la factorielle."""
        if n < 0:
            raise ValueError("Factorielle définie uniquement pour n >= 0")
        if not isinstance(n, int):
            raise TypeError("La factorielle nécessite un entier")
        result = math.factorial(n)
        self._add_to_history(f"{n}!", result)
        return result
    
    def permutation(self, n: int, r: int) -> int:
        """Calcule le nombre de permutations P(n,r)."""
        if n < 0 or r < 0:
            raise ValueError("n et r doivent être positifs")
        if r > n:
            raise ValueError("r ne peut pas être supérieur à n")
        result = math.factorial(n) // math.factorial(n - r)
        self._add_to_history(f"P({n},{r})", result)
        return result
    
    def combination(self, n: int, r: int) -> int:
        """Calcule le nombre de combinaisons C(n,r)."""
        if n < 0 or r < 0:
            raise ValueError("n et r doivent être positifs")
        if r > n:
            raise ValueError("r ne peut pas être supérieur à n")
        result = math.comb(n, r)
        self._add_to_history(f"C({n},{r})", result)
        return result
    
    def mean(self, numbers: List[float]) -> float:
        """Calcule la moyenne."""
        if not numbers:
            raise ValueError("La liste ne peut pas être vide")
        result = self._format_result(sum(numbers) / len(numbers))
        self._add_to_history(f"moyenne({numbers})", result)
        return result
    
    def std_dev(self, numbers: List[float]) -> float:
        """Calcule l'écart-type."""
        if len(numbers) < 2:
            raise ValueError("Au moins 2 valeurs requises")
        avg = sum(numbers) / len(numbers)
        variance = sum((x - avg) ** 2 for x in numbers) / (len(numbers) - 1)
        result = self._format_result(math.sqrt(variance))
        self._add_to_history(f"écart-type({numbers})", result)
        return result
    
    # ==================== Constantes ====================
    
    @property
    def pi(self) -> float:
        """Retourne la valeur de π."""
        return math.pi
    
    @property
    def e(self) -> float:
        """Retourne la valeur de e."""
        return math.e
    
    @property
    def tau(self) -> float:
        """Retourne la valeur de τ (2π)."""
        return math.tau
    
    # ==================== Gestion de la mémoire ====================
    
    def memory_store(self, value: float) -> None:
        """Stocke une valeur en mémoire."""
        self.memory = value
    
    def memory_recall(self) -> float:
        """Rappelle la valeur en mémoire."""
        return self.memory
    
    def memory_clear(self) -> None:
        """Efface la mémoire."""
        self.memory = 0.0
    
    def memory_add(self, value: float) -> None:
        """Ajoute une valeur à la mémoire."""
        self.memory += value
    
    # ==================== Historique ====================
    
    def get_history(self, limit: Optional[int] = None) -> List[Tuple[str, float, datetime]]:
        """
        Retourne l'historique des calculs.
        
        Args:
            limit: Nombre maximum d'entrées à retourner (None = tout)
        """
        if limit:
            return self.history[-limit:]
        return self.history
    
    def clear_history(self) -> None:
        """Efface l'historique."""
        self.history = []
    
    def print_history(self, limit: Optional[int] = 10) -> None:
        """Affiche l'historique formaté."""
        history = self.get_history(limit)
        if not history:
            print("Historique vide")
            return
        
        print("\n" + "=" * 50)
        print("HISTORIQUE DES CALCULS")
        print("=" * 50)
        for operation, result, timestamp in history:
            time_str = timestamp.strftime("%H:%M:%S")
            print(f"[{time_str}] {operation} = {result}")
        print("=" * 50 + "\n")


def interactive_mode():
    """Mode interactif de la calculatrice."""
    calc = Calculator()
    
    print("\n" + "=" * 60)
    print("   CALCULATRICE SCIENTIFIQUE PYTHON")
    print("=" * 60)
    print("Commandes disponibles:")
    print("  +, -, *, /     : Opérations de base")
    print("  sqrt, pow      : Racine et puissance")
    print("  sin, cos, tan  : Trigonométrie")
    print("  log, ln, exp   : Logarithmes")
    print("  history        : Afficher l'historique")
    print("  help           : Afficher l'aide")
    print("  quit           : Quitter")
    print("=" * 60 + "\n")
    
    while True:
        try:
            user_input = input("calc> ").strip().lower()
            
            if user_input in ('quit', 'exit', 'q'):
                print("Au revoir !")
                break
            elif user_input == 'history':
                calc.print_history()
            elif user_input == 'help':
                print("Aide : entrez une opération comme '5 + 3' ou 'sqrt 16'")
            elif user_input == 'pi':
                print(f"π = {calc.pi}")
            elif user_input == 'e':
                print(f"e = {calc.e}")
            elif not user_input:
                continue
            else:
                # Parsing simple pour démonstration
                parts = user_input.split()
                
                if len(parts) == 3:
                    a, op, b = parts
                    a, b = float(a), float(b)
                    
                    operations = {
                        '+': calc.add,
                        '-': calc.subtract,
                        '*': calc.multiply,
                        '/': calc.divide,
                        '^': calc.power,
                        'mod': calc.modulo,
                    }
                    
                    if op in operations:
                        result = operations[op](a, b)
                        print(f"= {result}")
                    else:
                        print(f"Opérateur inconnu: {op}")
                        
                elif len(parts) == 2:
                    op, x = parts
                    x = float(x)
                    
                    unary_ops = {
                        'sqrt': calc.sqrt,
                        'sin': lambda v: calc.sin(v, degrees=True),
                        'cos': lambda v: calc.cos(v, degrees=True),
                        'tan': lambda v: calc.tan(v, degrees=True),
                        'log': calc.log,
                        'ln': calc.ln,
                        'exp': calc.exp,
                    }
                    
                    if op in unary_ops:
                        result = unary_ops[op](x)
                        print(f"= {result}")
                    else:
                        print(f"Fonction inconnue: {op}")
                else:
                    print("Format invalide. Utilisez 'a op b' ou 'fonction x'")
                    
        except ValueError as e:
            print(f"Erreur: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nAu revoir !")
            break


def demo():
    """Démonstration des fonctionnalités de la calculatrice."""
    calc = Calculator()
    
    print("\n" + "=" * 60)
    print("   DÉMONSTRATION DE LA CALCULATRICE SCIENTIFIQUE")
    print("=" * 60)
    
    # Opérations de base
    print("\n--- Opérations de base ---")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    print(f"10 ÷ 5 = {calc.divide(10, 5)}")
    
    # Puissances et racines
    print("\n--- Puissances et racines ---")
    print(f"2^10 = {calc.power(2, 10)}")
    print(f"√144 = {calc.sqrt(144)}")
    print(f"3√27 = {calc.nth_root(27, 3)}")
    
    # Trigonométrie
    print("\n--- Trigonométrie (en degrés) ---")
    print(f"sin(30°) = {calc.sin(30, degrees=True)}")
    print(f"cos(60°) = {calc.cos(60, degrees=True)}")
    print(f"tan(45°) = {calc.tan(45, degrees=True)}")
    
    # Logarithmes
    print("\n--- Logarithmes ---")
    print(f"log₁₀(100) = {calc.log(100)}")
    print(f"ln(e) = {calc.ln(calc.e)}")
    print(f"e^2 = {calc.exp(2)}")
    
    # Statistiques
    print("\n--- Statistiques ---")
    data = [10, 20, 30, 40, 50]
    print(f"Données: {data}")
    print(f"Moyenne = {calc.mean(data)}")
    print(f"Écart-type = {calc.std_dev(data)}")
    
    # Combinatoire
    print("\n--- Combinatoire ---")
    print(f"5! = {calc.factorial(5)}")
    print(f"P(5,3) = {calc.permutation(5, 3)}")
    print(f"C(5,3) = {calc.combination(5, 3)}")
    
    # Constantes
    print("\n--- Constantes ---")
    print(f"π = {calc.pi}")
    print(f"e = {calc.e}")
    print(f"τ = {calc.tau}")
    
    # Historique
    calc.print_history(5)
    
    print("=" * 60 + "\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        demo()
