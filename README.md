# 🏥 Hospital Data Management Dashboard  
*A TIBCO Spotfire Interactive Analytics & Data-Entry System*

This repository contains a **Spotfire dashboard (.dxp)** designed to streamline hospital data intake and provide deep analytical insights across patient demographics, admissions, treatments, and clinical outcomes.

The dashboard integrates **data entry**, **data quality monitoring**, and **advanced analytics** into a unified interface for healthcare institutions.

---

## 📌 Key Features
- **Patient Data Entry Interface** – Enter and validate patient information directly inside Spotfire  
- **Admission & Encounter Analytics** – Track patient volume, demographics, stay duration, and disease categories  
- **Clinical Outcomes & Treatment Effectiveness** – Understand how treatments correlate with outcomes  
- **Financial Performance Monitoring** – Analyze cost of care and department-wise performance  
- **Interactive Filtering** – Explore data by doctor, disease type, age group, gender, and more  

---

# 📂 Dashboard Pages

## 1️⃣ Intro Page – Navigation Hub 

![alt text](./Snapshots/Intro.JP)


The **Intro** page acts as the central navigation hub of the dashboard.  
It provides quick access to both **data-entry** and **analytics** modules.

### **Purpose**
- Guide users to the correct functional area  
- Provide a clean and user-friendly entry point  

### **Components**
- **Patient Data Entry** button  
- **Analytics Navigation** buttons:
  - Patient Admission & Encounter Analytics  
  - Treatment Effectiveness & Clinical Outcomes  
  - Financial Performance & Cost of Care  

---

## 2️⃣ Patient Admission & Encounter Analytics  
![Admission Analytics](./Patient Admission & Encounter Analytics.JPG)

This page provides **descriptive and interactive analytics** focused on hospital admissions, demographics, and disease categories.

### **Purpose**
Helps hospital administrators and clinicians understand:
- Patient inflow  
- Doctor distribution  
- Disease burden trends  
- Gender & age-based distributions  

### **Key Visualizations**
#### 🧮 KPI Summary Tiles
- Total Patient Count  
- Female Patient Count  
- Male Patient Count  
- Doctor Count  

#### 📈 Average Stay Duration vs Age  
A line chart showing:
- Relationship between **age** and **stay duration**  
- Gender-based comparison (Male vs Female)

#### 📊 Disease Type per Age Category  
Bar chart representing:
- Distribution of disease types across age groups  
- Separate bars for gender comparison  

#### 👨‍⚕️ No. of Specialists Treating Each Disease Type  
- Shows which specialties treat the highest volume of cases  
- Useful for workload planning  

#### 🧾 Patient Details Table  
- Displays detailed information for individual patients  
- Includes doctor-based filtering and reset options  

---

## 3️⃣ Patient Data Entry Page  
![Patient Entry](./Patient Data Entry.JPG)

This section provides an intuitive **form-based data entry interface** inside Spotfire.

### **Purpose**
Allows users to manually input or update patient demographic details.

### **Form Fields**
- Patient ID  
- First Name & Last Name  
- Gender  
- Height (cm) & Weight (kg)  
- Marital Status  
- Nationality  
- Blood Type  
- Birth Date  

### **Features**
- Drop-down menus for controlled data entry  
- Submit button for adding new entries  
- Full patient table for real-time verification  

---

# 🛠️ Technologies Used
- **TIBCO Spotfire Analyst**  
- **Interactive Visualizations**  
- **(Optional) IronPython scripts for automation**  

---

# 🚀 How to Use
1. Download and open the `.dxp` file in Spotfire Analyst.  
2. Use the **Intro page** for navigation.  
3. Enter data via the **Patient Data Entry** page.  
4. Explore analytics through the **Admission, Treatment, and Financial** pages.  

---

# 🤝 Contributions
Contributions are welcome — dashboards, enhanced visualizations, or integration improvements.

---

# 📄 License
This project is licensed under the MIT License.

---
