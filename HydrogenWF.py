import numpy
import math
from scipy.special import sph_harm
import scipy.special


def WF(n, l, m, X, Y, Z):
    R = numpy.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    Theta = numpy.arccos(Z / R)
    Phi = numpy.arctan2(Y, X)

    rho = 2. * R / n
    s_harm = sph_harm(m, l, Phi, Theta)
    l_poly = scipy.special.genlaguerre(n - l - 1, 2 * l + 1)(rho)

    prefactor = numpy.sqrt((2. / n) ** 3 * math.factorial(n - l - 1) / (2. * n * math.factorial(n + l)))
    wf = prefactor * numpy.exp(-rho / 2.) * rho ** l * s_harm * l_poly
    wf = numpy.nan_to_num(wf)
    return wf
