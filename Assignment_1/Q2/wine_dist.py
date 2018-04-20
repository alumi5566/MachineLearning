from statistics import mean, median
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

size_of_sttribute = 4
size_of_data = 178
list_of_data = [[""] for i in range(size_of_data)]
Class_list = ["1", "2", "3"]

# For any two data entity and p value, return the distance
def distance(Class1, Class2, p):
    sum = 0
    for i in range(size_of_sttribute):
        sum += math.pow(abs(float(list_of_data[Class1][i+1])-float(list_of_data[Class2][i+1])),p)
    for i in range(p-1):
        #print("sqrt once")
        sum = math.sqrt(sum)
    return sum

# Initialize correlation matrix with all zero,
matrix = [[0 for i in range(size_of_data)] for i in range(size_of_data)]
for i in range(size_of_data):
    matrix[i][i] = 0
# Read all data entity into list_of_data
i=0
fp = open('wine.data', "r")
while True:
    data = fp.readline().split(',')
    if data[0] == '\n' or data[0] == '':break
    list_of_data[i] = data
    i+=1
#end of read file
fp.close()

print(list_of_data)
for k in (1,2):
    nearest_node = 0
    for i in range(size_of_data):
        min_dist = 100000
        min_num = i
        for j in range(i+1, size_of_data):
            p=k
            matrix[i][j] = distance(i,j,p)
            # (j,i) don't need to re-calculate
            matrix[j][i] = matrix[i][j]
            if matrix[i][j] <= min_dist:
                min_dist = matrix[i][j]
                min_num = j
        if list_of_data[i][0] == list_of_data[min_num][0]:
            nearest_node += 1
    print("size=",len(matrix))
    #for s in range(len(matrix)):
    #print(matrix[s])
    sns.heatmap(matrix)
    #plt.imshow(matrix, cmap='hot', interpolation='nearest')
    titles = "p = "+str(k)
    plt.title(titles)
    plt.show()
    print("Nearest node=",nearest_node)

