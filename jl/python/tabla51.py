import itertools
from multiprocessing import Pool, cpu_count

import numpy as np


def run_experiment(epsilon):
    n, d = 150, 20000
    np.random.seed(None)
    X = np.random.uniform(0, 1, (n, d))
    sample_pairs = list(itertools.combinations(range(n), 2))
    num_total_pairs = len(sample_pairs)
    k1 = np.ceil(48 * np.log(n) / (epsilon**2))
    k2 = np.ceil(4 * np.log(n) / ((epsilon**2) / 2 - (epsilon**3) / 3))
    k_vals = [k1, k2]

    media_porcentaje_cumple = []

    for ki in k_vals:
        ki = int(ki)
        phi = np.random.normal(0, 1 / np.sqrt(ki), (ki, d))
        Z = X @ phi.T
        porcentaje_cumple = []
        for _ in range(10):
            # Sample 500 indices from the available pairs
            selected_indices = np.random.choice(num_total_pairs, 500, replace=False)

            d_original = []
            d_proj = []

            for idx in selected_indices:
                i, j = sample_pairs[idx]
                # Euclidean distances
                dist_orig = np.linalg.norm(X[i] - X[j])
                dist_proj = np.linalg.norm(Z[i] - Z[j])

                d_original.append(dist_orig)
                d_proj.append(dist_proj)

            d_original = np.array(d_original)
            d_proj = np.array(d_proj)
            r = d_proj / d_original
            cumplen = (r >= (1 - epsilon)) & (r <= (1 + epsilon))
            porcentaje_cumple.append(np.mean(cumplen) * 100)

        media_porcentaje_cumple.append(np.mean(porcentaje_cumple))
        print(
            f"Epsilon: {epsilon:.2f} | k: {ki:5d} | Mean Success: {media_porcentaje_cumple[-1]:.3f}%"
        )

    return [
        epsilon,
        int(k_vals[0]),
        media_porcentaje_cumple[0],
        int(k_vals[1]),
        media_porcentaje_cumple[1],
    ]


if __name__ == "__main__":
    epsilon_vals = [0.2, 0.17, 0.15]
    print(f"Starting simulation using {max(1, cpu_count() - 1)} cores...")

    with Pool(processes=max(1, cpu_count() - 1)) as pool:
        results = pool.map(run_experiment, epsilon_vals)

    print(
        f"{'epsilon':>8} | {'k1':>6} | {'cumplen_k1(%)':>15} | {'k2':>6} | {'cumplen_k2(%)':>15}"
    )
    print("-" * 65)
    for res in results:
        print(
            f"{res[0]:8.2f} | {res[1]:6d} | {res[2]:14.3f}% | {res[3]:6d} | {res[4]:14.3f}%"
        )
