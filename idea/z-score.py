import math
from scipy.stats import norm

p_observed = <0.25>
p_expected = <0.301>
n = 17824

std_error = math.sqrt(p_expected * (1 - p_expected) / n)
z_score = (p_observed - p_expected) / std_error
p_value = 2 * norm.sf(abs(z_score))

print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.6f}")

if p_value < 0.05:
    print("problem")
else:
    print("normal")
