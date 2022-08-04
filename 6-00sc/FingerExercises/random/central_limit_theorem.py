import random
import seaborn as sns
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

random.seed(0)

def roll_dice(iterations):
    """ Expects iterations to be a positive integer
        Returns a list of positive integers """
    sample = []
    possibilities = [1,2,3,4,5,6] #fair 6 sided dice
    for i in range(iterations): 
        sample.append(random.choice(possibilities))
    return sample

def make_samples(sample_size, samples):
    """ Expects samples and sample_size to be positive integers.
        Returns a list of samples containing positive integers"""
    result = []
    for s in range(samples):
        result.append(roll_dice(sample_size))
    return result

def get_global_mean(samples):
    """ Expects population to be a list of lists containing positive integers
        Returns the population global mean """
    population = sum(samples, [])
    return sum(population)/len(population)

def get_samples_mean(samples):
    """ Expects samples to be a list of lists containing integers 
        returns a list of integers containing the mean of every sample """
    means = []
    for s in samples:
        means.append(sum(s)/len(s))
    return means

#Experiment 1: 
print("Population of 1000 samples of random 100 elements")
''' Suppose the entire population of trials is equal to the sum of the number of trials in each sample
    Test if the global mean (population) approximate the mean of means (mean of the distribution of sample means '''

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Experiments')

x = make_samples(1000, 100)
x_pop = sum(x, [])
x_means = get_samples_mean(x)

x_mean = get_global_mean(x)
x_means_mean = sum(x_means)/len(x_means)

print("global mean: ", x_mean)
print("means mean: ", x_means_mean)
print("SE of pop:", np.std(x_pop))

#Experiment 2:
print("\n100 samples of random 500 elements (larger sample size)")
x_2 = []
for n in range(100):
    l = []
    for i in range(500): 
        l.append(random.choice(x_pop))
    x_2.append(l)

x_2_pop = sum(x_2, [])
x_2_means = get_samples_mean(x_2)
x_2_mean = get_global_mean(x_2)
x_2_means_mean = sum(x_2_means)/len(x_2_means)

sns.histplot(ax=axes[0, 0], data=x_2_means)
axes[0, 0].plot(x_2_mean, 0, 'bo')
axes[0, 0].plot(x_2_means_mean, 0, 'ro')
axes[0, 0].set_title("Large samples - 500 elements per sample")

print("global mean x_2: ", x_2_mean)
print("means mean x_2: ", x_2_means_mean)
print("SE of pop:", np.std(x_2_pop))

print()
sample_x_2 = random.choice(x_2)
sem_2 = np.std(sample_x_2)/(500**0.5)
sample_2_mean = sum(sample_x_2)/len(sample_x_2)
print("SEM: ", sem_2, "Mean of means SE:", np.std(x_2_means))
#95% probability
print("Result by SE: Mean = ", x_2_means_mean, " +/- ", 1.96*np.std(x_2_means))
print("Result by SEM: Mean = ", sample_2_mean, " +/- ", 1.96*sem_2)
print()
print("Results diff: \nSEM Expected <= ", sem_2*1.96, "\nSEM = ", abs(x_2_mean-sample_2_mean), "\nSE Expected <= ", 1.96*np.std(x_2_means), "\nSE = ", abs(x_2_mean-x_2_means_mean))

#Obs: SEM is calculated over the elements of a single sample and this number approaches the SE of the mean of means if the sample is large enough.

#Experiment 3:
''' Check if the histogram of the population (sum of all elements in each sample) is uniform '''
sns.histplot(ax=axes[0, 1], data=x_2_pop) 
axes[0, 1].set_title("Histogram of population")

#Experiment 4:
''' Check if the distribuition of the means gets wider when size of samples decrease '''
x_3 = []
for n in range(100):
    l = []
    for i in range(100): 
        l.append(random.choice(x_2_pop))
    x_3.append(l)

x_3_pop = sum(x_3, [])
x_3_means = get_samples_mean(x_3)
x_3_mean = get_global_mean(x_3)
x_3_means_mean = sum(x_3_means)/len(x_3_means)

sns.histplot(ax=axes[0, 2], data=x_3_means)
axes[0, 2].plot(x_3_mean, 0, 'bo')
axes[0, 2].plot(x_3_means_mean, 0, 'ro')
axes[0, 2].set_title("Short samples - 100 elements per sample")

print("\n100 samples of 100 elements (short sample size)")
print("global mean x_3: ", x_3_mean)
print("means mean x_3: ", x_3_means_mean)
print("SE of pop:", np.std(x_3_pop))

print()
sample_x_3 = random.choice(x_3)
sem_3 = np.std(sample_x_3)/(100**0.5)
sample_3_mean = sum(sample_x_3)/len(sample_x_3)
print("SEM: ", sem_3, "Mean of means SE:", np.std(x_3_means))
#95% probability
print("Result by SE: Mean = ", x_3_means_mean, " +/- ", 1.96*np.std(x_3_means))
print("Result by SEM: Mean = ", sample_3_mean, " +/- ", 1.96*sem_3)
print()
print("Results diff: \nSEM Expected <= ", sem_3*1.96, "\nSEM = ", abs(x_3_mean-sample_3_mean), "\nSE Expected <= ", 1.96*np.std(x_3_means), "\nSE = ", abs(x_3_mean-x_3_means_mean))

#Obs: SEM is calculated over the elements of a single sample and this number approaches the SE of the mean of means if the sample is large enough.

plt.show()
