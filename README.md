# Py_BMICalculator
Task 
    1). Calculate BMI on patient's data (JSON Format) 
        (Weight(kg)/(Height(m)) and assign Health Risk and BMI Category according to the BMI (Maintained in BMI index Master Table)
    2). Count total no. of Overweight people from the Patient's data

# Data and Formats:-
    1). Patient's Data (JSON format) containing 3 columns (Gender, Heights in cm and Weight in Kg)
    Gender   : Male / Female  - String
    HeightCm : Height in CM   - Int64
    WeightKg : Weight in Kg   - Int64
    2). Standard BMI Master Table (csv file) with BMI Range in (Kg/m2), BMI Category and Health Risk
    BMI Category        : BMI Category          - String
    BMI Range (kg/m2)   : BMI range in kg/m2    - String
    Health risk         : Health Risk           - String

# Output Table
    JSON and CSV files with the following Data Frame:-
    Gender              : Male / Female         - String
    HeightCm            : Height in CM          - Int64
    WeightKg            : Weight in Kg          - Int64
    BMI                 : BMI                   - Float64
    BMI Category        : BMI Category          - String
    BMI Range (kg/m2)   : BMI range in kg/m2    - String
    Health risk         : Health Risk           - String

# The sample Patient's data file (JSON Format) named "Patient_data.txt and BMI Master Table file named "BMI_MasterTable.csv are in Folder named "Data"
# The Output files named PatientdataBM in csv and txt format created and saved thru program in Output folder

# Sample data and Results:-

1). The data file is in JSON format with 6 records

The output of the program on sample file:-
   Gender  HeightCm  WeightKg    BMI BMI Range (kg/m2)      BMI Category    Health risk
0    Male       171        96  32.83         30 - 34.9  Moderately obese    Medium risk
1    Male       161        85  32.79         30 - 34.9  Moderately obese    Medium risk
2  Female       150        70  31.11         30 - 34.9  Moderately obese    Medium risk
3  Female       167        82  29.40         25 - 29.9        Overweight  Enhanced risk
4    Male       180        77  23.77       18.5 - 24.9     Normal weight       Low risk
5  Female       166        62  22.50       18.5 - 24.9     Normal weight       Low risk

Results:
The total no. of Overweight people: 1

Observations:
The total no. of people records : 6
The total no. of *Moderately obese* people : 3
The total no. of *Overweight* people : 1


The total no. of *Moderately obese* Female : 1
The total no. of *Moderately obese* Male : 2
The total no. of *Normal weight* Female : 1
The total no. of *Normal weight* Male : 1
The total no. of *Overweight* Female : 1

# Algorithm:-
Library used numpy, Python and json
1). Create 2 data frame
    a). Master Table: df_BMIMasterTable
    b). Data File   : df_Patientdata

2). Calculate and insert new column in Data File with BMI calculated on the following formula :-
BMI(kg/m2) = mass(kg) / height(m)2

3). Assign the relevant BMI Range (kg/m2) to the BMI calculated
4). Join the 2 data frame on key="BMI Range (kg/m2)" to get the final output table / Data frame
5). Calculate and obtain the result on the final data frame based on criteria e.g. BMI Category is "Overweight"
