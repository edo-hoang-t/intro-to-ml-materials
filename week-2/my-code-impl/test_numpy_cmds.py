Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
data = np.transpose(np.array([[1, 2], [1, 3], [2, 1], [1, -1], [2, -1]]))
data
array([[ 1,  1,  2,  1,  2],
       [ 2,  3,  1, -1, -1]])
labels = rv([-1, -1, +1, +1, +1])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    labels = rv([-1, -1, +1, +1, +1])
NameError: name 'rv' is not defined
np.array([[1, 2],[3, 4]]) == 3
array([[False, False],
       [ True, False]])
x = np.arange(8.0)
x
array([0., 1., 2., 3., 4., 5., 6., 7.])
9 // 4
2
a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
a
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])
np.split(a, 1)
[array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])]
np.split(a, 2)
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]])]
np.split(a, 2, axis=1)
[array([[1],
       [3],
       [5],
       [7]]), array([[2],
       [4],
       [6],
       [8]])]
np.split(a, 1, axis=1)
[array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])]
np.split(a, [1], axis=1)
[array([[1],
       [3],
       [5],
       [7]]), array([[2],
       [4],
       [6],
       [8]])]
np.split(a, [1])
[array([[1, 2]]), array([[3, 4],
       [5, 6],
       [7, 8]])]
tup = (1,2)
tup[0]
1
tup[2]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tup[2]
IndexError: tuple index out of range
tup[1]
2
(x, y) = tup
x
1
y
2
theta = np.array([[0]])
theta
array([[0]])
theta.shape
(1, 1)
labels = np.zeroes((1, 10))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    labels = np.zeroes((1, 10))
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python310\lib\site-packages\numpy\__init__.py", line 315, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'zeroes'. Did you mean: 'zeros'?
labels = np.zeros((1, 10))
                         
labels
                         
array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
labels[0]
                         
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
labels[5]
                         
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    labels[5]
IndexError: index 5 is out of bounds for axis 0 with size 1
labels[0][2
          ]
                         
0.0
labels.shape
                         
(1, 10)
a = np.array([[1, 2], [3, 4]])
                         
a[:, 0]
                         
array([1, 3])
a[:, [0]]
                         
array([[1],
       [3]])
x = 1
                         
x += 2
                         
x
                         
3
a
                         
array([[1, 2],
       [3, 4]])
a += 2
                         
a
                         
array([[3, 4],
       [5, 6]])
a[:, [1]]
                         
array([[4],
       [6]])
th = np.array([[1], [1]])
                         
th += a[:, [1]] * -1
                         
th
                         
array([[-3],
       [-5]])
a[:, 0]
                         
array([3, 5])
a[:, 0].T
                         
array([3, 5])
a[:, [0]].T
                         
array([[3, 5]])
a[:, [0]]
                         
array([[3],
       [5]])
a[:, [0]] += th
                         
a[:, [0]]
                         
array([[0],
       [0]])
th /= 2
                         
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    th /= 2
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'true_divide' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'
th
                         
array([[-3],
       [-5]])
th / 2
                         
array([[-1.5],
       [-2.5]])
th = th / 2
                         
th
                         
array([[-1.5],
       [-2.5]])
x = np.arange(8.0)
                         
np.array_split(x, 4)
                         
[array([0., 1.]), array([2., 3.]), array([4., 5.]), array([6., 7.])]
np.array_split(x, 4)[2:4]
                         
[array([4., 5.]), array([6., 7.])]
np.concatenate(np.array_split(x, 4)[2:4])
                         
array([4., 5., 6., 7.])
np.concatenate(np.array_split(x, 4)[2:4], axis=1)
                         
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    np.concatenate(np.array_split(x, 4)[2:4], axis=1)
  File "<__array_function__ internals>", line 180, in concatenate
numpy.AxisError: axis 1 is out of bounds for array of dimension 1
np.array([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
         )
                         
array([[1, 2, 3, 4, 5, 6, 7, 8],
       [1, 2, 3, 4, 5, 6, 7, 8]])
arr = np.array([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]])
                         
np.array_split(arr, 4)
                         
[array([[1, 2, 3, 4, 5, 6, 7, 8]]), array([[1, 2, 3, 4, 5, 6, 7, 8]]), array([], shape=(0, 8), dtype=int32), array([], shape=(0, 8), dtype=int32)]
KeyboardInterrupt
np.array_split(arr, 4, axis=1)
                         
[array([[1, 2],
       [1, 2]]), array([[3, 4],
       [3, 4]]), array([[5, 6],
       [5, 6]]), array([[7, 8],
       [7, 8]])]
splitted = np.array_split(arr, 4, axis=1)
                         
k = 0
                         
splitted[0:0]
                         
[]
left = np.concatenate(splitted[0:k])
                         
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    left = np.concatenate(splitted[0:k])
  File "<__array_function__ internals>", line 180, in concatenate
ValueError: need at least one array to concatenate
splitted[1:4]
                         
[array([[3, 4],
       [3, 4]]), array([[5, 6],
       [5, 6]]), array([[7, 8],
       [7, 8]])]
splitted[1:3]
                         
[array([[3, 4],
       [3, 4]]), array([[5, 6],
       [5, 6]])]
left_half = splitted[0:i]
                         
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    left_half = splitted[0:i]
NameError: name 'i' is not defined. Did you mean: 'id'?
left_half = splitted[0:k]
                         
left_half
                         
[]
right_half = splitted[(k+1):4]
                         
right_half
                         
[array([[3, 4],
       [3, 4]]), array([[5, 6],
       [5, 6]]), array([[7, 8],
       [7, 8]])]
np.concatenate((left_half, right_half), axis=1)
                         
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    np.concatenate((left_half, right_half), axis=1)
  File "<__array_function__ internals>", line 180, in concatenate
numpy.AxisError: axis 1 is out of bounds for array of dimension 1
np.concatenate((left_half, right_half), axis=0)
                         
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    np.concatenate((left_half, right_half), axis=0)
  File "<__array_function__ internals>", line 180, in concatenate
ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 1 dimension(s) and the array at index 1 has 3 dimension(s)
left_half.shape
                         
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    left_half.shape
AttributeError: 'list' object has no attribute 'shape'
right_half.shape
                         
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    right_half.shape
AttributeError: 'list' object has no attribute 'shape'
right_half.size
                         
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    right_half.size
AttributeError: 'list' object has no attribute 'size'
length(right_half)
                         
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    length(right_half)
NameError: name 'length' is not defined
size(right_half)
                         
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    size(right_half)
NameError: name 'size' is not defined. Did you mean: 'slice'?
len(right_half)
                         
3
right_half
                         
[array([[3, 4],
       [3, 4]]), array([[5, 6],
       [5, 6]]), array([[7, 8],
       [7, 8]])]

left_half + right_half
                         
[array([[3, 4],
       [3, 4]]), array([[5, 6],
       [5, 6]]), array([[7, 8],
       [7, 8]])]
[left_half + right_half]
                         
[[array([[3, 4],
       [3, 4]]), array([[5, 6],
       [5, 6]]), array([[7, 8],
       [7, 8]])]]
np.concatenate([left_half + right_half], axis=1)
                         
array([[[3, 4],
        [3, 4]],

       [[5, 6],
        [5, 6]],

       [[7, 8],
        [7, 8]]])
np.concatenate([left_half + right_half], axis=1).shape
                         
(3, 2, 2)
np.concatenate(left_half + right_half, axis=1)
                         
array([[3, 4, 5, 6, 7, 8],
       [3, 4, 5, 6, 7, 8]])
splitted[k]
                         
array([[1, 2],
       [1, 2]])
splitted[k].shape
                         
(2, 2)
theta0 = np.array([[0.0]])
                         
theta0
                         
array([[0.]])
theta0.dtype
                         
dtype('float64')
theta0 = np.array([[0]])

theta0
                         
array([[0]])
theta0 += 1
                         
theta0
                         
array([[1]])
theta0 += 1.1
                         
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    theta0 += 1.1
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'
