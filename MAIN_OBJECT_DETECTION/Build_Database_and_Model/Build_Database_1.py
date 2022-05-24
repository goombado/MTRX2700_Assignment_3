import numpy as np
import time

def create_database(object_filename = None, object_name = None, database_file = None):
    
    data_list = []
    data_list_divided = []
    
    data_row_index = -1
    nth_scan = 1
    first_element = 0
    last_element = -1
    
    with open(object_filename, 'r') as file:
        
        origin_data = file.readlines()
        
        # Store origin_data to data_list
        # Each row of the list corresponds to one scan result
        for eachline in origin_data:
            
            # skip empty line
            if eachline == '\n': continue
            
            # Indicates whether the data is forward or reverse
            forward = "SCAN {} - Left to Right".format(nth_scan)
            reverse = "SCAN {} - Right to Left".format(nth_scan)
            
            # remove '\n' in each line
            eachline = eachline.replace("\n", "")
            
            if eachline == forward or eachline == reverse:
                data_list.append([])
                nth_scan += 1
                data_row_index += 1
            
            data_list[data_row_index].append(eachline)
        
        
    # This part removes the redundant values at both ends of the data
    # and converts the reverse data to forward
    nth_scan = 1
    for index in range(len(data_list)):
        
        reverse = "SCAN {} - Right to Left".format(nth_scan)
        forward = "SCAN {} - Left to Right".format(nth_scan)
        
        if data_list[index][0] == reverse:
            data_list[index].pop(first_element)
            data_list[index].pop(first_element)
            data_list[index].pop(last_element)
            data_list[index].reverse() # IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!
            nth_scan += 1
            
        elif data_list[index][0] == forward: 
            data_list[index].pop(first_element)
            data_list[index].pop(first_element)
            data_list[index].pop(last_element)
            nth_scan += 1
            continue
    
    # The code below divides each row in the list into 6 equal parts
    # and averages each part.
    
    num_split = 6 # IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for index in range(len(data_list)):
        temp = np.array(data_list[index])
        temp = temp.astype(np.float)
        temp = np.array_split(temp, num_split)
        temp2 = []
        for i in range(len(temp)):
            temp2.append(np.mean(temp[i]))
        data_list_divided.append(temp2)
    
    # Store the segmented data in a new document 
    # and add the name of the object after each line of data
    with open(database_file, 'a') as file:
        Class = ",{}\n".format(object_name)
        for row in data_list_divided:
            res = ",".join([str(int(i)) for i in row])
            file.write(res)
            file.write(Class)
            


def clear_database(database_filename):
    with open(database_filename, 'w') as file:
        file.write("")


if __name__ == '__main__':
    start = time.perf_counter()
    
    database_file = 'DATABASE.csv'
    clear_database(database_file)
    
    object_name1 = 'box'
    object_name2 = 'coffee'
    object_name3 = 'wall'
    
    object_filename1 = "box_data_50_modified.csv"
    object_filename2 = "coffee_data_50_modified.csv"
    object_filename3 = "wall_data_50_modified.csv"
    
    create_database(object_filename1, object_name1, database_file)
    create_database(object_filename2, object_name2, database_file)
    create_database(object_filename3, object_name3, database_file)
    
    # Remove the last line manually !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    end   = time.perf_counter()
    print("\nRun Time: {}".format(float(end - start)))
