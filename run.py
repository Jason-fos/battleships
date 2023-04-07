# Battleships terminal game written in python
# Import modules
import random
import sys
import time

# CPU and player boards, small and big
player_board_small = [[''] * 6 for x in range(6)]
cpu_board_small = [[''] * 6 for x in range(6)]
player_board_big = [[''] * 9 for x in range(9)]
cpu_board_big = [[''] * 9 for x in range(9)]