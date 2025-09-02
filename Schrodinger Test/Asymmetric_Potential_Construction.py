import numpy as np

def asymmetric_potential(x, a=50, b=-200, c=500, d=0):
    """
    Constructs an asymmetric potential in log-price space:
        V(x) = a * x^2 + b * x^3 + c * x^4 + d * x^5

    Args:
        x (np.ndarray): Log-price deviations (x = log(P / P0)).
        a (float): Quadratic coefficient (well depth).
        b (float): Cubic coefficient (asymmetry).
        c (float): Quartic coefficient (barrier height).
        d (float): Quintic coefficient (fine asymmetry control).

    Returns:
        np.ndarray: Potential values V(x).
    """
    return a * x**2 + b * x**3 + c * x**4 + d * x**5
