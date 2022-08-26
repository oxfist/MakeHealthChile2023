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

- **Codigo_region**:  country's first-level administrative division (numerical code)

- **Codigo_provincia**: region subdivision (numerical code)

- **Codigo_comuna**: smallest administrative subdivision in Chile (numerical code)

- **HOMBRES**: number of people identified as men

- **MUJERES**: number of people identified as women

- **EDAD_0A5**: people from 0 to 5 years old

- **EDAD_6A14**: people from 6 to 14 years old

- **EDAD 15A64**: people from 15 to 64 years old

- **EDAD 65YMAS**: people from 65 years old or more

- **INMIGRANTES**: number of inmigrants

- **LugarNacimiento_(En esta comuna, 
                     En otra comuna,
                     Peru, 
                     Argentina,
                     Bolivia, 
                     Ecuador, 
                     Colombia,
                     Otro, 
                     Missing)** : Birth location. 

- **EducacionFormal_(Si,
                     No asiste actualmente, 
                     Nunca asistio, 
                     Missing)**: people that currently attend to formal education

- **UltimoAñoEscolarAprobado_(0, 
                              1°, 
                              2°, 
                              3°, 
                              4°, 
                              5°, 
                              6°, 
                              7°, 
                              8°, 
                              No aplica, Missing)**: higher school year approved

- **NivelEducacional_(Sala Cuna o Jardin Infantil, <br />
                      Prekinder, <br />
                      Kinder, <br />
                      Especial o Diferencial, <br />
                      Educación básica, <br />
                      Primaria o Preparatorio, <br /> 
                      Cientifico-Humanista, <br />
                      Técnica Profesional, <br />
                      Humanidades, <br />
                      Técnica Comercial Industrial o Normalista, <br />
                      Técnico Superior, Profesional, <br />
                      Magister, <br />
                      Doctorado, <br />
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

- **ActividadEconomica_(Agricultura ganadería silvicultura y pesca, <br />
                        Explotación de minas y canteras, <br />
                        Industrias manufactureras, <br />
                        Suministro de electricidad gas vapor y aire acondicionado, <br />
                        Suministro de agua evacuación de aguas residuales y gestion de desechos y contaminación, <br />
                        Construcción, <br />
                        Reparación de vehiculos automotores y motocicletas, <br />
                        Transporte y almacenamiento, <br />
                        Actividades de alojamiento y servicios de comidas, <br />
                        Información y comunicaciones, <br />
                        Actividades financieras y seguros, <br />
                        Actividades inmobiliarias, <br />
                        Actividades profesionales científicas y técnicas, <br />
                        Actividades de servicios administrativos y apoyo, <br />
                        Administración pública defensa y planes de seguridad social y afiliación obligatoria, <br />
                        Enseñanza, <br />
                        Actividades de atención de salud humana y asistencia social, <br />
                        Actividades artísticas entretenimiento y recreativas, <br />
                        Otras actividades y servicios, <br />
                        Actividades no diferenciadas de hogares como productores de bienes y servicios de uso propio, <br />
                        Actividades de organanizaciones y órganos extraterritoriales, <br />
                        Rama no declarada, <br />
                        No aplica, Missing)**: economic activity
