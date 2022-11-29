# Data curation

Document to annotate the transformations required to get a final clean version of the dataset.

- Remove the first column containing the dataframe indices.
- Fix unallowed PT value (Pta -> Ta).
- Map TNM to base categories (T1a -> T1, N2b -> N2, etc).
- Map stages to base categories 0, I, II, III and IV.
- Remove cases with infrequent TNM categories?
	- Tis
	- Ta
	- NO CORRESPONDE (FIGO)

