# Import necessary modules
import pandas as pd

# Load the attendance data into a pandas dataframe
df = pd.read_csv('attendance_data.csv')

# Calculate the average attendance for each hour of the day
hourly_average = df.groupby('hour')['attendance'].mean()

# Find the hour with the highest average attendance
most_full_hour = hourly_average.idxmax()

# Find the hour with the lowest average attendance
least_crowded_hour = hourly_average.idxmin()

# Print out the results
print("The dog park is most full at", most_full_hour, "o'clock.")
print("The dog park is least crowded at", least_crowded_hour, "o'clock.")
