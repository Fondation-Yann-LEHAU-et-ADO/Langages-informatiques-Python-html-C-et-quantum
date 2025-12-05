"""
Application Flask d'intégration.

Cette application démontre l'interopérabilité entre Python, HTML et C++.
Elle utilise Flask comme backend Python, des templates HTML Jinja2,
et peut interfacer avec une bibliothèque C++ via ctypes.
"""

import ctypes
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Chemin vers la bibliothèque C++ compilée
MATH_LIB_PATH = os.path.join(os.path.dirname(__file__), "math_lib.so")


def get_math_lib():
    """
    Charge la bibliothèque C++ si elle existe.

    Returns:
        La bibliothèque C++ chargée ou None si elle n'existe pas
    """
    if os.path.exists(MATH_LIB_PATH):
        try:
            lib = ctypes.CDLL(MATH_LIB_PATH)

            # Configuration des types de retour et d'arguments
            lib.addition.argtypes = [ctypes.c_double, ctypes.c_double]
            lib.addition.restype = ctypes.c_double

            lib.soustraction.argtypes = [ctypes.c_double, ctypes.c_double]
            lib.soustraction.restype = ctypes.c_double

            lib.multiplication.argtypes = [ctypes.c_double, ctypes.c_double]
            lib.multiplication.restype = ctypes.c_double

            lib.division.argtypes = [ctypes.c_double, ctypes.c_double]
            lib.division.restype = ctypes.c_double

            lib.puissance.argtypes = [ctypes.c_double, ctypes.c_int]
            lib.puissance.restype = ctypes.c_double

            lib.racine_carree.argtypes = [ctypes.c_double]
            lib.racine_carree.restype = ctypes.c_double

            lib.factorielle.argtypes = [ctypes.c_int]
            lib.factorielle.restype = ctypes.c_ulonglong

            lib.est_premier.argtypes = [ctypes.c_int]
            lib.est_premier.restype = ctypes.c_bool

            return lib
        except OSError:
            return None
    return None


# Fonctions Python de secours
def py_addition(a: float, b: float) -> float:
    """Addition en Python."""
    return a + b


def py_soustraction(a: float, b: float) -> float:
    """Soustraction en Python."""
    return a - b


def py_multiplication(a: float, b: float) -> float:
    """Multiplication en Python."""
    return a * b


def py_division(a: float, b: float) -> float:
    """Division en Python."""
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b


def py_puissance(base: float, exp: int) -> float:
    """Puissance en Python."""
    return base ** exp


def py_racine_carree(n: float) -> float:
    """Racine carrée en Python."""
    import math
    if n < 0:
        raise ValueError("Nombre négatif")
    return math.sqrt(n)


def py_factorielle(n: int) -> int:
    """Factorielle en Python."""
    import math
    if n < 0:
        raise ValueError("Nombre négatif")
    return math.factorial(n)


def py_est_premier(n: int) -> bool:
    """Vérifie si un nombre est premier en Python."""
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


@app.route("/")
def index():
    """Page d'accueil."""
    math_lib = get_math_lib()
    cpp_available = math_lib is not None
    return render_template("index.html", cpp_available=cpp_available)


@app.route("/api/calculate", methods=["POST"])
def calculate():
    """
    API de calcul.

    Utilise la bibliothèque C++ si disponible, sinon Python.
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Données manquantes"}), 400

    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if operation is None:
        return jsonify({"error": "Opération non spécifiée"}), 400

    # Charge la bibliothèque C++
    math_lib = get_math_lib()
    using_cpp = math_lib is not None

    try:
        if operation == "addition":
            if a is None or b is None:
                return jsonify({"error": "Paramètres a et b requis"}), 400
            result = math_lib.addition(a, b) if using_cpp else py_addition(a, b)

        elif operation == "soustraction":
            if a is None or b is None:
                return jsonify({"error": "Paramètres a et b requis"}), 400
            result = math_lib.soustraction(a, b) if using_cpp else py_soustraction(a, b)

        elif operation == "multiplication":
            if a is None or b is None:
                return jsonify({"error": "Paramètres a et b requis"}), 400
            result = math_lib.multiplication(a, b) if using_cpp else py_multiplication(a, b)

        elif operation == "division":
            if a is None or b is None:
                return jsonify({"error": "Paramètres a et b requis"}), 400
            if b == 0:
                return jsonify({"error": "Division par zéro"}), 400
            result = math_lib.division(a, b) if using_cpp else py_division(a, b)

        elif operation == "puissance":
            if a is None or b is None:
                return jsonify({"error": "Paramètres a (base) et b (exposant) requis"}), 400
            result = math_lib.puissance(a, int(b)) if using_cpp else py_puissance(a, int(b))

        elif operation == "racine_carree":
            if a is None:
                return jsonify({"error": "Paramètre a requis"}), 400
            if a < 0:
                return jsonify({"error": "Nombre négatif"}), 400
            result = math_lib.racine_carree(a) if using_cpp else py_racine_carree(a)

        elif operation == "factorielle":
            if a is None:
                return jsonify({"error": "Paramètre a requis"}), 400
            if a < 0:
                return jsonify({"error": "Nombre négatif"}), 400
            result = math_lib.factorielle(int(a)) if using_cpp else py_factorielle(int(a))

        elif operation == "est_premier":
            if a is None:
                return jsonify({"error": "Paramètre a requis"}), 400
            result = bool(math_lib.est_premier(int(a))) if using_cpp else py_est_premier(int(a))

        else:
            return jsonify({"error": f"Opération inconnue: {operation}"}), 400

        return jsonify({
            "result": result,
            "operation": operation,
            "using_cpp": using_cpp,
            "a": a,
            "b": b
        })

    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/info")
def info():
    """Retourne des informations sur l'application."""
    math_lib = get_math_lib()
    return jsonify({
        "name": "Application d'intégration Python/HTML/C++",
        "version": "1.0.0",
        "cpp_library_available": math_lib is not None,
        "cpp_library_path": MATH_LIB_PATH,
        "languages": ["Python", "HTML", "C++"],
        "framework": "Flask"
    })


if __name__ == "__main__":
    print("=== Application d'intégration Python/HTML/C++ ===")
    print(f"Bibliothèque C++: {'Disponible' if get_math_lib() else 'Non disponible'}")
    print("Démarrage du serveur sur http://localhost:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)
