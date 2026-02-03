import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    
    # Your code here
    g = np.poly1d(g_coeffs)
    h = np.poly1d(h_coeffs)

    g_prime = np.polyder(g)
    h_prime = np.polyder(h)

    no = g_prime(x) * h(x) - h_prime(x) * g(x)
    den =[h(x) ** 2]

    return float(no / den)