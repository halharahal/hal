import scipy.stats.distributions as dis
import numpy as np
import pylab as pl

x = np.arange(-10, 10, 0.1)

norm = dis.norm.pdf(x, scale=1)
pl.plot(x, norm, label="sigma = "+str(1))

pl.legend(loc = 'upper right')

pl.show()

pl.savefig("norm.svg")