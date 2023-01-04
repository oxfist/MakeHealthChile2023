# Dataset description

1. **RC_SEXO**: Gender. 
2. **RC_EDAD**: Age of the patient at diagnosis (Computed as: RC_FECHA_PRIMER_DIAG - FECHA_NAC).
3. **REGION**: Country region of residence.
4. **COMUNA**: "comuna" (county) of residence. 
5. **RC_FECHA_PRIMER_DIAG**: Date of first confirmatory diagnosis.
6. **CATEGORIA_REGISTRO**: Diagnostic category.
7. **SUBCATEGORIA_REGISTRO**: Diagnosis subcategory.
8. **MORFOLOGIA_COD**: The Code of morphology of the Tumor of CIEO-3.
9. **RC_EXTENSION_DIAG**: Tumor extension.
10. **ESTADIO**: Cancer stage.
11. **FECHA_BIOPSIA**: Biopsy date.
12. **FECHA_NAC**: Patient's birth date.
13. **FECHA_DEFUNCION**: Patient death date.
14. **PREVISION_NOMBRE**: Health insurance.
15. **TRAMO_FONASA**: FONASA health insurance section.
16. **TIPO_PREST_NOMBRE**: Type of healthcare (CNE: New Specialty Consultation, IQ: Surgical interventions, PROC: procedures).
17. **PRESTA_MIN**: FONASA code of the healthcare provision.
18. **CLASE**: Healthcare provision class.
19. **SUBCLASE**: Healthcare provision subclass.
20. **ESPECIALIDAD_MEDICA**: Medical specialty associated with the healthcare provision.
21. **F_ENTRADA**: Entrance date to the waiting list.
22. **ESTAB_ORIG_NOMBRE**: Name of the health institution of origin.
23. **ESTAB_DEST_NOMBRE**: Name of the destination health institution.
24. **F_SALIDA**: Waiting list release date.
25. **C_SALIDA**: Waiting list exit condition (dictionary of values ​​to be confirmed)
26. **PRESTA_MIN_SALIDA**: FONASA code of the main exit health service.
27. **SOSPECHA_DIAG**: Diagnostic suspicion (free text, although sometimes they include ICD-10).
28. **CONFIRMACION_DIAG**: Diagnostic confirmation (free text, although sometimes they include ICD-10).
29. **DIAS_ESTAD**: Lenght of the inpatient visit stay (computed as: DISCHARGE_FMT_DATE - ENTRY_FMT_DATE).
30. **COND_EGR**: Patient discharge condition (Dictionary of values to be confirmed). 
31. **DIAG1**: Main ICD-10 diagnosis.
32. **DIAG2**: Additional ICD-10 diagnosis (optional).
33. **DIAG3**: Additional ICD-10 diagnosis (optional).
34. **DIAG4**: Additional ICD-10 diagnosis (optional).
35. **INTERV_Q**: Indicates whether or not the patient had surgery.
36. **INTERV_Q_PPAL**: FONASA code of the main surgical intervention.
37. **INTERV_Q_2**: Fonasa code of the additional surgical intervention (optional).
38. **PROCED**: Indicates whether or not a procedure was performed on the patient.
39. **PROCED_PPAL**: FONASA code of the main procedure.
40. **USO_PABELL**: Indicates whether the intervention used the surgery room (it is not required, so it may be incomplete).
41. **INGRESO_FMT_FECHA**: Inpatient visit admission date.
42. **EGRESO_FMT_FECHA**: Inpatient visit discharge date.
