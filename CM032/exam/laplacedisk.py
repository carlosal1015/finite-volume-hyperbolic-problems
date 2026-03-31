from numpy.linalg import norm
import numpy as np
from matplotlib import pyplot as plt

samples = 64
epsilon = 1e-3
domain = (400, 400)


def boundary_value(a, freq=5):
    return np.sin(np.arctan2(*a) * freq)


def closest_boundary(a):
    return np.divide(a, d := norm(x=a, axis=0), where=d != 0)


grid = np.stack(np.meshgrid(*(np.linspace(start=-1, stop=1, num=d) for d in domain)))
mask = norm(x=grid, axis=0) <= 1
rng = np.random.default_rng()
result = np.zeros(domain)

for s in range(samples):
    points = grid.copy()
    alive = mask.copy()
    radii = np.zeros(domain)
    angles = np.zeros(domain)
    closest = np.zeros_like(grid)

    while np.sum(alive) > 0:
        closest[:, alive] = closest_boundary(points[:, alive])
        radii[alive] = norm(points[:, alive] - closest[:, alive], axis=0)
        alive[alive] = radii[alive] > epsilon
        angles[alive] = rng.uniform(-np.pi, np.pi, np.count_nonzero(alive))
        points[:, alive] += np.stack(
            (radii[alive] * np.cos(angles[alive]), radii[alive] * np.sin(angles[alive]))
        )

    result[mask] += boundary_value(closest)[mask]

result /= samples

plt.imshow(result)
plt.show()
