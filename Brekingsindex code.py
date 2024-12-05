# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 14:23:16 2024

@author: Mathieu
"""

import math

# Parameters (gemeten waarden en onzekerheden)
N = 1.0          # Aantal interferentiebanden
delta_N = 0.01   # Onzekerheid in N
lambda_ = 500e-9 # Golflengte in meter
delta_lambda = 1e-9 # Onzekerheid in lambda
t = 1e-6         # Dikte in meter
delta_t = 1e-8   # Onzekerheid in t
alpha_deg = 30.0 # Invalshoek in graden
delta_alpha_deg = 0.5 # Onzekerheid in alpha in graden

# Conversie van graden naar radialen
alpha_rad = math.radians(alpha_deg)
delta_alpha_rad = math.radians(delta_alpha_deg)

# Berekening van de brekingsindex n
numerator = ((N * lambda_ / (2 * t)) + math.cos(alpha_rad) - 1)**2 + math.sin(alpha_rad)**2
denominator = 2 * (-(N * lambda_ / (2 * t)) - math.cos(alpha_rad) + 1)
n = numerator / denominator

# Partiële afgeleiden voor foutvoortplanting
partial_N = (2 * ((N * lambda_ / (2 * t)) + math.cos(alpha_rad) - 1) * (lambda_ / (2 * t))) / denominator
partial_lambda = (2 * ((N * lambda_ / (2 * t)) + math.cos(alpha_rad) - 1) * (N / (2 * t))) / denominator
partial_t = -((2 * ((N * lambda_ / (2 * t)) + math.cos(alpha_rad) - 1) * (N * lambda_ / (2 * t**2))) / denominator +
              numerator / (2 * denominator**2) * (N * lambda_ / t**2))
partial_alpha = (2 * (math.sin(alpha_rad) * math.cos(alpha_rad)) / denominator -
                 numerator / (2 * denominator**2) * math.sin(alpha_rad))

# Foutvoortplanting
delta_n = math.sqrt(
    (partial_N * delta_N)**2 +
    (partial_lambda * delta_lambda)**2 +
    (partial_t * delta_t)**2 +
    (partial_alpha * delta_alpha_rad)**2
)

# Resultaten
print(f"Brekingindex n: {n:.4f} ± {delta_n:.4f}")
