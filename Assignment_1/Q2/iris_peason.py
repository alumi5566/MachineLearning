from statistics import mean, median
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# for two given attribute list, calculate the pearson correlation
def correlation(listA, listB):
    avgA = mean(listA)
    avgB = mean(listB)
    sA = np.std(listA)
    sB = np.std(listB)
    if len(listA) != len(listB):
        print("len wrong in correlation()")
    tmp = 0
    for i in range(len(listA)):
        tmp += (listA[i]-avgA)*(listB[i]-avgB)
    return (tmp/len(listA))/(sA*sB)

def Iris_pearson(attr_number, Class_name):
    #array = [0] * attr_number
    #matrix = [array]*attr_number
    #print(matrix)
    #matrix[1][1] = 1
    # above method create 3 duplicate array (by refernece)

    # Initialize correlation matrix with all zero,
    matrix = [[0 for i in range(attr_number)] for i in range(attr_number)]
    # Fill one at diagonal
    for i in range(attr_number):
        matrix[i][i] = 1
    # For all pair attribute (j,k), where j != j
    # Fill the corresponding matrix value
    for j in range(attr_number):
        for k in range(j+1, attr_number):
            print("cmp:( ",j,",",k," )")
            attr_target_list1 =[]
            attr_target_list2 =[]
            i=0
            fp = open('iris.data', "r")
            while True:
                data = fp.readline().split(',')
                if data[0] == '\n' or data[0] == '':break
                if data[4] == Class_name: #Iris-setosa/ Iris-versicolor/ Iris-virginica/
                    print (i)
                    print (data[0])
                    i+=1
                    attr_target_list1.append(float(data[j]))
                    attr_target_list2.append(float(data[k]))
            #end of read file
            fp.close()
            # now we have two attribute in attr_target_list1 and attr_target_list2
            matrix[j][k] = correlation(attr_target_list1, attr_target_list2)
            # (k,j) don't need to re-calculate
            matrix[k][j] = matrix[j][k]
    #output matrix
    print("size=",len(matrix))
    for i in range(len(matrix)):
        print(matrix[i])
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.show()

def Iris_pearson_all_class(attr_number):
    # Initialize correlation matrix with all zero,
    matrix = [[0 for i in range(attr_number)] for i in range(attr_number)]
    # Fill one at diagonal
    for i in range(attr_number):
        matrix[i][i] = 1
    # For all pair attribute (j,k), where j != j
    # Fill the corresponding matrix value
    for j in range(attr_number):
        for k in range(j+1, attr_number):
            print("cmp:( ",j,",",k," )")
            attr_target_list1 =[]
            attr_target_list2 =[]
            i=0
            fp = open('iris.data', "r")
            while True:
                data = fp.readline().split(',')
                if data[0] == '\n' or data[0] == '':break
                if 1: #Iris-setosa/ Iris-versicolor/ Iris-virginica/
                    print (i)
                    print (data[0])
                    i+=1
                    attr_target_list1.append(float(data[j]))
                    attr_target_list2.append(float(data[k]))
            #end of read file
            fp.close()
            # now we have two attribute in attr_target_list1 and attr_target_list2
            matrix[j][k] = correlation(attr_target_list1, attr_target_list2)
            # (k,j) don't need to re-calculate
            matrix[k][j] = matrix[j][k]
    #output matrix
    print("size=",len(matrix))
    for i in range(len(matrix)):
        print(matrix[i])
    #plt.imshow(matrix, cmap='hot', interpolation='nearest')
    sns.heatmap(matrix)
    plt.show()

size_of_sttribute = 4
Class_list = ["Iris-setosa\n", "Iris-versicolor\n", "Iris-virginica\n"]
for j in range(len(Class_list)):
    print("Class=",Class_list[j])
    #Iris_pearson(4, Class_list[j])
Iris_pearson_all_class(4)

