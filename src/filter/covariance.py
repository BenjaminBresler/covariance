"""This module contains class definitions for the covariance matrix and its
derivatives (information, information square root)."""

from abc import ABC, abstractmethod

class ErrorMatrix(ABC):
    """Abstract class for a generic error statistics matrix. Defines the 
    required methods for child classes."""

    def __init__(self, arr):
        self.arr = arr

    @abstractmethod
    def time_update(self):
        pass

    @abstractmethod
    def measurement_update(self):
        pass

    @abstractmethod
    def sigmas(self):
        pass


class Covariance(ErrorMatrix):
    """Error covariance matrix."""

    def time_update(self, phi, Q)