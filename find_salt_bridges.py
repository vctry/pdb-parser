import utils
import argparse


def find_salt_bridges(data, output_path):
    bridges = []

    for chain in data['chain'].unique():
        curr_data = utils.select_atoms(data, {'chain': [chain]})

        for row_idx in range(len(curr_data)):
            for sec_row_idx in range(len(curr_data)):
                if row_idx != sec_row_idx:
                    dist = utils.compute_distance(curr_data.loc[row_idx], curr_data.loc[sec_row_idx])

                    if dist < 2.5:
                        bridges.append(str([curr_data.loc[row_idx]['resname'] + '-'
                                            + str(curr_data.loc[row_idx]['resseq']),
                                            curr_data.loc[sec_row_idx]['resname'] + '-'
                                            + str(curr_data.loc[sec_row_idx]['resseq'])]))

    with open(output_path, 'w') as fl:
        fl.write('\n')


def main(f, o):

    data = utils.pdb_reader(f)
    find_salt_bridges(data, o)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find all salt bridges in a pandas data frame '
                                                 'and return them as a list of residue pairs'
                                                 '\n'
                                                 'Example of usage: '
                                                 'find_salt_bidges.py -f ../my_pdb.pdb -o my_pdb_bridges.txt')
    parser.add_argument('-f', '--f', default='data/1jd4.pdb', help='Path to input pdb file')
    parser.add_argument('-o', '--o', default='data/salt_bridges.txt', help='Path to output txt file')
    args = parser.parse_args()

    main(**vars(args))
