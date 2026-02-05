from typing import Callable, List

def compute_hessian(f: Callable[[List[float]], float], point: List[float], h: float = 1e-5) -> List[List[float]]:
    n = len(point)
    x0 = list(point)
    f0 = f(x0)

    H = [[0.0] * n for _ in range(n)]

    # Diagonal terms
    for i in range(n):
        xp = x0.copy()
        xm = x0.copy()
        xp[i] += h
        xm[i] -= h
        H[i][i] = (f(xp) - 2.0 * f0 + f(xm)) / (h * h)

    # Off-diagonal terms
    for i in range(n):
        for j in range(i + 1, n):
            xpp = x0.copy()
            xpm = x0.copy()
            xmp = x0.copy()
            xmm = x0.copy()

            xpp[i] += h; xpp[j] += h
            xpm[i] += h; xpm[j] -= h
            xmp[i] -= h; xmp[j] += h
            xmm[i] -= h; xmm[j] -= h

            val = (f(xpp) - f(xpm) - f(xmp) + f(xmm)) / (4.0 * h * h)
            H[i][j] = val
            H[j][i] = val

    return H
