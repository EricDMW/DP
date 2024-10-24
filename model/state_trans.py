#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File   : state_trans.py
@Author : Dongming Wang
@Email  : dongming.wang@email.ucr.edu
@Project: DP
@Date   : 10/21/2024
@Time   : 15:02:31
@Info   : state tansition model
"""

# avoid potential path issues
import sys
from pathlib import Path
path_dir = Path(__file__).resolve().parents[0]

class state_tansation:
    def __init__(self, args):
        """
        Constructor for state_tansation
        """
        self.num_agents = args.num_agents
    