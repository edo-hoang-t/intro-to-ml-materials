from curses import curs_set
from util import *
from tests import test_acc_sign_rnn, test_auto_rnn

class SM:
    start_state = None  # default start state

    def transition_fn(self, s, x):
        '''s:       the current state
           x:       the given input
           returns: the next state'''
        raise NotImplementedError

    def output_fn(self, s):
        '''s:       the current state
           returns: the corresponding output'''
        raise NotImplementedError

    def transduce(self, input_seq):
        '''input_seq: the given list of inputs
           returns:   list of outputs given the inputs'''
        # Your code here
        outputs = []
        cur_state = self.start_state
        for input in input_seq:
            cur_state = self.transition_fn(cur_state, input)
            outputs.append(self.output_fn(cur_state))
        return outputs

            


class Accumulator(SM):
    start_state = 0

    def transition_fn(self, s, x):
        return s + x

    def output_fn(self, s):
        return s


class Binary_Addition(SM):
    start_state = [0, 0] # [result, carry]

    def transition_fn(self, s, x): # x: (1, 1)
        # Your code here
        return [int(((x[0] + x[1]) + s[1]) % 2), int(((x[0] + x[1]) + s[1]) / 2)]

    def output_fn(self, s):
        # Your code here
        return s[0]


class Reverser(SM):
    start_state = 0 # stage
    reversed_seq1 = []
    reversed_seq1_id = 0

    def transition_fn(self, s, x): # x: a string
        # Your code here
        if x == 'end':
            s = 1
            return s
        if s == 0:
            self.reversed_seq1.insert(0, x)
            return s
        if s == 2:
            return s
        if self.reversed_seq1_id == len(self.reversed_seq1):
            return 2
        


    def output_fn(self, s):
        # Your code here
        if s == 0 or s == 2:
            return None
        self.reversed_seq1_id += 1
        return self.reversed_seq1[self.reversed_seq1_id - 1]

        


class RNN(SM):

    def __init__(self, Wsx, Wss, Wo, Wss_0, Wo_0, f1, f2):
        # Your code here
        self.Wss = Wss
        self.Wsx = Wsx
        self.Wss_0 = Wss_0
        self.Wo = Wo
        self.Wo_0 = Wo_0
        self.f1 = f1
        self.f2 = f2
        self.start_state = np.zeros((Wss_0.shape[0], 1))

    def transition_fn(self, s, i):
        # Your code here
        return self.f1(self.Wss @ s + self.Wsx @ i + self.Wss_0)

    def output_fn(self, s):
        # Your code here
        return self.f2(self.Wo @ s + self.Wo_0)


# Wsx =    np.array([[1]])
# Wss =    np.array([[1]])
# Wo =     np.array([[100]])
# Wss_0 =  np.array([[0]])
# Wo_0 =   np.array([[0]])
# f1 =     lambda x : x
# f2 =     np.tanh
# acc_sign = RNN(Wsx, Wss, Wo, Wss_0, Wo_0, f1, f2)
# test_acc_sign_rnn(acc_sign)

Wsx =    np.array([[1], [0], [0]])
Wss =    np.array([[0, 0, 0],
                   [1, 0, 0],
                   [0, 1, 0]])
Wo =     np.array([[1, -2, 3]]) # shape=(1, 3)
Wss_0 =  np.array([[0], [0], [0]])
Wo_0 =   np.array([[0]])
f1 =     lambda x: x
f2 =     lambda x: x
auto = RNN(Wsx, Wss, Wo, Wss_0, Wo_0, f1, f2)
test_auto_rnn(auto)