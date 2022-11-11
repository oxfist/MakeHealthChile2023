import re


class Standardizer:
    not_allowed_tnm = [
        "Tis",
        "Tx",
        "Ta",
        "Pta",
        "Nx",
        "NO CORRESPONDE (FIGO)",
        "Mx"
    ]
    stages = ['0', 'I', 'II', 'III', 'IV']
    tnm = [
        'T0', 'T1', 'T2', 'T3', 'T4',
        'N0', 'N1', 'N2', 'N3',
        'M0', 'M1'
    ]

    def transform_tnm(self, data):
        """
        Standardize TNM categories.

            - Remove not allowed
            - Map N+ -> N1, M+ -> M1
            - Map the rest according to the two first letters        

        Parameters
        ----------
        data : pandas DataFrame
            Data to be transformed.
        """
        normalized = data.loc[
            ~data["CT"].isin(self.not_allowed_tnm) &
            ~data["CN"].isin(self.not_allowed_tnm) &
            ~data["CM"].isin(self.not_allowed_tnm) &
            ~data["PT"].isin(self.not_allowed_tnm) &
            ~data["PN"].isin(self.not_allowed_tnm) &
            ~data["PM"].isin(self.not_allowed_tnm)
        ].copy()
        normalized[['CN', 'PN']] = normalized[['CN', 'PN']].replace('N+', 'N1')
        normalized[['CM', 'PM']] = normalized[['CM', 'PM']].replace('M+', 'M1')
        for category in ['CT', 'CN', 'CM', 'PT', 'PN', 'PM']:
            normalized[category] = normalized[category].str.slice(0,2)
        return normalized

    def transform_stages(self, data):
        """
        Standardize stages to categories 0, I, II, III, IV.
        """
        normalized = data.copy()
        normalized["ESTADIO"] = [re.match('[IivV]+|0', stage).group() for stage in data["ESTADIO"]]
        return normalized

    def transform(self, data):
        """
        Standardize TNM categories and stages.  
        """
        normalized = self.transform_tnm(data)
        return self.transform_stages(normalized)

    def check(self, data, display_not_allowed=False):
        """
        Check data for including values specified in 'tnm' and 'stages'
        class attributes.
        """
        not_allowed = data.loc[
            ~data['CT'].isin(self.tnm) |
            ~data['CN'].isin(self.tnm) |
            ~data['CM'].isin(self.tnm) |
            ~data['PT'].isin(self.tnm) |
            ~data['PN'].isin(self.tnm) |
            ~data['PM'].isin(self.tnm) |
            ~data['ESTADIO'].isin(self.stages)
        ]
        if not_allowed.shape[0]:
            if display_not_allowed:
                print(not_allowed)
            return False
        return True
