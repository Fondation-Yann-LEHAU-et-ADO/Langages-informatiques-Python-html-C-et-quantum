#!/usr/bin/env python3
"""
Application Flask d'intégration Python + C++ + HTML

Cette application démontre l'intégration de trois langages :
- Python (Flask) : Backend web
- C++ (ctypes) : Calculs mathématiques performants
- HTML (Jinja2) : Interface utilisateur

Exécution :
    1. Compiler la bibliothèque C++ :
       g++ -shared -fPIC -o libmath.so math_lib.cpp
    
    2. Lancer l'application :
       python app.py
    
    3. Ouvrir http://localhost:5000 dans un navigateur
"""

import ctypes
import os
import platform
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Charger la bibliothèque C++
math_lib = None


def load_math_library():
    """Charge la bibliothèque mathématique C++."""
    global math_lib
    
    # Déterminer le nom de la bibliothèque selon l'OS
    if platform.system() == 'Windows':
        lib_name = 'math_lib.dll'
    elif platform.system() == 'Darwin':
        lib_name = 'libmath.dylib'
    else:
        lib_name = 'libmath.so'
    
    # Chemin de la bibliothèque
    lib_path = os.path.join(os.path.dirname(__file__), lib_name)
    
    if os.path.exists(lib_path):
        try:
            math_lib = ctypes.CDLL(lib_path)
            
            # Définir les types de retour des fonctions
            math_lib.add.argtypes = [ctypes.c_double, ctypes.c_double]
            math_lib.add.restype = ctypes.c_double
            
            math_lib.subtract.argtypes = [ctypes.c_double, ctypes.c_double]
            math_lib.subtract.restype = ctypes.c_double
            
            math_lib.multiply.argtypes = [ctypes.c_double, ctypes.c_double]
            math_lib.multiply.restype = ctypes.c_double
            
            math_lib.divide.argtypes = [ctypes.c_double, ctypes.c_double]
            math_lib.divide.restype = ctypes.c_double
            
            math_lib.power.argtypes = [ctypes.c_double, ctypes.c_double]
            math_lib.power.restype = ctypes.c_double
            
            math_lib.sqrt_num.argtypes = [ctypes.c_double]
            math_lib.sqrt_num.restype = ctypes.c_double
            
            math_lib.factorial.argtypes = [ctypes.c_int]
            math_lib.factorial.restype = ctypes.c_ulonglong
            
            math_lib.fibonacci.argtypes = [ctypes.c_int]
            math_lib.fibonacci.restype = ctypes.c_ulonglong
            
            math_lib.is_prime.argtypes = [ctypes.c_int]
            math_lib.is_prime.restype = ctypes.c_int
            
            math_lib.gcd.argtypes = [ctypes.c_int, ctypes.c_int]
            math_lib.gcd.restype = ctypes.c_int
            
            math_lib.lcm.argtypes = [ctypes.c_int, ctypes.c_int]
            math_lib.lcm.restype = ctypes.c_int
            
            print(f"✓ Bibliothèque C++ chargée : {lib_path}")
            return True
        except OSError as e:
            print(f"✗ Erreur lors du chargement de la bibliothèque : {e}")
            return False
    else:
        print(f"✗ Bibliothèque non trouvée : {lib_path}")
        print("  Compilez-la avec : g++ -shared -fPIC -o libmath.so math_lib.cpp")
        return False


# Fonctions de calcul Python (fallback si C++ non disponible)
import math as python_math


def py_add(a, b):
    return a + b


def py_subtract(a, b):
    return a - b


def py_multiply(a, b):
    return a * b


def py_divide(a, b):
    if b == 0:
        return float('nan')
    return a / b


def py_power(base, exp):
    return python_math.pow(base, exp)


def py_sqrt(n):
    if n < 0:
        return float('nan')
    return python_math.sqrt(n)


def py_factorial(n):
    if n < 0:
        return 0
    return python_math.factorial(n)


def py_fibonacci(n):
    if n < 0:
        return 0
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def py_is_prime(n):
    if n <= 1:
        return 0
    if n <= 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6
    return 1


def py_gcd(a, b):
    return python_math.gcd(abs(a), abs(b))


def py_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // py_gcd(a, b)


@app.route('/')
def index():
    """Page d'accueil."""
    cpp_loaded = math_lib is not None
    return render_template('index.html', cpp_loaded=cpp_loaded)


@app.route('/calculate', methods=['POST'])
def calculate():
    """Endpoint pour les calculs."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        
        # Utiliser C++ si disponible, sinon Python
        use_cpp = math_lib is not None
        
        if operation == 'add':
            a, b = float(data['a']), float(data['b'])
            result = math_lib.add(a, b) if use_cpp else py_add(a, b)
        
        elif operation == 'subtract':
            a, b = float(data['a']), float(data['b'])
            result = math_lib.subtract(a, b) if use_cpp else py_subtract(a, b)
        
        elif operation == 'multiply':
            a, b = float(data['a']), float(data['b'])
            result = math_lib.multiply(a, b) if use_cpp else py_multiply(a, b)
        
        elif operation == 'divide':
            a, b = float(data['a']), float(data['b'])
            if b == 0:
                return jsonify({'error': 'Division par zéro'}), 400
            result = math_lib.divide(a, b) if use_cpp else py_divide(a, b)
        
        elif operation == 'power':
            base, exp = float(data['base']), float(data['exp'])
            result = math_lib.power(base, exp) if use_cpp else py_power(base, exp)
        
        elif operation == 'sqrt':
            n = float(data['n'])
            if n < 0:
                return jsonify({'error': 'Racine carrée de nombre négatif'}), 400
            result = math_lib.sqrt_num(n) if use_cpp else py_sqrt(n)
        
        elif operation == 'factorial':
            n = int(data['n'])
            if n < 0:
                return jsonify({'error': 'Factorielle de nombre négatif'}), 400
            result = math_lib.factorial(n) if use_cpp else py_factorial(n)
        
        elif operation == 'fibonacci':
            n = int(data['n'])
            if n < 0:
                return jsonify({'error': 'Index Fibonacci négatif'}), 400
            result = math_lib.fibonacci(n) if use_cpp else py_fibonacci(n)
        
        elif operation == 'is_prime':
            n = int(data['n'])
            is_prime = (math_lib.is_prime(n) if use_cpp else py_is_prime(n)) == 1
            return jsonify({
                'result': is_prime,
                'message': f"{n} est {'premier' if is_prime else 'pas premier'}",
                'backend': 'C++' if use_cpp else 'Python'
            })
        
        elif operation == 'gcd':
            a, b = int(data['a']), int(data['b'])
            result = math_lib.gcd(a, b) if use_cpp else py_gcd(a, b)
        
        elif operation == 'lcm':
            a, b = int(data['a']), int(data['b'])
            result = math_lib.lcm(a, b) if use_cpp else py_lcm(a, b)
        
        else:
            return jsonify({'error': 'Opération non reconnue'}), 400
        
        return jsonify({
            'result': result,
            'backend': 'C++' if use_cpp else 'Python'
        })
    
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({'error': str(e)}), 400


@app.route('/info')
def info():
    """Informations sur le système."""
    return jsonify({
        'platform': platform.system(),
        'python_version': platform.python_version(),
        'cpp_library_loaded': math_lib is not None
    })


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("  Application d'Intégration Python + C++ + HTML")
    print("=" * 60)
    
    # Charger la bibliothèque C++
    load_math_library()
    
    print("\nDémarrage du serveur Flask...")
    print("Ouvrez http://localhost:5000 dans votre navigateur")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
