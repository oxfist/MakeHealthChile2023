# Folder structure

This folder contains the consolidated datasets with public information about COVID-19 in Chile. 
The folder is structured as follows:

```
challenge_datasets
├── census
│   └── consolidado_censo.csv
└──  consolidado_covid19.csv
```

# Data
## consolidado_covid19.csv

[Data Source, Ministry of Science repository](https://github.com/MinCiencia/Datos-COVID19)

1. **Fecha**: date in the format YYYY-MM-DD
2. **Region**: country's first-level administrative division
3. **Codigo_region**: numeric code for region
4. **Comuna**: smallest administrative subdivision in Chile. It may contain cities, towns, villages, hamlets and rural areas
5. **Codigo_comuna**: numeric code for comuna
6. **Poblacion**: population of each *comuna*
7. **Casos_incremental**: incremental count of new cases
8. **Casos_nuevos**: new cases for that specific date
9. ** Superficie_km2**: surface of the *comuna* in km2
10. **IM_interno**:  intern mobility index. It's a measure of the journeys inside the *comuna*
11. **IM_externo**: external mobility index. Includes the journeys *from* and *to* the *comuna*
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

[Data source, National Institute of Statistics](https://www.ine.cl/estadisticas/sociales/censos-de-poblacion-y-vivienda/censo-de-poblacion-y-vivienda)

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

- **LugarNacimiento_(En esta comuna, <br />
                     En otra comuna, <br />
                     Peru, <br />
                     Argentina, <br />
                     Bolivia, <br />
                     Ecuador, <br />
                     Colombia, <br />
                     Otro, <br />
                     Missing)** : Birth location. 

- **EducacionFormal_(Si, <br />
                     No asiste actualmente, <br />
                     Nunca asistio, <br />
                     Missing)**: people that currently attend to formal education

- **UltimoAñoEscolarAprobado_(0, <br />
                              1°, <br />
                              2°, <br />
                              3°, <br />
                              4°, <br />
                              5°, <br />
                              6°, <br />
                              7°, <br />
                              8°, <br />
                              No aplica, Missing)**: higher school year approved

- **NivelEducacional_(Sala Cuna o Jardin Infantil, 
                      Prekinder, 
                      Kinder, 
                      Especial o Diferencial, 
                      Educación básica, 
                      Primaria o Preparatorio, 
                      Cientifico-Humanista, 
                      Técnica Profesional, 
                      Humanidades, 
                      Técnica Comercial Industrial o Normalista, 
                      Técnico Superior, Profesional, 
                      Magister, 
                      Doctorado,
                      No aplica, Missing)**: higher education level approved

- **NivelEducacionalCompleto_(Si, 
                              No, 
                              No aplica, Missing)**: higher education level approved was completed?

- **PertenenciaComunidadIndigena_(Si, No, Missing)**: people identified as indigenous

- **ComunidadIndigena_(Mapuche, 
                       Aymara, 
                       Rapa Nui, 
                       Lican Antai, 
                       Quechua, 
                       Colla, 
                       Diaguita, 
                       Kawesqar, 
                       Yagan o Yamana, 
                       Otro pueblo, 
                       No aplica, Missing)**: indigenous group

- **TrabajoSemanaAnterior_(Por pago, 
                           Sin pago, 
                           Empleado en vacaciones licencia descanso, 
                           Buscando empleo, 
                           Estudiando, 
                           Quehaceres del hogar, 
                           Jubilado pensionado o rentista, 
                           Otra situacion, 
                           No aplica, Missing)**: amount of people that worked previous week of the census

- **ActividadEconomica_(Agricultura ganadería silvicultura y pesca, 
                        Explotación de minas y canteras, 
                        Industrias manufactureras, 
                        Suministro de electricidad gas vapor y aire acondicionado, 
                        Suministro de agua evacuación de aguas residuales y gestion de desechos y contaminación, 
                        Construcción, 
                        Reparación de vehiculos automotores y motocicletas, 
                        Transporte y almacenamiento, 
                        Actividades de alojamiento y servicios de comidas, 
                        Información y comunicaciones, 
                        Actividades financieras y seguros, 
                        Actividades inmobiliarias, 
                        Actividades profesionales científicas y técnicas, 
                        Actividades de servicios administrativos y apoyo,
                        Administración pública defensa y planes de seguridad social y afiliación obligatoria, 
                        Enseñanza, 
                        Actividades de atención de salud humana y asistencia social, 
                        Actividades artísticas entretenimiento y recreativas, 
                        Otras actividades y servicios, 
                        Actividades no diferenciadas de hogares como productores de bienes y servicios de uso propio,
                        Actividades de organanizaciones y órganos extraterritoriales, 
                        Rama no declarada, 
                        No aplica, Missing)**: economic activity
