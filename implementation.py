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
import math

import sympy as sp


from model import root_solve

def functions():
    # Model parameters
    N = 6
    r_t = 0.5
    r_c = 0.5 / N
    gamma = 0.9
    
    # For coding efficiency
    C = math.comb
    
    # Define the symbolic variable and polynomial
    x = sp.symbols('x')
    
    # Calculate P_1 and V_1
    # p = r_t
    # q = 1 - gamma + x * gamma # Solution p_1 = 1.0, v_1 = 0.5
    v_1 = 0.5
    
    # Calculate P_2 and V_2
    # p = C(2,2)*x**2*(2*r_t+2**2*r_c) + C(2,1)*x*(1-x)*(2*r_t+gamma*v_1) + C(2,0)*(1-x)**2*(2*r_t)
    # q = 1 - C(2,0)*(1-x)**2*gamma # Solution p_2 = 1.0, v_2 = 1.3333333730697632
    v_2 = 1.3333333730697632
    
    # Calculate P_3 and V_3
    # p = C(3,3)*x**3*(3*r_t+3**2*r_c) + C(3,2)*x**2*(1-x)*(3*r_t+2**2*r_c+gamma*v_1)\
    #     +C(3,1)*x*(1-x)**2*(3*r_t+gamma*v_2)+C(3,0)*(1-x)**3*3*r_t
    # q = 1 - C(3,0)*(1-x)**3*gamma # Solution p_3 = 1.0, v_3 = 2.25
    v_3 = 2.25
    
    
    # Calculate P_4 and V_4
    # p = C(4,4)*x**4*(4*r_t+4**2*r_c) + C(4,3)*x**3*(1-x)*(4*r_t+3**2*r_c+gamma*v_1)\
    #     + C(4,2)*x**2*(1-x)**2*(4*r_t+2**2*r_c+gamma*v_2) + C(4,1)*x*(1-x)**3*(4*r_t+gamma*v_3)\
    #         + C(4,0)*(1-x)**4*4*r_t
    # q = 1 - C(4,0)*(1-x)**4*gamma # Solution p_4 = 0.8981289863586426, v_4 = 3.306820869445801
    v_4 = 3.306820869445801
    
    
    # Calculate P_5 and V_5
    # p = C(5,5)*x**5*(5*r_t+5**2*r_c) + C(5,4)*x**4*(1-x)*(5*r_t+4**2*r_c+gamma*v_1)\
    #     + C(5,3)*x**3*(1-x)**2*(5*r_t+3**2*r_c+gamma*v_2) + C(5,2)*x**2*(1-x)**3*(5*r_t+2**2*r_c+gamma*v_3)\
    #         + C(5,1)*x*(1-x)**4*(5*r_t+gamma*v_4) + C(5,0)*(1-x)**5*5*r_t
    # q = 1 - C(5,0)*(1-x)**5*gamma # Solution p_5 = 0.8174982070922852, v_5 = 4.452413558959961
    v_5 = 4.452413558959961
    
    # Calculate P_6 and V_6
    p = C(6,6)*x**6*(6*r_t+6**2*r_c) + C(6,5)*x**5*(1-x)*(6*r_t+5**2*r_c+gamma*v_1)\
        + C(6,4)*x**4*(1-x)**2*(6*r_t+4**2*r_c+gamma*v_2) + C(6,3)*x**3*(1-x)**3*(6*r_t+3**2*r_c+gamma*v_3)\
            + C(6,2)*x**2*(1-x)**4*(6*r_t+2**2*r_c+gamma*v_4) + C(6,1)*x*(1-x)**5*(6*r_t+gamma*v_5)\
                + C(6,0)*(1-x)**6*6*r_t
    q = 1 - C(6,0)*(1-x)**6*gamma # Solution p_6 = 0.756657600402832, v_6 = 5.680700778961182
    
    
    return p,q




def main():
   solver = root_solve.root_forpoly
   p, q = functions()
   f_x, x = solver(p,q)
   print(f'p = {x}\n')
   print(f'v = {f_x}\n')   

if __name__ == '__main__':
    main()