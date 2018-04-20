from statistics import mean, median
import math
import matplotlib.pyplot as plt
import numpy as np

def Wine_histo(attr_index, Class_name):
    fp = open('wine.data', "r")

    index_of_arrtibute = attr_index
    attr_target_list =[]

    list_of_attribute = [[]] * size_of_sttribute
    print("len of lol=",len(list_of_attribute))

    # Read file
    # Extract entity, which lable equals Class_name
    i=0
    while True:
        data = fp.readline().split(',')
        print (data)
        if data[0] == '\n' or data[0] == '':break
        if data[0] == Class_name: #["1", "2", "3"]
            print (i)
            print (data[1])
            i+=1
            attr_target_list.append(float(data[index_of_arrtibute+1]))
    #end of read file
    print("attr=",index_of_arrtibute)

    max_value0 = max(attr_target_list)
    min_value0 = min(attr_target_list)
    avg_value0 = mean(attr_target_list)

    print("Attr_0: MAX= ",max_value0,",min= ",min_value0,",Avg= ",avg_value0)

    bin_list = [5, 10, 50, 100]
    width = 0.35
    # put 4 different bin number in one figure
    for j in range(len(bin_list)):
        bin=bin_list[j]
        # len of hist_0 equals the number of bin, use for accumulate the histogram
        hist_0 = [0] * bin
        interval = (max_value0 - min_value0)/ bin
        for i in range(len(attr_target_list)) :
            print(attr_target_list[i]," in slot:", (attr_target_list[i]-min_value0)/interval )
            if attr_target_list[i] == min_value0:
                hist_0[0] += 1
            elif attr_target_list[i] == max_value0:
                hist_0[bin-1] += 1
            else:
                hist_0[math.floor( (attr_target_list[i]-min_value0)/interval) ] += 1
        # check if the sum of histogram is not equals data count
        for i in range(len(hist_0)):
            print("[",i,"]: ",hist_0[i])
        if sum(hist_0) != len(attr_target_list):
            print("WARNING!! total number is wrong")
        # plot bar as histogram
        s = "bin="+str(bin_list[j-1])
        plt.title(s)
        #plt.title('bin=%d' % (bin_list[j-1]))
        ax = plt.subplot(2, 2, j+1)
        X = np.arange(bin)
        s = ['']*bin
        for k in range(bin):
            if bin == 5:
                s[k] = str("{0:.1f}".format(min_value0+k*interval))+"-"+str("{0:.1f}".format(min_value0+(k+1)*interval))
            elif bin == 10:
                if k%2 == 0 or k==bin-1:
                    s[k] = str("{0:.1f}".format(min_value0+k*interval))+"-"+str("{0:.1f}".format(min_value0+(k+1)*interval))
            else:
                if k%20 ==0 or k==bin-1:
                    s[k] = str("{0:.2f}".format(min_value0+k*interval))+"-"+str("{0:.2f}".format(min_value0+(k+1)*interval))
            #plt.xticks(rotation='vertical')
            print(s)
            ax.set_xticks(X + width / 2)
            ax.set_xticklabels(s)
        plt.bar(X, hist_0)
    #end of j loop
    fp.close()

size_of_sttribute = 3 #13
Class_list = ["1", "2", "3"]
for i in range(size_of_sttribute):
    for j in range(len(Class_list)):
        print(i,"-th Attribute")
        print("Class=",Class_list[j])
        fig = plt.figure(i)
        titles = str(i+1)+"-th Attribute, "+"Class_"+Class_list[j]
        fig.suptitle(titles)
        # output a histogram of attribute i and class j
        Wine_histo(i, Class_list[j])
        plt.show()

