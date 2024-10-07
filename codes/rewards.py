# Import the required libraries
import pandas as pd
import numpy as np


# Load the data set
path = 'C:\\Users\\ADMIN\\MentorshipRewards_Analysis\\MentorshipRewards_analysis\\assets\\Mentorship_Sessions.xlsx'
df = pd.read_excel(path, sheet_name = 'Mentorship_Sessions')


# Explore the data set
print(df)
df.dtypes


                                  ### --- TASK 1: DATA CLEANING --- ###

# 1. Rename Unnamed Columns
df.rename(columns={'Unnamed: 0': 'Mentee_ID'}, inplace=True)
# Verify changes
print(df.columns)


# 2. Handling Missing Values
# Check for missing values
MissingVals1 = df.isnull().sum()
print(MissingVals1)
# Handle the missing values by dropping or filling in rows/columns
df.dropna(subset=['Mentee_ID','Mentor_ID', 'Mentee_Name', 'Job_Info_Completed', 'Session_Date'])
# Fill NaN values in Session Number and duration with mean
Session_Number_Mean = df['Session_Number'].mean()
Session_Duration_Mean = df['Session_Duration_Min'].mean()
df['Session_Number'] = df['Session_Number'].fillna(Session_Number_Mean)
df['Session_Duration_Min'] = df['Session_Duration_Min'].fillna(Session_Duration_Mean)
df['Points_Awarded'] = df['Points_Awarded'].fillna(0)  # Replace with starting value of 0
# Verify Changes
MissingVals2 = df.isnull().sum()
print(MissingVals2)


# 3. Handling duplicates
duplicates = df.duplicated().sum()
print(f"Total duplicates: {duplicates}")


# 4. Correct the data types
df['Mentee_Name'] = df['Mentee_Name'].astype(str)
df['Mentor_Name'] = df['Mentor_Name'].astype(str)
df['Mentee_ID'] = df['Mentee_ID'].astype(str).apply(lambda x: str(x).split('.')[0])
df['Mentor_ID'] = df['Mentor_ID'].astype(str).apply(lambda x: str(x).split('.')[0])
df['Session_Date'] = pd.to_datetime(df['Session_Date'], format='%Y-%m-%d')
df['Session_Number'] = df['Session_Number'].astype(int)
df['Session_Duration_Min'] = df['Session_Duration_Min'].astype(int)
df['Points_Awarded'] = df['Points_Awarded'].astype(int)
# Verify Changes
print(df.dtypes)
print(df.head())


# 5. Standardize the Job_Info_Completed variable
df['Job_Info_Completed'] = df['Job_Info_Completed'].replace({'Yes': 'Yes', 'No': 'No'})


# Save the cleaned data set
df.to_excel('Mentorship_Session_Cleaned.xlsx', index=False)


                       ### --- TASK 2:  --- ####
                       
