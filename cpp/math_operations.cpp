/**
 * Bibliothèque d'opérations mathématiques en C++
 * 
 * Ce fichier démontre différentes fonctions mathématiques
 * implémentées en C++ : factorielle, Fibonacci, nombres premiers, etc.
 */

#include <iostream>
#include <cmath>
#include <vector>

/**
 * Calcule la factorielle d'un nombre
 * @param n Le nombre dont on veut la factorielle
 * @return n! (n factorielle)
 */
unsigned long long factorielle(int n) {
    if (n < 0) {
        return 0;
    }
    if (n <= 1) {
        return 1;
    }
    unsigned long long resultat = 1;
    for (int i = 2; i <= n; i++) {
        resultat *= i;
    }
    return resultat;
}

/**
 * Calcule le n-ième nombre de Fibonacci
 * @param n L'index dans la suite de Fibonacci
 * @return Le n-ième nombre de Fibonacci
 */
unsigned long long fibonacci(int n) {
    if (n < 0) {
        return 0;
    }
    if (n <= 1) {
        return n;
    }
    unsigned long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        unsigned long long temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

/**
 * Vérifie si un nombre est premier
 * @param n Le nombre à vérifier
 * @return true si n est premier, false sinon
 */
bool estPremier(int n) {
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false;
    }
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

/**
 * Calcule le PGCD (Plus Grand Commun Diviseur) de deux nombres
 * @param a Premier nombre
 * @param b Deuxième nombre
 * @return Le PGCD de a et b
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
 * Calcule le PPCM (Plus Petit Commun Multiple) de deux nombres
 * @param a Premier nombre
 * @param b Deuxième nombre
 * @return Le PPCM de a et b
 */
int ppcm(int a, int b) {
    if (a == 0 || b == 0) {
        return 0;
    }
    return std::abs(a * b) / pgcd(a, b);
}

/**
 * Calcule la puissance d'un nombre
 * @param base La base
 * @param exposant L'exposant
 * @return base^exposant
 */
double puissance(double base, int exposant) {
    return std::pow(base, exposant);
}

/**
 * Affiche les n premiers nombres de Fibonacci
 * @param n Le nombre de termes à afficher
 */
void afficherFibonacci(int n) {
    std::cout << "Les " << n << " premiers nombres de Fibonacci :" << std::endl;
    for (int i = 0; i < n; i++) {
        std::cout << fibonacci(i);
        if (i < n - 1) {
            std::cout << ", ";
        }
    }
    std::cout << std::endl;
}

/**
 * Affiche les nombres premiers jusqu'à n
 * @param n La limite supérieure
 */
void afficherPremiers(int n) {
    std::cout << "Nombres premiers jusqu'a " << n << " :" << std::endl;
    for (int i = 2; i <= n; i++) {
        if (estPremier(i)) {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;
}

int main() {
    std::cout << "=== Bibliotheque d'operations mathematiques en C++ ===" << std::endl;
    std::cout << std::endl;

    // Démonstration de la factorielle
    std::cout << "--- Factorielle ---" << std::endl;
    for (int i = 0; i <= 10; i++) {
        std::cout << i << "! = " << factorielle(i) << std::endl;
    }
    std::cout << std::endl;

    // Démonstration de Fibonacci
    std::cout << "--- Fibonacci ---" << std::endl;
    afficherFibonacci(15);
    std::cout << std::endl;

    // Démonstration des nombres premiers
    std::cout << "--- Nombres premiers ---" << std::endl;
    afficherPremiers(50);
    std::cout << std::endl;

    // Démonstration du PGCD et PPCM
    std::cout << "--- PGCD et PPCM ---" << std::endl;
    int a = 48, b = 18;
    std::cout << "PGCD(" << a << ", " << b << ") = " << pgcd(a, b) << std::endl;
    std::cout << "PPCM(" << a << ", " << b << ") = " << ppcm(a, b) << std::endl;
    std::cout << std::endl;

    // Démonstration de la puissance
    std::cout << "--- Puissance ---" << std::endl;
    std::cout << "2^10 = " << puissance(2, 10) << std::endl;
    std::cout << "3^5 = " << puissance(3, 5) << std::endl;

    return 0;
}
