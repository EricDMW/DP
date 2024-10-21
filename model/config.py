#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File   : config.py
@Author : Dongming Wang
@Email  : dongming.wang@email.ucr.edu
@Project: DP
@Date   : 10/21/2024
@Time   : 14:55:48
@Info   : Design the configs
"""


import argparse


def get_config():
    parser = argparse.ArgumentParser(description="DP parameters used")
    parser.add_argument('--decay_factor',
                        type=float, 
                        default=0.9, 
                        help="decaying factor")
    parser.add_argument('--environment_graph', 
                        type=dict, 
                        default={1:2,
                                 2:[1,3],
                                 3:2},
                        help='default environmental communication graph')
    
    return parser