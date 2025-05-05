# Task: Show that 2n+1 is O(2n). constants are dropped, so 1 is negated.
# This is because the constant becomes insignificant once sample sizes become large.
# after the statement above, that leaves 2n which is equal to o(2n).
# Big-O (longest time) can be seen in the 'Large sample size' right side of the graph (n = 1000).

import matplotlib.pyplot as plt
import numpy as np

# small sample graph
n = np.arange(0,20,1)

y_const = 2*n + 1
y_noconst = 2*n

plt.figure(figsize=(10,5))
plt.plot(n, y_const,label='2n +1')
plt.plot(n,y_noconst,label='2n',linestyle=':')
plt.title('Small sample size')
plt.legend()

# large sample graph
m = np.arange(0,1000,1)

y_bigc = 2*m + 1
y_big = 2*m
plt.figure(figsize=(10,5))
plt.plot(m, y_bigc,label='2n +1')
plt.plot(m,y_big,label='2n',linestyle=':')
plt.title('Large sample size')
plt.legend()
plt.show()
