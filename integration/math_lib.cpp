/**
 * @file math_lib.cpp
 * @brief Bibliothèque C++ pour l'intégration avec Python via ctypes
 *
 * Cette bibliothèque fournit des fonctions mathématiques qui peuvent
 * être appelées depuis Python en utilisant ctypes.
 *
 * Compilation:
 *   g++ -shared -fPIC -o math_lib.so math_lib.cpp
 *
 * Utilisation depuis Python:
 *   import ctypes
 *   lib = ctypes.CDLL('./math_lib.so')
 *   lib.addition.argtypes = [ctypes.c_double, ctypes.c_double]
 *   lib.addition.restype = ctypes.c_double
 *   result = lib.addition(5.0, 3.0)
 */

#include <cmath>

// Macro pour exporter les fonctions en C (évite le name mangling C++)
extern "C" {

/**
 * @brief Additionne deux nombres
 * @param a Premier nombre
 * @param b Deuxième nombre
 * @return Somme des deux nombres
 */
double addition(double a, double b) {
    return a + b;
}

/**
 * @brief Soustrait deux nombres
 * @param a Premier nombre
 * @param b Deuxième nombre
 * @return Différence des deux nombres
 */
double soustraction(double a, double b) {
    return a - b;
}

/**
 * @brief Multiplie deux nombres
 * @param a Premier nombre
 * @param b Deuxième nombre
 * @return Produit des deux nombres
 */
double multiplication(double a, double b) {
    return a * b;
}

/**
 * @brief Divise deux nombres
 * @param a Numérateur
 * @param b Dénominateur
 * @return Quotient de la division (retourne NaN si b est 0)
 */
double division(double a, double b) {
    if (b == 0) {
        return std::nan("");  // Retourne NaN pour indiquer une erreur
    }
    return a / b;
}

/**
 * @brief Calcule la puissance d'un nombre
 * @param base Base
 * @param exposant Exposant
 * @return base^exposant
 */
double puissance(double base, int exposant) {
    return std::pow(base, exposant);
}

/**
 * @brief Calcule la racine carrée d'un nombre
 * @param n Nombre positif
 * @return Racine carrée de n (retourne NaN si n est négatif)
 */
double racine_carree(double n) {
    if (n < 0) {
        return std::nan("");  // Retourne NaN pour indiquer une erreur
    }
    return std::sqrt(n);
}

/**
 * @brief Calcule la factorielle d'un nombre
 * @param n Nombre entier positif
 * @return Factorielle de n (retourne 0 si n est négatif pour indiquer une erreur)
 */
unsigned long long factorielle(int n) {
    if (n < 0) {
        return 0;  // Retourne 0 pour indiquer une erreur (factorielle n'est jamais 0 pour n >= 0)
    }
    if (n == 0 || n == 1) {
        return 1;
    }
    unsigned long long resultat = 1;
    for (int i = 2; i <= n; ++i) {
        resultat *= i;
    }
    return resultat;
}

/**
 * @brief Vérifie si un nombre est premier
 * @param n Nombre à vérifier
 * @return true (1) si le nombre est premier, false (0) sinon
 */
bool est_premier(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

/**
 * @brief Calcule le PGCD de deux nombres
 * @param a Premier nombre
 * @param b Deuxième nombre
 * @return PGCD de a et b
 */
int pgcd(int a, int b) {
    a = std::abs(a);
    b = std::abs(b);
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

/**
 * @brief Calcule le PPCM de deux nombres
 * @param a Premier nombre
 * @param b Deuxième nombre
 * @return PPCM de a et b
 */
int ppcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return std::abs(a * b) / pgcd(a, b);
}

}  // extern "C"
