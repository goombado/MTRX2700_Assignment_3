#   P(box|E) = P(E1|box ) x P(E2|box ) x P(En|box) x P(box)
#   P(cof|E) = P(E1|cof ) x P(E2|cof ) x P(En|cof) x P(cof)
#   P(wal|E) = P(E1|wal ) x P(E2|wal ) x P(En|wal) x P(wal)
#   E:one instance in testing set.          H: box, coffee, wall.

import numpy as np
import math as m

class testing_attributes:
    def __init__(self, instance = None, CLASS = None):
        self.instance = instance
        self.CLASS = CLASS
    def show_detail(self):
        print("{},{}".format(self.instance, self.CLASS))
        
class MODEL:
    def __init__(self, Name_Class = None, Mean_Class = None, Stddev_Class = None):
        self.Name_Class = Name_Class
        # mean for every attributes in current class
        self.Mean_Class = Mean_Class
        # standard deviation for every attributes in current class
        self.Stddev_Class = Stddev_Class
        
    def show_detail(self):
        print("{}:".format(self.Name_Class))
        print("\tmean:{}".format(self.Mean_Class))
        print("\tstdd:{}\n".format(self.Stddev_Class))
    
    
def MachineLearning(testing_file, training_file, model_file):
    
    test_lo, Class, all_Class = Process_Testing_File(testing_file, training_file)
    model_lo = Process_Training_Model(model_file, Class)
    
    
    
    prob_Class = []
    for i in range(len(Class)):
        num_one_class = all_Class.count(Class[i]) + 1
        total_class = len(all_Class) + len(Class)
        prob_Class.append(num_one_class/total_class)
    
    #print(Class)
    test_index = 7
    for test_index in range(len(test_lo)):
    # if test_index == 7:
        # e.g. [box|E, coffee|E, wall|E ...]
        probability = np.ones(len(Class))
        
        # calculate the probability density
        
        # loop through the attribute in one testing instance
        for x in range(len(test_lo[0].instance)):
            pro_idx = 0
            
            # use one value in a instance to calculate 
            # the probability density of all (e.g. three) classes
            for i in range(len(model_lo)):
                X = test_lo[test_index].instance[x] # current value in a instance
                mean = model_lo[i].Mean_Class[x]
                stddev = model_lo[i].Stddev_Class[x]
                pro_density = probability_density(X, mean, stddev)
                
                probability[pro_idx] = probability[pro_idx] * pro_density
                pro_idx += 1
            # print(probability)    
        # Calculate the probability of class in all instances (e.g. P(coffee))
        for i in range(len(probability)):
            probability[i] *= prob_Class[i]
        
        # print(probability)
        # Extract the maximum probability

        max_prob = max(probability)
        for i in range(len(probability)):
            if probability[i] == max_prob:
                max_prob_index = i
                break
        test_lo[test_index].CLASS = Class[max_prob_index]
            
    # for i in test_lo:
    #     i.show_detail()
    
    # for i in model_lo:
    #     i.show_detail()
    
    result = []
    for i in test_lo:
        result.append(i.CLASS)

    return result, Class

def probability_density(x, mean, sigma):
    # For a normal distribution with mean and standard deviation (sigma), the probability density function is:
    fx = 1 / ( sigma * m.sqrt(2 * m.pi) )
    fx = fx * m.exp( - (x-mean)**2 / (2 * sigma**2) )
    return fx

def Process_Training_Model(model_file, Class):
    header = 0
    indicator = -1
    model_lo = []
    
    # initialize a list of object (class instances) with object name
    for name in Class:
        model_lo.append(MODEL(Name_Class=name))
    
    # Process training model and store the information inside model_lo
    with open(model_file, 'r') as file:
        data = file.readlines()
        
        for row_index in range(len(data)):
            
            # Skip useless row
            if row_index == header:
                continue
            elif data[row_index] == '\n':
                continue
            
            # split row by comma, and remove '\n'
            temp = data[row_index].replace("\n", "")
            temp = temp.split(',')
            
            # Read indicator
            indicator_name = temp[indicator]
            indicator_name = indicator_name.split('_')
            
            # find element position in Class
            model_index = Class.index(indicator_name[1])
            
            # Store corresponding information
            temp.pop() # pop out the indicator
            temp = np.array(temp).astype(np.float)
            if indicator_name[0] == "stddev":
                
                model_lo[model_index].Stddev_Class = temp
            elif indicator_name[0] == "mean":
                model_lo[model_index].Mean_Class = temp
    
    return model_lo
    

def Process_Testing_File(testing_file, training_file):
    test = []
    train = []
    Class = []
    all_Class = []
    Class_index = -1
    
    with open(testing_file, 'r') as file1, open(training_file, 'r') as file2:
        
        # Read testing file, and store it into 2-d array, 'test'
        data1 = file1.readlines()
        for instance in data1:
            instance = instance.replace("\n", "")
            instance = instance.split(",")
            test.append(instance)
        test = np.array(test).astype(np.float)
        
        # Read training file and store data to 2-d array, 'train'
        data2 = file2.readlines()
        for instance in data2:
            instance = instance.replace("\n", "")
            instance = instance.split(",")
            temp_class = instance[Class_index]
            instance.pop()
            Class.append(temp_class)
            train.append(instance)
        train = np.array(train).astype(np.float)
        
        # Extract the min and max of each column in training data
        train = np.concatenate((train, test), axis=0)
        min_column_train = np.amin(train, axis = 0)
        max_column_train = np.amax(train, axis = 0)
        
        # Normalize (scale) attribute values between 0 and 1
        test = Normalize_data(test, min_column_train, max_column_train)
        
        # Store into a list of object (class instances)
        test_lo = [testing_attributes(instance = instance) for instance in test]
        
        # Remove repeated element in Class
        all_Class = Class
        Class = list(dict.fromkeys(Class))
        
    return test_lo, Class, all_Class

def Normalize_data(data, min_column, max_column):
    # input: 1. 2-d array, each row contain the distances of one scan
    #        2. two 1-d lists, the max and min of each column in database (training set)
    # output: normalized list 
    
    data = np.array(data)
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = (data[i][j]-min_column[j])/(max_column[j]-min_column[j])
    
    return data



if __name__ == '__main__':
    testing_file = "TESTING.csv"
    training_file = "DATABASE_TESTING.csv"
    model_file = "MODEL.csv"
    MachineLearning(testing_file, training_file, model_file)
    
    
    