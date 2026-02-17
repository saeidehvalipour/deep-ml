import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	x = np.array(x, dtype=int)
    
    # اگر تعداد ستون داده نشده، از داده پیدا کن
    if n_col is None:
        n_col = np.max(x) + 1
    
    # ساخت ماتریس صفر
    one_hot = np.zeros((len(x), n_col))
    
    # قرار دادن 1 در جای درست
    one_hot[np.arange(len(x)), x] = 1
    
    return one_hot