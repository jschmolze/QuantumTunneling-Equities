import numpy as np
import matplotlib.pyplot as plt
from Asymmetric_Potential_Construction import asymmetric_potential
from Schrodinger_Equation import solve_schrodinger_1d

x_vals = np.linspace(-0.3, 0.3, 1000)
V_asym = asymmetric_potential(x_vals, a=50, b=-200, c=500, d=0)
x_vals = np.linspace(-0.3, 0.3, 1000)
V_x = asymmetric_potential(x_vals, a=50, b=-200, c=500)

energies, wavefuncs = solve_schrodinger_1d(x_vals, V_x, num_eigen=3)
def plot_potential_and_wavefunctions(x_vals, V_x, energies, wavefuncs, num_levels=3):
    """
    Plots the potential V(x) along with the squared wavefunctions |\psi_n(x)|^2,
    vertically offset by their energy levels.

    Args:
        x_vals (np.ndarray): Log-price domain.
        V_x (np.ndarray): Potential V(x).
        energies (np.ndarray): Energy levels E_n.
        wavefuncs (np.ndarray): Corresponding eigenfunctions ψ_n(x).
        num_levels (int): Number of energy levels/wavefunctions to plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, V_x, label="Potential $V(x)$", color="black")

    for n in range(num_levels):
        psi_sq = wavefuncs[:, n]**2
        # Scale for visibility
        psi_scaled = psi_sq / psi_sq.max() * (V_x.max() * 0.4)
        plt.plot(x_vals, psi_scaled + energies[n], label=fr"$|\psi_{n}(x)|^2 + E_{n:.2f}$")

    plt.title("Asymmetric Log-Space Potential and Quantum States")
    plt.xlabel(r"$x = \log(P / P_0)$")
    plt.ylabel("Energy / Potential")
    plt.axvline(0, color='gray', linestyle='--', linewidth=1)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Call the function
plot_potential_and_wavefunctions(x_vals, V_x, energies, wavefuncs)