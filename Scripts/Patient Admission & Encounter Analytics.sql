SELECT
    p.Patient_ID, 
    p.Patient_Name,
    p.Gender,
    p.Nationality,
    DATEDIFF(year, p.Birth_Date, GETDATE()) AS Age,
    do.Doctor_ID,
    do.Doctor_Name,
    d.Disease_Type,
    r.RoomKey,
    r.Room_Type,
    e.Encounter_ID,
    e.CheckinDate,
    e.CheckoutDate,
    DATEDIFF(day,e.CheckinDate,e.CheckoutDate) 'Duration of Stay'
FROM prod.Patient p
LEFT JOIN prod.Encounter e ON e.Patient_ID = p.Patient_ID
LEFT JOIN prod.Disease d ON e.Disease_ID = d.Disease_ID
LEFT JOIN prod.Doctor do ON do.Doctor_ID=e.ResponsibleDoctorID
LEFT JOIN prod.Room r ON r.RoomKey=e.RoomKey


