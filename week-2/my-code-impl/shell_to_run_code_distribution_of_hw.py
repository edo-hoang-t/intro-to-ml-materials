Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 11, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 520, in <module>
    test_linear_classifier(datafn,averaged_perceptron,draw=True)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 391, in test_linear_classifier
    th, th0 = learner(data, labels, hook = hook, params = learner_params)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 505, in averaged_perceptron
    (d, n) = data.shape()
TypeError: 'tuple' object is not callable

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Final score 1.0
Params [[-24.  37.]] [[-3]]
Final score 0.5
Params [[ 0. -3.]] [[0]]
Final score 0.625
Params [[ 1. -3.]] [[0]]
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 520, in <module>
    test_linear_classifier(datafn,averaged_perceptron,draw=True)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 391, in test_linear_classifier
    th, th0 = learner(data, labels, hook = hook, params = learner_params)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 514, in averaged_perceptron
    theta0 += y_i
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Final score 1.0
Params [[-22.1925  34.06  ]] [[-2.1725]]
Final score 0.75
Params [[ 1.47   -1.7275]] [[0.985]]
Final score 0.625
Params [[ 1.48375 -1.85875]] [[0.62]]
Final score 1.0
Params [[16.5602227  23.04911126 12.39596162  6.01919397 -3.46570037 18.12387095]] [[1.4826]]
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 577, in <module>
    test_xval_learning_alg(xval_learning_alg,perceptron)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 474, in test_xval_learning_alg
    result=xval_learning_alg(perceptron, big_data, big_data_labels, 5)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 572, in xval_learning_alg
    sum_score += eval_classifier(learner, D_minus_i, labels_minus_i, D_splitted[i], labels_splitted[i])
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 540, in eval_classifier
    (th, th0) = learner(data_train, labels_train)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 497, in perceptron
    theta0 += y_i
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 579, in <module>
    test_xval_learning_alg(xval_learning_alg,perceptron)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 474, in test_xval_learning_alg
    result=xval_learning_alg(perceptron, big_data, big_data_labels, 5)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 574, in xval_learning_alg
    sum_score += eval_classifier(learner, D_minus_i, labels_minus_i, D_splitted[i], labels_splitted[i])
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 542, in eval_classifier
    (th, th0) = learner(data_train, labels_train)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 497, in perceptron
    theta0 += y_i
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 578, in <module>
    test_xval_learning_alg(xval_learning_alg,perceptron)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 474, in test_xval_learning_alg
    result=xval_learning_alg(perceptron, big_data, big_data_labels, 5)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 574, in xval_learning_alg
    sum_score = sum_score + eval_classifier(learner, D_minus_i, labels_minus_i, D_splitted[i], labels_splitted[i])
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 542, in eval_classifier
    (th, th0) = learner(data_train, labels_train)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 497, in perceptron
    theta0 += y_i
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Final score 1.0
Params [[-9. 18.]] [[2]]
Final score 1.0
Params [[-24.  37.]] [[-3]]

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
-----------Test Perceptron 0-----------
Passed! 

-----------Test Perceptron 1-----------
Passed! 


==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Final score 1.0
Params [[-22.1925  34.06  ]] [[-2.1725]]
Final score 0.75
Params [[ 1.47   -1.7275]] [[0.985]]
Final score 0.625
Params [[ 1.48375 -1.85875]] [[0.62]]
Final score 1.0
Params [[18.67305261 21.08311519 15.69131684  7.16241826 -3.68913036 15.24387375]] [[8.2428]]

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
-----------Test Averaged Perceptron 0-----------
Passed! 

-----------Test Averaged Perceptron 1-----------
Passed! 


==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 546, in <module>
    test_eval_classifier(eval_classifier,perceptron)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 446, in test_eval_classifier
    result = eval_classifier(perceptron, data_train, labels_train,data2,labels2)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 542, in eval_classifier
    (th, th0) = learner(data_train, labels_train)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 497, in perceptron
    theta0 += y_i
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 547, in <module>
    test_eval_classifier(eval_classifier,perceptron)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 446, in test_eval_classifier
    result = eval_classifier(perceptron, data_train, labels_train,data2,labels2)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 542, in eval_classifier
    (th, th0) = learner(data_train, labels_train)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 497, in perceptron
    theta0 += y_i
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'

==== RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ===
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 546, in <module>
    test_eval_classifier(eval_classifier,perceptron)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 446, in test_eval_classifier
    result = eval_classifier(perceptron, data_train, labels_train,data2,labels2)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 542, in eval_classifier
    th, th0 = learner(data_train, labels_train)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 497, in perceptron
    theta0 += y_i
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
-----------Test Eval Classifier 0-----------
Passed! 

-----------Test Eval Classifier 1-----------
Passed! 


========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
-----------Test Eval Learning Algo-----------
Passed! 


========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
-----------Test Cross-eval Learning Algo-----------
Passed! 


========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.5

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.78

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.68

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.7399999999999999

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.6700000000000002

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.7699999999999999

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8700000000000001

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8099999999999999

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.7500000000000001

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.73

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.6700000000000002

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8300000000000001

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8099999999999999

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.86

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.85

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8699999999999999

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.79

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.73

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.86

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8100000000000002

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.7999999999999999

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.75

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8400000000000001

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.76

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8099999999999999

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 584, in <module>
    score += eval_learning_alg(averaged_perceptron, gen_flipped_lin_separable(pflip=.1), 20, 20, 5)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 554, in eval_learning_alg
    sum_accur += eval_classifier(learner, data_train, labels_train, data_test, labels_test)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 543, in eval_classifier
    return score(data_test, labels_test, th, th0) / (data_test.shape[1])
TypeError: 'float' object is not callable

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 584, in <module>
    score += eval_learning_alg(averaged_perceptron, gen_flipped_lin_separable(pflip=.1), 20, 20, 5)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 554, in eval_learning_alg
    sum_accur += eval_classifier(learner, data_train, labels_train, data_test, labels_test)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 543, in eval_classifier
    return score(data_test, labels_test, th, th0) / (data_test.shape[1])
TypeError: 'float' object is not callable

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 584, in <module>
    print(eval_learning_alg(averaged_perceptron, gen_flipped_lin_separable(pflip=.1), 20, 20, 5))
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 554, in eval_learning_alg
    sum_accur += eval_classifier(learner, data_train, labels_train, data_test, labels_test)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 543, in eval_classifier
    return score(data_test, labels_test, th, th0) / (data_test.shape[1])
TypeError: 'float' object is not callable

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.51

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.51
0.45999999999999996
0.43000000000000005
0.52

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 583, in <module>
    score += eval_learning_alg(perceptron, gen_flipped_lin_separable(pflip=.5), 20, 20, 5)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 554, in eval_learning_alg
    sum_accur += eval_classifier(learner, data_train, labels_train, data_test, labels_test)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 543, in eval_classifier
    return score(data_test, labels_test, th, th0) / (data_test.shape[1])
TypeError: 'float' object is not callable

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 583, in <module>
    score = score + eval_learning_alg(perceptron, gen_flipped_lin_separable(pflip=.5), 20, 20, 5)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 554, in eval_learning_alg
    sum_accur += eval_classifier(learner, data_train, labels_train, data_test, labels_test)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 543, in eval_classifier
    return score(data_test, labels_test, th, th0) / (data_test.shape[1])
TypeError: 'float' object is not callable

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
Traceback (most recent call last):
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 583, in <module>
    score = score + eval_learning_alg(perceptron, gen_flipped_lin_separable(pflip=.5), 20, 20, 5)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 554, in eval_learning_alg
    sum_accur += eval_classifier(learner, data_train, labels_train, data_test, labels_test)
  File "D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py", line 543, in eval_classifier
    return score(data_test, labels_test, th, th0) / (data_test.shape[1])
TypeError: 'int' object is not callable

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
score_sum
2.32

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.7820000000000003

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.5615

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.605

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.6352

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.7284000000000002

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8656000000000001

========= RESTART: D:\stuff\mar\code_for_hw02_downloadable\code_for_hw02_downloadable.py ========
0.8442000000000002
0.6779999999999999
