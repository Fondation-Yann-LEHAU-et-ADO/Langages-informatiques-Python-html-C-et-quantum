/**
 * @file math_operations.cpp
 * @brief Démonstration d'opérations mathématiques en C++
 *
 * Ce fichier contient des exemples de fonctions mathématiques
 * démontrant les capacités du langage C++.
 */

#include <iostream>
#include <cmath>
#include <stdexcept>

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
 * @return Quotient de la division
 * @throws std::invalid_argument si b est égal à 0
 */
double division(double a, double b) {
    if (b == 0) {
        throw std::invalid_argument("Division par zéro impossible");
    }
    return a / b;
}

/**
 * @brief Calcule la factorielle d'un nombre
 * @param n Nombre entier positif
 * @return Factorielle de n
 * @throws std::invalid_argument si n est négatif
 */
unsigned long long factorielle(int n) {
    if (n < 0) {
        throw std::invalid_argument("La factorielle n'est pas définie pour les nombres négatifs");
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
 * @return true si le nombre est premier, false sinon
 */
bool estPremier(int n) {
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
 * @return Racine carrée de n
 * @throws std::invalid_argument si n est négatif
 */
double racineCarree(double n) {
    if (n < 0) {
        throw std::invalid_argument("La racine carrée n'est pas définie pour les nombres négatifs");
    }
    return std::sqrt(n);
}

/**
 * @brief Fonction principale - démonstration des opérations
 */
int main() {
    std::cout << "=== Démonstration des Opérations Mathématiques en C++ ===" << std::endl;
    std::cout << std::endl;

    double a = 10.0, b = 3.0;

    std::cout << "Avec a = " << a << " et b = " << b << ":" << std::endl;
    std::cout << "Addition: " << a << " + " << b << " = " << addition(a, b) << std::endl;
    std::cout << "Soustraction: " << a << " - " << b << " = " << soustraction(a, b) << std::endl;
    std::cout << "Multiplication: " << a << " * " << b << " = " << multiplication(a, b) << std::endl;
    std::cout << "Division: " << a << " / " << b << " = " << division(a, b) << std::endl;
    std::cout << std::endl;

    int n = 5;
    std::cout << "Factorielle de " << n << " = " << factorielle(n) << std::endl;
    std::cout << std::endl;

    std::cout << "Nombres premiers de 1 à 20: ";
    for (int i = 1; i <= 20; ++i) {
        if (estPremier(i)) {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;
    std::cout << std::endl;

    std::cout << "Puissance: 2^8 = " << puissance(2, 8) << std::endl;
    std::cout << "Racine carrée de 16 = " << racineCarree(16) << std::endl;

    return 0;
}
