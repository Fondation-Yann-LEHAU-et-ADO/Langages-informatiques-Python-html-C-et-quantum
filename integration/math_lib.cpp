/**
 * @file math_lib.cpp
 * @brief Librairie C++ partagée pour les calculs mathématiques
 * 
 * Cette librairie est conçue pour être compilée en tant que librairie partagée (.so)
 * et appelée depuis Python via ctypes.
 * 
 * Compilation :
 *   g++ -shared -fPIC -o libmath.so math_lib.cpp
 * 
 * Utilisation depuis Python :
 *   import ctypes
 *   lib = ctypes.CDLL('./libmath.so')
 *   lib.add.restype = ctypes.c_double
 *   lib.add.argtypes = [ctypes.c_double, ctypes.c_double]
 *   result = lib.add(5.0, 3.0)
 */

#include <cmath>
#include <map>

// Macro pour exporter les fonctions en C (évite le name mangling C++)
extern "C" {

// ================== Opérations de base ==================

/**
 * @brief Addition de deux nombres
 */
double add(double a, double b) {
    return a + b;
}

/**
 * @brief Soustraction de deux nombres
 */
double subtract(double a, double b) {
    return a - b;
}

/**
 * @brief Multiplication de deux nombres
 */
double multiply(double a, double b) {
    return a * b;
}

/**
 * @brief Division de deux nombres
 * @note Retourne NaN si b == 0
 */
double divide(double a, double b) {
    if (b == 0.0) {
        return std::nan("");
    }
    return a / b;
}

// ================== Puissances et racines ==================

/**
 * @brief Élève un nombre à une puissance
 */
double power(double base, double exponent) {
    return std::pow(base, exponent);
}

/**
 * @brief Calcule la racine carrée
 * @note Retourne NaN si x < 0
 */
double square_root(double x) {
    if (x < 0.0) {
        return std::nan("");
    }
    return std::sqrt(x);
}

// ================== Trigonométrie (en radians) ==================

/**
 * @brief Calcule le sinus
 */
double sine(double x) {
    return std::sin(x);
}

/**
 * @brief Calcule le cosinus
 */
double cosine(double x) {
    return std::cos(x);
}

/**
 * @brief Calcule la tangente
 */
double tangent(double x) {
    return std::tan(x);
}

// ================== Logarithmes et exponentielles ==================

/**
 * @brief Calcule le logarithme naturel
 * @note Retourne NaN si x <= 0
 */
double natural_log(double x) {
    if (x <= 0.0) {
        return std::nan("");
    }
    return std::log(x);
}

/**
 * @brief Calcule le logarithme base 10
 * @note Retourne NaN si x <= 0
 */
double log_base_10(double x) {
    if (x <= 0.0) {
        return std::nan("");
    }
    return std::log10(x);
}

/**
 * @brief Calcule l'exponentielle
 */
double exponential(double x) {
    return std::exp(x);
}

// ================== Fonctions spéciales ==================

/**
 * @brief Calcule la factorielle
 * @note Retourne 0 si n < 0
 */
unsigned long long factorial(int n) {
    if (n < 0) {
        return 0;
    }
    if (n <= 1) {
        return 1;
    }
    unsigned long long result = 1;
    for (int i = 2; i <= n; ++i) {
        result *= i;
    }
    return result;
}

/**
 * @brief Calcule le n-ième nombre de Fibonacci
 * 
 * Utilise une approche itérative pour l'efficacité
 */
unsigned long long fibonacci(int n) {
    if (n <= 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    
    unsigned long long prev = 0;
    unsigned long long curr = 1;
    
    for (int i = 2; i <= n; ++i) {
        unsigned long long next = prev + curr;
        prev = curr;
        curr = next;
    }
    
    return curr;
}

// ================== Constantes mathématiques ==================

/**
 * @brief Retourne la valeur de π
 */
double get_pi() {
    return M_PI;
}

/**
 * @brief Retourne la valeur de e
 */
double get_e() {
    return M_E;
}

// ================== Utilitaires ==================

/**
 * @brief Convertit des degrés en radians
 */
double to_radians(double degrees) {
    return degrees * M_PI / 180.0;
}

/**
 * @brief Convertit des radians en degrés
 */
double to_degrees(double radians) {
    return radians * 180.0 / M_PI;
}

/**
 * @brief Calcule la valeur absolue
 */
double absolute(double x) {
    return std::fabs(x);
}

/**
 * @brief Arrondit au nombre entier le plus proche
 */
double round_value(double x) {
    return std::round(x);
}

/**
 * @brief Arrondit vers le bas
 */
double floor_value(double x) {
    return std::floor(x);
}

/**
 * @brief Arrondit vers le haut
 */
double ceil_value(double x) {
    return std::ceil(x);
}

} // extern "C"
