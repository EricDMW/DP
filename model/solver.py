#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File   : implementation.py
@Author : Dongming Wang
@Email  : dongming.wang@email.ucr.edu
@Project: DP
@Date   : 10/23/2024
@Time   : 16:32:29
@Info   : main func
"""
# Solve potential root issues
import sys
from pathlib import Path
path_dir = Path(__file__).resolve().parents[0]
sys.path.append(str(path_dir))


import math
from root_solve import root_solve
import sympy as sp


class calculate_station_prob:
    def __init__(self, N=6, r_t=0.5, r_c = 0.5, gamma=0.9,**args):
        """
        Constructor for calculate_station_prob
        """
        # Initialize class calculate_station_prob attributes here
        self.N = N
        self.r_t = r_t
        self.r_c = r_c / N
        self.gamma = gamma
        
        # For recording the p here
        self.prob = [0]
        self.v_func = [0]
        
        # Initialize the solver
        self.solver = root_solve.root_forpoly
        
        
    def prob_solve(self,i):
        """
        Description of the function functions.
        """
        # Implement function logic here
        # For coding efficiency
        C = math.comb
        # Define the symbolic variable and polynomial
        x = sp.symbols('x')
        
        # Calculate the polynomials f(x) = p(x)/q(x)
        q = 1 - self.gamma * C(i,0) * (1-x)**i
        # Initialize a default p with the last term of it
        p = C(i,0)*(1-x)**i*i*self.r_t
        
        for k in range(i):
            p += C(i,i-k)*x**(i-k)*(1-x)**k*(i*self.r_t+((i-k)>1)*(i-k)**2*self.r_c+self.gamma*self.v_func[k])
            
        f_x, x = self.solver(p,q)
        self.v_func.append(f_x)
        self.prob.append(x)





# def main():
#    test_class = calculate_station_prob()
   
#    for i in range(6):
#        test_class.prob_solve(i+1)
    
#    print(test_class.v_func)

# if __name__ == '__main__':
#     main()