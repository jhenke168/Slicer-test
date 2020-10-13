import numpy as np
import numpy.matlib
A = [[1,2],[3,4]]
A = np.array(A)
print(A)
meanA = np.mean(A,0)
print(meanA)
rows = len(A)
Xr = np.matlib.repmat(meanA, rows, 1)
print(Xr)