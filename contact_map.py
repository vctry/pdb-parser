import utils
import argparse
import numpy as np
import matplotlib.pyplot as plt


def plot_contact_map(data, output_path, col):

    curr_data_A = utils.select_atoms(data, {'chain': ['A'], 'atom_name': ['CA']})
    curr_data_B = utils.select_atoms(data, {'chain': ['B'], 'atom_name': ['CA']})

    curr_data_A.reset_index(drop=True, inplace=True)
    curr_data_B.reset_index(drop=True, inplace=True)

    dist_matrix = np.zeros((len(curr_data_A), len(curr_data_B)))

    for row_idx in range(len(curr_data_A)):
        for col_idx in range(len(curr_data_B)):
            dist = utils.compute_distance(curr_data_A.loc[row_idx], curr_data_B.loc[col_idx])

            if col == 0:
                if dist < 25:
                    dist_matrix[row_idx, col_idx] = 1

            else:
                dist_matrix[row_idx, col_idx] = dist

    if col == 0:
        plt.imshow(dist_matrix, cmap='Greys')
        plt.savefig(output_path)

    else:
        plt.imshow(dist_matrix, cmap='afmhot')
        plt.savefig(output_path)


def main(f, o, col):

    data = utils.pdb_reader(f)
    plot_contact_map(data, o, col)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script plot the contact map '
                                                 'and save it in a file defined by the user.')
    parser.add_argument('-f', '--f', default='data/1jd4.pdb', help='Path to input data file')
    parser.add_argument('-o', '--o', default='data/contact_map.png', help='Path to output image')
    parser.add_argument('-bw', '--bw', action='store_true', help='Use bw option for black and white representation')
    parser.add_argument('-col', '--col', action='store_true', help='Use col option for color representation')

    args = parser.parse_args()

    if args.bw:
        col = 0

    elif args.col:
        col = 1

    else:
        col = 0

    main(args.f, args.o, col)
