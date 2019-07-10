import pylab as plt
import numpy as np
plt.style.use('ggplot')
fig = plt.figure(1)
ax = plt.gca()
# make some testing data
x = np.linspace( 0, np.pi, 1000 )
test_f = lambda x: np.sin(x)*3 + np.cos(2*x)
# plot the test data
ax.plot( x, test_f(x) , lw = 2)
# set the axis labels
ax.set_xlabel(r'$x$', fontsize=14, labelpad=10)
ax.set_ylabel(r'$f(x)$', fontsize=14, labelpad=25, rotation=0)
# set axis limits
ax.set_xlim(0,np.pi)
plt.show()