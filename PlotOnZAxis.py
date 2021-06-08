import numpy
import matplotlib.pyplot as plt
from HydrogenWF import WF

d = 0.2
min = -20
max = 20
x = numpy.arange(min, max, d)
y = numpy.arange(min, max, d)
z = numpy.arange(min, max, d)
X, Y, Z = numpy.meshgrid(x, y,
                         z)  # X, Y, Z are 3d arrays that tell us the values of x, y, and z at every point in space

n = int(input("Please input the value for n: "))
l = int(input("Please input the value for l: "))
m = int(input("Please input the value for m: "))

data = WF(n, l, m, X, Y, Z)
data = abs(data) ** 2

plt.figure()
plt.plot(z, data[int(len(z) / 2), int(len(z) / 2), :])
plt.title("$|\psi_{nlm}|^2$(x=0,y=0,z): n=" + str(n) + ", l=" + str(l) + ", m=" + str(m))
plt.xlabel('z')
plt.ylabel("$|\psi_{nlm}|^2$")
plt.show()
