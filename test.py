"""
Module math_ops
================

Ce module fournit quelques opérations mathématiques simples destinées à servir
d'exemples pour les exercices de tests unitaires dans le cadre du TP
d'intégration continue. Les fonctions ici sont volontairement basiques pour que
les apprenants puissent écrire des tests couvrant les cas standards et les
côtés limites. N'hésitez pas à étendre ce module avec d'autres fonctions
selon vos besoins.
"""

from typing import Union


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiplie deux nombres et renvoie le résultat."""
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divise ``a`` par ``b`` et renvoie le résultat.

    Raises:
        ZeroDivisionError: si ``b`` est égal à zéro.
    """
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    return a / b


def is_prime(n: int) -> bool:
    """Renvoie True si l’entier ``n`` est premier, sinon False.

    Raises:
        TypeError: si ``n`` n’est pas un entier.
    """
    if not isinstance(n, int):
        raise TypeError("n doit être un entier")
    if n <= 1:
        return False
    # 2 et 3 sont premiers
    if n <= 3:
        return True
    # Élimination des multiples de 2 et 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Test des diviseurs potentiels jusqu’à √n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
