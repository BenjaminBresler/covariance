"""This module contains functions for implementing a Kalman filter."""

import numpy as np

def prop_cov(P0, stm, Q=0):
    """Return the result of a covariance matrix propagation."""
    cov = stm * P0 * stm.T + Q
    return P

def msr_update(P_bar, H, R, K):
    """Perform a measurement update on an initial coavariance matrix, P_bar,
    given a measurement sensitivity matrix and measurement noise covariance."""
    I_KH = np.eye(np.size(P_bar,0))
    P_hat = (I_KH * P_bar * I_KH.T) + K*R*K.T
    return P_hat

def calc_optimal_gain(P_bar, H, R):
    """Return the optimal Kalman gain matrix given initial covariance,
    measurement sensitivity matrix, and measurement noise covariance."""
    HT = H.T
    K = P_bar * HT * (H * P_bar * HT + R).pseudoInverse()
    return K

def enforce_pos_def(m):
    """Enforce matrix positive definiteness."""
    matPosDef = (m + m.T)/2
    return matPosDef

def run_filter()