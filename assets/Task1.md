# Summary Report

## Tools Used

- 1. Python: For data manipulation and cleaning.
- 2. Pandas: To handle dataframes and perform data cleaning operations.
- 3. Excel: To load and save the dataset. 

## Data Cleaning Process

The following steps were followed:
- **Loading data**: The dataset 'Mentorship_Sessions.xlsx' was loaded using `pandas` library
- **Renaming the unnamed column**
- **Handling missing values**: Missing values were identified and filled with appropriate placeholders.
```python
# Handle the missing values by dropping or filling in rows/columns
df.dropna(subset=['Mentee_ID','Mentor_ID', 'Mentee_Name', 'Job_Info_Completed', 'Session_Date'])

# Fill NaN values in Session Number and duration with mean
Session_Number_Mean = df['Session_Number'].mean()
Session_Duration_Mean = df['Session_Duration_Min'].mean()
df['Session_Number'] = df['Session_Number'].fillna(Session_Number_Mean)
df['Session_Duration_Min'] = df['Session_Duration_Min'].fillna(Session_Duration_Mean)
df['Points_Awarded'] = df['Points_Awarded'].fillna(0)  # Replace with starting
```
- **Handling duplicates**: There were no duplicates identified in the dataset
- **Correcting inconsistent data**: The data was standardized by converting the data types to the correct format, e.g the `'Session_Date'`column was converted to a consistent datetime format.
- **Saving the cleaned dataset**: The cleaned dataset was saved as 'Mentorship_Session_Cleaned.xlsx' for further data analysis.

# Findings
- The first column was unnamed and after exploring the data using Excel it seemed to be the mentees ID and hence renamed `'Mentee_ID'`
- Missing values in the columns were recorded as shown in the table below:

|Variable|Missing values|
|---|---|
|Mentee_ID|1|
|Mentor_ID|1|
|Mentor_Name|0|
|Mentee_Name|2|
|Session_Number|1|
|Session_Duration_Min|2|
|Job_Info_Completed|1|
|Session_Date|1|
|Points_Awarded|109|

For the `Session_Number` and `Session_Duration_Min`, the missing values were filled with the means of the respective columns. The other variables were flagged `NaN` for missing values. The `Points_Awarded` was filled with 0 and was to be filled with the correct values   