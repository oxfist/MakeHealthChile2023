import argparse
import json
import os
from datetime import datetime
import pandas as pd

from falp_preprocessing import Standardizer

PATH_TO_ALLOWED = 'allowed.json'


class QualityMeasurer:
    """Class to measure the quality of an instance of the FALP
    dataset.

    Attributes
    ----------
    data : pandas dataframe
        FALP dataset containing in each row the record of a cancer
        treatment service provided to a patient.
    """
    with open(PATH_TO_ALLOWED, 'r') as file:
        allowed = json.load(file)

    def __init__(self, data):
        self.data = data

    def get_duplicated(self):
        """Return a pandas dataframe containing the duplicated rows."""
        return self.data.loc[self.data.duplicated(keep=False) == True]

    def get_unallowed_ids(self, column):
        return self.data.loc[
            (self.data[column] < 0) &
            self.data[column].isna()].copy()

    def get_unallowed_ages(self, column):
        return self.data.loc[
            (self.data[column] < 0) &
            ~self.data[column].isna()].copy()

    def get_unallowed_dates(self, column):
        converted = pd.to_datetime(
            self.data[column],
            format='%Y-%m-%d',
            errors='ignore').copy()
        return converted.loc[~converted.isna() & 
                             ~converted.apply(lambda x: isinstance(x, datetime))]

    def get_unallowed(self, column):
        return self.data.loc[
            ~self.data[column].isin(self.allowed[column]) &
            ~self.data[column].isna()].copy()

    def measure_columns(self):
        """Return a pandas dataframe indicating for each column
        variable:
            - missing values
            - out of range (unallowed) values
        """
        metrics = {'METRIC': ['missing', 'unallowed']}
        metrics.update({column: [] for column in self.data.columns})
        for column in list(metrics)[1:]:
            # Missing values
            metrics[column].append(self.data.loc[self.data[column].isna()].shape[0])
            # Out of range (unallowed) values
            if column == 'ID_CASO':
                metrics[column].append(self.get_unallowed_ids(column).shape[0])
            elif column == 'EDAD':
                metrics[column].append(self.get_unallowed_ages(column).shape[0])
            elif column in ['FECHA_DIAGNOSTICO',
                            'FECHA_DEFUNCION',
                            'FECHA_INICIO_TTO',
                            'FECHA_FIN_TTO']:
                metrics[column].append(self.get_unallowed_dates(column).shape[0])
            else:
                metrics[column].append(self.get_unallowed(column).shape[0])
        metrics = pd.DataFrame.from_dict(metrics)
        return metrics


def main():
    parser = argparse.ArgumentParser(
        description="Measure quality of FALP dataset.",
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
        help='Path to the directory to store the output csv files.'
    )
    parser.add_argument(
        '--path_to_allowed',
        type=str,
        default=PATH_TO_ALLOWED,
        help="Path to the JSON file containing the allowed values."
    )
    args = parser.parse_args()
    data = pd.read_csv(args.path_to_data, index_col=0)
    standardizer = Standardizer()
    data = standardizer.transform_stages(data)
    measurer = QualityMeasurer(data)
    with open(args.path_to_allowed, 'r') as file:
        measurer.allowed = json.load(file)
    metrics = measurer.measure_columns()
    duplicated = measurer.get_duplicated()
    unallowed_cm = measurer.get_unallowed('CM')
    unallowed_pt = measurer.get_unallowed('PT')
    metrics.to_csv(
        os.path.join(args.path_to_output, 'column_metrics.csv'),
        index=False
    )
    duplicated.to_csv(
        os.path.join(args.path_to_output, 'duplicated_rows.csv')
    )
    unallowed_cm.to_csv(
        os.path.join(args.path_to_output, 'unallowed_cm.csv')
    )
    unallowed_pt.to_csv(
        os.path.join(args.path_to_output, 'unallowed_pt.csv')
    )


if __name__ == "__main__":
    main()
