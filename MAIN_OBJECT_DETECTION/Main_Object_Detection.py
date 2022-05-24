from Machine_Learning import MachineLearning
import numpy as np
import random
import time

def main_object_detection(training_file, testing_file, model_file):
    
    results, Class = MachineLearning(testing_file, training_file, model_file)
    print(results)
    # print(Class)
    
    # Take the name with the most occurrences as the final result
    count = np.zeros(len(Class))
    for name in range(len(Class)):
        for result in results:
            if Class[name] == result:
                count[name] += 1
    max_count = count.max()
    count = list(count)
    index = count.index(max_count)
    
    # Get a price for an object
    price = random.randint(50, 200)
    price += 0.99
    
    # Formatting final result
    Final_result = []
    Final_result.append(str(Class[index]))
    Final_result.append(str(price))
    
    print(Final_result)
    return Final_result


if __name__ == '__main__':
     start = time.perf_counter()
    
     testing_file = "detected.csv"
     training_file = "DATABASE_NEW.csv"
     model_file = "MODEL_NEW.csv"
     
     main_object_detection(training_file, testing_file, model_file)
     
     end   = time.perf_counter()
     print("\nRun Time: {}".format(float(end - start)))
     