from statistics import mean, median
import math
import matplotlib.pyplot as plt
import numpy as np

def Iris_box(attr_number, Class_name):
    
    for j in range(attr_number):
        index_of_arrtibute = j
        attr_target_list =[]

        list_of_attribute = [[]] * size_of_sttribute
        print("len of lol=",len(list_of_attribute))

        # Read file
        # Extract entity, which lable equals Class_name
        i=0
        fp = open('iris.data', "r")
        while True:
            data = fp.readline().split(',')
            if data[0] == '\n' or data[0] == '':break
            if data[4] == Class_name: #Iris-setosa/ Iris-versicolor/ Iris-virginica/
                print (i)
                print (data[0])
                i+=1
                attr_target_list.append(float(data[index_of_arrtibute]))
        #end of read file
        fp.close()
        
        titel_atr = "attr_" + str(j)
        plt.title(titel_atr)
        plt.subplot(2, 2, j+1)
        #X = np.arange(bin)
        plt.boxplot(attr_target_list)


size_of_sttribute = 4
Class_list = ["Iris-setosa\n", "Iris-versicolor\n", "Iris-virginica\n"]
for j in range(len(Class_list)):
    print("Class=",Class_list[j])
    fig = plt.figure(j)
    titles = "Class_"+Class_list[j]
    fig.suptitle(titles)
    # output a boxplot of all 4 attribute of class j
    Iris_box(4, Class_list[j])
    plt.show()

