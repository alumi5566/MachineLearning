from statistics import mean, median
import math
import matplotlib.pyplot as plt
import numpy as np

# to indicate different class in one plot
color =['red','blue','green']

# for any given 2 attribute, scatter all three class in one figure
def Iris_plot(attr_number_1, attr_number_2, Class_list):
    # output one attribute at a time (on the same figure)
    for j in range(len(Class_list)):
        attr_target_list1=[]
        attr_target_list2=[]
        i=0
        fp = open('iris.data', "r")
        while True:
            data = fp.readline().split(',')
            if data[0] == '\n' or data[0] == '':break
            if data[4] == Class_list[j]: #Iris-setosa/ Iris-versicolor/ Iris-virginica/
                print (i)
                print (data[0])
                i+=1
                attr_target_list1.append(float(data[attr_number_1]))
                attr_target_list2.append(float(data[attr_number_2]))
        #end of read file
        plt.scatter(attr_target_list1, attr_target_list2,c=color[j],label=Class_list[j])
        fp.close()
    # end of i loop
    print("attr:",attr_number_1+1,", attr:",attr_number_2+1)
    plt.legend(loc='upper right')
    titles = "attr:"+str(attr_number_1+1)+", attr:"+str(attr_number_2+1)
    plt.title(titles)
    plt.show()

size_of_sttribute = 4
Class_list = ["Iris-setosa\n", "Iris-versicolor\n", "Iris-virginica\n"]
for j in range(size_of_sttribute):
    for k in range(j+1, size_of_sttribute):
        Iris_plot(j,k,Class_list)


