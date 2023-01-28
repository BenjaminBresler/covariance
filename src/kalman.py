"""This module contains functions for implementing a Kalman filter."""

import numpy as np

def prop_cov(cov0, stm):
    """Return the result of a covariance matrix propagation."""
    cov = stm * cov0 * stm.T
    return cov

def msr_update(cov0, H, R, K):
    return cov0

def calc_optimal_gain(cov0, H, R):
    return K