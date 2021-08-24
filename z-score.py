import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random 
import pandas as pd 
import csv 

df = pd.read_csv("medium_data.csv")
data = df['reading_time'].tolist()

def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean
mean_list = []
for i in range(0,100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)
def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],['temp'], show_hist = False)
    fig.show()
st_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("The Standard Deviation of the random numbers is:", st_deviation)
print("The Mean of the random numbers is:", mean)

first_stdev_start,first_stdev_end = mean-st_deviation, mean+st_deviation 
second_stdev_start,second_stdev_end = mean-(2*st_deviation), mean+(2*st_deviation) 
third_stdev_start,third_stdev_end = mean-(3*st_deviation), mean+(3*st_deviation)

#Finding the Mean of the students who gave extra time to Maths Lab
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean1 = statistics.mean(data)
print("The Mean of Sample is:", mean1)
fig = ff.create_distplot([mean_list],['Students Marks'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17],mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean1,mean1], y = [0,0.17],mode = "lines", name = "Mean of Students who had Fun Maths Sheets"))
fig.add_trace(go.Scatter(x = [first_stdev_end,first_stdev_end], y = [0,0.17],mode = "lines", name = "The First Standard Deviation"))
fig.add_trace(go.Scatter(x = [second_stdev_end,second_stdev_end], y = [0,0.17],mode = "lines", name = "The Second Standard Deviation"))
fig.add_trace(go.Scatter(x = [third_stdev_end,third_stdev_end], y = [0,0.17],mode = "lines", name = "The Third Standard Deviation"))
fig.show()
#If Z is greater than 3, it has a good impact
z_score1 = (mean-mean1)/st_deviation
print('Z Score of Sample 1:', z_score1)