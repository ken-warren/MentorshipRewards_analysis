# Mentorship Rewards Optimization
---

## Context
The Rewards Program team is preparing for a major evaluation of how effectively the rewards are driving user engagement and satisfaction. They need insights to help optimize reward offerings, identify key segments, and understand the overall impact of the reward types on user behavior. Accurate data analysis is crucial for making data driven decisions on reward offerings and tailoring them to different user segments.

## Task 1. Data Cleaning

**Context:**

As part of our reward efforts, it’s crucial to maintain accurate and clean data. Recently, we discovered challenges in our data, which impacted our ability to allocate points to graduates and learners.

**Assignment:** You are provided with a sample dataset in the “Mentorship_Sessions” sheet that includes data related to mentorship sessions. This dataset has several duplicates and inconsistencies. Your task is to:

- Identify and address any missing, incorrect, or inconsistent data within the columns. Ensure that all data is cleaned and standardised for accurate analysis and reporting.
- Identify and remove any duplicate records.
- Explain your approach to data cleaning, including the tools you used.
- Provide a summary of the cleaned data, highlighting the number of duplicates removed and any other anomalies found.

**Deliverables:**

- A clean version of the dataset in Excel.
- A brief report (300-500 words) detailing your process, tools used, and findings.

## Task 2: Legacy Point Allocation

**Context:**
Every week, you will be required to analyse, calculate, and manually award learners and graduates with points based on a set of point criteria.

**Assignment:**
Using your cleaned sample dataset for “Mentorship_Sessions”, allocate points according to the criteria listed below. 

Mentors earn points as follows:
- 250 points for signing up to become a mentor (one-time allocation).
- 1000 points for conducting mentorship with 2 different mentees.

The mentor receives 500 points per mentorship relationship, with the points being allocated as follows:
- 250 points per session.
- Must hold two sessions with the same mentee to earn the maximum of 500 points.
- Each session must be a minimum of 30 minutes in length.
- At least one session must include the completion of job information.
- The session must be with the same mentee.

**Deliverables:**
- Compile the main rules that needed to be applied for point allocation.
- Create the points allocation calculation to award the mentor points. Provide an explanation of the calculations that you applied to award the mentor points.
- A brief report (300-500 words) detailing the point allocation results and providing reasons for the results.
- Use the provided data and award the points to mentors.
- Provide a step-by-step outline of the process you would follow to complete the allocation, ensuring the points are awarded correctly on the system. This should include your approach to testing and verifying the accuracy of the allocations.

## Task 3:  Deriving Reward Dashboard and Insights

**Context:**
The Rewards Program team is focused on enhancing user engagement and maximising the effectiveness of their reward offerings. To achieve this, they require a detailed analysis of user behaviour and reward redemption patterns based on the most recent data.

**Assignment:**
- Using the cleaned data from the previous tasks analyse and create a reward dashboard and provide insights that could be used to optimise the Rewards Program. Your analysis should help identify key user segments (e.g., new users, top performers, low engagement) and suggest how these insights could inform future reward offerings and engagement strategies.

**Deliverables:**
- A visual data insights report that includes at least three actionable recommendations based on your analysis (500-700 words).

  # Task 1: Data Cleaning

## Summary Report

## Tools Used

- **Python**: Utilized for data manipulation and cleaning.
- **Pandas**: Essential for handling data-frames and performing various data cleaning operations.
- **Excel**: Employed for loading and saving the dataset.

## Data Cleaning Process
- The data cleaning process involved several meticulous steps to ensure the dataset's integrity and readiness for analysis:
1. **Loading Data**: The dataset 'Mentorship_Sessions.xlsx' was imported using the pandas library.
2. **Renaming Columns**: An unnamed column was identified and renamed to `Mentee_ID` based on its content.
3. **Handling Missing Values**: Missing values were identified and appropriately filled or flagged.
4. **Handling Duplicates**: No duplicates were found in the dataset.
5. **Correcting Inconsistent Data**: Inconsistent data types were corrected to ensure uniformity and validity.
6. **Saving the Cleaned Dataset**: The final cleaned dataset was saved for further analysis.

# Findings

Upon inspection, the following findings were noted:
1. The first column was unnamed, but it appeared to represent mentee IDs and was therefore renamed `Mentee_ID`.
2. **Missing Values Analysis**
- The table below illustrates the missing values in various columns:

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

**Handling Missing Values**:

- Missing values in `Session_Number` and `Session_Duration_Min` were filled using the mean of the respective columns.
- Other variables with missing values were flagged as `NaN`.
- `Points_Awarded` had numerous 109 missing values, which were initially filled with 0, to be updated later with the correct reward points in Task 2.
- The Python code used for handling missing values is shown below:
```python
# Handle the missing values by dropping or filling in rows/columns
df.dropna(subset=['Mentee_ID','Mentor_ID', 'Mentee_Name', 'Job_Info_Completed', 'Session_Date'])

# Fill NaN values in Session Number and duration with mean
Session_Number_Mean = df['Session_Number'].mean()
Session_Duration_Mean = df['Session_Duration_Min'].mean()
df['Session_Number'] = df['Session_Number'].fillna(Session_Number_Mean)
df['Session_Duration_Min'] = df['Session_Duration_Min'].fillna(Session_Duration_Mean)
df['Points_Awarded'] = df['Points_Awarded'].fillna(0)  # Replace with starting value
```

3. **No Duplicates Detected**: There were no duplicate entries found in the dataset.
4. **Inconsistent Data Types**: Several variables had inconsistent or invalid data types. For instance, the 'Session_Date' column was converted to a consistent datetime format.

Finally, the cleaned dataset was saved in Excel format for subsequent analysis.

# Task 2: Legacy Point Allocation Report

## Summary
This report details the allocation of points to mentors based on the criteria outlined in the legacy point allocation system. The process included importing and cleaning the dataset, applying point criteria, and merging the results for final reporting.

## Tools Used
- **Python**: For data manipulation and point calculation.
- **Pandas**: To handle dataframes and perform data cleaning and aggregation.
- **Excel**: To load and save the dataset.

## Data Cleaning
The cleaned dataset included relevant columns such as `Mentor_ID`, `Mentee_ID`, `Session_Duration_Min`, `Job_Info_Completed`, and `Points_Awarded`. Initial processing ensured all data was in the correct format and ready for point allocation.

## Point Allocation Criteria
1. **Mentor Signup Points**: Each mentor received 250 points for signing up.
2. **Mentoring Multiple Mentees**: Mentors who conducted sessions with at least two different mentees were awarded 1000 points.
3. **Session-Specific Points**: Each mentorship session contributed 250 points, with a maximum of 500 points per mentor-mentee relationship.
4. Each session must be at least 30 minutes long.
5. At least one session with the same mentee included job-related information.

## Process
- **Initialization**: Points were initialized for each mentor with 250 points for signing up.
- **Mentorship Points Calculation**: Mentors with sessions involving at least two different mentees received an additional 1000 points.
- **Session Points Calculation**: Grouped by mentor-mentee pairs to process each relationship.
- Verified session duration and job information criteria.
- Allocated 250 points per session, up to a maximum of 500 points per mentor-mentee relationship.

## Results
- The point allocation results for the mentors were as follows:

|Mentor_ID|	Points_Awarded|
|---|---|
|1003|	3250|
|1005|	3250|
|1004|	2750|
|1002|	1500|
|1001|	2250|
|NaN|	250|

- **Updated Dataset**: The final updated dataset, saved as Updated_Mentorship_Sessions.xlsx, included the points awarded to each mentor alongside the original data.
```python
# Merge the points dataframe to the cleaned dataframe and save
df = df.merge(points_df, on='Mentor_ID', how='left', suffixes=('', '_new'))
df['Points_Awarded'] += df['Points_Awarded_new']
df.drop(columns=['Points_Awarded_new'], inplace=True)

# Save the updated dataframe to a new Excel file
df.to_excel('Updated_Mentorship_Sessions.xlsx', index=False)
```
## Conclusion
The point allocation system successfully recognized and rewarded the efforts of mentors based on the defined criteria. The process involved a systematic approach to ensure accurate and fair distribution of points. The updated dataset and the report provide a clear overview of the mentors' contributions and their corresponding rewards.
