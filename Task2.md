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
