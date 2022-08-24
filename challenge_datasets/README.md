# Folder structure

This folder contains the consolidated datasets with public information about COVID-19 in Chile. 
The folder is structured as follows:

```
challenge_datasets
├── census
│   ├── consolidado_censo.csv
│   ├──labels_p12.csv
│   ├──labels_p13.csv
│   ├──labels_p14.csv
│   ├──labels_p15.csv
│   ├──labels_p16.csv
│   ├──labels_p17.csv
│   └──labels_p18.csv
└──  consolidado_covid19.csv
```

# Data
## consolidado_covid19.csv

[Data Source](https://github.com/MinCiencia/Datos-COVID19)

1. **Fecha**: date in the format YYYY-MM-DD.
2. **Region**: country's first-level administrative division.
3. **Codigo_region**: numeric code for region.
4. **Comuna**: smallest administrative subdivision in Chile. It may contain cities, towns, villages, hamlets and rural areas.
5. **Codigo_comuna**: numeric code for comuna.
6. **Poblacion**: population of each *comuna*.
7. **Casos_incremental**: incremental count of new cases.
8. **Casos_nuevos**: new cases for that specific date.
9. ** Superficie_km2**: surface of the *comuna* in km2.
10. **IM_interno**:  intern mobility index. It's a measure of the journeys inside the *comuna*.
11. **IM_externo**: external mobility index. Includes the journeys *from* and *to* the *comuna*.
12. **IM**: IM_interno + IM_externo
13. **Fallecidos_totales**: incremental COVID-19 deaths
14. **Fallecidos_nuevos**: COVID-19 deaths reported in that date
15. **Positividad**: rate of positive results of PCR tests
16. **Dosis_unica**: amount of people with only one dose of covid-19 vaccine
17. **Primera_dosis**: amount of people with the first dose of covid-19 vaccine
18. **Segunda_dosis**: amount of people with the second dose of COVID-10 vaccine
19. **Tercera_dosis**: amount of people with the third dose of COVID-10 vaccine
20. **Cuarta_dosis**: amount of people with the fourth dose of COVID-10 vaccine

## census/consolidado_censo.csv

[Data source](https://www.ine.cl/estadisticas/sociales/censos-de-poblacion-y-vivienda/censo-de-poblacion-y-vivienda)

- **REGION**:  country's first-level administrative division (numerical code)
- **PROVINCIA**: region subdivision (numerical code)
- **COMUNA**: smallest administrative subdivision in Chile (numerical code)
- **HOMBRES**: number of people identified as men
- **MUJERES**: number of people identified as women
- **EDAD_0A5**: people from 0 to 5 years old
- **EDAD_6A14**: people from 6 to 14 years old
- **EDAD 15A64**: people from 15 to 64 years old
- **EDAD 65YMAS**: people from 65 years old or more
- **INMIGRANTES**: number of inmigrants
- **P12_1-99**: Birth location
- **P13_1-99**: people that currently attend to formal education
- **P14_0-99**: higher school year approved
- **P15_1-99**: higher education level approved
- **P15A_1-99**: higher education level approved was completed?
- **P16_1-99**: people identified as indigenous
- **P16A_1-99**: indigenous group
- **P17_1-99**: amount of people that worked previous week of the census
- **P18_A-99**: economic activity

Each topic category labels are specified in the files __labels_p*.csv__