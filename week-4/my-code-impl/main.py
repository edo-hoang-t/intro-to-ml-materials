from re import X
import numpy as np
from pytest import PytestAssertRewriteWarning

def rv(value_list):
    return np.array([value_list])

def cv(value_list):
    return np.transpose(rv(value_list))

def f1(x):
    return float((2 * x + 3)**2)

def df1(x):
    return 2 * 2 * (2 * x + 3)

def f2(v):
    x = float(v[0]); y = float(v[1])
    return (x - 2.) * (x - 3.) * (x + 3.) * (x + 1.) + (x + y -1)**2

def df2(v):
    x = float(v[0]); y = float(v[1])
    return cv([(-3. + x) * (-2. + x) * (1. + x) + \
               (-3. + x) * (-2. + x) * (3. + x) + \
               (-3. + x) * (1. + x) * (3. + x) + \
               (-2. + x) * (1. + x) * (3. + x) + \
               2 * (-1. + x + y),
               2 * (-1. + x + y)])

def gd(f, df, x0, step_size_fn, max_iter):
    '''
    f: given function, e.g. f1, f2 above
    df: derivative of function f (also given), e.g. df1, df2 above
    x: value of BIG theta (including theta0)
    step_size_fn: i.e. eta
    max_iter: T
    '''
    fs = [f(x0)]
    xs = [x0]
    for i in range(max_iter):
        x0 = x0 - step_size_fn(i) * df(x0)
        fs.append(f(x0))
        xs.append(x0)
    return x0, fs, xs


# TEST gd function
def package_ans(gd_vals):
    x, fs, xs = gd_vals
    return [x.tolist(), [fs[0], fs[-1]], [xs[0].tolist(), xs[-1].tolist()]]

# Test case 1
# ans=package_ans(gd(f1, df1, cv([0.]), lambda i: 0.1, 1000))

# Test case 2
# ans=package_ans(gd(f2, df2, cv([0., 0.]), lambda i: 0.01, 1000))

########################################################

def num_grad(f, delta=0.001):
    def fx(x): # x is a column vector
        res = []
        for i in range(len(x)):
            delta_i = np.zeros(x.shape)
            delta_i[i] += delta
            res.append((f(x + delta_i) - f(x - delta_i)) / (2 * delta))
        return cv(res)
    return fx

# TEST CASE
x = cv([0.])
ans=(num_grad(f1)(x).tolist(), x.tolist())

x = cv([0.1])
ans=(num_grad(f1)(x).tolist(), x.tolist())

x = cv([0., 0.])
ans=(num_grad(f2)(x).tolist(), x.tolist())

x = cv([0.1, -0.1])
ans=(num_grad(f2)(x).tolist(), x.tolist())

########################################################
def minimize(f, x0, step_size_fn, max_iter):
    numerical_df = num_grad(f)
    return gd(f, numerical_df, x0, step_size_fn, max_iter)

########################################################
# 7.1) Calculating the SVM objective 

def hinge(v): # v: 1 x n
    return np.where(v >= 1, 0, 1 - v)

# x is d x n, y is 1 x n, th is d x 1, th0 is 1 x 1
def hinge_loss(x, y, th, th0):
    return hinge((th.T @ x + th0) * y) # 1 x n

# x is dxn, y is 1xn, th is dx1, th0 is 1x1, lam is a scalar
def svm_obj(x, y, th, th0, lam):
    return np.sum(hinge_loss(x, y, th, th0)) / y.shape[1] + lam * ((th.T @ th)[0][0])


# TEST CASE
def super_simple_separable():
    X = np.array([[2, 3, 9, 12],
                  [5, 2, 6, 5]])
    y = np.array([[1, -1, 1, -1]])
    return X, y

sep_e_separator = np.array([[-0.40338351], [1.1849563]]), np.array([[-2.26910091]])

# Test case 1
x_1, y_1 = super_simple_separable()
th1, th1_0 = sep_e_separator
ans = svm_obj(x_1, y_1, th1, th1_0, .1)

# Test case 2
ans = svm_obj(x_1, y_1, th1, th1_0, 0.0)

#########################################################
# 7.2) Calculating the SVM gradient

# Returns the gradient of hinge(v) with respect to v.
def d_hinge(v):
    return np.where(v >= 1, 0, -1)

# Returns the gradient of hinge_loss(x, y, th, th0) with respect to th
def d_hinge_loss_th(x, y, th, th0):
    return -1 * x * d_hinge(y * (th.T @ x + th0))

# Returns the gradient of hinge_loss(x, y, th, th0) with respect to th0
def d_hinge_loss_th0(x, y, th, th0):
    return -1 * d_hinge(y * (th.T @ x + th0)) # 1 x n

# Returns the gradient of svm_obj(x, y, th, th0) with respect to th
def d_svm_obj_th(x, y, th, th0, lam):
    d, n = x.shape
    return (np.reshape(np.sum(d_hinge_loss_th(x, y, th, th0), axis=1), (d, 1)) / n) + 2 * lam * th

# Returns the gradient of svm_obj(x, y, th, th0) with respect to th0
def d_svm_obj_th0(x, y, th, th0, lam):
    d, n = x.shape
    return np.reshape(np.sum(d_hinge_loss_th0(x, y, th, th0), axis=1), (1, 1)) / n

# Returns the full gradient as a single vector (which includes both th, th0)
def svm_obj_grad(X, y, th, th0, lam):
    return np.vstack((d_svm_obj_th(X, y, th, th0, lam), d_svm_obj_th0(X, y, th, th0, lam)))

#######################################################
# 7.3) Batch SVM minimize 

def batch_svm_min(data, labels, lam):
    d, n = data.shape
    
    def svm_min_step_size_fn(i):
       return 2/(i+1)**0.5
    
    def f(x0):
        return svm_obj(data, labels, x0[:d, :], x0[d:, :], lam)
    
    def df(x0):
        return svm_obj_grad(data, labels, x0[:d, :], x0[d:, :], lam)
    
    x0 = np.zeros((d + 1, 1))
    
    return gd(f, df, x0, svm_min_step_size_fn, 10)
