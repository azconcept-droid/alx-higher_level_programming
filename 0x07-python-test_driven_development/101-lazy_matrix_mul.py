#!/usr/bin/python3
"""Defines Matrix multiplication using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns multiplication 2 matrices using numpy module
    Args:
        m_a (list of lists of (int/floats)): left hand matrix.
        m_b (list of lists of (int/floats)): right hand matrix.
    """
    result = np.matmul(m_a, m_b)
    return (result)
