import pandas as pd
import os
import math


def pdb_reader(filepath):

    colspecs = [(0, 6), (6, 11), (12, 16), (16, 17), (17, 20), (21, 22), (22, 26),
                (26, 27), (30, 38), (38, 46), (46, 54), (54, 60), (60, 66), (76, 78),
                (78, 80)]
    names = ['ATOM', 'serial', 'atom_name', 'altloc', 'resname', 'chain', 'resseq',
             'icode', 'x', 'y', 'z', 'occupancy', 'tempfactor', 'element', 'charge']

    pdb_data = pd.read_fwf(filepath, names=names, colspecs=colspecs)
    pdb_data = pdb_data.loc[pdb_data['ATOM'].isin(['ATOM', 'HETATM'])]
    pdb_data['resseq'] = pdb_data['resseq'].astype('int')

    for coords in ['x', 'y', 'z']:
        pdb_data[coords] = pdb_data[coords].astype(float).apply('{:.3f}'.format).astype(float)

    pdb_data.reset_index(drop=True, inplace=True)

    return pdb_data


def write_pdb(filepath, pdb_data):
    colspecs = [(0, 6), (6, 11), (12, 16), (16, 17), (17, 20), (21, 22), (22, 26),
                (26, 27), (30, 38), (38, 46), (46, 54), (54, 60), (60, 66), (76, 78),
                (78, 80)]

    with open(filepath, "w") as fl:
        for idx in range(len(pdb_data)):
            stringToSave = " " * 81
            for elem in range(len(pdb_data.iloc[idx].values)):
                if not pd.isna(pdb_data.iloc[idx].values[elem]):
                    stringToSave = stringToSave[0:colspecs[elem][0]] + str(pdb_data.iloc[idx].values[elem]) + \
                                   stringToSave[colspecs[elem][0] + len(str(pdb_data.iloc[idx].values[elem])):
                                                len(stringToSave)]

            fl.write('{}'.format(stringToSave))

            fl.write('\n')

        fl.write('END')


def select_atoms(data, selector):
    result = data

    for idx in selector:
        result = result.loc[result[idx].isin(selector[idx])]

    result.reset_index(drop=True, inplace=True)

    return result


def get_aa_seq(data):
    for chain in data['chain'].unique():
        print('\nChain ID: %s' % chain)
        chainStr = ''

        for row in data.loc[data['chain'] == chain, 'resname']:
            chainStr = chainStr + row[0]

        print(chainStr)


def compute_distance(first_row, second_row):

    if pd.isna(first_row['x']) or pd.isna(first_row['y']) or pd.isna(first_row['z']) or \
            pd.isna(second_row['x']) or pd.isna(second_row['y']) or pd.isna(second_row['z']):

        print('Error!',
              '\nNot all coordinates are defined. Try another rows')

        return False

    else:
        sum = 0
        for coord in ['x', 'y', 'z']:
            sum += (first_row[coord] - second_row[coord]) ** 2

        distance = math.sqrt(sum)

        return distance



def main():
    filepath = os.path.join('data', '1jd4.pdb')

    data = pdb_reader(filepath)
    get_aa_seq(data)

    compute_distance(data.loc[1], data.loc[2])

    print('k')


if __name__ == '__main__':
    main()