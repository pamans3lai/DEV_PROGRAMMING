# https://www.w3schools.com/python/scipy/scipy_sparse_data.php
#
import numpy as np 
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))
