from scipy.linalg import eigh_tridiagonal
import numpy as np

def solve_schrodinger_1d(x, V_x, mass=1.0, hbar=1.0, num_eigen=5):
    """
    Numerically solves the 1D time-independent Schrödinger equation:
        - (ħ² / 2m) ψ''(x) + V(x) ψ(x) = E ψ(x)

    using a finite-difference discretization of the Hamiltonian.

    Args:
        x (np.ndarray): Discretized spatial domain (log-price space).
        V_x (np.ndarray): Potential energy array V(x).
        mass (float): Effective mass of the particle.
        hbar (float): Reduced Planck's constant.
        num_eigen (int): Number of eigenstates to compute.

    Returns:
        energies (np.ndarray): Array of eigenvalues (energy levels).
        wavefuncs (np.ndarray): 2D array of eigenfunctions ψ_n(x), shape (len(x), num_eigen).
    """
    dx = x[1] - x[0]
    N = len(x)

    # Kinetic energy operator: second derivative finite difference
    coeff = hbar**2 / (2 * mass * dx**2)
    main_diag = 2.0 * coeff * np.ones(N)
    off_diag  = -1.0 * coeff * np.ones(N - 1)

    # Add potential to diagonal
    H_diag = main_diag + V_x

    # Solve eigenvalue problem
    energies, wavefuncs = eigh_tridiagonal(H_diag, off_diag, select='i', select_range=(0, num_eigen - 1))

    # Normalize wavefunctions
    for i in range(num_eigen):
        norm = np.sqrt(np.trapz(np.abs(wavefuncs[:, i])**2, x))
        wavefuncs[:, i] /= norm

    return energies, wavefuncs
