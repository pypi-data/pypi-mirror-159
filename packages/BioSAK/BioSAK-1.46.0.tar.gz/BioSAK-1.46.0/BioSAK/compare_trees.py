import os
import argparse
from BioSAK.BioSAK_config import config_dict


compare_trees_usage = '''
============= compare_trees example command =============

BioSAK compare_trees -t1 tree_1.newick -t2 tree_2.newick

=========================================================
'''


def compare_trees(args):

    compare_trees_R = config_dict['compare_trees_R']
    tree_file_1 = args['t1']
    tree_file_2 = args['t2']
    compare_trees_cmd = 'Rscript %s -a %s -b %s' % (compare_trees_R, tree_file_1, tree_file_2)
    os.system(compare_trees_cmd)


if __name__ == '__main__':

    compare_trees_parser = argparse.ArgumentParser(usage=compare_trees_usage)
    compare_trees_parser.add_argument('-t1', required=True, help='tree 1')
    compare_trees_parser.add_argument('-t2', required=True, help='tree 2')
    args = vars(compare_trees_parser.parse_args())

    compare_trees(args)
