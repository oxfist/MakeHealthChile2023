# Dataset description

1. **ID_CASO**: patient id.
2. **CATEGORIA**: tumor diagnostic category (e.g digestive organ). 
3. **SUBCATEGORIA**: tumor diagnostic subcategory (e.g colon, pancreas or stomage).
4. **SEXO**: patient sex. Options: F or M, Femenine or Masculine respectively.
5. **EDAD**: patient age.
6. **REGION**: country region of residence.
7. **COMUNA**: "comuna" (county) of residence.
8. **PREVISION**: patient health insurance. Options: FONASA (public health insurance), 
    BENEFICIARIO (beneficiary, subset of FONASA), ISAPRE (private health insurance), 
    PARTICULAR (no health insurance), FFAA (military health insurance).
9. **CONVENIO_ONCOLOGICO**: FALP beneficiary. Options: SI (yes), NO (no).
10. **FECHA_DIAGNOSTICO**: diagnostic date.
11. **CT**: T clinic
12. **CN**: N clinic
13. **CM**: M clinic
14. **PT**: T pathology
15. **PN**: N pathology
16. **PM**: M pathology
17. **ESTADIO**: cancer stage at diagnostic date. Options: O, I, II, III, IV. (target variable)
18. **EXTENSION_DIAGNOSTICA**: tumor extension at diagnostic date. Options: LOCAL, REGIONAL, AVANZADO (advanced), PERITONEAL. (target variable)
19. **ESTADO_VITAL**: patient vital state. Options: VIVO (alive), FALLECIDO (death).
20. **FECHA_DEFUNCION**: date of death.
21. **TTO_FALP_SUBCATEGORIA**: treatment.
22. **FECHA_INICIO_TTO**: treatment start date.
23. **FECHA_FIN_TTO: treatment end date.

More information about T/N/M in *How_to_use_TNM.pdf*
