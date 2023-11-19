import numpy as np
print(np.__version__)
np.show_config()
Z = np.zeros(10)
print(Z)
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))
#%run `python -c "import numpy; http://numpy.info(numpy.add)"`
Z = np.zeros(10)
Z[4] = 1
print(Z)
Z = np.arange(10,50)
print(Z)
Z = np.arange(50)
Z = Z[::-1]
print(Z)
Z = np.arange(9).reshape(3,3)
print(Z)
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
Z = np.eye(3)
print(Z)
Z = np.random.random((3,3,3))
print(Z)
Z = np.random.random((10,10)) 
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)
Z = np.random.random(30)
m = Z.mean()
print(m)
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
print(np.unravel_index(100,(6,7,8)))
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
color = np.dtype([("r", np.ubyte, 1),
("g", np.ubyte, 1),
("b", np.ubyte, 1),
("a", np.ubyte, 1)])
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)
Z = np.ones((5,3)) @ np.ones((3,2))
print(Z)
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))
Z = np.random.uniform(-10,+10,10)
print (np.copysign(np.ceil(np.abs(Z)), Z))
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0
_ = np.seterr(**defaults)
with np.errstate(divide='ignore'):
  Z = np.ones(1) / 0
  np.sqrt(-1) == np.emath.sqrt(-1)
  yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
  today = np.datetime64('today', 'D')
  tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
  Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
  print(Z)
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)
Z = np.random.uniform(0,10,10)
print (Z - Z%1)
print (np.floor(Z))
print (np.ceil(Z)-1)
print (Z.astype(int))
print (np.trunc(Z))
Z = np.zeros((5,5))
Z += np.arange(5)
print(Z)
def generate():
  for x in range(10):
    yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)
Z = np.linspace(0,1,12,endpoint=True)[1:-1]
print(Z)
Z = np.random.random(10)
Z.sort()
print(Z)
Z = np.arange(10)
np.add.reduce(Z)
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A,B)
print(equal)
equal = np.array_equal(A,B)
print(equal)
Z = np.zeros(10)
Z.flags.writeable = False
Z[0] = 1
Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(R)
print(T)
Z = np.random.random(10)
Z[Z.argmax()] = 0
print(Z)
Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),
np.linspace(0,1,5))
print(Z)
X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
print(np.linalg.det(C))
for dtype in [np.int8, np.int32, np.int64]:
  print(np.info(dtype).min)
  print(np.info(dtype).max)
for dtype in [np.float32, np.float64]:
  print(np.finfo(dtype).min)
  print(np.finfo(dtype).max)
  print(np.finfo(dtype).eps)
np.set_printoptions(threshold=np.nan)
Z = np.zeros((16,16))
print(Z)
Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()
print(Z[index])
Z = np.zeros(10, [ ('position', [ ('x', float, 1),
('y', float, 1)]),
('color', [ ('r', float, 1),
('g', float, 1),
('b', float, 1)])])
print(Z)
Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0], Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)
import scipy
import scipy.spatial
Z = np.random.random((10,2))
D = scipy.spatial.distance.cdist(Z,Z)
print(D)
Z = np.arange(10, dtype=np.int32)
Z = Z.astype(np.float32, copy=False)
print(Z)
from io import StringIO
s = StringIO("""1, 2, 3, 4, 5\n
6, , , 7, 8\n
, , 9,10,11\n""")
Z = np.genfromtxt(s, delimiter=",", dtype="https://np.int" )
print(Z)
Z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(Z):
  print(index, value)
for index in np.ndindex(Z.shape):
  print(index, Z[index])
X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
print(G)
n = 10
p = 3
Z = np.zeros((n,n))
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)
print(Z)
X = np.random.rand(5, 10)
Y = X - X.mean(axis=1, keepdims=True)
Y = X - X.mean(axis=1).reshape(-1, 1)
print(Y)
Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])
Z = np.random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())
Z = np.random.uniform(0,1,10)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)
A = np.arange(3).reshape(3,1)
B = np.arange(3).reshape(1,3)
it = np.nditer([A,B,None])
for x,y,z in it: z[...] = x + y
print(it.operands[2])
class NamedArray(np.ndarray):
  def __new__(cls, array, name="no name"):
    obj = np.asarray(array).view(cls)
    obj.name = name
    return obj
def __array_finalize__(self, obj):
  if obj is None: return
    "https://self.info" = getattr(obj, 'name', "no name")
    Z = NamedArray(np.arange(10), "range_10")
    print (Z.name)
    Z = np.ones(10)
    I = np.random.randint(0,len(Z),20)
    Z += np.bincount(I, minlength=len(Z))
    print(Z)
    np.add.at(Z, I, 1)
    print(Z)
    X = [1,2,3,4,5,6]
    I = [1,3,9,3,4,1]
    F = np.bincount(I,X)
    print(F)
w,h = 16,16
I = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)
F = I[...,0]*256*256 + I[...,1]*256 +I[...,2]
n = len(np.unique(F))
print(np.unique(I))
A = np.random.randint(0,10,(3,4,3,4))
sum = A.sum(axis=(-2,-1))
print(sum)
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)
D = np.random.uniform(0,1,100)
S = np.random.randint(0,10,100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
print(D_means)