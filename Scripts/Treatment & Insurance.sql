SELECT 
e.Encounter_ID,
t.Treatment_Type,
t.Treatment_Name,
d.Disease_ID,
d.Admission_Diagnosis,
d.Disease_Type,
i.InsuranceKey,
i.Insurance_Plan_Name
FROM prod.Encounter e 
LEFT JOIN prod.Treatment t ON t.Encounter_ID=e.Encounter_ID 
LEFT JOIN prod.Disease d ON d.Disease_ID=e.Disease_ID
LEFT JOIN prod.Insurance i ON i.InsuranceKey=e.InsuranceKey