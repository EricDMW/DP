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

from model import calculate_station_prob,get_config


def main():
   test_class = calculate_station_prob()
   config = get_config()
   args = config.parse_args()
   # have to start from 1
   for i in range(args.num_init_agents):
       test_class.prob_solve(i+1)
    
   print(test_class.v_func)

if __name__ == '__main__':
    main()