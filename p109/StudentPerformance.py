# IMPORT LIBRARIES
import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff

# READ THE CSV FILE
df = pd.read_csv('p109/StudentsPerformance.csv')

# GET THE LIST OF TWO DATA FROM CSV FILW
reading_score_list = df["reading score"].tolist()
writing_score_list = df["writing score"].tolist()

# FIND AND PRINT THE MEAN,MEDIAN AND MODE FOR THE TWO LISTS 
read_score_mean = statistics.mean(reading_score_list)
writing_score_mean = statistics.mean(writing_score_list)

read_score_median = statistics.median(reading_score_list)
writing_score_median = statistics.median(writing_score_list)

read_score_mode = statistics.mode(reading_score_list)
writing_score_mode = statistics.mode(writing_score_list)

print("MEAN , MEDIAN AND MODE FOR READING SCORE IS {},{} AND {} RESPECTIVELY".format(read_score_mean,read_score_median,read_score_mode))

print("MEAN , MEDIAN AND MODE FOR WRITING SCORE IS {},{} AND {} RESPECTIVELY".format(writing_score_mean,writing_score_median,writing_score_mode))

# FIND AND PRINT THE STANDARD DEVIATION OF THE TWO DATA LISTS
reading_std_deviation = statistics.stdev(reading_score_list)
writing_std_deviation = statistics.stdev(writing_score_list)

print("STANDARD DEVIATION OF READING SCORE IS {}".format(reading_std_deviation))
print("STANDARD DEVIATION OF WRITING SCORE IS {}".format(writing_std_deviation))

# FIND THE 1,2, AND 3 STANDARD DEVIATION FOR BOTH DATA LIST
read_1_std_deviation_start,read_1_std_deviation_end = read_score_mean-reading_std_deviation,read_score_mean+reading_std_deviation
read_2_std_deviation_start,read_2_std_deviation_end = read_score_mean-(2*reading_std_deviation),read_score_mean+(2*reading_std_deviation)
read_3_std_deviation_start,read_3_std_deviation_end = read_score_mean-(3*reading_std_deviation),read_score_mean+(3*reading_std_deviation)

write_1_std_deviation_start,write_1_std_deviation_end = writing_score_mean-writing_std_deviation,writing_score_mean+writing_std_deviation
write_2_std_deviation_start,write_2_std_deviation_end = writing_score_mean-(2*writing_std_deviation),writing_score_mean+(2*writing_std_deviation)
write_3_std_deviation_start,write_3_std_deviation_end = writing_score_mean-(3*writing_std_deviation),writing_score_mean+(3*writing_std_deviation)

# FIND THE % OF DATA WITHIN 1,2,3 STANDARD DEVIATION FOR READING SCORE AND WRITING SCORE
read_list_of_data_within_1_std_deviation = [result for result in reading_score_list if result > read_1_std_deviation_start and result < read_1_std_deviation_end]
read_list_of_data_within_2_std_deviation = [result for result in reading_score_list if result > read_2_std_deviation_start and result < read_2_std_deviation_end]
read_list_of_data_within_3_std_deviation = [result for result in reading_score_list if result > read_3_std_deviation_start and result < read_3_std_deviation_end]

write_list_of_data_within_1_std_deviation = [result for result in writing_score_list if result > write_1_std_deviation_start and result < write_1_std_deviation_end]
write_list_of_data_within_2_std_deviation = [result for result in writing_score_list if result > write_2_std_deviation_start and result < write_2_std_deviation_end]
write_list_of_data_within_3_std_deviation = [result for result in writing_score_list if result > write_3_std_deviation_start and result < write_3_std_deviation_end]

# PRINT THE % OF DATA WITHIN 1,2,3 STANDARD DEVIATION FOR READING AND WRITING SCORE
print("{}% OF DATA FOR READING SCORE LIES WITHIN 1 STANDARD DEVIATION ".format(len(read_list_of_data_within_1_std_deviation)* 100/len(reading_score_list)))
print("{}% OF DATA FOR READING SCORE LIES WITHIN 2 STANDARD DEVIATION ".format(len(read_list_of_data_within_2_std_deviation)* 100/len(reading_score_list)))
print("{}% OF DATA FOR READING SCORE LIES WITHIN 3 STANDARD DEVIATION ".format(len(read_list_of_data_within_3_std_deviation)* 100/len(reading_score_list)))


print("{}% OF DATA FOR WRITING SCORE LIES WITHIN 1 STANDARD DEVIATION ".format(len(write_list_of_data_within_1_std_deviation)* 100/len(writing_score_list)))
print("{}% OF DATA FOR WRITING SCORE LIES WITHIN 2 STANDARD DEVIATION ".format(len(write_list_of_data_within_2_std_deviation)* 100/len(writing_score_list)))
print("{}% OF DATA FOR WRITING SCORE LIES WITHIN 3 STANDARD DEVIATION ".format(len(write_list_of_data_within_3_std_deviation)* 100/len(writing_score_list)))