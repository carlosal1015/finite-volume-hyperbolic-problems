import matplotlib.pyplot as plt
import numpy as np

a1 = 0.00189
a2 = 27.6
a3 = 0.9  # 0.00252
b1 = 1.1
# m = (β * SoR) / (b1 * SyL * tast * kp)
m = 3.702113166195264e-12
ε = 4 - 4e-2  # 20.546467805308318
# ε = Er / (RTast)
α = 1
# α = Tres / Tast
q = -1e-2
# q = (a1*b3) / (b1 * (c-a3))
# print(1 + q * ε)
# print(ε, 2 * α)
Δ = ε * (ε - 4 * α - 4 * q * α**2)
# print(Δ)
Δ = 0
θcp = (-(2 * α - ε) + np.sqrt(Δ)) / (2 * (1 + q * ε))
θcm = (-(2 * α - ε) - np.sqrt(Δ)) / (2 * (1 + q * ε))
# print(θcp, θcm)
# print(-m / q)
# print(1 + q * ε)
# print(-(2 * α - ε))
# print(-np.sqrt(Δ))
# assert q < 0 and (1 + q * ε) > 0 and ε < 2 * α
# assert q < 0 and Δ > 0

θ = np.linspace(start=0, stop=3000, num=300)
# f = m * θ / (1 - q * θ) * np.exp(ε / (α + θ))
f = lambda θ: m * θ / (1 - q * θ) * np.exp(ε / (α + θ))
# fprime = f * (1 / θ + q / (1 - q * θ) - ε / (α + θ) ** 2)
fprime = lambda θ: f(θ) * (1 / θ + q / (1 - q * θ) - ε / (α + θ) ** 2)
fprimeprime = lambda θ: -f(θ) * (
    (2 * ε * q) / ((1 - q * θ) * (α + θ) ** 2)
    - ε * (2 + ε / (α + θ)) / (α + θ) ** 3
    + 2 * ε / (θ * (α + θ) ** 2)
    - 2 * q**2 / (1 - q * θ) ** 2
    - 2 * q / (θ * (1 - q * θ))
)
# fprimeprime = -f * (
#     (2 * ε * q) / ((1 - q * θ) * (α + θ) ** 2)
#     - ε * (2 + ε / (α + θ)) / (α + θ) ** 3
#     + 2 * ε / (θ * (α + θ) ** 2)
#     - 2 * q**2 / (1 - q * θ) ** 2
#     - 2 * q / (θ * (1 - q * θ))
# )
# fig, ax = plt.subplots()
# ax.plot(θ, f, label=r"$f$", linewidth=.5)
# ax.legend()
# ax.grid()
# ax.axhline(-m / q, color="red", linestyle='dashed', linewidth=.5)
# ax.axvline(θcm, color="green", linestyle='dashed', linewidth=.5)
# # ax.ylim()
# plt.savefig("f.pdf")
# plt.clf()

# fig, ax = plt.subplots()
# ax.plot(θ, fprime, label=r"$f^{\prime}$")
# ax.axvline(θcm, color="red", linestyle='dashed', linewidth=.5)
# ax.legend()
# ax.grid()
# plt.savefig("fprime.pdf")
# plt.clf()

# fig, ax = plt.subplots()
# ax.plot(θ, fprimeprime, label=r"$f^{\prime\prime}$")
# ax.set_ylim(-1e-12, 1e-12)
# # ax.axvline(θcm, color="red", linestyle='dashed', linewidth=.5)
# ax.legend()
# ax.grid()
# plt.savefig("fprimeprime.pdf")
# plt.clf()

# fig, ax = plt.subplots()
# ax.plot(θ, f, label=r"$f$", linewidth=1)
# ax.plot(θ, fprime, label=r"$f^{\prime}$", linewidth=1)
# ax.plot(θ, fprimeprime, label=r"$f^{\prime\prime}$", linewidth=1)
# ax.axvline(θcm, color="red", linestyle="dashed", linewidth=0.5)
# ax.axhline(-m / q, color="red", linestyle="dashed", linewidth=0.5)
# ax.set_ylim(0, 5e-10)
# ax.legend()
# ax.grid()
# plt.savefig("fall.pdf")
# plt.clf()

# print(-m / q)
print(θcp)
print(fprime(θcp))
print(fprimeprime(1000 * θcp))
