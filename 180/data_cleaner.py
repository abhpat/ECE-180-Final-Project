import os
import pandas as pd

from os import listdir
from os.path import isfile, join

# Get current working path
cur_dir = os.curdir + '/Data/Txt/'
# Get list of data files to work on
file_names = [f for f in listdir(cur_dir) if isfile(join(cur_dir, f))]

for f in file_names:
    if '.txt' in f:
        # Read files from Txt folder
        df = pd.read_csv(cur_dir+f, sep=',')

        columns = ["County Code", "District Code", "School Code", "Charter Number", "Test Year", "Subgroup ID", "Test Type",
                   "CAPA Assessment Level", "Total STAR Enrollment", "Total Tested At Entity Level",
                   "Total Tested At Subgroup Level", "Grade", "Test Id", "STAR Reported Enrollment/CAPA Eligible",
                   "Students Tested", "Percent Tested", "Mean Scale Score", "Percentage Advanced", "Percentage Proficient",
                   "Percentage At Or Above Proficient", "Percentage Basic", "Percentage Below Basic",
                   "Percentage Far Below Basic", "Students with Scores", "CMA/STS Average Percent Correct"]

        # list of columns to keep
        keep_col = [
            "District Code",
            "Percent Tested",
            "Mean Scale Score",
            "Percentage Advanced",
            "Percentage Proficient",
            "Percentage Basic",
            "Percentage Below Basic",
            "Percentage Far Below Basic"]

        for x in range(len(columns)):
            if columns[x] in keep_col:
                pass
            else:
                # Drop columns which are not included in "keep_col" list
                if columns[x] in df:
                    df.drop(columns[x], inplace=True, axis=1)

        # Drop rows with NAN or ''
        df = df.dropna()

        # Create a directory to save cleaned data
        new_dir = "/CleanedData"
        if not os.path.exists(cur_dir + new_dir):
            os.makedirs(cur_dir + new_dir)

        # Splits SD2009.txt to ['SD2009', 'txt']
        # Use 1st element from split and add '.csv'
        # Final result -> SD2009.csv
        filtered_file = f.split('.')[0] + '.csv'

        # Save the new filtered file
        df.to_csv(cur_dir+new_dir+'/'+filtered_file, index=False)
