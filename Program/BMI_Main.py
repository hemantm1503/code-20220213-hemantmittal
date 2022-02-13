import ConfigBMI # Config file for Input/Output files and folders 
import json #To code and decode JSON data
import numpy as np
import pandas as pd #pandas data frame

df_BMIMasterTable = pd.read_csv(ConfigBMI.BMITableFile) #define data frame for BMI master table

df_Patientdata = pd.read_json(ConfigBMI.PatientDataFile) #define data frame for BMI master table

#Cleaning PatientData 
##Remove rows where Height or Weight is NULL
df_Patientdata.dropna(subset=["HeightCm"], inplace = True)
df_Patientdata.dropna(subset=["WeightKg"], inplace = True)

#Data Preparation & Processing 
## Calculate and insert BMI based on Height and Weight based on the following formula: - BMI(kg/m2) = mass(kg) / height(m)2
df_Patientdata["BMI"] = round(df_Patientdata["WeightKg"]/((df_Patientdata["HeightCm"]/100)*(df_Patientdata["HeightCm"]/100)),2)

##Remove rows where BMI is Infinite or NULL
df_Patientdata.replace([np.inf, -np.inf], np.nan, inplace=True)
df_Patientdata.dropna(subset=["BMI"], inplace = True)

##Sorting the Patient's data on BMI (Descending) and Gender
df_Patientdata = df_Patientdata.sort_values (by = ["BMI","Gender"], ascending = [False,True],ignore_index=True)

## Insert a column as a key "BMI Range (kg/m2)" similar to the BMI Master table in Patient's Data conditions on BMI and values accordingly
conditions = [
    (df_Patientdata["BMI"] <= 18.4),
    (df_Patientdata["BMI"] > 18.4) & (df_Patientdata["BMI"] <= 24.9),
    (df_Patientdata["BMI"] > 24.9) & (df_Patientdata["BMI"] <= 29.9),
    (df_Patientdata["BMI"] > 29.9) & (df_Patientdata["BMI"] <= 34.9),
    (df_Patientdata["BMI"] > 34.9) & (df_Patientdata["BMI"] <= 39.9),
    (df_Patientdata["BMI"] > 39.9)]

values = ["18.4 and below","18.5 - 24.9","25 - 29.9","30 - 34.9","35 - 39.9","40 and above"]

df_Patientdata["BMI Range (kg/m2)"] = np.select(conditions,values)

##Join the Patient's data and BMI Master data
df_PatientdataBMI = pd.merge(left=df_Patientdata,right=df_BMIMasterTable, how="left", on=["BMI Range (kg/m2)"])

# Print Final Patient's final data with BMI and BMI Category and Health Risk columns and save the result in CSV and JSON file
print (df_PatientdataBMI)
try:
    df_PatientdataBMI.to_csv(ConfigBMI.OutputFolder+"/PatientdataBMI.csv")
    df_PatientdataBMI.to_json(ConfigBMI.OutputFolder+"/PatientdataBMI.txt")
except:
  print("Something went wrong with file")

#Result & Observations
df_BMIObservation1 = df_PatientdataBMI.groupby(["BMI Category","Gender"]).size().reset_index(name="No. of People")
df_BMIObservation2 = df_PatientdataBMI.groupby(["BMI Category"]).size().reset_index(name="No. of People")
df_BMIOverweight = df_BMIObservation2.loc[df_BMIObservation2["BMI Category"] == "Overweight"]["No. of People"].reset_index()

print("\nResults: ")
for x in range(len(df_BMIOverweight)):
    print("The total no. of Overweight people: "+str(df_BMIOverweight["No. of People"].iloc[x]))

print("\nObservations: ")

print("The total no. of people records : "+str(df_PatientdataBMI["BMI Category"].count()))
for x in range(len(df_BMIObservation2)):
    print("The total no. of *"+df_BMIObservation2["BMI Category"].iloc[x]+"* people : "+str(df_BMIObservation2["No. of People"].iloc[x]))
print("\n")
for x in range(len(df_BMIObservation1)):
    print("The total no. of *"+df_BMIObservation1["BMI Category"].iloc[x]+"* "+df_BMIObservation1["Gender"].iloc[x]+" : "+str(df_BMIObservation1["No. of People"].iloc[x]))