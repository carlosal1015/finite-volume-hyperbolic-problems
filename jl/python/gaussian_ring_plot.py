import numpy as np
import matplotlib.pyplot as plt

def plot_gaussian_ring(d, num_samples=500):
    # Generate random Gaussian vectors N(0, I_d)
    X = np.random.normal(0, 1, (num_samples, d))
    
    # Calculate norms
    norms = np.linalg.norm(X, axis=1)
    
    # Expected value sqrt(d)
    expected = np.sqrt(d)
    
    plt.figure(figsize=(10, 4))
    
    # Plot norms on a single horizontal axis
    plt.scatter(norms, np.zeros_like(norms), alpha=0.5, label='Muestras $\|x\|$')
    plt.axvline(expected, color='red', linestyle='--', label=f'$\\sqrt{{d}} \\approx {expected:.2f}$')
    
    plt.title(f'Concentración en el Anillo Gaussiano (d={d})')
    plt.xlabel('Norma $\|x\|$')
    plt.yticks([]) # Hide y-axis
    plt.legend()
    plt.grid(True, axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figuras/gaussian_ring.pdf')
    print(f"Plot saved to figuras/gaussian_ring.pdf. Expected norm: {expected:.2f}")

if __name__ == "__main__":
    plot_gaussian_ring(d=1000)
