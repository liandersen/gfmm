import numpy as np
import membership


class GFMM:

    def __init__(self, membership_func=membership.Classification):
        print('Hello GFMM')
        self.X_l = np.zeros((0, 0))
        self.X_u = np.zeros((0, 0))
        self.n = 0
        self.mfunc = membership_func(self)

    def fit(self, X, Y):
        """
        :param X: array-like, size=[n_samples, n_features]
            Training Data
        :param Y: array, dtype=float64, size=[n_samples]
            Target Values
            note that d=0 corresponds to an unlabeled item
        """
        # TODO: check to see if X is (X_l, X_u); otherwise default to assume they are the same
        self.X_l = X
        self.X_u = np.copy(X)

        self.n = len(X[0])
        self._initialize(self.n)

    def predict(self, X):
        pass

    def _expansion(self):
        pass

    def _overlap_test(self):
        pass

    def _contraction(self):
        pass

    def _initialize(self, n):
        """
        Initializes the V and W matrices
        :param n: the number of input dimensions
        """
        self.V = np.zeros((n, 1))
        self.W = np.zeros((n, 1))
