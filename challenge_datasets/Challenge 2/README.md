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
23. **FECHA_FIN_TTO**: treatment end date.

Information about the TNM cancer staging system can be found in *How_to_use_TNM.pdf*. In addition, we include a Q&A section to help you quickly to resolve more specific questions.

# Q&A

**Q1: The category X is used in each element to indicate that there has been no assessment of that characteristic of the tumor [AJCC](https://training.seer.cancer.gov/staging/systems/ajcc/guidelines.html). What’s the difference between the X categories and the unreported TNM values?**

**A1:** The TNM values are directly extracted from medical health records, then the X categories are explicitly reported as such by the professionals, while missing values mean that TNM could not be retrieved from clinical records.

**Q2: What does “Tis” mean in pathological T? Can this variable be grouped?**

**A2:** Tis means carcinoma in situ, and it is an intermediate stage between T0 and T1 which refers to a low risk tumor.

**Q3: What does “Ta” mean in both clinical and pathological T? Can this variable be grouped?**

**A3:** Similar to the previous question, Ta means noninvasive papillary carcinoma and it is a low risk stage between T0 and T1. Only certain types of cancer can be classified as Tis and Ta.

**Q4: What is the importance of the treatment sequence?**

**A4:** Treatment order could give important information, for example, generally a surgery followed by a chemo is curative, while a chemo followed by a surgery is sometimes palliative.

**Q5: Why are there missing treatment dates previous 2018?**

**A5:** In 2018 FALP started to use a specialized software to register the information. Previous to that information was filled manually, thus the quality is lower. It is important to notice that there are patients who don’t receive any treatment, therefore the columns *TTO_FALP_SUBCATEGORIA*, *FECHA_INICIO_TTO* and *FECHA_FIN_TTO* are empty.

**Q6: Could we map region and comuna to socioeconomic indicators?**

**A6:** Yes. You can use the [IDC socioeconomic indicator](https://repositorio.uautonoma.cl/handle/20.500.12728/6742) developed and published by the Universidad Autónoma in 2020. This indicator measures the local development for each Chilean county based on a dozen socioeconomic variables grouped into 3 main dimensions: Health and social wellness, economy, and education.
