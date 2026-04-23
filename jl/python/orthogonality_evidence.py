import numpy as np

def analyze_orthogonality(d, num_samples=1000):
    # Generate random Gaussian vectors
    v1 = np.random.normal(0, 1, (num_samples, d))
    v2 = np.random.normal(0, 1, (num_samples, d))
    
    # Normalize vectors
    v1_norm = v1 / np.linalg.norm(v1, axis=1, keepdims=True)
    v2_norm = v2 / np.linalg.norm(v2, axis=1, keepdims=True)
    
    # Calculate dot products (cosine of angles)
    dot_products = np.sum(v1_norm * v2_norm, axis=1)
    
    # Calculate angles in degrees
    angles = np.arccos(np.clip(dot_products, -1.0, 1.0)) * 180 / np.pi
    
    print(f"Dimension d = {d}")
    print(f"Mean Dot Product: {np.mean(dot_products):.6f}")
    print(f"Std Dev Dot Product: {np.std(dot_products):.6f}")
    print(f"Mean Angle: {np.mean(angles):.2f} degrees")
    print(f"Std Dev Angle: {np.std(angles):.2f} degrees")
    print("-" * 30)

if __name__ == "__main__":
    for d in [2, 10, 100, 1000, 10000]:
        analyze_orthogonality(d)
