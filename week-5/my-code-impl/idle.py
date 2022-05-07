Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:\OneDrive\current-month-workspace\apr\intro-to-ml-mit-ex\week5\code_and_data_for_hw05\code_and_data_for_hw05\code_for_hw5.py
X = np.array([[ 1.,  2.,  3.,  4.], [ 1.,  1.,  1.,  1.]])
th = np.array([[ 1.  ], [ 0.05]]); th0 = np.array([[ 2.]])
d_lin_reg_th(X[:,0:1], th, th0).tolist()
[[1.0], [1.0]]
d_lin_reg_th(X, th, th0).tolist()
[[1.0, 2.0, 3.0, 4.0], [1.0, 1.0, 1.0, 1.0]]
Y = np.array([[ 1. ,  2.2,  2.8,  4.1]])
d_square_loss_th(X[:,0:1], Y[:,0:1], th, th0).tolist()
[[4.1], [4.1]]
d_square_loss_th(X, Y, th, th0).tolist()
[[4.1, 7.399999999999999, 13.5, 15.600000000000001], [4.1, 3.6999999999999993, 4.5, 3.9000000000000004]]
np.mean(d_square_loss_th(x, y, th, th0), axis = 1, keepdims = True)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    np.mean(d_square_loss_th(x, y, th, th0), axis = 1, keepdims = True)
NameError: name 'x' is not defined. Did you mean: 'X'?
np.mean(d_square_loss_th(X, y, th, th0), axis = 1, keepdims = True)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    np.mean(d_square_loss_th(X, y, th, th0), axis = 1, keepdims = True)
NameError: name 'y' is not defined. Did you mean: 'Y'?
np.mean(d_square_loss_th(X, Y, th, th0), axis = 1, keepdims = True)
array([[10.15],
       [ 4.05]])

= RESTART: D:\OneDrive\current-month-workspace\apr\intro-to-ml-mit-ex\week5\code_and_data_for_hw05\code_and_data_for_hw05\code_for_hw5.py

= RESTART: D:\OneDrive\current-month-workspace\apr\intro-to-ml-mit-ex\week5\code_and_data_for_hw05\code_and_data_for_hw05\code_for_hw5.py
X = np.array([[ 1.,  2.,  3.,  4.], [ 1.,  1.,  1.,  1.]])
th = np.array([[ 1.  ], [ 0.05]]); th0 = np.array([[ 2.]])
th
array([[1.  ],
       [0.05]])
Y
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Y
NameError: name 'Y' is not defined
Y = np.array([[ 1. ,  2.2,  2.8,  4.1]])
d_ridge_obj_th(X, Y, th, th0, 0.0).tolist()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d_ridge_obj_th(X, Y, th, th0, 0.0).tolist()
  File "D:\OneDrive\current-month-workspace\apr\intro-to-ml-mit-ex\week5\code_and_data_for_hw05\code_and_data_for_hw05\code_for_hw5.py", line 206, in d_ridge_obj_th
    return 2 / n * x @ (th.T @ x + th0 - y) + 2 * lam * th
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 1 is different from 4)
_, n = x.shape
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    _, n = x.shape
NameError: name 'x' is not defined. Did you mean: 'X'?
_, n = X.shape

= RESTART: D:\OneDrive\current-month-workspace\apr\intro-to-ml-mit-ex\week5\code_and_data_for_hw05\code_and_data_for_hw05\code_for_hw5.py
X = np.array([[ 1.,  2.,  3.,  4.], [ 1.,  1.,  1.,  1.]])
th = np.array([[ 1.  ], [ 0.05]]); th0 = np.array([[ 2.]])
Y = np.array([[ 1. ,  2.2,  2.8,  4.1]])
d_ridge_obj_th(X, Y, th, th0, 0.0).tolist()
[[10.15], [4.05]]
np.mean(th.T @ X + th0 - y))
SyntaxError: unmatched ')'
np.mean(th.T @ X + th0 - y)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    np.mean(th.T @ X + th0 - y)
NameError: name 'y' is not defined. Did you mean: 'Y'?
np.mean(th.T @ X + th0 - Y)
2.025
np.mean(th.T @ X + th0 - Y) * 2
4.05
def d_ridge_obj_th0(x, y, th, th0, lam):
    return 2 * np.mean(th.T @ x + th0 - y, axis = 1, keepdims = True)

d_ridge_obj_th0(X, Y, th, th0, 0.0).tolist()
[[4.05]]
d_ridge_obj_th0(X, Y, th, th0, 100.).tolist()
[[4.05]]



np.random.randint(100)
55
X[:,2:3]
array([[3.],
       [1.]])
range(0, 0.1, 10)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    range(0, 0.1, 10)
TypeError: 'float' object cannot be interpreted as an integer
range(0, 0.1, .01)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    range(0, 0.1, .01)
TypeError: 'float' object cannot be interpreted as an integer
