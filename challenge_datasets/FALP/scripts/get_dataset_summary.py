import os
import numpy as np
import pandas as pd
from datetime import datetime
import argparse
import json


class Characterizer:
    """Class to characterize an instance of the FALP dataset.

    Attributes
    ----------
    data : pandas dataframe
        FALP dataset containing in each row the record of a cancer
        treatment service provided to a patient.
    """
    def __init__(self, data):
        self.data = data

    def get_period(self):
        start_years = [
            datetime.strptime(date, "%Y-%m-%d").year
            for date in self.data["FECHA_INICIO_TTO"]
            if date is not np.nan
        ]
        end_years = [
            datetime.strptime(date, "%Y-%m-%d").year
            for date in self.data["FECHA_FIN_TTO"]
            if date is not np.nan
        ]
        return {'start': min(start_years), 'end': max(end_years)}

    def get_summary(self):
        """Return a dictionary with the properties characterizing
        the dataset."""
        properties = {}
        patients = self.data.drop_duplicates(subset='ID_CASO')
        patients_with_tnm = patients.loc[
            ~patients["CT"].isna() &
            ~patients["CN"].isna() &
            ~patients["CM"].isna() &
            ~patients["PT"].isna() &
            ~patients["PN"].isna() &
            ~patients["PM"].isna()
        ]
        deceased = patients.loc[patients['ESTADO_VITAL'] == 'FALLECIDO']
        deceased_with_tnm = deceased.loc[
            ~deceased["CT"].isna() &
            ~deceased["CN"].isna() &
            ~deceased["CM"].isna() &
            ~deceased["PT"].isna() &
            ~deceased["PN"].isna() &
            ~deceased["PM"].isna()
        ]
        properties['period'] = self.get_period()
        properties['samples'] = self.data.shape[0]
        properties['variables'] = self.data.shape[1]
        properties['patients'] = {
            'all': patients.shape[0],
            'with stage': patients.loc[~patients['ESTADIO'].isna()].shape[0],
            'with all tnm': patients_with_tnm.shape[0],
            'with all tnm and stage': patients_with_tnm.loc[~patients_with_tnm['ESTADIO'].isna()].shape[0]
        }
        properties['deceased'] = {
            'all': deceased.shape[0],
            'with stage': deceased.loc[~deceased['ESTADIO'].isna()].shape[0],
            'with all tnm': deceased_with_tnm.shape[0],
            'with all tnm and stage': deceased_with_tnm.loc[~deceased_with_tnm['ESTADIO'].isna()].shape[0]
        }
        properties['male'] = patients.loc[patients['SEXO'] == 'M'].shape[0]
        properties['female'] = patients.loc[patients['SEXO'] == 'F'].shape[0]
        properties['cancer categories'] = patients['CATEGORIA'].nunique()
        properties['cancer subcategories'] = patients['SUBCATEGORIA'].nunique()
        return properties

def main():
    parser = argparse.ArgumentParser(
        description="Get a csv with the properties of the FALP dataset.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--path_to_data',
        type=str,
        default=os.path.join('..', 'RegistroTumoresFALP.csv'),
        help='Path to the FALP dataset saved as csv file.'
    )
    parser.add_argument(
        '--path_to_output',
        type=str,
        default='..',
        help='Path to the directory to store output csv files.'
    )
    args = parser.parse_args()
    data = pd.read_csv(args.path_to_data)
    characterizer = Characterizer(data)
    summary = characterizer.get_summary()
    with open(os.path.join(args.path_to_output, 'falp_summary.json'), 'w') as file:
        json.dump(summary, file, indent=4)


if __name__ == '__main__':
    main()
