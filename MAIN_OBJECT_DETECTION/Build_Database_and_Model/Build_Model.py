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


    
def Build_Model(database_filename, object_name, model_filename):
    database = []  # data in 2-d array format
    database_class = []
    
    # Process Database
    with open(database_filename, 'r') as file:
        data = file.readlines()
        CLASS_INDEX = -1
        for row in data:
            row = row.replace("\n", "")
            row = row.split(',')
            
            # Temporarily store the item's name and remove it from the list
            CLASS = row[CLASS_INDEX]
            row.pop(CLASS_INDEX)
            
            # store each line of the data into list
            database.append(row)
            database_class.append(CLASS)
            
    # convert database_list to numpy array
    database = np.array(database)
    
    # convert to float
    database = database.astype(np.float)
    
    # Extract the min and max of each column
    min_column_database = np.amin(database, axis = 0)
    max_column_database = np.amax(database, axis = 0)
    
    # Normalize (scale) attribute values between 0 and 1
    database = Normalize_data(database, min_column_database, max_column_database)
    
   
    # separate database by name
    database_seperate = []
    temp = []
    for i in range(len(object_name)):
        # initialise a list of object with object name
        database_seperate.append(DATABASE(CLASS = object_name[i]))
        temp.append([])
        
    
    for row_index in range(len(database)):
        for name_index in range(len(object_name)):
            if database_class[row_index] == object_name[name_index]:
                temp[name_index].append(database[row_index])
                break
    
    for i in range(len(temp)):
        database_seperate[i].instances = np.array(temp[i])
    
    # Calculate mean for each attributes, also in each class
    box = 0; coffee = 1; wall = 2
    mean_box = np.mean(database_seperate[box].instances, axis = 0)
    mean_coffee = np.mean(database_seperate[coffee].instances, axis = 0)
    mean_wall = np.mean(database_seperate[wall].instances, axis = 0)
    
    # Calculate standard deviation for each attributes, also in each class
    stddev_box = np.std(database_seperate[box].instances, axis = 0)
    stddev_coffee = np.std(database_seperate[coffee].instances, axis = 0)
    stddev_wall = np.std(database_seperate[wall].instances, axis = 0)

    with open(model_filename, 'w') as file:
        file.write("")
    
    with open(model_filename, 'a') as file:
        
        header = "attr1,attr2,attr3,attr4,attr5,attr6\n"
        
        meanbox = ','.join([str(elem) for elem in mean_box])
        meancoffee = ','.join([str(elem) for elem in mean_coffee])
        meanwall = ','.join([str(elem) for elem in mean_wall])
        
        stddevbox = ','.join([str(elem) for elem in stddev_box])
        stddevcoffee = ','.join([str(elem) for elem in stddev_coffee])
        stddevwall = ','.join([str(elem) for elem in stddev_wall])
        
        file.write(header)
        
        file.write(meanbox)
        file.write(",mean_box\n")
        file.write(stddevbox)
        file.write(",stddev_box\n\n")
        
        file.write(meancoffee)
        file.write(",mean_coffee\n")
        file.write(stddevcoffee)
        file.write(",stddev_coffee\n\n")
        
        file.write(meanwall)
        file.write(",mean_wall\n")
        file.write(stddevwall)
        file.write(",stddev_wall")
        
        
        
    
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
    
    database_filename = "DATABASE_TESTING.csv"
    model_filename = "MODEL.csv"
    object_name = ['box', 'coffee', 'wall']
    
    Build_Model(database_filename, object_name, model_filename)
    
    end   = time.perf_counter()
    print("\nRun Time: {}".format(float(end - start)))