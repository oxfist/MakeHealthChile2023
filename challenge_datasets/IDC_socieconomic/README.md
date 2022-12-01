# Dataset description
## counties_idc.csv

Socioeconomic characterization of the chilean counties in terms of the IDC (*Indice de Desarrollo Comunal*) index. The IDC index measures the socioeconomic situation of each county based on 3 dimensions: Health and social wellness, economy, and education. Data considered to compute the IDC index was mainly collected between 2017 and 2018. [Source: IDC_U_AUTONOMA.pdf](IDC_U_AUTONOMA.pdf)

1. **REGIÓN**: Region containing the county on which the index is calculated. Chilean territory has 16 regions.
2. **COMUNA**: County on which the index is calculated.
3. **BIENESTAR**: Health and social wellness dimension computed from variables such as the percentage of households in a situation of poverty, percentage of households without basic services, among others.
4. **ECONOMÍA**: Economy dimension computed from variables such as permanent incomes, internet connections per habitant, among others.
5. **EDUCACIÓN**: Education dimension computed from variables such as mean scores obtained in Simce and PSU tests, among others.
6. **IDC**: IDC Index computed as the geometric mean of the 3 dimensions described above.
7. **RANKING**: Integer indicating the ranking of counties in terms of the IDC index in descending order.
8. **RANGOS**: Category for each county according to the IDC index. Categories are: *Alto* (high), *Medio alto* (medium high), *Medio* (medium), *Medio bajo* (medium low), *Bajo* (low).

## regions_idc.csv

Mean IDC index for each chilean region. The mean is computed over the IDC indices of the counties belonging to the specified region.

1. **REGIÓN**: Region belonging to the chilean territory.
2. **BIENESTAR**: Health and social wellness dimension computed as the mean of those counties belonging to the region.
3. **EDUCACIÓN**: Education dimension computed as the mean of those counties belonging to the region.
4. **ECONOMÍA**: Economy dimension computed as the mean of those counties belonging to the region.
5. **IDC**: IDC index computed as the mean of those counties belonging to the region.
