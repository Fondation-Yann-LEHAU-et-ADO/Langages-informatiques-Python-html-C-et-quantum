#!/usr/bin/env python3
"""
Application Flask intégrée avec librairie C++

Cette application démontre l'interopérabilité entre :
- Python (Flask) pour le backend web
- C++ (via ctypes) pour les calculs haute performance
- HTML/CSS/JavaScript pour l'interface utilisateur
"""

import os
import ctypes
from flask import Flask, render_template, request, jsonify
from typing import Optional

app = Flask(__name__)

# ================== Chargement de la librairie C++ ==================

# Chemin vers la librairie partagée
LIB_PATH = os.path.join(os.path.dirname(__file__), 'libmath.so')

# Variable globale pour la librairie
math_lib: Optional[ctypes.CDLL] = None


def load_math_library() -> Optional[ctypes.CDLL]:
    """
    Charge la librairie C++ partagée.
    
    Returns:
        La librairie chargée ou None si non disponible
    """
    global math_lib
    
    if math_lib is not None:
        return math_lib
    
    if not os.path.exists(LIB_PATH):
        print(f"[ATTENTION] Librairie C++ non trouvée: {LIB_PATH}")
        print("Compilez avec: g++ -shared -fPIC -o libmath.so math_lib.cpp")
        return None
    
    try:
        math_lib = ctypes.CDLL(LIB_PATH)
        
        # Configuration des types de retour
        math_lib.add.restype = ctypes.c_double
        math_lib.add.argtypes = [ctypes.c_double, ctypes.c_double]
        
        math_lib.subtract.restype = ctypes.c_double
        math_lib.subtract.argtypes = [ctypes.c_double, ctypes.c_double]
        
        math_lib.multiply.restype = ctypes.c_double
        math_lib.multiply.argtypes = [ctypes.c_double, ctypes.c_double]
        
        math_lib.divide.restype = ctypes.c_double
        math_lib.divide.argtypes = [ctypes.c_double, ctypes.c_double]
        
        math_lib.power.restype = ctypes.c_double
        math_lib.power.argtypes = [ctypes.c_double, ctypes.c_double]
        
        math_lib.square_root.restype = ctypes.c_double
        math_lib.square_root.argtypes = [ctypes.c_double]
        
        math_lib.factorial.restype = ctypes.c_ulonglong
        math_lib.factorial.argtypes = [ctypes.c_int]
        
        math_lib.fibonacci.restype = ctypes.c_ulonglong
        math_lib.fibonacci.argtypes = [ctypes.c_int]
        
        math_lib.sine.restype = ctypes.c_double
        math_lib.sine.argtypes = [ctypes.c_double]
        
        math_lib.cosine.restype = ctypes.c_double
        math_lib.cosine.argtypes = [ctypes.c_double]
        
        math_lib.tangent.restype = ctypes.c_double
        math_lib.tangent.argtypes = [ctypes.c_double]
        
        math_lib.natural_log.restype = ctypes.c_double
        math_lib.natural_log.argtypes = [ctypes.c_double]
        
        math_lib.log_base_10.restype = ctypes.c_double
        math_lib.log_base_10.argtypes = [ctypes.c_double]
        
        math_lib.exponential.restype = ctypes.c_double
        math_lib.exponential.argtypes = [ctypes.c_double]
        
        print(f"[OK] Librairie C++ chargée: {LIB_PATH}")
        return math_lib
        
    except OSError as e:
        print(f"[ERREUR] Impossible de charger la librairie: {e}")
        return None


# ================== Fallback Python ==================

class PythonMath:
    """Implémentation Python de secours si la librairie C++ n'est pas disponible."""
    
    import math as _math
    
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        if abs(b) < 1e-10:
            raise ValueError("Division par zéro")
        return a / b
    
    @staticmethod
    def power(base: float, exp: float) -> float:
        return base ** exp
    
    @staticmethod
    def square_root(x: float) -> float:
        if x < 0:
            raise ValueError("Racine carrée d'un nombre négatif")
        return PythonMath._math.sqrt(x)
    
    @staticmethod
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Factorielle d'un nombre négatif")
        return PythonMath._math.factorial(n)
    
    @staticmethod
    def fibonacci(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def sine(x: float) -> float:
        return PythonMath._math.sin(x)
    
    @staticmethod
    def cosine(x: float) -> float:
        return PythonMath._math.cos(x)
    
    @staticmethod
    def tangent(x: float) -> float:
        return PythonMath._math.tan(x)
    
    @staticmethod
    def natural_log(x: float) -> float:
        if x <= 0:
            raise ValueError("Logarithme d'un nombre non positif")
        return PythonMath._math.log(x)
    
    @staticmethod
    def log_base_10(x: float) -> float:
        if x <= 0:
            raise ValueError("Logarithme d'un nombre non positif")
        return PythonMath._math.log10(x)
    
    @staticmethod
    def exponential(x: float) -> float:
        return PythonMath._math.exp(x)


# ================== Routes Flask ==================

@app.route('/')
def index():
    """Page principale."""
    lib = load_math_library()
    using_cpp = lib is not None
    return render_template('index.html', using_cpp=using_cpp)


@app.route('/api/calculate', methods=['POST'])
def calculate():
    """
    API de calcul.
    
    Attend un JSON avec:
    - operation: nom de l'opération
    - a: premier opérande (optionnel selon l'opération)
    - b: second opérande (optionnel selon l'opération)
    
    Retourne:
    - result: le résultat du calcul
    - using_cpp: true si la librairie C++ est utilisée
    - error: message d'erreur si échec
    """
    lib = load_math_library()
    using_cpp = lib is not None
    
    try:
        data = request.get_json()
        operation = data.get('operation', '')
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        
        result = None
        
        # Opérations binaires
        binary_ops = {
            'add': 'add',
            'subtract': 'subtract',
            'multiply': 'multiply',
            'divide': 'divide',
            'power': 'power',
        }
        
        # Opérations unaires
        unary_ops = {
            'sqrt': 'square_root',
            'sin': 'sine',
            'cos': 'cosine',
            'tan': 'tangent',
            'ln': 'natural_log',
            'log10': 'log_base_10',
            'exp': 'exponential',
        }
        
        # Opérations avec entier
        int_ops = {
            'factorial': 'factorial',
            'fibonacci': 'fibonacci',
        }
        
        if operation in binary_ops:
            func_name = binary_ops[operation]
            if using_cpp:
                func = getattr(lib, func_name)
                result = func(a, b)
            else:
                func = getattr(PythonMath, func_name)
                result = func(a, b)
                
        elif operation in unary_ops:
            func_name = unary_ops[operation]
            if using_cpp:
                func = getattr(lib, func_name)
                result = func(a)
            else:
                func = getattr(PythonMath, func_name)
                result = func(a)
                
        elif operation in int_ops:
            func_name = int_ops[operation]
            n = int(a)
            if using_cpp:
                func = getattr(lib, func_name)
                result = func(n)
            else:
                func = getattr(PythonMath, func_name)
                result = func(n)
        else:
            return jsonify({
                'error': f'Opération inconnue: {operation}',
                'using_cpp': using_cpp
            }), 400
        
        return jsonify({
            'result': result,
            'using_cpp': using_cpp,
            'operation': operation
        })
        
    except ValueError as e:
        return jsonify({
            'error': str(e),
            'using_cpp': using_cpp
        }), 400
    except (TypeError, KeyError) as e:
        return jsonify({
            'error': f'Données invalides: {str(e)}',
            'using_cpp': using_cpp
        }), 400


@app.route('/api/info')
def info():
    """Retourne des informations sur l'application."""
    lib = load_math_library()
    return jsonify({
        'name': 'Math API',
        'version': '1.0.0',
        'using_cpp': lib is not None,
        'operations': {
            'binary': ['add', 'subtract', 'multiply', 'divide', 'power'],
            'unary': ['sqrt', 'sin', 'cos', 'tan', 'ln', 'log10', 'exp'],
            'integer': ['factorial', 'fibonacci']
        }
    })


# ================== Point d'entrée ==================

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("   Application Flask - Intégration Python/C++")
    print("=" * 60)
    
    # Tentative de chargement de la librairie C++
    lib = load_math_library()
    
    if lib is None:
        print("\n[INFO] Mode dégradé: utilisation de Python pour les calculs")
        print("[INFO] Pour activer C++, compilez math_lib.cpp:")
        print("       g++ -shared -fPIC -o libmath.so math_lib.cpp\n")
    
    print("=" * 60)
    print("   Démarrage du serveur sur http://localhost:5000")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
