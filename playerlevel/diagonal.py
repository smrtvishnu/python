import numpy as np
a = [[11,2,4],[4,5,6],[10,8,-12]]
b = np.asarray(a)
b = np.fliplr(b)
print 'Antidiagonal (sum): ', np.trace(b)
print 'Antidiagonal (elements): ', np.diagonal(b)
