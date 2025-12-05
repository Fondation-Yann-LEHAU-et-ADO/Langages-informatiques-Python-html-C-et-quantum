/**
 * Bibliothèque mathématique C++ pour l'intégration avec Python
 * 
 * Ce fichier définit des fonctions mathématiques exportées
 * pour être utilisées avec Python via ctypes.
 * 
 * Compilation :
 *   Linux/Mac : g++ -shared -fPIC -o libmath.so math_lib.cpp
 *   Windows   : g++ -shared -o math_lib.dll math_lib.cpp
 */

#include <cmath>

// Macro pour l'export des fonctions
#ifdef _WIN32
    #define EXPORT extern "C" __declspec(dllexport)
#else
    #define EXPORT extern "C"
#endif

/**
 * Additionne deux nombres
 */
EXPORT double add(double a, double b) {
    return a + b;
}

/**
 * Soustrait deux nombres
 */
EXPORT double subtract(double a, double b) {
    return a - b;
}

/**
 * Multiplie deux nombres
 */
EXPORT double multiply(double a, double b) {
    return a * b;
}

/**
 * Divise deux nombres
 * Retourne 0 si division par zéro
 */
EXPORT double divide(double a, double b) {
    if (b == 0) {
        return 0;
    }
    return a / b;
}

/**
 * Calcule la puissance
 */
EXPORT double power(double base, double exponent) {
    return std::pow(base, exponent);
}

/**
 * Calcule la racine carrée
 */
EXPORT double sqrt_num(double n) {
    if (n < 0) {
        return -1;
    }
    return std::sqrt(n);
}

/**
 * Calcule la factorielle (version itérative)
 */
EXPORT unsigned long long factorial(int n) {
    if (n < 0) {
        return 0;
    }
    if (n <= 1) {
        return 1;
    }
    unsigned long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

/**
 * Calcule le n-ième nombre de Fibonacci
 */
EXPORT unsigned long long fibonacci(int n) {
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
 * Retourne 1 si premier, 0 sinon
 */
EXPORT int is_prime(int n) {
    if (n <= 1) {
        return 0;
    }
    if (n <= 3) {
        return 1;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return 0;
    }
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return 0;
        }
    }
    return 1;
}

/**
 * Calcule le PGCD de deux nombres
 */
EXPORT int gcd(int a, int b) {
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
 * Calcule le PPCM de deux nombres
 */
EXPORT int lcm(int a, int b) {
    if (a == 0 || b == 0) {
        return 0;
    }
    return std::abs(a * b) / gcd(a, b);
}
