import numpy as np

def SM(z): # z_l: n_l x 1 
  # implement softmax
  return np.exp(z) / np.sum(np.exp(z))

''' === PROBLEM 2
z = np.array([[-1, 0, 1]]).T
# print(SM(z))

w = np.array([[1, -1, -2], [-1, 2, 1]])
x = np.array([[1], [1]])
y = np.array([[0, 1, 0]]).T

w_grad = x @ (SM(w.T @ x) - y).T
w = w - 0.5 * w_grad
print(SM(w.T @ x))
'''

# layer 1 weights
w_1 = np.array([[1, 0, -1, 0], [0, 1, 0, -1]])
w_1_bias = np.array([[-1, -1, -1, -1]]).T
# layer 2 weights
w_2 = np.array([[1, -1], [1, -1], [1, -1], [1, -1]])
w_2_bias = np.array([[0, 2]]).T

# your code here
X = np.array([[3, 14]]).T

def relu(z):
    return np.where(z <= 0, 0, z)

# 3.1.A
a_1 = relu(w_1.T @ X + w_1_bias)
a_2 = SM(w_2.T @ a_1 + w_2_bias)
# print(a_2)

# 3.2.C
X = np.array([[0.5, 0, -3], [0.5, 2, 0.5]])
z_1 = w_1.T @ X + w_1_bias
a_1 = relu(z_1)
print(a_1)