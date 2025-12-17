# 🏥 Hospital Data Management Dashboard  
*A TIBCO Spotfire Interactive Analytics & Data-Entry System*

This repository contains a **Spotfire dashboard (.dxp)** designed to streamline hospital data intake and provide deep analytical insights across patient demographics, admissions, Financial performance, treatments, and clinical outcomes.

The dashboard integrates **data entry**, **data quality monitoring**, and **advanced analytics** into a unified interface for healthcare institutions.


> 📂 **Dataset Reference:**  
> [Medical Dataset – Data Warehousing Project](https://github.com/siva-sankari-subramanian/Medical-Dataset/blob/main/README.md)


---

## 🚀 Why This Project Matters
Healthcare organizations rely on timely, accurate insights to improve patient outcomes and manage costs.  
This dashboard enables:

- Faster **clinical insights** into patient conditions and treatment effectiveness  
- Better **operational planning** through admission, doctor, and room utilization analysis  
- Clear **financial visibility** into treatment costs and insurance coverage  
- Seamless **data capture + analytics** in one platform (no external forms)

---

## 📊 What This Dashboard Does
✔ Captures patient demographic data through an interactive form  
✔ Tracks admissions, encounters, diseases, and doctor workloads  
✔ Compares vitals and lab results from **admission vs discharge**  
✔ Evaluates **treatment effectiveness and clinical outcomes**  
✔ Analyzes **cost drivers, insurance coverage, and room occupancy**


---

## 🧠 Skills Demonstrated
- Healthcare Data Analytics  
- BI Dashboard Design & UX  
- SQL-based Data Modeling  
- Data Quality & Validation  
- Clinical & Financial KPI Design  
- Interactive Filtering & Drill-Down Analysis  

---

# 📂 Dashboard Pages Overview

## 1️⃣ Intro Page – Navigation Hub
![Alt text](Dashboard/Snapshots/Intro.JPG)


| Section | Detailed Description | Key Components |
| :--- | :--- | :--- |
| **Navigation Hub** | The Intro page serves as the central landing page of the dashboard. It guides users to both data-entry workflows and analytical modules, ensuring smooth navigation for clinical and administrative users. | Buttons for Patient Data Entry, Admission & Encounter Analytics, Treatment Effectiveness & Clinical Outcomes, Financial Performance & Cost of Care |
| **User Experience Design** | Designed with simplicity and clarity to reduce cognitive load. The layout helps users quickly understand where to begin, which is critical in time-sensitive healthcare environments. | Clear labels, structured layout, intuitive navigation |
  

---

## 2️⃣ Patient Data Entry Page
![Alt text](Dashboard/Snapshots/Patient%20Data%20Entry.JPG)

| Section | Detailed Description | Key Fields / Features |
| :--- | :--- | :--- |
| **Patient Data Form** | Provides a form-based interface within Spotfire that allows hospital staff to manually enter or update patient demographic details directly into the source system. | Patient ID, First Name, Last Name, Gender, Height (cm), Weight (kg), Marital Status, Nationality, Blood Type, Birth Date |
| **Controlled Data Entry** | Ensures data consistency and quality by minimizing free-text inputs and enforcing standardized values across records. | Drop-down menus, predefined categories |
| **Submission & Verification** | Enables real-time submission and validation of new records. The live patient table allows immediate verification and correction if needed. | Submit button, real-time patient table |


---

## 3️⃣ Patient Admission & Encounter Analytics
![Alt text](Dashboard/Snapshots/Patient%20Admission%20%26%20Encounter%20Analytics.JPG)

| Section | Detailed Description | Key Visualizations & Metrics |
| :--- | :--- | :--- |
| **KPI Summary Tiles** | Displays high-level operational KPIs that provide an instant snapshot of hospital activity and staffing distribution. | Total Patient Count, Female Patient Count, Male Patient Count, Doctor Count |
| **Average Stay Duration vs Age** | Analyzes the relationship between patient age and length of hospital stay, highlighting age groups associated with longer admissions and gender-based trends. | Line chart segmented by gender |
| **Disease Type per Age Category** | Visualizes disease prevalence across age groups, helping identify demographic-specific disease patterns. | Bar chart by age category with gender comparison |
| **Specialist Distribution** | Shows how medical specialties are allocated across disease types, supporting workload analysis and staffing decisions. | Specialists per disease type |
| **Patient Details Table** | Enables drill-down into individual patient encounters with filtering options for detailed case analysis. | Interactive patient-level table |

---

## 4️⃣ Treatment Effectiveness & Clinical Outcomes
![Alt text](Dashboard/Snapshots/Treatment%20Effectiveness%20%26%20Clinical%20Outcomes.JPG)

| Section | Detailed Description | Key Visualizations & Metrics |
| :--- | :--- | :--- |
| **Vitals Comparison** | Tracks changes in key vital signs between admission and discharge to assess patient improvement or stability during treatment. | Line charts for BP, Heart Rate, Resp Rate, O₂ Saturation, Temperature |
| **Laboratory Test Analysis** | Compares lab results across treatment stages to objectively measure treatment impact. | Scatter plots for CBC, Chem, CRP, Lipids |
| **Treatment Details** | Links diagnoses and disease types with administered drugs, therapies, or surgeries at an encounter level. | Treatment details table |
| **Specialized Tests** | Monitors condition-specific diagnostic markers such as inflammation, clotting risk, and genetic indicators. | Scatter plots for D-Dimer, ESR, LDLP Gene Mutation, Synovial Fluid Analysis |
| **Encounter Selector** | Allows filtering of all visuals using selected encounter IDs for focused patient-level analysis. | Interactive encounter list box |

---

## 5️⃣ Financial Performance & Cost of Care
![Alt text](Dashboard/Snapshots/Financial%20Performance%20%26%20Cost%20of%20Care.JPG)


| Section | Detailed Description | Key Visualizations & Metrics |
| :--- | :--- | :--- |
| **Treatment & Insurance Mapping** | Correlates administered treatments with insurance plans to analyze coverage patterns and cost exposure. | Treatment vs insurance table |
| **Room Occupancy Analysis** | Examines hospital room utilization by month and room type to support capacity planning. | Monthly occupancy heatmap |
| **Cost Distribution Breakdown** | Breaks total cost into contributing components to identify major cost drivers. | Cost treemap |
| **Total Cost vs Insurance Coverage** | Compares billed costs with insurance coverage to assess patient out-of-pocket risk. | Pie / Donut chart |


---

## 🛠️ Technology Stack
- **BI Tool:** TIBCO Spotfire  
- **Data Source:** [Medical Dataset – Data Warehousing Project](https://github.com/siva-sankari-subramanian/Medical-Dataset/blob/main/README.md)
- **Languages & Scripting:** SQL, IronPython, JavaScript, HTML  
- **Domain:** Healthcare Analytics, Financial Analytics  

