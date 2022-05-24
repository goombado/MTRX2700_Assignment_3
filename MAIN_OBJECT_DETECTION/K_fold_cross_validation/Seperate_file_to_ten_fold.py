import time

class FOLD():
    def __init__(self, instances, count_yes, count_no, num_instances, ratio_yes):
        self.instances = instances
        self.count_yes = count_yes
        self.count_no  = count_no
        self.num_instances = num_instances
        self.ratio_yes = ratio_yes
        

def Stratified_Cross_Validation(training_filename, K):
    instances_yes = []  # store instances that has been classified as 'yes' or 'no'
    instances_no  = []  # and it's a 2D array, each row contains one instance
    CLASS = -1
    
    with open(training_filename, 'r') as file:
        data = file.readlines()
        for row in data:
            row = row.replace("\n", "")
            row = row.split(',')
            # classify each instance by class
            if row[CLASS] == 'yes':
                instances_yes.append(row)
            else:
                instances_no.append(row)
    
    
    # initialise K empty folds
    FOLDS = []
    for i in range(K):
        FOLDS.append(FOLD([], None, None, None, None))
    
    fold_index = 0
    # start assigning instance with class 'yes' into 10 fold
    for instance in instances_yes:
        if fold_index == K:
            fold_index = 0
        FOLDS[fold_index].instances.append(instance)
        fold_index += 1
    
    fold_index = 0
    # start assigning instance with class 'no' into 10 fold
    for instance in instances_no:
        if fold_index == K:
            fold_index = 0
        FOLDS[fold_index].instances.append(instance)
        fold_index += 1


    # calculate number of 'yes' and 'no' instances in each fold
    for i in range(len(FOLDS)):
        temp = sum(FOLDS[i].instances, []) # convert 2D to 1D
        count_yes = temp.count("yes")
        count_no  = temp.count("no")
        FOLDS[i].count_yes = count_yes
        FOLDS[i].count_no  = count_no
        FOLDS[i].num_instances = len(FOLDS[i].instances)
        FOLDS[i].ratio_yes = count_yes / FOLDS[i].num_instances
        
        
    # Store result into txt file
    with open("10_fold_training_data.txt", 'a') as file:
        fold_index = 1
        for i in range(len(FOLDS)):
            msg = "fold{}\n".format(fold_index)
            file.write(msg)
            for j in range(len(FOLDS[i].instances)):
                FOLDS[i].instances[j] = ",".join(FOLDS[i].instances[j]) + '\n'
            msg = "".join(FOLDS[i].instances)
            file.write(msg)
            file.write("\n")
            fold_index += 1
    
        
    
    for i in range(len(FOLDS)):
        print("fold: {}".format(i+1))
        print("Count yes: {}".format(FOLDS[i].count_yes))
        print("Count no: {}".format(FOLDS[i].count_no))
        print("number of instances: {}".format(FOLDS[i].num_instances))
        print("ratio yes: {}".format(FOLDS[i].ratio_yes))
        # for j in range(len(FOLDS[i].instances)):
        #     print(FOLDS[i].instances[j])
        print("\n")
    return
    

if __name__ == '__main__':

    training_filename = "DATABASE_TESTING.csv"
    start = time.perf_counter()
    
    K_folds = 10
    Stratified_Cross_Validation(training_filename, K_folds)
    
    end   = time.perf_counter()
    print("\nRun Time: {}".format(float(end - start)))