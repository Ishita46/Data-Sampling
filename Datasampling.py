import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv

df = pd.read_csv("Data.csv")
data = df["average"].tolist()

#why are we creating so many randoms in the code? 
#ans. It is because we are sampling the data, means creating differennt different samples of the data. to make it as normal distribution.This kind of distribution will be called as sampling mean distribution
#how are we creating this function?
#ans. 1)create a function using def
#2) take empty array dataset
#3) using for loop we should repeatedly calculate the random values to get their mean.
#4) until the for loop is running index number and value is being calculated using randint(random integer)
#5) appending the above calculated values and then find the mean from it.

def random_set_of_mean(counter):
  dataset = []
  for i in range(0, counter):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
  mean = statistics.mean(dataset)
  return mean


#function to plot the mean on the graph
def show_fig(mean_list):
  df = mean_list
  mean = statistics.mean(df)
  fig = ff.create_distplot([data], ["average"], show_hist = False)
  fig.add_trace(go.Scatter(x=[mean, mean], y=[0,1], mode="lines", name = "MEAN"))
  fig.show()


#Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
  mean_list = []
  for i in range(0,500):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)
  show_fig(mean_list)

  mean = statistics.mean(mean_list)
  print("Mean of sampling distribution :-", mean)

setup()

#code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("population_mean :-", population_mean)


#code to find the standard deviation of the sample data
def standard_deviation():
  mean_list = []
  for i in range(0,500):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

  std_deviation = statistics.stdev(mean_list)
  print("Standard Deviation of sampling distribution:-", std_deviation)

standard_deviation()

