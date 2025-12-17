import clr
clr.AddReference('System.Data')
from System.Data import SqlClient
from System import DateTime

# Get variables from Spotfire document properties
Date = Document.Properties[Birth_Date]

sql = "INSERT INTO dev.Patient ([Patient_ID],[First_Name],[Last_Name],[Gender],[Height],[Weight],[Blood_Type],[Nationality],[Marital_Status],[Birth_Date]) VALUES (@PatientID,@FirstName,@LastName,@Gender,@Height,@Weight,@BloodType,@Nationality,@MaritalStatus,@BirthDate)"

conn = SqlClient.SqlConnection("Server=DESKTOP-QLLBB4M;Database=Medical_dataset;Integrated Security=True")
conn.Open()

cmd = SqlClient.SqlCommand(sql, conn)
cmd.Parameters.AddWithValue("@PatientID", Patient_ID)
cmd.Parameters.AddWithValue("@FirstName", First_Name)
cmd.Parameters.AddWithValue("@LastName", Last_Name)
cmd.Parameters.AddWithValue("@Gender", Gender)
cmd.Parameters.AddWithValue("@Height", Height)
cmd.Parameters.AddWithValue("@Weight", Weight)
cmd.Parameters.AddWithValue("@BloodType", Blood_Type)
cmd.Parameters.AddWithValue("@Nationality", Nationality)
cmd.Parameters.AddWithValue("@MaritalStatus", Marital_Status)
cmd.Parameters.AddWithValue("@BirthDate", Date)



exe = cmd.ExecuteNonQuery()

conn.Close()
