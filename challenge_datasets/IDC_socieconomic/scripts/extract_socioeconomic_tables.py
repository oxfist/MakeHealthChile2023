import os
import pandas as pd
from tabula import read_pdf
import argparse


class IDCExtractor:
    path_to_idc = os.path.join('..', 'IDC_U_AUTONOMA.pdf')

    def split_regions_table(self, table):
        """Return the specified regions table with the first column
        split in 3 parts."""
        column_data = table[table.columns[0]].copy()
        column_labels = table.columns[0].split()
        first, second, third = [], [], []
        for row in column_data:
            interim = row.split()
            first.append(' '.join(interim[:-2]))
            second.append(interim[-2])
            third.append(interim[-1])
        corrected = pd.DataFrame(
            {
                column_labels[0]: first,
                column_labels[1]: second,
                column_labels[2]: third
            },
            index=column_data.index
        )
        corrected = pd.concat(
            [corrected, table.drop(columns=table.columns[0])],
            axis=1
        )
        return corrected

    def split_counties_table(self, table):
        """Return the specified counties table with the first column
        split in 3 parts."""
        regions = [
            'ARICA Y PARINACOTA', 'TARAPACÁ', 'ANTOFAGASTA', 'ATACAMA',
            'COQUIMBO', 'VALPARAÍSO', 'RM', "O'HIGGINS", 'MAULE',
            'BIOBÍO-ÑUBLE', 'BIOBÍO', 'ARAUCANÍA', 'LOS RÍOS', 'LOS LAGOS',
            'AYSÉN', 'MAGALLANES'
        ]
        column_data = table[table.columns[0]].copy()
        column_labels = table.columns[0].split()
        first, second, third = [], [], []
        for row in column_data:
            interim = row.split()
            region_county = ' '.join(interim[:-1])
            for region in regions:
                index = region_county.find(region, 0)
                if index == 0:
                    matched_region = region_county[index:len(region)]
                    county  = region_county[len(region):len(region_county)].strip()
                    break
            first.append(matched_region)
            second.append(county)
            third.append(interim[-1])
        corrected = pd.DataFrame(
            {
                column_labels[0]: first,
                column_labels[1]: second,
                column_labels[2]: third
            },
            index=column_data.index
        )
        corrected = pd.concat(
            [corrected, table.drop(columns=table.columns[0])],
            axis=1
        )
        return corrected

    def fix_long_counties(self, table):
        """Return a fixed version of the specified table containing
        empty cells as a consequence of long-named counties."""
        corrected = table.copy()
        long_counties = corrected.loc[
            ~corrected['REGIÓN'].isna() &
            ~corrected['COMUNA'].isna() &
            corrected['BIENESTAR'].isna()
        ]
        for index in long_counties.index:
            corrected['COMUNA'].iloc[index] = ' '.join(
                [
                    corrected['COMUNA'][index],
                    corrected['COMUNA'][index+1]
                ]
            )
            for column in corrected.columns[2:]:
                corrected[column].iloc[index] = corrected[column][index+2]
        with_nan = corrected.loc[corrected['REGIÓN'].isna()]
        corrected.drop(index=with_nan.index, inplace=True)
        corrected.reset_index(drop=True, inplace=True)
        return corrected

    def extract_regions(self):
        """Return the table with mean IDC indicators for each region."""
        regions_table = read_pdf(
            self.path_to_idc, pages=20, stream=True
        )
        regions_table = regions_table[1].rename(columns=regions_table[1].iloc[0]).loc[1:]
        regions_table.reset_index(drop=True, inplace=True)
        regions_table = self.split_regions_table(regions_table)
        regions_table[regions_table.columns[1:]] = regions_table[regions_table.columns[1:]].apply(lambda x: x.str.replace(',', '.'))
        return regions_table

    def extract_counties(self):
        """Return the table with IDC indicators for each county."""
        counties_tables = read_pdf(
            self.path_to_idc, pages=list(range(58, 66)), stream=True
        )
        first_counties_table = counties_tables[0].rename(columns=counties_tables[0].iloc[0]).loc[1:]
        first_counties_table.reset_index(drop=True, inplace=True)
        first_counties_table = self.split_counties_table(first_counties_table)
        counties_table = pd.concat([first_counties_table, *counties_tables[1:]])
        counties_table.reset_index(drop=True, inplace=True)
        counties_table = self.fix_long_counties(counties_table)
        counties_table[counties_table.columns[2:-2]] = counties_table[counties_table.columns[2:-2]].apply(lambda x: x.str.replace(',', '.'))
        counties_table['RANKING'] = counties_table['RANKING'].apply(int)
        return counties_table


class IPSExtractor:
    path_to_ips = os.path.join('..', 'IPS-INDICE-DE-PRIORIDAD-SOCIAL-2022_V2.pdf')


def main():
    parser = argparse.ArgumentParser(
        description="Extract socieconomic tables for chilean counties.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--path_to_output',
        type=str,
        default='..',
        help='Path to the directory to store output csv files.'
    )
    args = parser.parse_args()
    idc_extractor = IDCExtractor()
    regions_idc = idc_extractor.extract_regions()
    counties_idc = idc_extractor.extract_counties()
    regions_idc.to_csv(
        os.path.join(args.path_to_output, 'regions_idc.csv'),
        index=False
    )
    counties_idc.to_csv(
        os.path.join(args.path_to_output, 'counties_idc.csv'),
        index=False
    )


if __name__ == '__main__':
    main()
