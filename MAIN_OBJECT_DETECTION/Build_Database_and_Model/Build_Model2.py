import numpy as np
import time

class DATABASE:
    def __init__(self, instances = None, CLASS = None):
        self.instances = instances
        self.CLASS = CLASS
        
    def print_database(self):
        for row in self.instances:
            print("{},{}".format(row, self.CLASS))
        print(type(self.instances))
        print()

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
        
def Build_Model(database_file, model_file):
    Class = []
    all_Class = []
    Class_index = -1
    train = []
    
    with open(database_file, 'r') as file:
        # Read training file and store data to 2-d array, 'train'
        data = file.readlines()
        for instance in data:
            instance = instance.replace("\n", "")
            instance = instance.split(",")
            temp_class = instance[Class_index]
            instance.pop()
            all_Class.append(temp_class)
            train.append(instance)
        train = np.array(train).astype(np.float)
        Class = list(dict.fromkeys(all_Class))
    
    # Extract the min and max of each column
    min_column = np.amin(train, axis = 0)
    max_column = np.amax(train, axis = 0)
    
    # Normalize (scale) attribute values between 0 and 1
    train = Normalize_data(train, min_column, max_column)
    
    # separate database by name
    train_seperate = []
    temp = []
    for i in range(len(Class)):
        # initialise a list of object with object name
        train_seperate.append(DATABASE(CLASS = Class[i]))
        temp.append([])
        
    for row_index in range(len(train)):
        for name_index in range(len(Class)):
            if all_Class[row_index] == Class[name_index]:
                temp[name_index].append(train[row_index])
                break
            
    for i in range(len(temp)):
        train_seperate[i].instances = np.array(temp[i])
    
    for i in train_seperate:
        i.print_database()
    
    # initialize a list of object (class instances) with object name
    model_lo = []
    for name in Class:
        model_lo.append(MODEL(Name_Class=name))
    
    for part_idx in range(len(train_seperate)):
        temp = train_seperate[part_idx].instances
        mean = np.mean(temp, axis = 0)
        stddev = np.std(temp, axis = 0)
        model_lo[part_idx].Mean_Class = mean
        model_lo[part_idx].Stddev_Class = stddev
    
    # for i in model_lo:
    #     i.show_detail()
    
    with open(model_file, 'w') as file:
        file.write("")
    
    with open(model_file, 'a') as file:
        header = "attr1,attr2,attr3,attr4,attr5,attr6\n"
        file.write(header)
        
        for i in range(len(model_lo)):
            temp = list(model_lo[i].Mean_Class)
            temp = ",".join([str(i) for i in temp])
            file.write(temp)
            object_name = ",mean_{}\n".format(model_lo[i].Name_Class)
            file.write(object_name)
            
            temp = list(model_lo[i].Stddev_Class)
            temp = ",".join([str(i) for i in temp])
            file.write(temp)
            object_name = ",stddev_{}\n\n".format(model_lo[i].Name_Class)
            file.write(object_name)
    return


def Normalize_data(data, min_column, max_column):
    # input: 2-d array (data), each row contain the distances of one scan
    #        two 1-d lists, which indicate the max and min of each column in database
    # output: normalized list 
    
    data = np.array(data)
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = ((data[i][j] - min_column[j]) / (max_column[j] - min_column[j]))
    return data


if __name__ == '__main__':
    start = time.perf_counter()
    
    database_filename = "DATABASE_NEW.csv"
    model_filename = "MODEL_NEW.csv"
    
    Build_Model(database_filename, model_filename)
    
    end   = time.perf_counter()
    print("\nRun Time: {}".format(float(end - start)))
        
