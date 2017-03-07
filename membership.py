"""Fuzzy Membership Functions for FMMs"""
import numpy as np


class FuzzyMembershipFunction:
    """The standard Fuzzy Membership Function, introduced by Simpson"""

    def __init__(self, parent, gamma=1):
        """
        :param parent: the GFMM reference for accessing variables
        :param gamma: sensitivity parameter
        """
        self.parent = parent
        self.gamma = gamma

    def degree(self, al, au):
        """
        Returns the degree-of-membership for a given hyperbox
        :param al: The min value of the h'th input vector to consider
        :param au: The max value of the h'th input vector to consider
        :return: the degree of membership for all hyperboxes has for input Ah
        """
        dw = au.reshape(len(au), 1) - self.W
        dw = self._inner_maxmins(dw)
        dv = self.V - al.reshape(len(al), 1)
        dv = self._inner_maxmins(dv)
        wv = np.add(dw, dv)
        total = np.sum(wv, axis=0) * (1 / (2 * self.n))
        return total
    
    def _inner_maxmins(self, q):
        q[q > 1] = 1  # min(1, q)
        q *= self.gamma
        q[q < 0] = 0  # max(0, γ*min(1,q))
        q = 1 - q
        q[q < 0] = 0  # max(0, 1-max(0, γ*min(1,q)))
        return q

    def __call__(self, *args, **kwargs):
        return self.degree(*args)

    @property
    def V(self):
        return self.parent.V

    @property
    def W(self):
        return self.parent.W

    @property
    def n(self):
        """ number of dimensions. """
        return self.parent.n or self.parent.V.shape[0]


class Clustering(FuzzyMembershipFunction):
    pass


class General(FuzzyMembershipFunction):
    pass
