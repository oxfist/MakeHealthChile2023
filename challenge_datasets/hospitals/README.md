# Dataset description
## chile_hospitales.csv


List of hospitals in Chile, including georeferenced information. It contains th same headers as the dataset above. [Source: Departamento de Estadísticas e Información de Salud](https://deis.minsal.cl/#datosabiertos)

1. **C_ANT**: unique alphanumeric identifier, which allows the provider to be recognized unequivocally.
2. **C_VIG**: numerical identifier of the provider that allows it to be recognized unequivocally.
3. **C_MAD**: code of the provider that integrates into its structure and operation another less complex establishment and is part of its jurisdiction.
4. **C_NMAD**: new **C_MAD** code.
5. **C_REG**: region code.
6. **NOM_REG**: region name.
7. **C_DEPEND**: unique identifier used by the Health Services and the SEREMI.
8. **DEPEN**: dependence that the provider has on a higher hierarchival level. It is made of the Health Services and the SEREMIs.
9. **PERTEN**: relationship of jurisdiction established with the National Health Services System. Public establishments are part of a Health Service, therefore they are considered Belonging to the National Health Services System. On the other hand, private, Armed Forces, Order and Security establishments have a different jurisdiction, therefore they will be considered not belonging to the National Health Services System.
10. **TIPO**: category given to the provider according to the medical services it provides.
11. **AMBITO**: category given to the provider according to its administrative and care functionality in accordance with current regulations.
12. **URGENCIA**: has or not emergency system.
13. **CERTIFICA**: Procedure by which a third party, different and independent from the evaluated party, issues a document in which it acknowledges that an establishment meets the expected quality requirements. For hospitals there are EARs (current and invited) and for APS there are family health centers (implementation of the family health model). Accredited establishments are not considered in this category, as they are a different concept and whose information is available at the Superintendence of Health.
14. **DEPEN_A**: institution that is responsible for the administration of the provider, either directly or setting the standards to which health providers must abide in order to manage their assets.
15. **NIVEL**: the health system is organized into levels of care, according to the coverage and complexity of the care it provides.
16. **NOMBRE**: health provider name.
17. **C_COM**: county (*comuna*) code.
18. **NOM_COM**: county (*comuna*) name.
19. **VIA**: Specific location of the provider address.
20. **NUMERO**: Specific number of the provider address.
21. **DIRECCION**: Provider address.
22. **FONO**: Provider phone number.
23. **F_INICIO**: Start date of operation of the provider's activities.
24. **F_REAPER**: TODO.
25. **SAPU**: classification used to differentiate Emergency Services from Primary Care according to opening hours. In the event that the SAPU works seasonally, it is designated as "Summer".
26. **F_CAMBIO**: TODO.
27. **TIPO_CAMB**: TODO.
28. **LATITUD**: latitude in decimal degrees.
29. **LONGITUG**: longitude in decimal degrees.
30. **PRESTADOR**: provider category related to the Health System in Chile. Considering a Mixed System, it establishes the differences between public and private providers, armed forces and order and security.
31. **ESTADO**: current status of the provider with respect to its administrative and care functionality in accordance with current regulations.
32. **NIVEL_COM**: complexity level. Depends on the activity of a healthcare unit, in terms of the number of complex procedures, degree of development reached by it, availability of human resources and degree of specialization, equipment and hours of care.
33. **MODALIDAD**: care modality. Distinguishes providers that are qualified for ambulatory care from those that offer closed care with hospitalization. 

## chile_sitios_salud.csv

List of health facilities in Chile (at all levels: primary, secondary and tertiary), including georeferenced information. It contains the same headers as the dataset above. [Source: Departamento de Estadísticas e Información de Salud](https://deis.minsal.cl/#datosabiertos)

