import numpy as np

def calculate_latency_percentiles(latencies: list[float]) -> dict[str, float]:
    if not latencies:
        return {'P50': 0.0, 'P95': 0.0, 'P99': 0.0}

     
    arr = np.asarray(latencies, dtype=float)
    return {
        "P50": round(np.percentile(arr, 50, method = 'linear'), 4),
        "P95": round(np.percentile(arr, 95, method = 'linear'), 4),
        "P99": round(np.percentile(arr, 99, method = 'linear'), 4),
    }