/**
 * @file math_operations.cpp
 * @brief Démonstration des opérations mathématiques et de la STL en C++
 * 
 * Ce programme illustre :
 * - Les opérations mathématiques de base et avancées
 * - L'utilisation de la Standard Template Library (STL)
 * - Les structures de données modernes (vector, map, etc.)
 * - La programmation fonctionnelle avec lambdas
 * - Les templates et la généricité
 */

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iomanip>
#include <memory>
#include <stdexcept>

// ================== Classe MathOperations ==================

/**
 * @class MathOperations
 * @brief Classe regroupant diverses opérations mathématiques
 */
class MathOperations {
public:
    // Opérations de base
    static double add(double a, double b) { return a + b; }
    static double subtract(double a, double b) { return a - b; }
    static double multiply(double a, double b) { return a * b; }
    
    static double divide(double a, double b) {
        if (b == 0) {
            throw std::invalid_argument("Division par zéro");
        }
        return a / b;
    }
    
    // Puissances et racines
    static double power(double base, double exponent) {
        return std::pow(base, exponent);
    }
    
    static double squareRoot(double x) {
        if (x < 0) {
            throw std::invalid_argument("Racine carrée d'un nombre négatif");
        }
        return std::sqrt(x);
    }
    
    // Trigonométrie (en radians)
    static double sine(double x) { return std::sin(x); }
    static double cosine(double x) { return std::cos(x); }
    static double tangent(double x) { return std::tan(x); }
    
    // Conversion degrés/radians
    static double toRadians(double degrees) {
        return degrees * M_PI / 180.0;
    }
    
    static double toDegrees(double radians) {
        return radians * 180.0 / M_PI;
    }
    
    // Logarithmes
    static double naturalLog(double x) {
        if (x <= 0) {
            throw std::invalid_argument("Logarithme d'un nombre non positif");
        }
        return std::log(x);
    }
    
    static double log10(double x) {
        if (x <= 0) {
            throw std::invalid_argument("Logarithme d'un nombre non positif");
        }
        return std::log10(x);
    }
    
    // Factorielle
    static unsigned long long factorial(int n) {
        if (n < 0) {
            throw std::invalid_argument("Factorielle d'un nombre négatif");
        }
        if (n <= 1) return 1;
        unsigned long long result = 1;
        for (int i = 2; i <= n; ++i) {
            result *= i;
        }
        return result;
    }
    
    // Fibonacci (récursif avec mémoïsation)
    static unsigned long long fibonacci(int n, std::map<int, unsigned long long>& memo) {
        if (n <= 1) return n;
        if (memo.find(n) != memo.end()) return memo[n];
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
        return memo[n];
    }
    
    // Surcharge sans mémo (crée un nouveau map)
    static unsigned long long fibonacci(int n) {
        std::map<int, unsigned long long> memo;
        return fibonacci(n, memo);
    }
};

// ================== Démonstration STL ==================

/**
 * @brief Démontre l'utilisation des vectors et algorithmes STL
 */
void demonstrateVectors() {
    std::cout << "\n=== Démonstration des Vectors ===" << std::endl;
    
    // Création et initialisation
    std::vector<int> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    std::cout << "Vector initial: ";
    for (const auto& n : numbers) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    
    // Tri
    std::sort(numbers.begin(), numbers.end());
    std::cout << "Après tri: ";
    for (const auto& n : numbers) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    
    // Somme avec accumulate
    int sum = std::accumulate(numbers.begin(), numbers.end(), 0);
    std::cout << "Somme: " << sum << std::endl;
    
    // Moyenne
    double moyenne = static_cast<double>(sum) / numbers.size();
    std::cout << "Moyenne: " << std::fixed << std::setprecision(2) << moyenne << std::endl;
    
    // Recherche
    auto it = std::find(numbers.begin(), numbers.end(), 5);
    if (it != numbers.end()) {
        std::cout << "5 trouvé à l'index: " << std::distance(numbers.begin(), it) << std::endl;
    }
    
    // Transformation avec lambda
    std::vector<int> squared;
    squared.reserve(numbers.size());
    std::transform(numbers.begin(), numbers.end(), std::back_inserter(squared),
                   [](int x) { return x * x; });
    
    std::cout << "Carrés: ";
    for (const auto& n : squared) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    
    // Filtrage avec remove_if
    std::vector<int> filtered = numbers;
    auto new_end = std::remove_if(filtered.begin(), filtered.end(),
                                   [](int x) { return x % 2 == 0; });
    filtered.erase(new_end, filtered.end());
    
    std::cout << "Nombres impairs: ";
    for (const auto& n : filtered) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
}

/**
 * @brief Démontre l'utilisation des maps
 */
void demonstrateMaps() {
    std::cout << "\n=== Démonstration des Maps ===" << std::endl;
    
    // Création d'une map
    std::map<std::string, double> constants;
    constants["pi"] = M_PI;
    constants["e"] = M_E;
    constants["phi"] = 1.618033988749895;  // Nombre d'or
    constants["sqrt2"] = std::sqrt(2);
    
    // Affichage
    std::cout << "Constantes mathématiques:" << std::endl;
    for (const auto& [name, value] : constants) {
        std::cout << "  " << name << " = " << std::fixed << std::setprecision(10) << value << std::endl;
    }
    
    // Recherche
    if (constants.find("pi") != constants.end()) {
        std::cout << "\nπ existe dans la map" << std::endl;
    }
    
    // Itération avec count
    std::cout << "Nombre d'éléments: " << constants.size() << std::endl;
}

/**
 * @brief Démontre les lambdas et fonctions d'ordre supérieur
 */
void demonstrateLambdas() {
    std::cout << "\n=== Démonstration des Lambdas ===" << std::endl;
    
    // Lambda simple
    auto square = [](double x) { return x * x; };
    std::cout << "Carré de 7: " << square(7) << std::endl;
    
    // Lambda avec capture
    double multiplier = 3.0;
    auto multiply = [multiplier](double x) { return x * multiplier; };
    std::cout << "5 × " << multiplier << " = " << multiply(5) << std::endl;
    
    // Lambda générique (C++14+)
    auto genericAdd = [](auto a, auto b) { return a + b; };
    std::cout << "Addition entiers: " << genericAdd(5, 3) << std::endl;
    std::cout << "Addition doubles: " << genericAdd(2.5, 3.7) << std::endl;
    
    // Fonction d'ordre supérieur
    auto applyTwice = [](std::function<double(double)> f, double x) {
        return f(f(x));
    };
    
    auto increment = [](double x) { return x + 1; };
    std::cout << "Appliquer (+1) deux fois à 5: " << applyTwice(increment, 5) << std::endl;
    
    // Composition de fonctions
    auto compose = [](auto f, auto g) {
        return [f, g](auto x) { return f(g(x)); };
    };
    
    auto addOne = [](double x) { return x + 1; };
    auto multiplyTwo = [](double x) { return x * 2; };
    auto composed = compose(multiplyTwo, addOne);  // (x + 1) * 2
    
    std::cout << "Composition (5 + 1) × 2 = " << composed(5) << std::endl;
}

// ================== Template de statistiques ==================

/**
 * @brief Classe template pour les calculs statistiques
 */
template<typename T>
class Statistics {
public:
    static T sum(const std::vector<T>& data) {
        return std::accumulate(data.begin(), data.end(), T{});
    }
    
    static double mean(const std::vector<T>& data) {
        if (data.empty()) {
            throw std::invalid_argument("Données vides");
        }
        return static_cast<double>(sum(data)) / data.size();
    }
    
    static T min(const std::vector<T>& data) {
        if (data.empty()) {
            throw std::invalid_argument("Données vides");
        }
        return *std::min_element(data.begin(), data.end());
    }
    
    static T max(const std::vector<T>& data) {
        if (data.empty()) {
            throw std::invalid_argument("Données vides");
        }
        return *std::max_element(data.begin(), data.end());
    }
    
    static double variance(const std::vector<T>& data) {
        if (data.size() < 2) {
            throw std::invalid_argument("Au moins 2 valeurs requises");
        }
        double avg = mean(data);
        double sumSquares = 0;
        for (const auto& x : data) {
            sumSquares += std::pow(static_cast<double>(x) - avg, 2);
        }
        return sumSquares / (data.size() - 1);
    }
    
    static double stdDev(const std::vector<T>& data) {
        return std::sqrt(variance(data));
    }
};

/**
 * @brief Démontre les templates statistiques
 */
void demonstrateStatistics() {
    std::cout << "\n=== Démonstration des Statistiques ===" << std::endl;
    
    std::vector<double> data = {10.5, 20.3, 15.8, 25.1, 18.6, 22.4, 12.9};
    
    std::cout << "Données: ";
    for (const auto& x : data) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "Somme: " << Statistics<double>::sum(data) << std::endl;
    std::cout << "Moyenne: " << Statistics<double>::mean(data) << std::endl;
    std::cout << "Min: " << Statistics<double>::min(data) << std::endl;
    std::cout << "Max: " << Statistics<double>::max(data) << std::endl;
    std::cout << "Variance: " << Statistics<double>::variance(data) << std::endl;
    std::cout << "Écart-type: " << Statistics<double>::stdDev(data) << std::endl;
}

// ================== Programme principal ==================

int main() {
    std::cout << "=============================================" << std::endl;
    std::cout << "   Démonstration C++ : Math & STL" << std::endl;
    std::cout << "=============================================" << std::endl;
    
    // Opérations mathématiques de base
    std::cout << "\n=== Opérations Mathématiques ===" << std::endl;
    std::cout << std::fixed << std::setprecision(4);
    
    std::cout << "10 + 5 = " << MathOperations::add(10, 5) << std::endl;
    std::cout << "10 - 5 = " << MathOperations::subtract(10, 5) << std::endl;
    std::cout << "10 × 5 = " << MathOperations::multiply(10, 5) << std::endl;
    std::cout << "10 ÷ 5 = " << MathOperations::divide(10, 5) << std::endl;
    
    // Puissances et racines
    std::cout << "\n=== Puissances et Racines ===" << std::endl;
    std::cout << "2^10 = " << MathOperations::power(2, 10) << std::endl;
    std::cout << "√144 = " << MathOperations::squareRoot(144) << std::endl;
    
    // Trigonométrie
    std::cout << "\n=== Trigonométrie ===" << std::endl;
    double angle30 = MathOperations::toRadians(30);
    std::cout << "sin(30°) = " << MathOperations::sine(angle30) << std::endl;
    std::cout << "cos(60°) = " << MathOperations::cosine(MathOperations::toRadians(60)) << std::endl;
    std::cout << "tan(45°) = " << MathOperations::tangent(MathOperations::toRadians(45)) << std::endl;
    
    // Factorielle et Fibonacci
    std::cout << "\n=== Factorielle et Fibonacci ===" << std::endl;
    std::cout << "10! = " << MathOperations::factorial(10) << std::endl;
    std::cout << "Fibonacci(20) = " << MathOperations::fibonacci(20) << std::endl;
    
    // Série Fibonacci
    std::cout << "Série Fibonacci: ";
    for (int i = 0; i <= 10; ++i) {
        std::cout << MathOperations::fibonacci(i) << " ";
    }
    std::cout << std::endl;
    
    // Démonstrations STL
    demonstrateVectors();
    demonstrateMaps();
    demonstrateLambdas();
    demonstrateStatistics();
    
    std::cout << "\n=============================================" << std::endl;
    std::cout << "   Fin de la démonstration" << std::endl;
    std::cout << "=============================================" << std::endl;
    
    return 0;
}
