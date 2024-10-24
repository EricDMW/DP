#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File   : root_solve.py
@Author : Dongming Wang
@Email  : dongming.wang@email.ucr.edu
@Project: DP
@Date   : 10/23/2024
@Time   : 16:15:00
@Info   : Root solve
"""
import math
import torch


import sympy as sp


class root_solve:
    @classmethod
    def root_forpoly(cls,p,q):
        """
        Description of the function root_forpoly.
        """
        # assume the only variable
        x = sp.symbols('x')

        # Define the symbolic function f(x) = p(x)/q(x)

        f_sym = p / q

        # Convert the symbolic expression to a numerical function that PyTorch can use
        f_lambdified = sp.lambdify(x, f_sym, 'numpy')

        # Generate a grid of x values in the interval [0, 1] using PyTorch (GPU-enabled)
        x_values = torch.linspace(0, 1, 100000, device='cuda')

        # Evaluate f(x) using the lambdified function (now a numerical function)
        f_values = torch.tensor(f_lambdified(x_values.cpu().numpy()), device='cuda')

        # Find the minimum value of f(x) and the corresponding x
        min_value, min_idx = torch.min(f_values, dim=0)
        min_x = x_values[min_idx]

        # Move results back to CPU for printing
        min_value_cpu = min_value.cpu().item()
        min_x_cpu = min_x.cpu().item()

        print(f"The minimum value of f(x) on [0,1] is {min_value_cpu} at x = {min_x_cpu}")
        
        return min_value, min_x




