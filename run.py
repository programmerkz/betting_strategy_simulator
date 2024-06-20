import getopt
import os
import sys

from hypothesis.real_prob import RealProbHypothesis
from hypothesis.bet_test import BetTestHypothesis


RESOURCE_FILE_NAME = os.path.join('.', 'resources', 'help.txt')

with open(RESOURCE_FILE_NAME, 'r') as f:
    help_information = f.read()

args_list = sys.argv[1:]
short_options = 'hs:'
long_options = ['help', 'simulate']

try:
    args, trailes = getopt.getopt(args_list, short_options, long_options)

    for cur_arg, cur_val in args:
        if cur_arg in ('-h', '--help'):
            print(help_information)
        elif cur_arg in ('-s', '--simulate'):
            if cur_val == '=1':
                RealProbHypothesis().simulate()
            elif cur_val == '=2':
                BetTestHypothesis().simulate()


except getopt.error as err:
    print(f'Argument Error! Reason: {str(err)}', help_information, sep='\n\n')
