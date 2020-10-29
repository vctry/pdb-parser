import utils
import argparse
import numpy as np


def split_chains(data):
    chains = np.unique(data['chain'])

    for chain in chains:
        chain_data = utils.select_atoms(data, {'chain': chain})

        utils.write_pdb('data/' + chain + '.pdb', chain_data)


def main(f):
    data = utils.pdb_reader(f)
    split_chains(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read a pdb file and '
                                                 'split it in multiple files for each of its chains')
    parser.add_argument('--f', default='data/result.pdb', help='Path to input pdb file')
    args = parser.parse_args()

    main(**vars(args))