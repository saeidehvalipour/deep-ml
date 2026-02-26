import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	x= np.array(scores, dtype= float)
	
	x_shifted = x-np.max(x)
	log_sum_exp = np.log(np.sum(np.exp(x_shifted)))
	return x_shifted - log_sum_exp

