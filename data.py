#libraries
import pandas as pd
import statistics 
import csv
#uploadingFile
df = pd.read_csv('height-weight.csv')
#we are saving the data into two variables
height_list = df['Height(Inches)'].tolist()
weight_list = df['Weight(Pounds)'].tolist()
#we are finding mean
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)
#we are finding median
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)
#we are finding mode
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)
#printing mean, median and mode to validate
print("Mean, Median, Mode of height is {}, {} and {} respectively".format(height_mean, height_median, height_mode))
print("Mean, Median, Mode of weight is {}, {} and {} respectively".format(weight_mean, weight_median, weight_mode))
#Finding standard deviation
height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)
height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation,height_mean+ height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)
weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-weight_std_deviation,weight_mean+ weight_std_deviation
weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)
#percentage of data 1 2 3 standard deviation for height 
height_list_of_data_within_1_std_deviation = [result for result in height_list if result>height_first_std_deviation_start and result< height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result>height_second_std_deviation_start and result< height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result>height_third_std_deviation_start and result< height_third_std_deviation_end]

weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result>weight_first_std_deviation_start and result< weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result>weight_second_std_deviation_start and result< weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result>weight_third_std_deviation_start and result< weight_third_std_deviation_end]

#printing data for heihgt and weight standard deviation
print("{}% of data for height lies within 1 standard deviation ". format(len(height_data_wihtin_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation ". format(len(height_data_wihtin_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation ". format(len(height_data_wihtin_3_std_deviation)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard deviation ". format(len(weight_data_wihtin_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation ". format(len(weight_data_wihtin_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation ". format(len(weight_data_wihtin_3_std_deviation)*100.0/len(weight_list)))
