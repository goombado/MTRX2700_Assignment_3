import numpy as np

def Split_and_reverse_data(instance):
    first_element = 0
    num_split = 6
    # Reverse instance if there is a zero in front
    if instance[first_element]  ==  0:
        instance.reverse()
        
    # pop out the elements
    instance.pop()
    instance.pop()
    instance.pop()
    instance.pop(first_element)
    instance.pop(first_element)
    instance.pop(first_element)
    
    # Split instance to 6 parts and take average to each part
    instance = np.array(instance).astype(np.float)
    instance = np.array_split(instance, num_split)
    
    temp = []
    for i in range(len(instance)):
        temp.append(np.mean(instance[i]))
        
    temp = list(temp)
    temp2 = [str(i) for i in temp]
    instance = temp2
    
    return instance


sensorfile1 = "cookie_new_50.csv"
base_file1 = "DATABASE_NEW.csv"
name = "cookie"

database = []

with open(sensorfile1, 'r') as file:
    data = file.readlines()
    for instance in data:
        instance = instance.replace("\n", "")
        instance = instance.split(",")
        
        if len(instance) < 10:
            continue
        
        while '' in instance:
            instance.remove('')
        instance = Split_and_reverse_data(instance)
        database.append(instance)
        

with open(base_file1, 'a') as file:
    for instance in database:
        msg = ",".join(instance)
        file.write(msg)
        msg = ",{}\n".format(name)
        file.write(msg)
        
        
    
    

















