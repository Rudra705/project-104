import pandas as pd 
import statistics

file = pd.read_csv("data_file.csv")
data = file["Weight(Pounds)"]

# calculating and printing mean
mean = statistics.mean(data)
print("The mean of this data is =>",mean)

# calculating and printing mode
mode = statistics.mode(data)
print("The mode of this data is => ",mode)

# calculating and printing median
median = statistics.median(data)
print("The median of this data is => ",median)


