import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    def derivative(coeffs):
        if len(coeffs) <= 1:
            return np.array([0.0])
        return np.array([i * coeffs[i] for i in range(1, len(coeffs))], dtype=float)

    f = np.array(f_coeffs, dtype=float)
    g = np.array(g_coeffs, dtype=float)

    fp = derivative(f_coeffs)
    gp = derivative(g_coeffs)

    c1 = np.convolve(fp, g)
    c2 = np.convolve(f, gp)

    # 🔧 pad to same length
    max_len = max(len(c1), len(c2))
    c1 = np.pad(c1, (0, max_len - len(c1)))
    c2 = np.pad(c2, (0, max_len - len(c2)))

    result = c1 + c2

    # round + cleanup
    result = [round(float(x), 4) for x in result]
    while len(result) > 1 and result[-1] == 0.0:
        result.pop()

    return result if any(x != 0.0 for x in result) else [0.0]