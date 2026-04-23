import numpy as np
import matplotlib.pyplot as plt

def plot_concentration(dimensions, num_samples=1000):
    plt.figure(figsize=(10, 6))
    
    for d in dimensions:
        X = np.random.normal(0, 1, (num_samples, d))
        # Normalize by sqrt(d) to compare distributions around 1
        norms = np.linalg.norm(X, axis=1) / np.sqrt(d)
        plt.hist(norms, bins=50, alpha=0.5, label=f'd={d}', density=True)
    
    plt.title('Concentración de la Norma (Normalizada por $\sqrt{d}$)')
    plt.xlabel('$\|x\| / \sqrt{d}$')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figuras/concentration_measure.pdf')
    print("Plot saved to figuras/concentration_measure.pdf")

if __name__ == "__main__":
    plot_concentration([10, 100, 1000, 10000])
